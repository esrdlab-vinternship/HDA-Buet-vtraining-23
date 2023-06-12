import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { Query1Component } from './components/query1/query1.component';
import { Query2Component } from './components/query2/query2.component';
import { Query3Component } from './components/query3/query3.component';
import { Query4Component } from './components/query4/query4.component';
import { Query5Component } from './components/query5/query5.component';

@NgModule({
  declarations: [
    AppComponent,
    Query1Component,
    Query2Component,
    Query3Component,
    Query4Component,
    Query5Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
