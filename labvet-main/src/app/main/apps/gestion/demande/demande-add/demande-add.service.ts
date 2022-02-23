import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from '@angular/router';
import { environment } from 'environments/environment';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class DemandeAddService {
  public rows: any;
  public onUserListChanged: BehaviorSubject<any>;

  /**
   * Constructor
   *
   * @param {HttpClient} _httpClient
   */
  constructor(private _httpClient: HttpClient) {
    // Set the defaults
    this.onUserListChanged = new BehaviorSubject({});
  }

  /**
   * Resolver
   *
   * @param {ActivatedRouteSnapshot} route
   * @param {RouterStateSnapshot} state
   * @returns {Observable<any> | Promise<any> | any}
   */








  //addUser()
  getClients() {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.get<any>(`${environment.apiUrl}/client/all`, optionRequete).pipe(
      map(users => {
        if (users) {
          return users;
        }
      })
    )
  }


  getNatures() {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.get<any>(`${environment.apiUrl}/natures/all`, optionRequete).pipe(
      map(users => {
        if (users) {
          return users;
        }
      })
    )
  }

  addEchantillon(data: any) {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.post<any>(`${environment.apiUrl}/echantillons/create`, data, optionRequete).pipe(
      map(users => {
        if (users) {
          console.log(users)
          return users;
        }
      })
    )
  }


  addDemande(data: any) {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.post<any>(`${environment.apiUrl}/demandes/create`, data, optionRequete).pipe(
      map(users => {
        if (users) {
          console.log(users)
          return users;
        }
      })
    )
  }



  getFamilles() {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.get<any>(`${environment.apiUrl}/familles/all`, optionRequete).pipe(
      map(users => {
        if (users) {
          console.log(users)
          return users;
        }
      })
    )
  }

  getParams() {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.get<any>(`${environment.apiUrl}/parametres/all`, optionRequete).pipe(
      map(users => {
        if (users) {
          console.log(users)
          return users;
        }
      })
    )
  }
  //todo


  ///


  /**
   * Get rows
   */


}
