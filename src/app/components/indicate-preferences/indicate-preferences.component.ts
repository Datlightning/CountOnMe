import { Component } from "@angular/core";
import { Router } from "@angular/router";
import { Subscription } from "rxjs/internal/Subscription";
import { WebsocketService } from "src/app/services/websocket-service";

/*
 * IndicatePreferences component
 */

@Component({
  selector: 'indicate-preferences',
  templateUrl: './indicate-preferences.component.html',
  styleUrls: ['./indicate-preferences.component.scss']
})
export class IndicatePreferencesComponent {
  error: string = "";
  successMessage: string = "";
  subject: any;
  subscription: Subscription;
  preferences: any[] = [
    { name: "Addictions", selected: false },
    { name: "Depression", selected: false },
    { name: "The Big Sad", selected: false },
    { name: "Thing3", selected: false },
    { name: "Thing4", selected: false },
    { name: "Thing4", selected: false },
    { name: "Thing4", selected: false },
    { name: "Thing4", selected: false },
    { name: "Thing4", selected: false },
    { name: "Thing4", selected: false },
    { name: "Thing4", selected: false },
    { name: "Thing4", selected: false }
  ];
  userPreferences: string[] = [];
  constructor(
    private router: Router,
    private wsService: WebsocketService,

  ) {
    if(!this.wsService.signingUp){
      this.router.navigateByUrl("/login")
    }
    this.subject = this.wsService.subject;
    this.subscription = this.subject.subscribe(
      (response: any) => {
        if (response && response.result === "Invalid Password/Username") this.error = response.result;
        else if(response.result === "success"){
          this.wsService.signedIn = true;
          this.wsService.signingUp = false;
          this.router.navigateByUrl("/main");

        }
        else{
          console.log(response);
        }
      },
      (error: any) => console.log("error", error),
    );
  }
  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
  updatePref(preference: any) {
    const index: number = this.userPreferences.indexOf(preference.name);
    if (index > -1) {
      this.userPreferences.splice(index, 1);
      preference.selected = false;
    } else {
      this.userPreferences.push(preference.name)
      preference.selected = true;
    }
  }
  sendPreferences(){
    this.error = "";
    this.successMessage = "";
    const addProblems = {
        action: "addProblems",
        username: this.wsService.user,
        problems: this.userPreferences
    }
    console.log(this.userPreferences);
    console.log(this.wsService.user);
    this.subject.subscribe();
    this.subject.next(addProblems);

  }
 
}