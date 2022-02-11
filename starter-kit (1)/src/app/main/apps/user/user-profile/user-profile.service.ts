import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from '@angular/router';
import { environment } from 'environments/environment';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
@Injectable()
export class UserProfileService implements Resolve<any> {
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



  //todo


  ///
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

  getUser() {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    let id = JSON.parse(localStorage.getItem("currentUser")).id;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.get<any>(`${environment.apiUrl}/users/byid?id=${id}`, optionRequete).pipe(
      map(users => {
        if (users) {
          return users;
        }
      })
    )
  }

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
      let id = JSON.parse(localStorage.getItem("currentUser")).id;
      let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
      const optionRequete = {
        headers: new HttpHeaders({
          'Access-Control-Allow-Origin': '*',
          'Authorization': token
        })
      };
      this._httpClient.get(`${environment.apiUrl}/users/byid?id=${id}`, optionRequete).subscribe((response: any) => {
        this.rows = response;
        console.log(this.rows)
        this.onUserListChanged.next(this.rows);
        resolve(this.rows);
      }, reject);
    });
    return;
  }
}
