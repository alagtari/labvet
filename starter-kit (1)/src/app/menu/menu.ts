import { CoreMenu } from '@core/types'

export const menu: CoreMenu[] = [
  {
    id: 'home',
    title: 'Home',
    translate: 'MENU.HOME',
    type: 'item',
    icon: 'home',
    url: 'home'
  },
  {
    id: 'sample',
    title: 'Sample',
    translate: 'MENU.SAMPLE',
    type: 'item',
    icon: 'file',
    url: 'sample'
  },
  {
    id: 'apps',
    type: 'section',
    title: 'Apps & Pages',
    translate: '',
    icon: 'package',
    children: [
      {
        id: 'users',
        title: 'Utilisateurs',
        translate: '',
        type: 'collapsible',
        icon: 'user',
        children: [
          {
            id: 'list',
            title: 'List',
            translate: '',
            type: 'item',
            icon: 'circle',
            url: 'apps/user/user-list'
          },]
        }
    ]
  }

]
