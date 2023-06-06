import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Query10Component } from './query10.component';

describe('Query10Component', () => {
  let component: Query10Component;
  let fixture: ComponentFixture<Query10Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Query10Component ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Query10Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
