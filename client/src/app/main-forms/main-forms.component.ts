// import { NONE_TYPE } from "@angular/compiler";
import { Component, Output } from "@angular/core";
import { EventEmitter } from "@angular/core";
import { DataService } from "../services/data.service";
import { HttpClient } from "@angular/common/http";


@Component({
  selector: "app-main-forms",
  templateUrl: "./main-forms.component.html",
  styleUrls: ["./main-forms.component.css"],
})

export class MainFormsComponent {
  
  constructor(private data:DataService){ 
  // constructor(private http:HttpClient){
  }
    
  file: any;


  toTransfer() {
    console.log('Tranfering ' + this.file) 
    // typeof(this.file)  -> string
    this.data.postData(this.file)
  };

  toGet() {
    console.log('File-Name:')
    console.log(this.file)
    this.data.getData().subscribe(data=>{
      console.log(data)
    })
  }
}

