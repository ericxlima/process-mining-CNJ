import { Component, EventEmitter, Output } from "@angular/core";
import { Observable } from "rxjs";
import { DataService } from "../services/data.service";


@Component({
  selector: "app-main-forms",
  templateUrl: "./main-forms.component.html",
  styleUrls: ["./main-forms.component.css"],
})

export class MainFormsComponent {

  file: string;
  fileData: File;
  response: any;
  
  hidden:boolean = false;
  disableButton: boolean = false;

  @Output() toPostURI = new EventEmitter<any>();  

  constructor(private apiService: DataService){
  }

  onFileChange(event: any) {
    if (event.target.files.length > 0) {
      this.fileData = event.target.files[0];
    }
  }

  toTransfer() {
    let headers = new Headers();
    this.disableButton = !this.disableButton
    headers.append('Accept', 'application/json');
    if(typeof this.fileData != undefined){
      this.hidden = !this.hidden
      this.response = this.apiService.postData(this.file, this.fileData, { headers: headers }).subscribe(
        
        (data:any)=>{
          this.toPostURI.emit(data.uri)
        }
      )
      // this.hidden = !this.hidden
    }
    else {
      alert('Please upload a file before submitting.')

    }
  };

  toGet() {
    console.log('File-Name:')
    console.log(this.file)
    this.apiService.getData().subscribe(data=>{
      console.log(data)
    })
  }
}

