export interface SideNavItem {
  key: string
  label: string
}

export interface SideNavGroup {
  label: string
  items: SideNavItem[]
}

export interface TableColumn {
  key: string
  label: string
  mono?: boolean
}
