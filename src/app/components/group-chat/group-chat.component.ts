import { Component, Input, OnDestroy } from "@angular/core";
import { Subscription } from "rxjs";
import { WebsocketService } from "src/app/services/websocket-service";

/*
 * GroupChat component
 */

@Component({
  selector: 'group-chat',
  templateUrl: './group-chat.component.html',
  styleUrls: ['./group-chat.component.scss']
})
export class GroupChatComponent implements OnDestroy {
  subscription: Subscription;
  constructor(
    private wsService: WebsocketService,
  ) {
    this.subscription = this.wsService.subject.subscribe(
      (response: any) => {
        // console.log(response);
      },
      (error: any) => console.log("error", error),
    );
  }
  @Input() groupchat: any = {};
  message: string = "";
  sendMessage() {
    console.log("we have arrived")
    const data = {
      "action": "sendMessage",
      "username": this.wsService.user,
      "groupchatId": this.groupchat.groupchatId,
      "message": this.message
    };
    this.wsService.subject.next(data);
    this.message = "";
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }


}