import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-viewer-svg',
  templateUrl: './viewer-svg.component.html',
  styleUrls: ['./viewer-svg.component.css']
})
export class ViewerSvgComponent implements OnInit {
  @Input() uri: any;

  // @Output() hidden = new EventEmitter<any>();  

  // title = 'angular-img-hover';

  constructor() { }

  ngOnInit(): void {
  }
}