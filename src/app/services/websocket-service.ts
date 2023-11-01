import { Injectable } from "@angular/core";
import { webSocket } from "rxjs/webSocket";

@Injectable()
export class WebsocketService{
    subject = webSocket("wss://9ycacmaxnh.execute-api.us-east-1.amazonaws.com/add-problems/")
    user: string = "";
    signedIn: boolean = false;
    signingUp: boolean = false;
}
