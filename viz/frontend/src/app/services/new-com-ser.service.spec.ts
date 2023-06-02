import { TestBed } from '@angular/core/testing';

import { NewComSerService } from './new-com-ser.service';

describe('NewComSerService', () => {
  let service: NewComSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(NewComSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
