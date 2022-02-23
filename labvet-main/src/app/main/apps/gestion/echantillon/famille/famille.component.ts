import { Component, Inject, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subject } from 'rxjs';
import { Router } from '@angular/router';
import { ColumnMode, DatatableComponent } from '@swimlane/ngx-datatable';
import { CoreConfigService } from '@core/services/config.service';
import { takeUntil } from 'rxjs/operators';
import { ToastrService } from 'ngx-toastr';
import { FamilleService } from './famille.service';

@Component({
  selector: 'app-famille',
  templateUrl: './famille.component.html',
  styleUrls: ['./famille.component.scss']
})
export class FamilleComponent implements OnInit {

  @ViewChild(DatatableComponent) table: DatatableComponent;
  public sidebarToggleRef = false;
  public rows;
  public selectedOption = 10;
  public ColumnMode = ColumnMode;
  public temp = [];
  public previousRoleFilter = 'All';
  public previousPlanFilter = '';
  public previousStatusFilter = '';
  public currentRow;
  public rowsz
  public avatarImage;
  public selectRole: any = [
    { name: 'All', value: '' },
    { name: 'Réceptionniste', value: 'Réceptionniste' },
    { name: 'technicien', value: 'technicien' },
  ];

  public selectPlan: any = [
    { name: 'All', value: '' },
    { name: 'Basic', value: 'Basic' },
    { name: 'Company', value: 'Company' },
    { name: 'Enterprise', value: 'Enterprise' },
    { name: 'Team', value: 'Team' }
  ];

  public selectStatus: any = [
    { name: 'All', value: '' },
    { name: 'Pending', value: 'Pending' },
    { name: 'Active', value: 'Active' },
    { name: 'Inactive', value: 'Inactive' }
  ];

  public selectedRole = [];
  public selectedPlan = [];
  public selectedStatus = [];
  public searchValue = '';
  public modal;
  public familles;
  public tempData;
  public tempRow;
  public urlLastValue;
  public items;
  public _unsubscribeAll;
  constructor(private modalservice: NgbModal, private _familleService: FamilleService, private _coreConfigService: CoreConfigService, private _router: Router, private _toastr: ToastrService) {
    this._unsubscribeAll = new Subject();
  }
  filterUpdate(event) {
    // Reset ng-select on search
    this.selectedRole = this.selectRole[0];
    this.selectedPlan = this.selectPlan[0];
    this.selectedStatus = this.selectStatus[0];

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
  addNature(modal) {
    let name = (<HTMLInputElement>document.getElementById("designation")).value
    this._familleService.addFamille({ "designation": name, "famille_id": 0, "id": 0 }).subscribe(result => {
      if (result) {
        if (result['status'] == 200) {
          this._toastr.success('Nature Ajoutée', 'Succès!', {
            toastClass: 'toast ngx-toastr',
            closeButton: true
          });
          modal.close('Accept click')
          setTimeout(() => {                           // <<<---using ()=> syntax
            window.location.reload()
          }, 1100);
        }
        else if (result['status'] == 401) {
          this._toastr.error('Session expirée', 'Erreur!', {
            toastClass: 'toast ngx-toastr',
            closeButton: true
          });
          this._router.navigate(['/pages/authentication/login-v2']);
          //ntofiy session expired and redirect after 1.1 secs
        }
      }
    })
  }
  deleteFamille(id) {
    console.log(this.rows)
    this.rows.map(row => {
      if (row.id == id) {
        this.rows.splice(this.rows.indexOf(row), 1)
      }
    })
    console.log(id)
    this._familleService.deleteFamille(id).subscribe(
      result => {
        if (result) {
          if (result['status'] == 200) {
            this._toastr.success('Nature supprimé', 'Succès!', {
              toastClass: 'toast ngx-toastr',
              closeButton: true
            });
            setTimeout(() => {                           // <<<---using ()=> syntax
              window.location.reload()
            }, 1100);

          }

          else if (result['status'] == 401) {
            localStorage.removeItem("currentUser")
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
  submit(form, modal) {
    form.form.value.idf = 0
    form.form.value.idn = form.form.value.nature.id
    delete form.form.value.nature
    console.log(form.form.value)
    if (form.valid) {

      this._familleService.addFamille(form.form.value).subscribe(
        result => {
          if (result) {
            if (result['status'] == 200) {
              this._toastr.success('Nature Ajoutée', 'Succès!', {
                toastClass: 'toast ngx-toastr',
                closeButton: true
              });
              modal.close('Accept click')
              setTimeout(() => {                           // <<<---using ()=> syntax
                window.location.reload()
              }, 1100);
            }
            else if (result['status'] == 400) {

              //error
            }
            else {

            }
          }
        }
      )

    }

  }

  modalOpenSM(modalSM) {
    this._familleService.getNatures().subscribe(
      result => {
        this.items = result.data;
      }
    )
    this.modal = modalSM;
    this.modalservice.open(modalSM, {
      centered: true,

      size: 'sm' // size: 'xs' | 'sm' | 'lg' | 'xl'
    });
  }
  ngOnInit(): void {
    this._coreConfigService.config.pipe(takeUntil(this._unsubscribeAll)).subscribe(config => {
      //! If we have zoomIn route Transition then load datatable after 450ms(Transition will finish in 400ms)
      if (config.layout.animation === 'zoomIn') {
        setTimeout(() => {

          this._familleService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {
            console.log(this.rows)
            this.rows = response;
            this.tempData = this.rows;
          });
        }, 450);
      } else {

        this._familleService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {
          console.log(this.rows)
          this.rows = response;
          this.tempData = this.rows;
        });
      }
    });
  }

}
