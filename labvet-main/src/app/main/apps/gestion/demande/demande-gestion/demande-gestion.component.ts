import { Component, EventEmitter, Inject, OnInit, Output, ViewChild, ViewEncapsulation } from '@angular/core';
import { NgbDateStruct, NgbModal } from '@ng-bootstrap/ng-bootstrap';
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
  @Output() dateSelect = new EventEmitter<NgbDateStruct>();
  @ViewChild(DatatableComponent) table: DatatableComponent;
  public ColumnMode = ColumnMode;
  public selectedOption = 10;
  public tempData;
  public selected_echantillons;
  public selected_echantillons_edit;
  public tempRow;
  public basicDPdata: NgbDateStruct;
  public previousPlanFilter = '';
  public previousStatusFilter = '';
  public selected_controle;
  public temp = [];
  public selectedEtat = [];
  public selectedControle = [];
  public selectControle = [
    {
      name: "Auto-Controle", value: "Auto-Controle"
    },
    {
      name: "controle officiel", value: "controle officiel"
    }
  ]

  public selectEtat = [
    {
      name: "Demandes en cours", value: "en cours"
    },
    {
      name: "Demandes traitées", value: "traite"
    }
  ]

  public rows: any;
  public searchValue: any;
  public previousControleFilter = ''
  public previousEtatFilter = '';
  public _unsubscribeAll;
  constructor(private modalservice: NgbModal, private _coreConfigService: CoreConfigService, private _router: Router, private _toastr: ToastrService, private _service: DemandeGestionService) {
    this._unsubscribeAll = new Subject();

  }
  filterByControle(event: any) {
    const filter = event ? event.value : '';
    this.previousControleFilter = filter;
    this.temp = this.filterRows(filter, this.previousEtatFilter, this.previousStatusFilter);
    this.rows = this.temp;
  }
  filterByEtat(event: any) {
    const filter = event ? event.value : '';
    this.previousEtatFilter = filter;
    this.temp = this.filterRows(this.previousControleFilter, filter, this.previousStatusFilter);
    this.rows = this.temp;
  }
  dateCompare(event) {
    console.log(event)
    this.searchValue = '';
    const temp = this.tempData.filter(function (row) {
      let currentDate = { day: 0, month: 0, year: 0 };
      let dateData = row.date_reception.split('-')
      currentDate.year = dateData[0]
      currentDate.month = dateData[1]
      currentDate.day = dateData[2].split(' ')[0]
      const match = (event.day == currentDate.day && event.month == currentDate.month && event.year == currentDate.year) || event == "none"
      return match
    })
    this.rows = temp;
    // Whenever The Filter Changes, Always Go Back To The First Page
    this.table.offset = 0;
  }
  filterRows(roleFilter, planFilter, statusFilter): any[] {
    // Reset search on select change
    this.searchValue = '';

    roleFilter = roleFilter.toLowerCase();
    planFilter = planFilter.toLowerCase();
    statusFilter = statusFilter.toLowerCase();

    return this.tempData.filter(row => {
      const isPartialNameMatch = row.controle.toLowerCase().indexOf(roleFilter) !== -1 || !roleFilter;

      return isPartialNameMatch;
    });
  }
  filterUpdate(event) {
    // Reset ng-select on search

    const val = event.target.value.toLowerCase();

    // Filter Our Data
    const temp = this.tempData.filter(function (d) {
      console.log(d)
      return d.ref.toString().indexOf(val) !== -1 || !val || d.client.toLowerCase().indexOf(val) !== -1 || d.controle.toLowerCase().indexOf(val) !== -1 || d.nbr.toString().indexOf(val) !== -1;
    });

    // Update The Rows
    this.rows = temp;
    // Whenever The Filter Changes, Always Go Back To The First Page
    this.table.offset = 0;
  }
  getDateFromMs(ms: any) {
    return new Date(ms).toLocaleDateString("en-US")
  }
  ToAdd() {
    this._router.navigate(['/apps/gestion/demande/add'])
  }
  AfficherModal(modal, echantillons) {
    this.selected_echantillons = echantillons;
    console.log(echantillons)
    this.modalservice.open(modal, {
      centered: true,

      size: 'lg' // size: 'xs' | 'sm' | 'lg' | 'xl'
    });
  }
  public selected_demande;
  public control_stat = true;
  onChange(event) {
    if (this.control_stat == true) {
      this.control_stat = false
    }
    else {
      this.control_stat = true
    }
  }
  sendUpdateDemande() {
    let controle = ""
    if (this.control_stat) {
      controle = "Auto-Controle"
    }
    else {
      controle = "Controle Officiel"
    }
    let demande_data = {
      ref: this.selected_demande.ref,
      observation: this.selected_demande.observation,
      "preleveur": "string",
      controle: controle,
      "client_id": 0,
      "etat": "string"
    }
    this._service.updateDemande(demande_data).subscribe(result => {
      if (result) {
        if (result['status'] == 200) {

          for (let i = 0; i < this.selected_echantillons_edit.length; i++) {
            let ech_data = {
              "id": this.selected_echantillons_edit[i].echantillon.id,
              "ref": "string",
              "quantite": this.selected_echantillons_edit[i].echantillon.quantite,
              "nlot": this.selected_echantillons_edit[i].echantillon.nlot,
              "temperature": this.selected_echantillons_edit[i].echantillon.temperature,
              "ref_codebarre": "string"
            }
            console.log(ech_data)
            this._service.updateEchantillon(ech_data).subscribe(result => {
              if (result) {
                if (result.stats == 200) {
                  console.log("Echantillon modifié")
                }
                else {
                  console.log(result)
                }

              }
            })
          }



          this._toastr.success('Demande modifiée', 'Succès!', {
            toastClass: 'toast ngx-toastr',
            closeButton: true
          });
          setTimeout(() => {                           // <<<---using ()=> syntax
            window.location.reload()
          }, 1);

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
    })
  }
  editDemande(modal, row) {
    console.log(row)
    this.selected_demande = row;
    this.selected_echantillons_edit = row.echantillons;
    if (row.controle == 'Auto-Controle') {
      this.control_stat = true;

    }
    else {
      this.control_stat = false;
    }
    this.modalservice.open(modal, {
      centered: true,

      size: 'lg' // size: 'xs' | 'sm' | 'lg' | 'xl'
    });
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
            setTimeout(() => {                           
              window.location.reload()
            }, 1100);

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
