import { NONE_TYPE } from "@angular/compiler";
import { Component, Output } from "@angular/core";
import { EventEmitter } from "@angular/core";
import { DataService } from "../services/data.service";


@Component({
  selector: "app-main-forms",
  templateUrl: "./main-forms.component.html",
  styleUrls: ["./main-forms.component.css"],
})

export class MainFormsComponent {
  
  file: any;


  constructor(private data:DataService){
    
  }
  
  toTransfer() {
    this.data.postData(this.file)
    return
  };

  toGet() {
    console.log('File-Name:')
    console.log(this.file)
    this.data.getData().subscribe(data=>{
      console.log(data)
    })
  }
}

