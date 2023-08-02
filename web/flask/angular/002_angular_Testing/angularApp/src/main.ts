import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { Routes, RouterModule } from '@angular/router';

import { AppComponent } from './components/app.component';
import {ButtonCounterComponent} from './components/experiments/001_ButtonCounter/ButtonCounter.component'
import { HttpClientModule } from '@angular/common/http';

const routes: Routes = [
  {path: '', component: ButtonCounterComponent  } // this is how you do an empty route
]


@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }



@NgModule({
  declarations: [
    AppComponent, ButtonCounterComponent
  ],
  imports: [
    BrowserModule, AppRoutingModule, HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
class AppModule { }

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
