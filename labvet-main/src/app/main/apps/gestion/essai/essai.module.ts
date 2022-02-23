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
import { MethodeComponent } from './methode/methode.component';
import { ParametreComponent } from './parametre/parametre.component';
import { MethodeService } from './methode/methode.service';
import { ParametreService } from './parametre/parametre.service';

// routing
const routes: Routes = [
    {
        path: 'methode',
        component: MethodeComponent,
        resolve: {
            ms: MethodeService
        },
        data: { animation: 'MethodeComponent' }
    },
    {
        path: 'parametre',
        component: ParametreComponent,
        resolve: {
            ps: ParametreService
        },
        data: { animation: 'ParametreComponent' }
    },
];

@NgModule({
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
    providers: [ParametreComponent, MethodeComponent, MethodeService, ParametreService]
})
export class EchantillonModule { }
