import { Component, Inject, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subject } from 'rxjs';
import { Router } from '@angular/router';
import { ColumnMode, DatatableComponent } from '@swimlane/ngx-datatable';
import { CoreConfigService } from '@core/services/config.service';
import { takeUntil } from 'rxjs/operators';
import { ToastrService } from 'ngx-toastr';
import { DemandeGestionService } from './deamnde-gestion.service';

@Component({
  selector: 'app-demande-gestion',
  templateUrl: './demande-gestion.component.html',
  styleUrls: ['./demande-gestion.component.scss']
})
export class DemandeGestionComponent implements OnInit {
  @ViewChild(DatatableComponent) table: DatatableComponent;
  public ColumnMode = ColumnMode;
  public selectedOption = 10;
  public tempData;
  public tempRow;
  public temp = [];
  public rows: any;
  public searchValue: any;
  public _unsubscribeAll;
  constructor(private _coreConfigService: CoreConfigService, private _router: Router, private _toastr: ToastrService, private _service: DemandeGestionService) {
    this._unsubscribeAll = new Subject();

  }
  filterUpdate(event) {
    // Reset ng-select on search

    const val = event.target.value.toLowerCase();

    // Filter Our Data
    const temp = this.tempData.filter(function (d) {
      return d.nomf.toLowerCase().indexOf(val) !== -1 || !val || d.nature.toLowerCase().indexOf(val) !== -1;
    });

    // Update The Rows
    this.rows = temp;
    // Whenever The Filter Changes, Always Go Back To The First Page
    this.table.offset = 0;
  }
  ToAdd() {
    this._router.navigate(['/apps/gestion/demande/add'])
  }
  deleteDemande(id: any) {
    this._service.deleteDemande(id).subscribe(
      result => {
        if (result) {
          if (result['status'] == 200) {
            this._toastr.success('Demande supprimée', 'Succès!', {
              toastClass: 'toast ngx-toastr',
              closeButton: true
            });

          }

          else if (result['status'] == 401) {
            localStorage.clear()
            this._toastr.error('Session expirée', 'Erreur!', {
              toastClass: 'toast ngx-toastr',
              closeButton: true
            });
            this._router.navigate(['/home']);
          }
          else {
            console.log(result)
          }
        }
      }
    )
  }
  ngOnInit(): void {
    this._coreConfigService.config.pipe(takeUntil(this._unsubscribeAll)).subscribe(config => {
      //! If we have zoomIn route Transition then load datatable after 450ms(Transition will finish in 400ms)
      if (config.layout.animation === 'zoomIn') {
        setTimeout(() => {

          this._service.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {

            this.rows = response;
            this.tempData = this.rows;
            console.log(this.rows)
          });
        }, 450);
      } else {

        this._service.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {
          this.rows = response;
          this.tempData = this.rows;
          console.log(this.rows)
        });
      }
    });
  }

}
