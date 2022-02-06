import { Component, Output } from "@angular/core";
import { EventEmitter } from "@angular/core";

@Component({
  selector: "app-main-forms",
  templateUrl: "./main-forms.component.html",
  styleUrls: ["./main-forms.component.css"],
})

export class MainFormsComponent {
  
  file: any;
  
  toTransfer() {
    console.log('clicou')
    console.log(this.file)
  }
  
}
