import { TestBed } from '@angular/core/testing';

import { Query1Service } from './query1.service';

describe('Query1Service', () => {
  let service: Query1Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Query1Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
