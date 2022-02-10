import { Component, EventEmitter, Output } from "@angular/core";
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
    this.hidden = !this.hidden
    headers.append('Accept', 'application/json');
    this.response = this.apiService.postData(this.file, this.fileData, { headers: headers }).subscribe(
      (data:any)=>{
        this.toPostURI.emit(data.uri)
      }
    )
  };

  toGet() {
    console.log('File-Name:')
    console.log(this.file)
    this.apiService.getData().subscribe(data=>{
      console.log(data)
    })
  }
}

