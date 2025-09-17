import { Component } from '@angular/core';

@Component({
  selector: 'app-suma',
  templateUrl: './sum.component.html',
  styleUrls: ['./sum.component.css'],
})
export class SumComponent {
  numberA = 0;
  numberB = 0;

  get total(): number {
    return this.numberA + this.numberB;
  }

  updateNumberA(value: string): void {
    this.numberA = Number(value);
  }

  updateNumberB(value: string): void {
    this.numberB = Number(value);
  }
}
