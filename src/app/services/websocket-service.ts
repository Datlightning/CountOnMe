import { Injectable } from "@angular/core";
import { webSocket } from "rxjs/webSocket";

@Injectable()
export class WebsocketService{
    subject = webSocket("wss://9ycacmaxnh.execute-api.us-east-1.amazonaws.com/gc_specific/")
    user: string = "Shreyas";
    signedIn: boolean = true;
    signingUp: boolean = false;
}
