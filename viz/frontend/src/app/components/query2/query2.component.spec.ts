import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Query2Component } from './query2.component';

describe('Query2Component', () => {
  let component: Query2Component;
  let fixture: ComponentFixture<Query2Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Query2Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Query2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
