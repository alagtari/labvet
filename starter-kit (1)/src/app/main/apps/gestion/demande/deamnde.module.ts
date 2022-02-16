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
import { DemandeGestionComponent } from './demande-gestion/demande-gestion.component';
import { DemandeGestionService } from './demande-gestion/deamnde-gestion.service';
import { DemandeAddComponent } from './demande-add/demande-add.component';
import { DemandeAddService } from './demande-add/demande-add.service';
import { FamilleService } from '../echantillon/famille/famille.service';
import { NatureService } from '../echantillon/nature/nature.service';







// routing
const routes: Routes = [
    {
        path: 'gestion',
        component: DemandeGestionComponent,
        resolve: {
            dgs: DemandeGestionService
        },
        data: { animation: 'DemandeGestionComponent' }
    },
    {
        path: 'add',
        component: DemandeAddComponent,
        resolve: {

        },
        data: { animation: 'DemandeAddComponent' }
    }
];

@NgModule({
    declarations: [
        DemandeGestionComponent,
        DemandeAddComponent
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
    providers: [DemandeGestionService, DemandeAddService, SweetAlert2LoaderService, FamilleService, NatureService]
})
export class DemandeModule { }
