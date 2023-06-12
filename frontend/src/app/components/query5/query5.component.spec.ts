import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Query5Component } from './query5.component';

describe('Query5Component', () => {
  let component: Query5Component;
  let fixture: ComponentFixture<Query5Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Query5Component]
    });
    fixture = TestBed.createComponent(Query5Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
