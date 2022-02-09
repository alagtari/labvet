import { Component, OnInit, ViewChild } from '@angular/core';
import { CoreSidebarService } from '@core/components/core-sidebar/core-sidebar.service';
import { ToastrService, GlobalConfig } from 'ngx-toastr';
import { ClientListService } from '../client-list.service';

@Component({
  selector: 'app-new-client-sidebar',
  templateUrl: './new-client-sidebar.component.html',
})
export class NewClientSidebarComponent implements OnInit {
  public unamePattern = "[2-5-4-7-9]\\d{7}";
  public pattern = "^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$"
  public email;
  public tel;
  public responsable;
  public adresse;
  public raisonSocial;

  /**
     * Constructor
     *
     * @param {CoreSidebarService} _coreSidebarService
     * @param {ToastrService} _toastr
     */
  constructor(private _coreSidebarService: CoreSidebarService, private _toastr: ToastrService, private _clientListService: ClientListService) { }

  /**
  * Toggle the sidebar
  *
  * @param name
  */
  toggleSidebar(name): void {
    this._coreSidebarService.getSidebarRegistry(name).toggleOpen();
  }

  submit(form) {
    if (form.valid) {
      form.form.value.idc = 0;
      this._clientListService.addClient(form.form.value).subscribe(
        result => {
          if (result.status == 200) {
            this._toastr.success('Client créé', 'Succès!', {
              toastClass: 'toast ngx-toastr',
              closeButton: true
            });
            setTimeout(() => {                           // <<<---using ()=> syntax
              window.location.reload()
            }, 1100);


          }
          else if (result.status == 400) {
            this._toastr.error("le client existe déjà!", 'Erreur', {
              toastClass: 'toast ngx-toastr',
              closeButton: true
            });
          }
        }
      )

      //ToDO
    }
  }
  ngOnInit(): void {
  }

}
