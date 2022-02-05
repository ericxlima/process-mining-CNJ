import { Component } from "@angular/core";

@Component({
  selector: "app-main-forms",
  templateUrl: "./main-forms.component.html",
  styleUrls: ["./main-forms.component.css"],
})

export class MainFormsComponent {
  transfer(){
    console.log('Requested Transfer...')
  }
}
