import { Component, Inject, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { ColumnMode, DatatableComponent } from '@swimlane/ngx-datatable';
import { Router } from '@angular/router';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
import { CoreConfigService } from '@core/services/config.service';
import { CoreSidebarService } from '@core/components/core-sidebar/core-sidebar.service';
import { ClientListService } from './client-list.service';
import { componentFactoryName } from '@angular/compiler';
import { ToastrService } from 'ngx-toastr';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { cloneDeep } from 'lodash';

@Component({
  selector: 'app-client-list',
  templateUrl: './client-list.component.html',
  styleUrls: ['./client-list.component.scss']
})
export class ClientListComponent implements OnInit {
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
  public tempRow;
  public urlLastValue;
  // Decorator
  @ViewChild(DatatableComponent) table: DatatableComponent;

  // Private
  private tempData = [];
  private _unsubscribeAll: Subject<any>;

  /**
  * Constructor
  *
  * @param {CoreConfigService} _coreConfigService
  * @param {CoreSidebarService} _coreSidebarService
  */
  constructor(
    private _clientListService: ClientListService,
    private _coreSidebarService: CoreSidebarService,
    private _coreConfigService: CoreConfigService,
    private _toastr: ToastrService,
    private _router: Router,
    private modalservice: NgbModal,
    private router: Router

  ) {
    this._unsubscribeAll = new Subject();

  }
  toggleSidebar(name): void {
    this._coreSidebarService.getSidebarRegistry(name).toggleOpen();
  }
  filterUpdate(event) {
    this.selectedRole = this.selectRole[0];
    this.selectedPlan = this.selectPlan[0];
    this.selectedStatus = this.selectStatus[0];

    const val = event.target.value.toLowerCase();

    // Filter Our Data
    const temp = this.tempData.filter(function (d) {
      return d.email.toLowerCase().indexOf(val) !== -1 || !val || d.responsable.toLowerCase().indexOf(val) !== -1 || d.tel.toLowerCase().indexOf(val) !== -1 || d.raisonSocial.toLowerCase().indexOf(val) !== -1 || d.adresse.toLowerCase().indexOf(val) !== -1;
    });

    // Update The Rows
    this.rows = temp;
    // Whenever The Filter Changes, Always Go Back To The First Page
    this.table.offset = 0;
  }


  submit(form, modal) {
    if (form.valid) {
      form.form.value.idc = parseInt(this.urlLastValue);
      console.log(form.form.value)
      this._clientListService.updateClient(JSON.stringify(form.form.value)).subscribe(
        result => {
          if (result) {
            if (result['status'] == 200) {
              this._toastr.success('Client modifié', 'Succès!', {
                toastClass: 'toast ngx-toastr',
                closeButton: true
              });
              modal.close('Accept click')
              setTimeout(() => {                           // <<<---using ()=> syntax
                window.location.reload()
              }, 1100);

            }
            else if (result['status'] == 401) {
              localStorage.clear()
              this._toastr.error('Session expirée', 'Erreur!', {
                toastClass: 'toast ngx-toastr',
                closeButton: true
              });
              this.router.navigate(['/pages/authentication/login-v2']);
              //ntofiy session expired and redirect after 1.1 secs
            }
          }
        }
      )

    }
  }
  modalOpenSM(modalSM, id) {
    this.modal = modalSM;
    this.urlLastValue = id;
    this.modalservice.open(modalSM, {
      centered: true,
      size: 'lg' // size: 'xs' | 'sm' | 'lg' | 'xl'
    });

    this.rows.map(row => {
      console.log(row)
      if (row.idc == id) {
        this.currentRow = row;
        this.tempRow = cloneDeep(row);
      }
    });

  }
  deleteClient(id: any) {
    this._clientListService.deleteClient(id).subscribe(
      result => {
        if (result) {
          if (result['status'] == 200) {
            this._toastr.success('Client supprimé', 'Succès!', {
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
  ngOnInit(): void {
    this._coreConfigService.config.pipe(takeUntil(this._unsubscribeAll)).subscribe(config => {
      //! If we have zoomIn route Transition then load datatable after 450ms(Transition will finish in 400ms)
      if (config.layout.animation === 'zoomIn') {
        setTimeout(() => {

          this._clientListService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {

            this.rows = response.data;
            console.log(this.rows)
            this.tempData = this.rows;
          });
        }, 450);
      } else {

        this._clientListService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {


          this.rows = response.data;
          console.log(this.rows)
          this.tempData = this.rows;
        });
      }
    });

  }

}
