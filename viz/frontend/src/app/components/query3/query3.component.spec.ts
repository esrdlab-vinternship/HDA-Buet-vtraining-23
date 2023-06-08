import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Query3Component } from './query3.component';

describe('Query3Component', () => {
  let component: Query3Component;
  let fixture: ComponentFixture<Query3Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Query3Component]
    });
    fixture = TestBed.createComponent(Query3Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
