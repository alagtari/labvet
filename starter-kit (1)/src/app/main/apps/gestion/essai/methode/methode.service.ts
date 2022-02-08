import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from '@angular/router';
import { environment } from 'environments/environment';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class MethodeService {
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


  deleteMethode(id) {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };

    return this._httpClient.delete<any>(`${environment.apiUrl}/methodes/delete?id=${id}`, optionRequete).pipe(

      map(result => {
        if (result) {
          return result;
        }
      })
    )

  }
  getFamilles() {
    ///familles/all
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.get<any>(`${environment.apiUrl}/methodes/all`, optionRequete).pipe(
      map(familles => {
        if (familles) {
          return familles;
        }
      })
    )
  }
  //addUser()
  addMethode(data: any) {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.post<any>(`${environment.apiUrl}/methodes/create`, data, optionRequete).pipe(
      map(users => {
        if (users) {
          return users;
        }
      })
    )
  }
  //todo


  ///
  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<any> | Promise<any> | any {
    return new Promise<void>((resolve, reject) => {
      Promise.all([this.getDataTableRows()]).then(() => {
        resolve();
      }, reject);
    });
  }

  /**
   * Get rows
   */

  getDataTableRows(): Promise<any[]> {

    return new Promise((resolve, reject) => {
      let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
      const optionRequete = {
        headers: new HttpHeaders({
          'Access-Control-Allow-Origin': '*',
          'Authorization': token
        })
      };
      this._httpClient.get(`${environment.apiUrl}/methodes/all`, optionRequete).subscribe((response: any) => {
        console.log(response)
        this.rows = response['data'];
        this.onUserListChanged.next(this.rows);
        resolve(this.rows);
      }, reject);
    });
    return;
  }
}
