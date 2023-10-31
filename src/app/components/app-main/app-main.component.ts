import { Component } from "@angular/core";
import { Router } from "@angular/router";
import { WebsocketService } from "src/app/services/websocket-service";

/*
 * AppMain component
 */

@Component({
  selector: 'app-main',
  templateUrl: './app-main.component.html',
  styleUrls: ['./app-main.component.scss']
})
export class AppMainComponent {
  constructor(
    private router: Router,
    private wsService: WebsocketService,
  )

  {
    if(!this.wsService.signedIn){
      router.navigateByUrl("/login")
    }
  }
}