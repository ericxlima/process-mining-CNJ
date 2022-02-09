import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'MP4CNJ';

  uri:string = '';

  transfering($event:any) {
    this.uri = 'http://127.0.0.1:5000/api/v1/get_data/' + $event
  }
}
