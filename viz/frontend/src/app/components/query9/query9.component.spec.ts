import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Query9Component } from './query9.component';

describe('Query9Component', () => {
  let component: Query9Component;
  let fixture: ComponentFixture<Query9Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Query9Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Query9Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
