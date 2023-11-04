import { Injectable } from "@angular/core";
import { webSocket } from "rxjs/webSocket";

@Injectable()
export class WebsocketService{
    subject: any; 
    user: string = "";
    signedIn: boolean = false;
    signingUp: boolean = false;
}
