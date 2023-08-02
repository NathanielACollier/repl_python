import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";

@Injectable()
export class GeneralService{
    private readonly serviceAPIRoot = "/general"

    constructor(private http: HttpClient){}

    getCurrentTime(): Promise<string>{
        return this.http.get<string>(this.serviceAPIRoot + "/currentTime")
                .toPromise();
    }
}