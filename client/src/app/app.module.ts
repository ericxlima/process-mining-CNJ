import { MainFormsComponent } from './main-forms/main-forms.component';
import { EventEmitter, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { TableContentComponent } from './table-content/table-content.component';

@NgModule({
  declarations: [
    AppComponent,
    MainFormsComponent,
    TableContentComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
