import { Component, Output } from "@angular/core";
import { EventEmitter } from "@angular/core";
// import { HttpClient } from '@angular/common/http';

@Component({
  selector: "app-main-forms",
  templateUrl: "./main-forms.component.html",
  styleUrls: ["./main-forms.component.css"],
})

export class MainFormsComponent {

  // constructor(private http: HttpClient) { }

  @Output() transfering:EventEmitter<any> = new EventEmitter();

  file: string ='';

  toTransfer(){
    console.log('Requested Transfer...');
    this.transfering.emit(this.file);

    // Make a POST Method
    // return this.http.get('http://127.0.0.1:5000/');
  }
}
