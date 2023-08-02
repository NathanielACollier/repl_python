import { Component, OnInit } from '@angular/core';
import { GeneralService } from '../../../services/general.service';

@Component({
  selector: 'app-root',
  templateUrl: "ButtonCounter.component.html",
  styleUrls: []
})
export class ButtonCounterComponent implements OnInit {
    clickCount: number = 0;
    currentTime: string = "";

    constructor(private generalSvc: GeneralService){}

    ngOnInit(): void {

        // start timer to show current time
        setInterval(async () => {
            this.currentTime = await this.generalSvc.getCurrentTime();
        }, 1000 * 10);
        
    }

    onClick_CounterButton(){

    }
}
