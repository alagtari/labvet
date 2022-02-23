import { Component, Inject, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subject } from 'rxjs';
import { Router } from '@angular/router';
import { ColumnMode, DatatableComponent } from '@swimlane/ngx-datatable';
import { CoreConfigService } from '@core/services/config.service';
import { takeUntil } from 'rxjs/operators';
import { ToastrService } from 'ngx-toastr';
import { ParametreService } from './parametre.service';

@Component({
  selector: 'app-parametre',
  templateUrl: './parametre.component.html',
  styleUrls: ['./parametre.component.scss']
})
export class ParametreComponent implements OnInit {

  @ViewChild(DatatableComponent) table: DatatableComponent;
  public sidebarToggleRef = false;
  public selectMultiSelected;
  public selectMultiSelected_deps;
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
  public methodes_param;
  public methodes;
  public natures;
  public familles;
  public tempData;
  public tempRow;
  public urlLastValue;
  public _unsubscribeAll;
  constructor(private modalservice: NgbModal, private _parametreService: ParametreService, private _coreConfigService: CoreConfigService, private _router: Router, private _toastr: ToastrService) {
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

      return d.nomf.toLowerCase().indexOf(val) !== -1 || !val || d.designation.toLowerCase().indexOf(val)! == -1;
    });

    // Update The Rows
    this.rows = temp;
    // Whenever The Filter Changes, Always Go Back To The First Page
    this.table.offset = 0;
  }
  addParametre(modal) {
    let name = (<HTMLInputElement>document.getElementById("designation")).value
    this._parametreService.addParametre({ "nomp": name, "id": 0 }).subscribe(result => {
      if (result) {
        if (result['status'] == 200) {
          this._toastr.success('Parametre Ajoutée', 'Succès!', {
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
  deleteParametre(id) {
    console.log(this.rows)
    this.rows.map(row => {
      if (row.id == id) {
        this.rows.splice(this.rows.indexOf(row), 1)
      }
    })
    console.log(id)
    this._parametreService.deleteParametre(id).subscribe(
      result => {
        if (result) {
          if (result['status'] == 200) {
            this._toastr.success('Parametre supprimé', 'Succès!', {
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
    let deps_ids = []
    for (let i = 0; i < this.selectMultiSelected_deps.length; i++) {
      deps_ids.push(this.selectMultiSelected_deps[i].id)
    }
    let data: { id: number, nomp: string, id_dep: any } = { id: 0, nomp: form.form.value.designation, id_dep: deps_ids }
    if (form.valid) {

      this._parametreService.addParametre(data).subscribe(
        result => {
          console.log(result)
          if (result) {
            if (result['status'] == 200) {
              let id = result.id
              for (let i = 0; i < this.selectMultiSelected.length; i++) {
                let data = { idp: id, idm: this.selectMultiSelected[i].id }
                this._parametreService.addPM(data).subscribe(
                  result => {
                    if (result) {
                      let data2 = { idp: id, idn: form.form.value.nature.id }
                      this._parametreService.addPN(data2).subscribe(
                        results => {
                          if (results) {
                            this._toastr.success('Parametre Ajoutée', 'Succès!', {
                              toastClass: 'toast ngx-toastr',
                              closeButton: true
                            });
                            modal.close('Accept click')
                            setTimeout(() => {                           // <<<---using ()=> syntax
                              window.location.reload()
                            }, 1100);
                          }
                        }
                      )
                    }
                  }
                )
              }



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
  AfficherMethodes(modal, methodes) {
    this.methodes_param = methodes;
    console.log(this.methodes_param)
    this.modalservice.open(modal, {
      centered: true,

      size: 'sm' // size: 'xs' | 'sm' | 'lg' | 'xl'
    });
  }
  public departements;
  modalOpenSM(modalSM) {
    this._parametreService.getMethodes().subscribe(result => {
      this.methodes = result.data;
    })
    this._parametreService.getDepartements().subscribe(result => {
      this.departements = result.data;
    })
    this._parametreService.getNatures().subscribe(r => {
      this.natures = r.data;
    })
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

          this._parametreService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {

            this.rows = response;
            console.log(this.rows)
            this.tempData = this.rows;
          });
        }, 450);
      } else {

        this._parametreService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {

          this.rows = response;
          console.log(this.rows)
          this.tempData = this.rows;
        });
      }
    });
  }
}
