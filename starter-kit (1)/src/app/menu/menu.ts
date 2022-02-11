import { CoreMenu } from '@core/types'

export const menu: CoreMenu[] = [
  {
    id: 'home',
    title: 'Dashboard',
    translate: '',
    type: 'item',
    icon: 'home',
    url: 'home'
  },

  {
    id: 'list',
    title: 'Gestion Personnels',
    translate: '',
    type: 'item',
    icon: 'users',
    role: ['Admin'],
    url: 'apps/user/user-list'
  },



  {
    id: 'clist',
    title: 'Gestion Clients',
    translate: '',
    type: 'item',
    icon: 'users',
    role: ['Admin'],
    url: 'apps/client/client-list'
  },


  {
    id: 'gestion',
    type: 'section',
    title: 'Gestion type',
    translate: '',
    icon: 'package',
    role: ['Admin'],
    children: [
      {
        id: "echantillon",
        title: "Echantillon",
        type: "collapsible",
        icon: 'list',
        children: [
          {
            id: 'nature',
            title: 'Nature',
            translate: '',
            type: 'item',
            icon: 'list',
            role: ['Admin'],
            url: 'apps/gestion/echantillon/nature'
          },
          {
            id: 'famille',
            title: 'Famille',
            translate: '',
            type: 'item',
            icon: 'home',
            role: ['Admin'],
            url: 'apps/gestion/echantillon/famille'
          },
        ]
      },
      {
        id: "essai",
        title: "Essai",
        type: "collapsible",
        icon: "list",
        children: [
          {
            id: "methode",
            title: "Methode",
            type: "item",
            icon: "tool",
            url: 'apps/gestion/essai/methode'
          },
          {
            id: "parametre",
            title: "Parametre",
            type: "item",
            icon: "tool",
            url: 'apps/gestion/essai/parametre'
          }
        ]
      }

    ]
  },


]
