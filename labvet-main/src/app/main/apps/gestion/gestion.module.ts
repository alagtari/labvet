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
import { NatureComponent } from './echantillon/nature/nature.component';
import { FamilleComponent } from './echantillon/famille/famille.component';
import { MethodeComponent } from './essai/methode/methode.component';
import { ParametreComponent } from './essai/parametre/parametre.component';











// routing
const routes: Routes = [
    {
        path: 'echantillon',
        loadChildren: () => import('./echantillon/echantillon.module').then(m => m.EchantillonModule)
    },
    {
        path: 'essai',
        loadChildren: () => import('./essai/essai.module').then(m => m.EchantillonModule)
    },
    {
        path: 'demande',
        loadChildren: () => import('./demande/deamnde.module').then
            (m => m.DemandeModule)
    },
    {
        path: 'departement',
        loadChildren: () => import('./departement/departement.module').then
            (m => m.DepartementModule)
    }
];

@NgModule({
    declarations: [NatureComponent, FamilleComponent, MethodeComponent, ParametreComponent,],
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
})
export class GestionModule { }
