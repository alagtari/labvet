import { Component, OnInit } from '@angular/core'
import { CoreConfigService } from '@core/services/config.service';
import { HomeService } from './home.service'
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(private _homeService: HomeService, private _coreConfigService: CoreConfigService) {
    this._unsubscribeAll = new Subject();
  }
  public rows: any;
  public contentHeader: object
  public _unsubscribeAll;
  // Lifecycle Hooks
  // -----------------------------------------------------------------------------------------------------

  /**
   * On init
   */
  ngOnInit() {
    this._coreConfigService.config.pipe(takeUntil(this._unsubscribeAll)).subscribe(config => {
      //! If we have zoomIn route Transition then load datatable after 450ms(Transition will finish in 400ms)
      if (config.layout.animation === 'zoomIn') {
        setTimeout(() => {

          this._homeService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {

            this.rows = response;
            console.log(this.rows)
          });
        }, 450);
      } else {

        this._homeService.onUserListChanged.pipe(takeUntil(this._unsubscribeAll)).subscribe(response => {


          this.rows = response;
          console.log(this.rows)
        });
      }
    });
  }
}
