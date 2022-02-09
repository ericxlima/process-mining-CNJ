import { MainFormsComponent } from './main-forms/main-forms.component';
import { ViewerSvgComponent } from './viewer-svg/viewer-svg.component';

import { EventEmitter, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { NgxImageZoomComponent } from 'ngx-image-zoom';


@NgModule({
  declarations: [
    AppComponent,
    MainFormsComponent,
    ViewerSvgComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    NgxImageZoomComponent,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
