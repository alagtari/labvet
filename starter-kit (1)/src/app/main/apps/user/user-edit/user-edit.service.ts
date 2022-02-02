import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'environments/environment';
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from '@angular/router';

import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable()
export class UserEditService implements Resolve<any> {
  public rows: any;
  public onUserEditChanged: BehaviorSubject<any>;

  /**
   * Constructor
   *
   * @param {HttpClient} _httpClient
   */
  constructor(private _httpClient: HttpClient) {
    // Set the defaults
    this.onUserEditChanged = new BehaviorSubject({});
  }

  /**
   * Resolver
   *
   * @param {ActivatedRouteSnapshot} route
   * @param {RouterStateSnapshot} state
   * @returns {Observable<any> | Promise<any> | any}
   */
  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<any> | Promise<any> | any {
    return new Promise<void>((resolve, reject) => {
      Promise.all([this.getApiData()]).then(() => {
        resolve();
      }, reject);
    });
  }


  updateUser(data: any) {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.put<any>(`${environment.apiUrl}/users/update`, data, optionRequete).pipe(
      map(result => {
        if (result) {
          return result;
        }
      })
    )
  }

  /**
   * Get API Data
   */
  getApiData(): Promise<any[]> {
    return new Promise((resolve, reject) => {
      let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
      const optionRequete = {
        headers: new HttpHeaders({
          'Access-Control-Allow-Origin': '*',
          'Authorization': token
        })
      };
      this._httpClient.get(`${environment.apiUrl}/users/all`, optionRequete).subscribe((response: any) => {
        console.log(response)
        this.rows = response;
        this.onUserEditChanged.next(this.rows);
        resolve(this.rows);
      }, reject);
    });
    return;
  }
}
