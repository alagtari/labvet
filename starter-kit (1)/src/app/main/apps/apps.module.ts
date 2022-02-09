import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { FullCalendarModule } from '@fullcalendar/angular';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';
import listPlugin from '@fullcalendar/list';
import timeGridPlugin from '@fullcalendar/timegrid';

// routing
const routes: Routes = [
  {
    path: 'user',
    loadChildren: () => import('./user/user.module').then(m => m.UserModule)
  },
  {
    path: 'gestion',
    loadChildren: () => import('./gestion/gestion.module').then(m => m.GestionModule)
  },
  {
    path: 'client',
    loadChildren: () => import('./client/client.module').then(m => m.ClientModule)
  },

];

FullCalendarModule.registerPlugins([dayGridPlugin, timeGridPlugin, listPlugin, interactionPlugin]);

@NgModule({
  declarations: [

  ],
  imports: [CommonModule, RouterModule.forChild(routes)]
})
export class AppsModule { }
