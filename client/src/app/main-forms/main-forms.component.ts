import { Component, EventEmitter, Output } from "@angular/core";
import { DataService } from "../services/data.service";
// import { EventEmitter } from "@angular/core";
import { HttpClient } from "@angular/common/http";


@Component({
  selector: "app-main-forms",
  templateUrl: "./main-forms.component.html",
  styleUrls: ["./main-forms.component.css"],
})

export class MainFormsComponent {

  file: string;
  fileData: File;
  response: any;

  @Output() toPostURI = new EventEmitter<any>();  

  constructor(private apiService: DataService){
  }

  onFileChange(event: any) {
    /*Add file content to fileData*/
    if (event.target.files.length > 0) {
      this.fileData = event.target.files[0];
    }
  }

  toTransfer() {
    let headers = new Headers();
    headers.append('Accept', 'application/json');
    this.response = this.apiService.postData(this.file, this.fileData, { headers: headers }).subscribe(
      (data:any)=>{
        // console.log('FRONT')
        // console.log(data)
        // data            <<<<<<<<<<<<<------------- Data 
        // console.log('Solicitada transferencia')
        this.toPostURI.emit(data.uri)
      }
    )
      // console.log('Response FRONT:', this.response)
      // console.log('Test: ', this.apiService.response)
  };

  toGet() {
    console.log('File-Name:')
    console.log(this.file)
    this.apiService.getData().subscribe(data=>{
      console.log(data)
    })
  }
}

