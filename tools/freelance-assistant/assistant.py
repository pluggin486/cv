#!/usr/bin/env python3
"""Local-only matcher and proposal drafter for saved freelance notifications."""

from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
from email import policy
from email.parser import BytesParser
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Optional
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[2]
LOCAL = ROOT / ".local" / "freelance-assistant"
DRAFTS = LOCAL / "drafts"
STATE_FILE = LOCAL / "state.json"
QUOTA_FILE = LOCAL / "quotas.json"
PORTFOLIO_URL = "https://ss-cv.vercel.app/freelance"

PLATFORMS = {
    "flru": "FL.ru",
    "kwork": "Kwork",
    "peopleperhour": "PeoplePerHour",
    "arc": "Arc",
    "toptal": "Toptal",
}
ALIASES = {
    "fl": "flru",
    "fl.ru": "flru",
    "flru": "flru",
    "kwork": "kwork",
    "pph": "peopleperhour",
    "peopleperhour": "peopleperhour",
    "people per hour": "peopleperhour",
    "arc": "arc",
    "toptal": "toptal",
}

KEYWORDS: dict[str, tuple[str, int]] = {
    "Vue": (r"vue(?:\.js)?(?:\s*[23])?", 4),
    "Nuxt": (r"nuxt(?:\s*[23])?", 4),
    "TypeScript": (r"typescript|type\s*script", 2),
    "frontend": (r"front[\s-]?end|фронтенд|фронт[\s-]?энд", 3),
    "веб-разработка": (r"веб[\s-]*(?:разработк\w*|программирован\w*)|web[\s-]*development|web[\s-]*programming", 3),
    "программирование": (r"программирован\w*|програмиирован\w*|programming|программист\w*|software\s+development", 1),
    "React": (r"react(?:\.js|\s+native)?", 2),
    "Svelte": (r"svelte(?:kit)?", 2),
    "JavaScript": (r"javascript|java\s*script", 1),
}
COMPILED_KEYWORDS = {
    label: re.compile(r"(?<![\w])(?:" + pattern + r")(?![\w])", re.IGNORECASE)
    for label, (pattern, _weight) in KEYWORDS.items()
}
STOP_TITLES = re.compile(r"^(?:new project|new job|новый заказ|новый проект)\s*[:\-–—]?\s*", re.IGNORECASE)
URL_PATTERN = re.compile(r"https?://[^\s<>\"')\]]+", re.IGNORECASE)

FACTS = {
    "base": "3+ года коммерческого frontend-опыта; Vue 2/3, Nuxt 3 и TypeScript.",
    "ui": "Разработал 50+ компонентов для корпоративного UI Kit.",
    "virtual": "Реализовал VirtualScroll для списков из 10 000+ строк без сторонней библиотеки виртуализации.",
    "migration": "Переводил приложение с Vue 2 / Vuex на Vue 3 / Composition API / Pinia.",
    "ci": "После перехода тестов с Jest на Vitest медианное время тестового этапа CI снизилось на 70%.",
    "api": "Работал с REST API и генерацией клиентских сервисов по OpenAPI.",
}
FACTS_EN = {
    FACTS["base"]: "3+ years of commercial frontend experience with Vue 2/3, Nuxt 3 and TypeScript.",
    FACTS["ui"]: "Built 50+ components for a corporate UI Kit.",
    FACTS["virtual"]: "Built VirtualScroll for lists with 10,000+ rows, without a third-party virtualization library.",
    FACTS["migration"]: "Migrated an application from Vue 2 / Vuex to Vue 3 / Composition API / Pinia.",
    FACTS["ci"]: "After moving tests from Jest to Vitest, median CI test-stage time fell by 70%.",
    FACTS["api"]: "Worked with REST APIs and generated client services from OpenAPI specifications.",
    "Подтверждённый production-стек — Vue/Nuxt; опыт React/Svelte в резюме не указан.": "My confirmed production stack is Vue/Nuxt; React or Svelte experience is not listed in my CV.",
}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.hidden_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "head"}:
            self.hidden_depth += 1
        if tag in {"br", "p", "div", "li", "tr", "h1", "h2", "h3"}:
            self.parts.append("\n")
        if tag == "a":
            href = dict(attrs).get("href")
            if href and href.startswith("http"):
                self.parts.append(" " + href + " ")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "head"} and self.hidden_depth:
            self.hidden_depth -= 1
        if tag in {"p", "div", "li", "tr", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("ё", "е").replace("Ё", "Е")).strip()


def normalize_platform(value: str) -> str:
    key = value.strip().lower()
    if key not in ALIASES:
        raise ValueError(f"Неизвестная площадка: {value}. Допустимые: {', '.join(PLATFORMS)}")
    return ALIASES[key]


def empty_state() -> dict[str, Any]:
    return {"schema": 1, "seen": {}, "sent": {}}


def load_json(path: Path, fallback: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return fallback
    except (json.JSONDecodeError, OSError) as exc:
        raise ValueError(f"Не удалось прочитать {path}: {exc}") from exc


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def canonical_url(url: str) -> str:
    if not url:
        return ""
    try:
        parts = urlsplit(url.strip())
        if parts.scheme not in {"http", "https"} or not parts.netloc:
            return url.strip().rstrip("/")
        query = [
            (key, value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
            if not key.lower().startswith("utm_") and key.lower() not in {"ref", "source", "tracking", "trk"}
        ]
        return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), urlencode(query), ""))
    except ValueError:
        return url.strip().rstrip("/")


def job_keys(job: dict[str, Any]) -> list[str]:
    keys: list[str] = []
    job_id = str(job.get("id", "")).strip()
    url = canonical_url(str(job.get("url", "")))
    if job_id:
        keys.append("id:" + str(job.get("platform", "")) + ":" + job_id.lower())
    if url:
        keys.append("url:" + url)
    if not keys:
        digest = re.sub(r"\W+", " ", normalize(str(job.get("title", "")) + " " + str(job.get("description", ""))).lower())
        keys.append("text:" + digest[:240])
    return keys


def clean_job(raw: dict[str, Any], default_platform: Optional[str] = None) -> dict[str, Any]:
    platform_value = raw.get("platform") or default_platform
    if not platform_value:
        raise ValueError("У каждой записи нужно указать platform или передать --platform для .eml")
    title = normalize(str(raw.get("title", "")))
    title = STOP_TITLES.sub("", title).strip()
    description = normalize(str(raw.get("description", "")))
    if not title:
        raise ValueError("У записи не заполнен title")
    if not description:
        raise ValueError(f"У записи «{title}» не заполнен description")
    budget = raw.get("budget")
    deadline = raw.get("deadline")
    return {
        "id": str(raw.get("id", "")).strip(),
        "platform": normalize_platform(str(platform_value)),
        "url": str(raw.get("url", "")).strip(),
        "title": title,
        "description": description,
        "budget": "" if budget is None else str(budget).strip(),
        "deadline": "" if deadline is None else str(deadline).strip(),
        "project_type": str(raw.get("project_type", "unknown")).strip().lower(),
        "responses_remaining": raw.get("responses_remaining"),
    }


def parse_json_jobs(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("jobs"), list):
        return payload["jobs"]
    if isinstance(payload, dict):
        return [payload]
    raise ValueError("JSON должен быть записью задачи, массивом или объектом с полем jobs")


def parse_eml_job(path: Path, platform: Optional[str]) -> dict[str, Any]:
    message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
    subject = normalize(str(message.get("subject", "")))
    body_part = message.get_body(preferencelist=("plain", "html")) if message.is_multipart() else message
    body = ""
    if body_part is not None:
        content = body_part.get_content()
        if isinstance(content, bytes):
            body = content.decode(body_part.get_content_charset() or "utf-8", errors="replace")
        else:
            body = str(content)
        if body_part.get_content_type() == "text/html":
            extractor = TextExtractor()
            extractor.feed(body)
            body = " ".join(extractor.parts)
    body = html.unescape(body)
    urls = URL_PATTERN.findall(body)
    ignored_url_parts = ("unsubscribe", "privacy", "preferences", "tracking", "click.", "utm_")
    usable_urls = [item.rstrip(".,;:") for item in urls if not any(part in item.lower() for part in ignored_url_parts)]
    platform_hosts = {
        "flru": ("fl.ru",),
        "kwork": ("kwork.ru",),
        "peopleperhour": ("peopleperhour.com",),
        "arc": ("arc.dev",),
        "toptal": ("toptal.com",),
    }
    platform_key = normalize_platform(platform) if platform else ""
    preferred = [item for item in usable_urls if any(host in urlsplit(item).netloc.lower() for host in platform_hosts.get(platform_key, ()))]
    raw_url = (preferred or usable_urls or [""])[0]
    body = URL_PATTERN.sub(" ", body)
    body = normalize(body)
    return clean_job(
        {
            "platform": platform,
            "url": raw_url,
            "title": subject,
            "description": body,
        }
    )


def analyze(job: dict[str, Any]) -> dict[str, Any]:
    title = job["title"]
    description = job["description"]
    combined = normalize(title + " " + description)
    title_normalized = normalize(title)
    matches: list[str] = []
    score = 0
    confirmed_stack: set[str] = set()
    frontend_terms: set[str] = set()
    for label, (_pattern, weight) in KEYWORDS.items():
        if COMPILED_KEYWORDS[label].search(combined):
            matches.append(label)
            score += weight
            if COMPILED_KEYWORDS[label].search(title_normalized):
                score += 1
            if label in {"Vue", "Nuxt", "TypeScript"}:
                confirmed_stack.add(label)
            if label in {"frontend", "веб-разработка"}:
                frontend_terms.add(label)
    if not matches:
        return {"matched": False, "score": 0, "terms": [], "reasons": [], "facts": [], "manual_review": False}

    react_svelte = {"React", "Svelte"}.intersection(matches)
    reasons = ["Ключевые слова: " + ", ".join(matches) + "."]
    manual_review = False
    if confirmed_stack:
        reasons.append("Есть совпадение с подтверждённым frontend-стеком Vue/Nuxt/TypeScript.")
    if react_svelte:
        reasons.append("React/Svelte найдено в описании, но этот опыт не подтверждён резюме; требуется ручная проверка.")
        manual_review = True
    elif not confirmed_stack and frontend_terms:
        reasons.append("Задача связана с web/frontend, но конкретный стек нужно проверить вручную.")
        manual_review = True
    elif not confirmed_stack:
        reasons.append("Совпадение только по общим словам; стек, роль и объём нужно проверить вручную.")
        manual_review = True

    text = combined.lower()
    selected = [FACTS["base"]]
    conditional_facts = [
        (("virtual", "виртуал", "список", "таблиц", "list", "table", "10 000"), FACTS["virtual"]),
        (("ui kit", "ui-kit", "компонент", "design system", "дизайн-систем", "дизайн систем"), FACTS["ui"]),
        (("миграц", "migration"), FACTS["migration"]),
        (("ci", "test", "тест", "vitest", "jest", "pipeline"), FACTS["ci"]),
        (("api", "openapi", "rest", "endpoint", "интеграц"), FACTS["api"]),
    ]
    for triggers, fact in conditional_facts:
        if any(trigger in text for trigger in triggers) and fact not in selected:
            selected.append(fact)
    if react_svelte:
        selected.append("Подтверждённый production-стек — Vue/Nuxt; опыт React/Svelte в резюме не указан.")
    return {
        "matched": True,
        "score": score,
        "terms": matches,
        "reasons": reasons,
        "facts": selected,
        "manual_review": manual_review,
    }


def platform_quota(platform: str, state: dict[str, Any], quota_config: dict[str, Any], job: dict[str, Any]) -> str:
    month = date.today().strftime("%Y-%m")
    sent = state.setdefault("sent", {})
    used = int(sent.get(platform, {}).get(month, 0))
    if job.get("responses_remaining") is not None:
        try:
            return f"По сохранённому уведомлению: {job['responses_remaining']} бесплатных откликов осталось; значение не сверено с площадкой."
        except Exception:
            pass
    if platform == "peopleperhour":
        left = max(15 - used, 0)
        return f"PeoplePerHour: {left}/15 бесплатных Proposal credits за {month} по локальному учёту ({used} отмечено вручную)."
    if platform == "kwork":
        limit = quota_config.get(platform, {}).get("free_monthly_limit")
        if isinstance(limit, int) and limit >= 0:
            left = max(limit - used, 0)
            return f"Kwork: {left}/{limit} по локально заданной квоте за {month} ({used} отмечено вручную); проверьте фактический остаток в аккаунте."
        return "Kwork: остаток не задан — зависит от уровня продавца и текущей квоты в аккаунте."
    if platform == "flru":
        kind = job.get("project_type", "unknown")
        if kind in {"for_all", "all", "всем", "для всех", "vacancy", "вакансия", "contest", "конкурс"}:
            return "FL.ru: для этого типа проекта отклик бесплатный; фиксированной месячной квоты нет."
        if kind in {"paid", "платный", "not_for_all"}:
            return "FL.ru: такой отклик может быть платным; проверьте метку и баланс перед отправкой."
        return "FL.ru: тип заказа не указан; проверьте метку «для всех» (вакансии и конкурсы бесплатны)."
    return f"{PLATFORMS[platform]}: лимит бесплатных заявок здесь не считается; проверяйте условия самой площадки ({used} отправок отмечено локально за {month})."


def proposal(job: dict[str, Any], analysis: dict[str, Any]) -> str:
    platform = job["platform"]
    title = job["title"].rstrip(".!? ")
    english = platform not in {"flru", "kwork"}
    facts = analysis["facts"]
    if english:
        fact_line = " ".join(FACTS_EN.get(fact, fact) for fact in facts[:2])
        scope = "Budget: to be discussed after scope review." if not job["budget"] else f"Listed budget: {job['budget']}. I suggest confirming deliverables before the final estimate."
        schedule = "Timeline: to be confirmed after scope review." if not job["deadline"] else f"Listed deadline: {job['deadline']}. I would confirm it against the agreed scope."
        unsupported = "" if not ({"React", "Svelte"}.intersection(analysis["terms"])) else "My CV confirms Vue/Nuxt work; I do not claim React or Svelte experience. We should review the expected work before estimating.\n\n"
    else:
        fact_line = " ".join(facts[:2])
        scope = "Бюджет: уточнить после оценки объёма." if not job["budget"] else f"Бюджет из объявления: {job['budget']}. Предлагаю подтвердить объём до оценки."
        schedule = "Срок: уточнить по составу работ." if not job["deadline"] else f"Срок из объявления: {job['deadline']}. Нужно сверить с объёмом работ."
        unsupported = "" if not ({"React", "Svelte"}.intersection(analysis["terms"])) else "В резюме подтверждён Vue/Nuxt; опыт React/Svelte не заявляю, совместимость задачи нужно обсудить до оценки.\n\n"

    if platform in {"flru", "kwork"}:
        return (
            f"Здравствуйте!\n\nПо задаче «{title}» могу сначала уточнить требования и предложить этапы реализации. "
            f"{fact_line}\n\n{unsupported}{scope}\n{schedule}\n"
            "Подскажите, какие страницы или сценарии входят в объём и есть ли макеты/API-контракт?\n\n"
            "Ставка и срок — после оценки точного объёма."
        ).replace("\n\n\n", "\n\n")

    portfolio_line = f"Portfolio: {PORTFOLIO_URL}\n" if platform in {"arc", "toptal"} else ""
    return (
        f"Hello! I read your brief for “{title}”. I can review the scope and suggest clear delivery steps.\n\n"
        f"{fact_line}\n\n{unsupported}{scope}\n{schedule}\n"
        "Could you share the main screens or user flows, the current stack, and any API or design files? "
        "I can agree on the rate and timeline after reviewing the scope.\n\n"
        f"{portfolio_line}"
        "English: B1. I can discuss technical details in writing."
    ).replace("\n\n\n", "\n\n")


def render_job(job: dict[str, Any], analysis: dict[str, Any], quota: str) -> str:
    facts = "\n".join(f"- {item}" for item in analysis["facts"])
    reasons = "\n".join(f"- {item}" for item in analysis["reasons"])
    budget = job["budget"] or "не указан — уточнить до оценки"
    deadline = job["deadline"] or "не указан — уточнить до оценки"
    url = job["url"] or "не сохранён"
    return (
        f"# {job['title']} · {PLATFORMS[job['platform']]}\n\n"
        f"- URL: {url}\n- Бюджет: {budget}\n- Срок: {deadline}\n"
        f"- Оценка: {analysis['score']} · {'ручная проверка обязательна' if analysis['manual_review'] else 'профильное совпадение'}\n"
        f"- Бесплатный отклик: {quota}\n- Найденные слова: {', '.join(analysis['terms'])}\n\n"
        f"## Почему совпало\n\n{reasons}\n\n"
        f"## Факты из резюме для этого отклика\n\n{facts}\n\n"
        f"## Черновик — проверьте вручную перед отправкой\n\n{proposal(job, analysis)}\n"
    )


def slug(value: str) -> str:
    value = value.lower().replace("ё", "е")
    value = re.sub(r"[^a-z0-9а-я]+", "-", value, flags=re.IGNORECASE).strip("-")
    return value[:60] or "job"


def process_jobs(jobs: list[dict[str, Any]], out_dir: Path, state_path: Path, quota_path: Path) -> int:
    state = load_json(state_path, empty_state())
    quota_config = load_json(quota_path, {})
    state.setdefault("seen", {})
    state.setdefault("sent", {})
    out_dir.mkdir(parents=True, exist_ok=True)
    found = 0
    for raw in jobs:
        job = clean_job(raw)
        keys = job_keys(job)
        duplicate_key = next((key for key in keys if key in state["seen"]), None)
        if duplicate_key:
            print(f"ДУБЛЬ · {job['title']} · уже обработан ({duplicate_key})")
            continue
        match = analyze(job)
        stamp = date.today().isoformat()
        state["seen"].update({key: {"platform": job["platform"], "title": job["title"], "date": stamp, "matched": match["matched"]} for key in keys})
        if not match["matched"]:
            print(f"ПРОПУСК · {job['title']} · нет ключевых совпадений")
            continue
        found += 1
        quota = platform_quota(job["platform"], state, quota_config, job)
        fingerprint = hashlib.sha256("|".join(keys).encode("utf-8")).hexdigest()[:8]
        filename = f"{stamp}-{job['platform']}-{slug(job['title'])}-{fingerprint}.md"
        draft_path = out_dir / filename
        draft_path.write_text(render_job(job, match, quota), encoding="utf-8")
        level = "ПРОВЕРИТЬ" if match["manual_review"] else "СОВПАДЕНИЕ"
        print(f"{level} · {job['title']} · {', '.join(match['terms'])} · {quota}")
        try:
            display_path = draft_path.relative_to(ROOT)
        except ValueError:
            display_path = draft_path
        print(f"Черновик: {display_path}")
    save_json(state_path, state)
    if not found:
        print("Подходящих новых задач нет.")
    return found


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Локальный помощник: поиск совпадений и черновики без входа на площадки.")
    sub = parser.add_subparsers(dest="command", required=True)

    match_parser = sub.add_parser("match", help="Обработать JSON или сохранённое .eml уведомление")
    match_parser.add_argument("--input", required=True, type=Path)
    match_parser.add_argument("--platform", help="Площадка для .eml: flru, kwork, peopleperhour, arc, toptal")
    match_parser.add_argument("--output-dir", type=Path, default=DRAFTS)
    match_parser.add_argument("--state", type=Path, default=STATE_FILE)
    match_parser.add_argument("--quotas", type=Path, default=QUOTA_FILE)

    manual_parser = sub.add_parser("manual", help="Передать описание задачи вручную")
    manual_parser.add_argument("--platform", required=True)
    manual_parser.add_argument("--title", required=True)
    manual_parser.add_argument("--description", required=True)
    manual_parser.add_argument("--url", default="")
    manual_parser.add_argument("--id", default="")
    manual_parser.add_argument("--budget", default="")
    manual_parser.add_argument("--deadline", default="")
    manual_parser.add_argument("--project-type", default="unknown", choices=["unknown", "for_all", "vacancy", "contest", "paid"])
    manual_parser.add_argument("--responses-remaining", type=int)
    manual_parser.add_argument("--output-dir", type=Path, default=DRAFTS)
    manual_parser.add_argument("--state", type=Path, default=STATE_FILE)
    manual_parser.add_argument("--quotas", type=Path, default=QUOTA_FILE)

    sent_parser = sub.add_parser("mark-sent", help="Записать уже вручную отправленный отклик")
    sent_parser.add_argument("--platform", required=True)
    sent_parser.add_argument("--job-id", default="")
    sent_parser.add_argument("--state", type=Path, default=STATE_FILE)

    quota_parser = sub.add_parser("quota", help="Показать квоты или задать локальный лимит Kwork")
    quota_parser.add_argument("--platform", choices=["kwork", "peopleperhour"], default="peopleperhour")
    quota_parser.add_argument("--limit", type=int, help="Бесплатная квота в месяц; для Kwork возьмите значение из аккаунта")
    quota_parser.add_argument("--state", type=Path, default=STATE_FILE)
    quota_parser.add_argument("--quotas", type=Path, default=QUOTA_FILE)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "match":
            path = args.input
            if not path.is_absolute():
                path = (ROOT / path).resolve()
            if path.suffix.lower() == ".eml":
                jobs = [parse_eml_job(path, args.platform)]
            elif path.suffix.lower() == ".json":
                jobs = parse_json_jobs(path)
            else:
                raise ValueError("Поддерживаются только файлы .eml и .json")
            process_jobs(jobs, args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir, args.state if args.state.is_absolute() else ROOT / args.state, args.quotas if args.quotas.is_absolute() else ROOT / args.quotas)
            return 0

        if args.command == "manual":
            job = clean_job({
                "platform": args.platform,
                "title": args.title,
                "description": args.description,
                "url": args.url,
                "id": args.id,
                "budget": args.budget,
                "deadline": args.deadline,
                "project_type": args.project_type,
                "responses_remaining": args.responses_remaining,
            })
            process_jobs([job], args.output_dir if args.output_dir.is_absolute() else ROOT / args.output_dir, args.state if args.state.is_absolute() else ROOT / args.state, args.quotas if args.quotas.is_absolute() else ROOT / args.quotas)
            return 0

        if args.command == "mark-sent":
            platform = normalize_platform(args.platform)
            state_path = args.state if args.state.is_absolute() else ROOT / args.state
            state = load_json(state_path, empty_state())
            month = date.today().strftime("%Y-%m")
            if args.job_id:
                sent_already = any(
                    item.get("platform") == platform and item.get("job_id", "").lower() == args.job_id.lower()
                    for item in state.get("sent_job_ids", [])
                )
                if sent_already:
                    print("Этот job-id уже отмечен как отправленный; счётчик не изменён.")
                    return 0
            sent = state.setdefault("sent", {}).setdefault(platform, {})
            sent[month] = int(sent.get(month, 0)) + 1
            if args.job_id:
                state.setdefault("sent_job_ids", []).append({"platform": platform, "job_id": args.job_id, "month": month})
            save_json(state_path, state)
            print(f"Отмечен отправленный отклик для {PLATFORMS[platform]} за {month}: {sent[month]}.")
            print("Команда ничего не отправляет на площадку.")
            return 0

        if args.command == "quota":
            state_path = args.state if args.state.is_absolute() else ROOT / args.state
            quota_path = args.quotas if args.quotas.is_absolute() else ROOT / args.quotas
            config = load_json(quota_path, {})
            if args.limit is not None:
                if args.limit < 0:
                    raise ValueError("Квота не может быть отрицательной")
                if args.platform != "kwork":
                    raise ValueError("Установить лимит можно только для Kwork; PeoplePerHour использует фиксированные 15 бесплатных credits в месяц")
                config.setdefault("kwork", {})["free_monthly_limit"] = args.limit
                save_json(quota_path, config)
            state = load_json(state_path, empty_state())
            month = date.today().strftime("%Y-%m")
            print(f"PeoplePerHour: {max(15 - int(state.get('sent', {}).get('peopleperhour', {}).get(month, 0)), 0)}/15 свободных credits за {month} по локальному учёту.")
            limit = config.get("kwork", {}).get("free_monthly_limit")
            if isinstance(limit, int):
                used = int(state.get("sent", {}).get("kwork", {}).get(month, 0))
                print(f"Kwork: {max(limit - used, 0)}/{limit} по установленной квоте за {month}; проверьте фактический баланс в аккаунте.")
            else:
                print("Kwork: лимит не настроен. После проверки аккаунта задайте его: nx run freelance-assistant:quota -- --platform kwork --limit N")
            return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
