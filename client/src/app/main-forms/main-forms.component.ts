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

  file: string
  fileData: File

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
    this.apiService.postData(this.file, this.fileData, { headers: headers })
  };

  toGet() {
    console.log('File-Name:')
    console.log(this.file)
    this.apiService.getData().subscribe(data=>{
      console.log(data)
    })
  }
}

