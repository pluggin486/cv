# SS Core workspace

Nx monorepo for the portfolio, the SS Core design-system sandbox, and its shared Vue UI library.

## Projects

| Nx project | Path | Purpose |
| --- | --- | --- |
| `portfolio` | repository root | Семён Сергеев's frontend portfolio |
| `design-system-sandbox` | `apps/design-system-sandbox` | Standalone design-system overview and examples |
| `ss-core-ui` | `libs/ss-core-ui` | Buildable Vue components and design tokens (`@ss/core-ui`) |

The portfolio remains at `/`. The sandbox overview is also `/` on its own app; its pages are `/colors`, `/typography`, `/spacing`, `/radius-shadows`, `/components`, `/assets`, and `/applied`.

## Commands

```bash
npm install
npx nx show projects
npx nx serve portfolio                 # http://localhost:3000
npx nx serve design-system-sandbox     # http://localhost:3001
npx nx build portfolio
npx nx build design-system-sandbox
npx nx run-many -t build
npx nx affected -t build
```

Application builds depend on the UI library build. Nx's project graph includes both application-to-library dependencies.

## Vercel

Create a Vercel project from this repository with Root Directory `apps/design-system-sandbox`. The app's `vercel.json` runs `npm ci` and the Nx build from the repository root, while Vercel includes source files outside the app root. Nitro writes the Vercel Build Output API to the app's `.vercel/output` directory.

## UI library

Components live in `libs/ss-core-ui/src/components`; design tokens live in `libs/ss-core-ui/src/styles/tokens.css`. Nuxt apps scan the shared component directory for typed `Ui*` auto-imports and consume the generated package CSS.
