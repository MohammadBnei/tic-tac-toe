import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-square',
  template: `
    <button nbButton *ngIf="!value" >{{ value }}</button>
    <button nbButton hero status="{{this.buttonStatus}}" *ngIf="value" >{{ value }}</button>
  `,
  styleUrls: ['./square.component.scss']
})
export class SquareComponent {

 @Input() value: 'X' | 'O';

 get buttonStatus() {
   if (this.value === 'X') {
     return 'success';
   } else if (this.value === 'O') {
     return 'info';
   }
 }

}
