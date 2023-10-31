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
  private subscription: Subscription;
  groupchats:any[] = [];

  constructor(
    private wsService: WebsocketService,
  ) {
    this.subscription = this.wsService.subject.subscribe(
      (response: any) => {
        console.log(response);
        if(response.newmessage != "true"){
          if(response.groupChatId != ""){
            this.groupchats.push(response);
          }
        }else{
          const currentChat = this.groupchats.find((gc) => gc.groupchatId === response.groupchatId)
          if(currentChat) currentChat.messages.push(response.messages[0])
        }
      },
      (error: any) => console.log("error", error),
    );
    this.getGroupChats();
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }

  getGroupChats() {
    const requestGcs = {
      action: "requestGc",
      username: this.wsService.user
    }
    this.wsService.subject.next(requestGcs);
  }
  onGroupChatSelected(groupChat: any){
    this.groupchat = groupChat;
  }
}