import { Component, OnInit, ViewChild } from '@angular/core';
import { CoreSidebarService } from '@core/components/core-sidebar/core-sidebar.service';
import { UserListService } from '../user-list.service';
import { ToastrService, GlobalConfig } from 'ngx-toastr';
import { UserListComponent } from '../user-list.component';
@Component({
  selector: 'app-new-user-sidebar',
  templateUrl: './new-user-sidebar.component.html'
})
export class NewUserSidebarComponent implements OnInit {
  public fullname;
  public pattern = "^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$"
  public role;
  public tel;
  public cin;
  public photo;
  public cinPattern = "[0-1]\\d{7}"
  public unamePattern = "[2-5-4-7-9]\\d{7}";
  public contrat;
  public email;
  public photo_url;
  public contrat_url;


  @ViewChild(UserListComponent) childComponent: UserListComponent;
  /**
   * Constructor
   *
   * @param {CoreSidebarService} _coreSidebarService
   * @param {ToastrService} _toastr
   */
  constructor(private _coreSidebarService: CoreSidebarService, private _userService: UserListService, private _toastr: ToastrService) { }

  /**
   * Toggle the sidebar
   *
   * @param name
   */
  toggleSidebar(name): void {
    this._coreSidebarService.getSidebarRegistry(name).toggleOpen();
  }


  /**
   * Submit
   *
   * @param form
   */


  submit(form) {
    if (form.valid) {
      console.log(form.form.value)
      form.form.value.photo = this.photo_url;
      form.form.value.contrat = this.contrat_url;
      this._userService.addUser(JSON.stringify(form.form.value)).subscribe(
        result => {
          console.log(result)
          if (result.status == 200) {
            this._toastr.success('Utilisateur créé', 'Succès!', {
              toastClass: 'toast ngx-toastr',
              closeButton: true
            });
            this.childComponent.refreshFromParent();

          }
          else if (result.status == 400) {
            this._toastr.error("L'utilisateur existe déjà!", 'Erreur', {
              toastClass: 'toast ngx-toastr',
              closeButton: true
            });
          }

        }
      )
      //add api call for create user from the user-list service
      this.toggleSidebar('new-user-sidebar');
    }
  }


  onSelectFile(event: any, from: any) {
    console.log(from)// called each time file input changes
    if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();

      reader.readAsDataURL(event.target.files[0]); // read file as data url

      reader.onload = async (event) => { // called once readAsDataURL is completed
        if (from == "photo") {
          this.photo_url = event.target!.result as string;
        }
        else {
          this.contrat_url = event.target!.result as string;
        }


      }
    }
  }

  ngOnInit(): void { }
}
