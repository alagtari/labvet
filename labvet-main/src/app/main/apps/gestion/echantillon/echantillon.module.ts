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


import { NatureComponent } from './nature/nature.component';
import { FamilleComponent } from './famille/famille.component';
import { NatureService } from './nature/nature.service';
import { FamilleService } from './famille/famille.service';

// routing
const routes: Routes = [
    {
        path: 'nature',
        component: NatureComponent,
        resolve: {
            ns: NatureService
        },
        data: { animation: 'NatureComponent' }
    },
    {
        path: 'famille',
        component: FamilleComponent,
        resolve: {
            fs: FamilleService
        },
        data: { animation: 'FamilleComponent' }
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
    providers: [NatureComponent, FamilleComponent, NatureService, FamilleService]
})
export class EchantillonModule { }
