import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-viewer-svg',
  templateUrl: './viewer-svg.component.html',
  styleUrls: ['./viewer-svg.component.css']
})
export class ViewerSvgComponent implements OnInit {
  @Input() uri: any;

  title = 'angular-img-hover';
  myThumbnail="https://static.vix.com/pt/sites/default/files/t/todo-mundo-odeia-o-chris-0718-1400x800.jpg";
  myFullresImage="https://static.vix.com/pt/sites/default/files/t/todo-mundo-odeia-o-chris-0718-1400x800.jpg";

  constructor() { }

  ngOnInit(): void {
  }

}
