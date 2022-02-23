import { Component, OnInit, ViewEncapsulation } from '@angular/core';

import Stepper from 'bs-stepper';
import { DemandeAddService } from './demande-add.service';
import Swal from 'sweetalert2';
import { cpuUsage } from 'process';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FamilleService } from '../../echantillon/famille/famille.service';
import { ToastrService } from 'ngx-toastr';
import { timeStamp } from 'console';
import { NatureService } from '../../echantillon/nature/nature.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-demande-add',
  templateUrl: './demande-add.component.html',
  styleUrls: ['./demande-add.component.scss']
})
export class DemandeAddComponent implements OnInit {

  public contentHeader: object;
  public TDNameVar;
  public TDEmailVar;
  public TDFirstNameVar;
  public TDLastNameVar;
  public current_i;
  public selected_famille = {
    0: { idf: 0, nomf: "" }
  };
  public selected_nature = {
    0: { id: 0, designation: "" }
  };
  public twitterVar;
  public facebookVar;
  public googleVar;
  public linkedinVar;
  public landmarkVar;
  public addressVar;

  public selectBasic = [
    { name: 'UK' },
    { name: 'USA' },
    { name: 'Spain' },
    { name: 'France' },
    { name: 'Italy' },
    { name: 'Australia' }
  ];
  public departements =
    [{
      name: 'Microbiologie', value: "MIC"
    },

    {
      name: 'Physio-chimique', value: "Phys"
    },
    {
      name: 'AGR', value: "AGR"
    }

    ];

  public items = [{ id: 0, nature: { id: 1, designation: 'Eau', parametres: [] }, famille: { idf: 0, nomf: '', nature_id: 2, nature: '' }, designation: '', nlot: 0, quantite: 0, temperature: 0, param: [], dep: { name: "", value: "" } }]


  public count = 0;
  addItem() {
    this.count = this.count + 1;
    this.selectMultiSelected[this.count] = [];
    this.items.push({
      id: 0, nature: { id: 1, designation: 'Eau', parametres: [] }, famille: { idf: 0, nomf: '', nature_id: 2, nature: '' }, designation: '', nlot: 0, quantite: 0, temperature: 0, param: [], dep: { name: "", value: "" }
    });

    console.log(this.count)
    console.log(this.selectMultiSelected);
  }
  deleteItem(id) {
    delete this.selectMultiSelected[this.count]
    delete this.selected_famille[this.count]
    delete this.selected_nature[this.count]
    for (let i = 0; i < this.items.length; i++) {
      if (this.items.indexOf(this.items[i]) === id) {
        this.items.splice(i, 1);
        break;
      }
    }
    this.count = this.count - 1;
    console.log(this.count)
    console.log(this.selectMultiSelected);

  }
  public selectMulti = [{ name: 'English' }, { name: 'French' }, { name: 'Spanish' }];
  public selectMultiSelected = {
    0: []
  }
  public client_id;
  public natures;
  public familles = {

  };
  public clients;
  public paramatres = {

  }
  afficherAddFamille(modal, i) {
    this.current_i = i;
    this.modalservice.open(modal, {
      centered: true,

      size: 'sm' // size: 'xs' | 'sm' | 'lg' | 'xl'
    });
  }
  afficherAddNature(modal, i) {
    this.current_i = i;
    this.modalservice.open(modal, {
      centered: true,

      size: 'sm' // size: 'xs' | 'sm' | 'lg' | 'xl'
    });
  }
  updateFamille(event, i) {
    this.selected_famille[i] = event
  }
  onSubmit(form, modal) {
    console.log(form.form.value)
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
              let id = result.id;
              this.familles[this.current_i] = [...this.familles[this.current_i], { idf: id, nomf: form.form.value.nomf }]
              this.selected_famille[this.current_i] = { idf: id, nomf: form.form.value.nomf }
              
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

  // private
  private horizontalWizardStepper: Stepper;
  private verticalWizardStepper: Stepper;
  private modernWizardStepper: Stepper;
  private modernVerticalWizardStepper: Stepper;
  private bsStepper;
  public selectBasicLoading = false;

  /**
   * Horizontal Wizard Stepper Next
   *
   * @param data
   */
  horizontalWizardStepperNext(data) {
    if (data.form.valid === true) {
      this.horizontalWizardStepper.next();
    }
  }
  /**
   * Horizontal Wizard Stepper Previous
   */
  horizontalWizardStepperPrevious() {
    this.horizontalWizardStepper.previous();
  }

  /**
   * Vertical Wizard Stepper Next
   */
  verticalWizardNext() {
    this.verticalWizardStepper.next();
  }
  /**
   * Vertical Wizard Stepper Previous
   */
  verticalWizardPrevious() {
    this.verticalWizardStepper.previous();
  }
  /**
   * Modern Horizontal Wizard Stepper Next
   */
  modernHorizontalNext() {
    this.modernWizardStepper.next();
  }
  /**
   * Modern Horizontal Wizard Stepper Previous
   */
  modernHorizontalPrevious() {
    this.modernWizardStepper.previous();
  }
  /**
   * Modern Vertical Wizard Stepper Next
   */
  modernVerticalNext() {
    this.modernVerticalWizardStepper.next();
  }
  /**
   * Modern Vertical Wizard Stepper Previous
   */
  modernVerticalPrevious() {
    this.modernVerticalWizardStepper.previous();
  }


  /**
   * On Submit
   */
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
              let id = result.id
              this.natures = [...this.natures, { id: id, designation: form.form.value.designation }]
              this.selected_nature[this.current_i] = { id: id, designation: form.form.value.designation }
              
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
  onChange(event: any) {
    console.log(event)
    this.client_id = event
  }

  constructor(private _service: DemandeAddService, private modalservice: NgbModal, private _familleService: FamilleService, private _toastr: ToastrService, private _natureService: NatureService,private _router: Router) { }

  ConfirmTextOpen() {
    console.log(this.items)
    let demande_data = { ref: 0, observation: "", date_recep: 0, preleveur: "", controle: "", client_id: this.client_id.idc, etat: "" }
    let controle = (<HTMLInputElement>document.getElementById('controle')).checked
    if (controle) {
      demande_data.controle = "Auto-Controle"
    }
    else {
      demande_data.controle = "controle officiel"
    }
    demande_data.observation = (<HTMLInputElement>document.getElementById("observation")).value

    this._service.addDemande(demande_data).subscribe(
      result => {
        if (result.status == 200) {
          let deamnde_id = result.id
          for (let i = 0; i < this.items.length; i++) {
            let item = this.items[i]
            let echantillon_data = { id: 0, ref: item.dep.value, quantite: item.quantite, nlot: item.nlot, temperature: item.temperature, idn: this.selected_nature[i].id, idp: [], idd: deamnde_id, idf: this.selected_famille[i].idf }

            for (let j = 0; j < this.selectMultiSelected[i].length; j++) {
              echantillon_data.idp.push(this.selectMultiSelected[i][j].id)
            }
            console.log(echantillon_data)
            this._service.addEchantillon(echantillon_data).subscribe(
              result => {

              }
            )

          }
          Swal.fire({
            icon: 'success',
            title: 'Demande Ajoutée',
            text: 'La demande a été ajoutée.',
            customClass: {
              confirmButton: 'btn btn-success'
            }
          }).then(result => {
            if (result.isConfirmed) {
              this._router.navigate(['/apps/gestion/demande/gestion']);
            }
          })



        }

      }
    )
  }

  // Lifecycle Hooks
  // -----------------------------------------------------------------------------------------------------

  /**
   * On Init
   */

  updateParams(event: any, i: any) {
    console.log(event)
    this.selected_nature[i] = event
    this.paramatres[i] = event.parametres
    this.familles[i] = event.familles
  }
  ngOnInit() {


    this._service.getClients().subscribe(
      result => {
        this.clients = result.data;
      }
    )
    this._service.getNatures().subscribe(
      result => {
        this.natures = result.data;
      }
    )


    this.verticalWizardStepper = new Stepper(document.querySelector('#stepper2'), {
      linear: false,
      animation: true
    });

    this.bsStepper = document.querySelectorAll('.bs-stepper');

    // content header
  }
}