import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { AppMainComponent } from './components/app-main/app-main.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { IndicatePreferencesComponent } from './components/indicate-preferences/indicate-preferences.component';


const appRoutes: Routes = [
  {
    path: 'login',
    component: LoginComponent,
  }, {
    path: "main",
    component: AppMainComponent,
  },{
    path: "signUp",
    component: SignUpComponent,
  },{
    path: "pref",
    component: IndicatePreferencesComponent,
  },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  // { path: '**', component: PageNotFoundComponent }
];

@NgModule({
  imports: [
    RouterModule.forRoot(
      appRoutes,
      {
        enableTracing: false, // <-- debugging purposes only
      }
    )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/