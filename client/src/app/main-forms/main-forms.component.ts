import { Component, Output } from "@angular/core";
import { EventEmitter } from "@angular/core";

@Component({
  selector: "app-main-forms",
  templateUrl: "./main-forms.component.html",
  styleUrls: ["./main-forms.component.css"],
})

export class MainFormsComponent {

  @Output() transfering:EventEmitter<any> = new EventEmitter();

  file: string ='';

  toTransfer(){
    console.log('Requested Transfer...');
    this.transfering.emit(this.file);
  }
}
