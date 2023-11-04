import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { webSocket } from 'rxjs/webSocket';
import { WebsocketService } from 'src/app/services/websocket-service';

@Component({
    selector: 'login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnDestroy {
    error: string = "";
    successMessage: string = "";
    subject: any;
    subscription: any;
    constructor(
        private router: Router,
        private wsService: WebsocketService,

    ) {
        
    }
    connect(){
        this.wsService.subject =webSocket("wss://9ycacmaxnh.execute-api.us-east-1.amazonaws.com/add-problems/")
        this.subject = this.wsService.subject;
        this.subscription = this.subject.subscribe(
            (response: any) => {
                if (response && response.result === "Invalid Password/Username") this.error = response.result;
                else {
                    this.wsService.user = this.username;
                    this.wsService.signingUp = true;
                    this.router.navigateByUrl("/pref");

                }
            },
            (error: any) => console.log("error", error),
        );
    }
    ngOnDestroy(): void {
        this.subscription.unsubscribe();
    }
    username: string = "";
    password: string = "";
    passwordSecond: string = "";

    onSignIn() {
        
        this.connect()
        if(this.password != this.passwordSecond){
          this.error = "Passwords Do Not Match."
          return;
        }
        this.error = "";
        this.successMessage = "";
        const authenticateUser = {
            action: "authenticateUser",
            username: this.username,
            password: this.password,
            first: "False"
        }
        this.subject.subscribe();
        this.subject.next(authenticateUser);
    }
}

