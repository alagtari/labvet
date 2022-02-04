import { Component, Inject, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { ColumnMode, DatatableComponent } from '@swimlane/ngx-datatable';
import { Router } from '@angular/router';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';

import { CoreConfigService } from '@core/services/config.service';
import { CoreSidebarService } from '@core/components/core-sidebar/core-sidebar.service';

import { UserListService } from 'app/main/apps/user/user-list/user-list.service';
import { componentFactoryName } from '@angular/compiler';
import { ToastrService } from 'ngx-toastr';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { UserEditService } from '../user-edit/user-edit.service';
import { cloneDeep } from 'lodash';
@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class UserListComponent implements OnInit {
  // Public
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
   * @param {UserListService} _userListService
   * @param {CoreSidebarService} _coreSidebarService
   */
  constructor(
    private _userListService: UserListService,
    private _coreSidebarService: CoreSidebarService,
    private _coreConfigService: CoreConfigService,
    private _toastr: ToastrService,
    private _router: Router,
    private modalservice : NgbModal,
    private _userEditService : UserEditService,
    private router : Router
  ) {
    this._unsubscribeAll = new Subject();
  }

  // Public Methods
  // -----------------------------------------------------------------------------------------------------

  /**
   * filterUpdate
   *
   * @param event
   */

  uploadImage(event: any) {
    if (event.target.files && event.target.files[0]) {
      let reader = new FileReader();

      reader.onload = (event: any) => {
        this.avatarImage = event.target.result;
      };

      reader.readAsDataURL(event.target.files[0]);
    }
  }

  /**
   * Submit
   *
   * @param form
   */
  submit(form  , modal) {
    if (form.valid) {
      form.form.value.photo = this.avatarImage;
      form.form.value.id = parseInt(this.urlLastValue);
      console.log(form.form.value)
      this._userEditService.updateUser(JSON.stringify(form.form.value)).subscribe(
        result => {
          if (result) {
            if (result['status'] == 200) {
              this._toastr.success('aaaaa', 'aaaa', {
                toastClass: 'toast ngx-toastr',
                closeButton: true
              });
              modal.close('Accept click')
              setTimeout(() => {                           // <<<---using ()=> syntax
                this.router.navigate(['/apps/user/user-list']);
              }, 1100);

            }
            else if (result['status'] == 401) {
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

   modalOpenSM(modalSM  , id) {
     this.modal = modalSM;
     this.urlLastValue = id;
    this.modalservice.open(modalSM, {
      centered: true,
      size: 'lg' // size: 'xs' | 'sm' | 'lg' | 'xl'
    });
    
      this.rows.map(row => {
        console.log(row)
        if (row.id == id) {
          this.currentRow = row;
          this.avatarImage = this.currentRow.photo;
          this.tempRow = cloneDeep(row);
        }
      });
   
  }

  showContrat(contrat: any) {
    var image = new Image();
    image.src = contrat;

    var w = window.open("");
    w.document.write(image.outerHTML);
  }

  filterUpdate(event) {
    // Reset ng-select on search
    this.selectedRole = this.selectRole[0];
    this.selectedPlan = this.selectPlan[0];
    this.selectedStatus = this.selectStatus[0];

    const val = event.target.value.toLowerCase();

    // Filter Our Data
    const temp = this.tempData.filter(function (d) {

      return d.name.toLowerCase().indexOf(val) !== -1 || !val || d.email.toLowerCase().indexOf(val) !== -1 || d.tel.toLowerCase().indexOf(val) !== -1 || d.cin.toLowerCase().indexOf(val) !== -1 || d.role.toLowerCase().indexOf(val) !== -1;
    });

    // Update The Rows
    this.rows = temp;
    // Whenever The Filter Changes, Always Go Back To The First Page
    this.table.offset = 0;
  }

  /**
   * Toggle the sidebar
   *
   * @param name
   */
  toggleSidebar(name): void {
    this._coreSidebarService.getSidebarRegistry(name).toggleOpen();
  }

  /**
   * Filter By Roles
   *
   * @param event
   */
  filterByRole(event) {
    const filter = event ? event.value : '';
    this.previousRoleFilter = filter;
    this.temp = this.filterRows(filter, this.previousPlanFilter, this.previousStatusFilter);
    this.rows = this.temp;
  }

  /**
   * Filter By Plan
   *
   * @param event
   */


  filterByPlan(event) {
    const filter = event ? event.value : '';
    this.previousPlanFilter = filter;
    this.temp = this.filterRows(this.previousRoleFilter, filter, this.previousStatusFilter);
    this.rows = this.temp;
  }

  /**
   * Filter By Status
   *
   * @param event
   */
  filterByStatus(event) {
    const filter = event ? event.value : '';
    this.previousStatusFilter = filter;
    this.temp = this.filterRows(this.previousRoleFilter, this.previousPlanFilter, filter);
    this.rows = this.temp;
  }

  /**
   * Filter Rows
   *
   * @param roleFilter
   * @param planFilter
   * @param statusFilter
   */
  filterRows(roleFilter, planFilter, statusFilter): any[] {
    // Reset search on select change
    this.searchValue = '';

    roleFilter = roleFilter.toLowerCase();
    planFilter = planFilter.toLowerCase();
    statusFilter = statusFilter.toLowerCase();

    return this.tempData.filter(row => {
      const isPartialNameMatch = row.role.toLowerCase().indexOf(roleFilter) !== -1 || !roleFilter;

      return isPartialNameMatch;
    });
  }

  // Lifecycle Hooks
  // -----------------------------------------------------------------------------------------------------
  /**
   * On init
   */
  deleteUser(id) {
    console.log(this.rows)
    this.rows.map(row => {
      if(row.id==id){
        this.rows.splice(this.rows.indexOf(row) , 1)
      }
    })
    console.log(id)
    this._userListService.deleteUser(id).subscribe(
      result => {
        if (result) {
          if (result['status'] == 200) {
            this._toastr.success('Utilisateur supprimé', 'Succès!', {
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
  refreshFromParent() {
    window.location.reload();
  }
  ngOnInit(): void {
    // Subscribe config change
    this._coreConfigService.config.pipe(takeUntil(this._unsubscribeAll)).subscribe(config => {
      //! If we have zoomIn route Transition then load datatable after 450ms(Transition will finish in 400ms)
      if (config.layout.animation === 'zoomIn') {
        setTimeout(() => {

          this._userListService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {
            console.log(this.rows)
            this.rows = response;
            this.tempData = this.rows;
          });
        }, 450);
      } else {

        this._userListService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {
          console.log(this.rows)
          this.rows = response;
          this.tempData = this.rows;
        });
      }
    });

  }

  /**
   * On destroy
   */
  ngOnDestroy(): void {
    // Unsubscribe from all subscriptions
    this._unsubscribeAll.next();
    this._unsubscribeAll.complete();
  }
}
