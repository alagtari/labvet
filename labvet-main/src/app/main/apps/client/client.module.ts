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
import { ClientListComponent } from './client-list/client-list.component';
import { NewClientSidebarComponent } from './client-list/new-client-sidebar/new-client-sidebar.component';
import { ClientListService } from './client-list/client-list.service';

// routing
const routes: Routes = [
    {
        path: 'client-list',
        component: ClientListComponent,
        resolve: {
            cls: ClientListService
        },
        data: { animation: 'ClientListComponent' }
    },
];

@NgModule({
    declarations: [ClientListComponent, NewClientSidebarComponent],
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
    providers: [ClientListService]
})
export class ClientModule { }
