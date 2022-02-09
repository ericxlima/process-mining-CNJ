import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewerSvgComponent } from './viewer-svg.component';

describe('ViewerSvgComponent', () => {
  let component: ViewerSvgComponent;
  let fixture: ComponentFixture<ViewerSvgComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewerSvgComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewerSvgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
