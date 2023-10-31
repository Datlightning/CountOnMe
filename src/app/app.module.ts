import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './components/login/login.component';
import { AppMainComponent } from './components/app-main/app-main.component';
import { Child1Component } from './components/child1/child1.component';
import { GroupChatComponent } from './components/group-chat/group-chat.component';
import { WebsocketService } from './services/websocket-service';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { IndicatePreferencesComponent } from './components/indicate-preferences/indicate-preferences.component';

@NgModule({
	declarations: [
		AppComponent,
		LoginComponent,
    AppMainComponent,
    Child1Component,
    GroupChatComponent,
	SignUpComponent,
	IndicatePreferencesComponent,
	],
	imports: [
		BrowserModule,
		AppRoutingModule,
		FormsModule
	],
	providers: [WebsocketService],
	bootstrap: [AppComponent]
})
export class AppModule { }
