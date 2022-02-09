import { Component, Inject, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subject } from 'rxjs';
import { Router } from '@angular/router';
import { ColumnMode, DatatableComponent } from '@swimlane/ngx-datatable';
import { NatureService } from './nature.service';
import { CoreConfigService } from '@core/services/config.service';
import { takeUntil } from 'rxjs/operators';
import { ToastrService } from 'ngx-toastr';
@Component({
  selector: 'app-nature',
  templateUrl: './nature.component.html',
  styleUrls: ['./nature.component.scss']
})


export class NatureComponent implements OnInit {
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
  public _unsubscribeAll;
  constructor(private modalservice: NgbModal, private _natureService: NatureService, private _coreConfigService: CoreConfigService, private _router: Router, private _toastr: ToastrService) {
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
      console.log(d)

      return d.designation.toLowerCase().indexOf(val) !== -1 || !val;
    });

    // Update The Rows
    this.rows = temp;
    // Whenever The Filter Changes, Always Go Back To The First Page
    this.table.offset = 0;
  }
  addNature(modal) {
    let name = (<HTMLInputElement>document.getElementById("designation")).value
    this._natureService.addNature({ "designation": name, "id": 0 }).subscribe(result => {
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
  deleteNature(id) {
    console.log(this.rows)
    this.rows.map(row => {
      if (row.id == id) {
        this.rows.splice(this.rows.indexOf(row), 1)
      }
    })
    console.log(id)
    this._natureService.deleteNature(id).subscribe(
      result => {
        if (result) {
          if (result['status'] == 200) {
            this._toastr.success('Nature supprimé', 'Succès!', {
              toastClass: 'toast ngx-toastr',
              closeButton: true
            });

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
    console.log(form.form.value)
    form.form.value.id = 0
    if (form.valid) {

      this._natureService.addNature(form.form.value).subscribe(
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
    this._natureService.getFamilles().subscribe(
      familles => {
        this.familles = familles['data'];

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

          this._natureService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {
            console.log(this.rows)
            this.rows = response;
            this.tempData = this.rows;
          });
        }, 450);
      } else {

        this._natureService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {
          console.log(this.rows)
          this.rows = response;
          this.tempData = this.rows;
        });
      }
    });
  }

}
