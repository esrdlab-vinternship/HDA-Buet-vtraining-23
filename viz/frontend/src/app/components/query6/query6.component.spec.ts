import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Query6Component } from './query6.component';

describe('Query6Component', () => {
  let component: Query6Component;
  let fixture: ComponentFixture<Query6Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Query6Component]
    });
    fixture = TestBed.createComponent(Query6Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
