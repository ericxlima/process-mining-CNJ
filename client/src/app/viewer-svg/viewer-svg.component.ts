import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-viewer-svg',
  templateUrl: './viewer-svg.component.html',
  styleUrls: ['./viewer-svg.component.css']
})

export class ViewerSvgComponent implements OnInit {
  @Input() uri: any;

  constructor() { }

  ngOnInit(): void {
  }
}