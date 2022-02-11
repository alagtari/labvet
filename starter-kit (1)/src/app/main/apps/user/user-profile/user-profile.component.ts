import { Component, OnInit, OnDestroy, ViewEncapsulation } from '@angular/core';

import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
import { FlatpickrOptions } from 'ng2-flatpickr';
import { UserProfileService } from './user-profile.service';
import { CoreConfigService } from '@core/services/config.service';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import * as CryptoJS from "crypto-js";

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit {

  public contentHeader: object;
  public oldpwdwrng = false;
  public data: any;
  public birthDateOptions: FlatpickrOptions = {
    altInput: true
  };
  public passwordTextTypeOld = false;
  public passwordTextTypeNew = false;
  public passwordTextTypeRetype = false;
  public avatarImage: string;
  public pwdmatch = false;

  // private
  private _unsubscribeAll: Subject<any>;

  /**
   * Constructor
   *
   * @param {CoreConfigService} _coreConfigService
   * @param {UserProfileComponent} _profileService
   */
  constructor(private _profileService: UserProfileService, private _coreConfigService: CoreConfigService, private _router: Router, private _toastr: ToastrService) {
    this._unsubscribeAll = new Subject();
  }

  // Public Methods
  // -----------------------------------------------------------------------------------------------------

  /**
   * Toggle Password Text Type Old
   */
  togglePasswordTextTypeOld() {
    this.passwordTextTypeOld = !this.passwordTextTypeOld;
  }

  /**
   * Toggle Password Text Type New
   */
  togglePasswordTextTypeNew() {
    this.passwordTextTypeNew = !this.passwordTextTypeNew;
  }

  /**
   * Toggle Password Text Type Retype
   */
  togglePasswordTextTypeRetype() {
    this.passwordTextTypeRetype = !this.passwordTextTypeRetype;
  }

  /**
   * Upload Image
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
  submitPassword(form) {
    let oldpassword = (<HTMLInputElement>document.getElementById("account-old-password")).value
    const hash = CryptoJS.MD5(CryptoJS.enc.Latin1.parse(oldpassword));
    const md5_pwd = hash.toString(CryptoJS.enc.Hex)
    if (md5_pwd != this.data.password) {
      this.oldpwdwrng = true;
    }
    else {
      this.oldpwdwrng = false;
      let newpwd = (<HTMLInputElement>document.getElementById("account-new-password")).value
      let newpwdretype = (<HTMLInputElement>document.getElementById("account-retype-new-password")).value
      if (newpwd != newpwdretype) {
        this.pwdmatch = true
      }
      else {
        this.pwdmatch = false;
        form.form.value.password = newpwd;
        form.form.value.name = this.data.name;
        form.form.value.photo = this.data.photo;
        form.form.value.role = this.data.role;
        form.form.value.id = this.data.id;
        form.form.value.tel = this.data.tel;
        form.form.value.cin = this.data.cin;
        form.form.value.email = this.data.email
        this._profileService.updateUser(form.form.value).subscribe(
          result => {
            if (result) {
              if (result['status'] == 200) {
                this._toastr.success('Utilisateur supprimé', 'Succès!', {
                  toastClass: 'toast ngx-toastr',
                  closeButton: true
                });
                setTimeout(() => {                           // <<<---using ()=> syntax
                  window.location.reload()
                }, 1100);
                console.log(this.data)

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
    }

  }
  submit(form) {
    form.form.value.photo = this.avatarImage;
    form.form.value.password = this.data.password;
    form.form.value.role = this.data.role;
    form.form.value.id = this.data.id;
    if (form) {
      this._profileService.updateUser(form.form.value).subscribe(
        result => {
          if (result) {
            if (result['status'] == 200) {
              this._toastr.success('Utilisateur supprimé', 'Succès!', {
                toastClass: 'toast ngx-toastr',
                closeButton: true
              });
              setTimeout(() => {                           // <<<---using ()=> syntax
                window.location.reload()
              }, 1100);
              console.log(this.data)

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
  }

  ngOnInit(): void {
    // Subscribe config change
    this._coreConfigService.config.pipe(takeUntil(this._unsubscribeAll)).subscribe(config => {
      //! If we have zoomIn route Transition then load datatable after 450ms(Transition will finish in 400ms)
      if (config.layout.animation === 'zoomIn') {
        setTimeout(() => {

          this._profileService.getUser().subscribe(
            result => {
              this.data = result.data;
              this.avatarImage = this.data.photo
              console.log(this.data)
            }
          )
        }, 450);
      } else {

        this._profileService.getUser().subscribe(
          result => {
            this.data = result.data;
            this.avatarImage = this.data.photo
            console.log(this.data)
          }
        )
      }
    });

  }

}
