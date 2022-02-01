import { NO_ERRORS_SCHEMA } from '@angular/core';
import { TestBed } from '@angular/core/testing';
import { UserListComponent } from './user-list.component';

import { UserListService } from './user-list.service';

describe('UserListService', () => {
  let service: UserListService;

  beforeEach((() => {
    TestBed.configureTestingModule({
      declarations: [ UserListComponent ],
      schemas: [NO_ERRORS_SCHEMA]
    })
    .compileComponents();
  }));

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
