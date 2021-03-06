import { CoreMenu } from '@core/types'

export const menu: CoreMenu[] = [
  {
    id: 'home',
    title: 'Menu',
    translate: '',
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
    title: 'PERSONNELS',
    translate: '',
    icon: 'package',
    role : ['Admin'],
    children: [
      {
        id: 'list',
        title: 'Liste',
        translate: '',
        type: 'item',
        icon: 'list',
        role : ['Admin'],
        url: 'apps/user/user-list'
      }
    ]
  }

]
