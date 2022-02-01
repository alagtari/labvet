import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NgSelectModule } from '@ng-select/ng-select';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { Ng2FlatpickrModule } from 'ng2-flatpickr';

import { CoreCommonModule } from '@core/common.module';
import { CoreDirectivesModule } from '@core/directives/directives';
import { CorePipesModule } from '@core/pipes/pipes.module';
import { CoreSidebarModule } from '@core/components';



import { UserListComponent } from 'app/main/apps/user/user-list/user-list.component';
import { UserListService } from 'app/main/apps/user/user-list/user-list.service';

import { NewUserSidebarComponent } from 'app/main/apps/user/user-list/new-user-sidebar/new-user-sidebar.component';

// routing
const routes: Routes = [
  {
    path: 'user-list',
    component: UserListComponent,
    resolve: {
      uls: UserListService
    },
    data: { animation: 'UserListComponent' }
  },
  
  
  {
    path: 'user-view',
    redirectTo: '/apps/user/user-view/2' // Redirection
  },
  {
    path: 'user-edit',
    redirectTo: '/apps/user/user-edit/2' // Redirection
  }
];

@NgModule({
  declarations: [UserListComponent,  NewUserSidebarComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    CoreCommonModule,
    FormsModule,
    NgbModule,
    NgSelectModule,
    Ng2FlatpickrModule,
    NgxDatatableModule,
    CorePipesModule,
    CoreDirectivesModule,
    CoreSidebarModule
  ],
  providers: [UserListService]
})
export class UserModule {}
