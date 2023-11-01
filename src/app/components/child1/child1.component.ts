import { Component, OnDestroy } from "@angular/core";
import { Subscription } from "rxjs";
import { WebsocketService } from "src/app/services/websocket-service";

/*
 * Child1 component
 */

@Component({
  selector: 'child1',
  templateUrl: './child1.component.html',
  styleUrls: ['./child1.component.scss']
})
export class Child1Component implements OnDestroy {
  gcs = [];
  groupchat: any;
  running: boolean = false;
  private subscription: Subscription;
  groupchats:any[] = [];
  problemNames:any = {};

  constructor(
    private wsService: WebsocketService,
  ) {
    this.subscription = this.wsService.subject.subscribe(
      (response: any) => {
        console.log(response);
        if(response.newmessage != "true"){
          if(response.groupchatId != "" && response.hasOwnProperty("groupchatId")){
            const name: string = response.name;

            if(this.problemNames.hasOwnProperty(name)){
              this.problemNames[name] += 1;
              response.name += " " + this.problemNames[name];
            }
            else{
              this.problemNames[name] = 1;

            }
            console.log("problem names", this.problemNames);
            this.groupchats.push(response);
          }else if(response.final === "True"){
            // this.running = false;
          }
        }else{
          const currentChat = this.groupchats.find((gc) => gc.groupchatId === response.groupchatId)
          if(currentChat) currentChat.messages.push(response.messages[0])
        }
      },
      (error: any) => console.log("error", error),
    );
    this.createGc();
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  getGroupChats() {
    this.groupchats = [];
    const requestGcs = {
      action: "requestGc",
      username: this.wsService.user
    }
    this.wsService.subject.next(requestGcs);
  }
  createGc(){
    if(!this.running){
      this.running = true
      const requestGcs = {
        action: "createGc",
        username: this.wsService.user
      }
      
      this.wsService.subject.next(requestGcs);
      this.groupchats = [];
      this.getGroupChats();
      setTimeout(() => {
        this.running = false;
      }, 3000);
    }
  }
  onGroupChatSelected(groupChat: any){
    this.groupchat = groupChat;
  }
}