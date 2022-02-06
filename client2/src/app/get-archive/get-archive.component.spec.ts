import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetArchiveComponent } from './get-archive.component';

describe('GetArchiveComponent', () => {
  let component: GetArchiveComponent;
  let fixture: ComponentFixture<GetArchiveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GetArchiveComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GetArchiveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
