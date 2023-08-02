import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";

import { firstValueFrom } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class GeneralService{
    private readonly serviceAPIRoot = "/general"

    /*
    NOTE: toPromise is deprecated in angular 16
    see: https://stackoverflow.com/questions/67044273/rxjs-topromise-deprecated
    */

    constructor(private http: HttpClient){}

    getCurrentTime(): Promise<string>{
        let obs = this.http.get<string>(this.serviceAPIRoot + "/currentTime");
        return firstValueFrom(obs);
    }
}