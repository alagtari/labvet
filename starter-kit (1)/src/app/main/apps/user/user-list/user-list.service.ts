import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from '@angular/router';
import { environment } from 'environments/environment';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
@Injectable()
export class UserListService implements Resolve<any> {
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


  deleteUser(id) {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };

    return this._httpClient.delete<any>(`${environment.apiUrl}/users/delete?id=${id}`, optionRequete).pipe(

      map(result => {
        if (result) {
          return result;
        }
      })
    )

  }
  //addUser()
  addUser(data: any) {
    let token = JSON.parse(localStorage.getItem("currentUser")).access_token;
    const optionRequete = {
      headers: new HttpHeaders({
        'Access-Control-Allow-Origin': '*',
        'Authorization': token
      })
    };
    return this._httpClient.post<any>(`${environment.apiUrl}/users/create`, data, optionRequete).pipe(
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
      this._httpClient.get(`${environment.apiUrl}/users/all`, optionRequete).subscribe((response: any) => {
        console.log(response)
        this.rows = response;
        this.onUserListChanged.next(this.rows);
        resolve(this.rows);
      }, reject);
    });
    return;
  }
}
