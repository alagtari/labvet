import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NgSelectModule } from '@ng-select/ng-select';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { Ng2FlatpickrModule } from 'ng2-flatpickr';
import { SweetAlert2LoaderService, SweetAlert2Module } from '@sweetalert2/ngx-sweetalert2';
import { CoreCommonModule } from '@core/common.module';
import { CoreDirectivesModule } from '@core/directives/directives';
import { CorePipesModule } from '@core/pipes/pipes.module';
import { CoreSidebarModule } from '@core/components';
import { DepartementGestionComponent } from './departement-gestion/departement-gestion.component';
import { DepartementGestionService } from './departement-gestion/departement-gestion.service';
import { DepartementAddComponent } from './departement-add/departement-add.component';
import { DepartementAddService } from './departement-add/departement-add.service';
import { FamilleService } from '../echantillon/famille/famille.service';
import { NatureService } from '../echantillon/nature/nature.service';







// routing
const routes: Routes = [
    {
        path: 'gestion',
        component: DepartementGestionComponent,
        resolve: {
            dgs: DepartementGestionService
        },
        data: { animation: 'DepartementGestionComponent' }
    },
    {
        path: 'add',
        component: DepartementAddComponent,
        resolve: {

        },
        data: { animation: 'DepartementAddComponent' }
    }
];

@NgModule({
    declarations: [
        DepartementGestionComponent,
        DepartementAddComponent,
    ],
    imports: [
        CommonModule,
        SweetAlert2Module,
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
    providers: [DepartementGestionService, DepartementAddService, SweetAlert2LoaderService, FamilleService, NatureService]
})
export class DepartementModule { }
