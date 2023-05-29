import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddTutorialComponent } from './components/add-tutorial/add-tutorial.component';
import { Query1Component } from './components/query1/query1.component';
import { CommonModule } from '@angular/common';
import { Query2Component } from './components/query2/query2.component';
import {NgChartsModule} from "ng2-charts";
import {HttpClientModule} from "@angular/common/http";
import { Query3Component } from './components/query3/query3.component';
import { Query7Component } from './components/query7/query7.component';
import {ReactiveFormsModule} from "@angular/forms";
import {DataTablesModule} from "angular-datatables";
import { NewComponentComponent } from './components/new-component/new-component.component';

@NgModule({
  declarations: [
    AppComponent,
    AddTutorialComponent,
    Query1Component,
    Query2Component,
    Query3Component,
    Query7Component,
    NewComponentComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        CommonModule,
        NgChartsModule,
        HttpClientModule,
        ReactiveFormsModule,
        DataTablesModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
