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
import { Query4Component } from './components/query4/query4.component';
import { Query5Component } from './components/query5/query5.component';
import { Query6Component } from './components/query6/query6.component';
import { Query8Component } from './components/query8/query8.component';
import { Query9Component } from './components/query9/query9.component';
import { Query10Component } from './components/query10/query10.component';

@NgModule({
  declarations: [
    AppComponent,
    AddTutorialComponent,
    Query1Component,
    Query2Component,
    Query3Component,
    Query7Component,
    NewComponentComponent,
    Query4Component,
    Query5Component,
    Query6Component,
    Query8Component,
    Query9Component,
    Query10Component
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
