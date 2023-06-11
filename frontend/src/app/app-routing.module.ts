import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { Query1Component } from './components/query1/query1.component';
import { Query2Component } from './components/query2/query2.component';
import { Query3Component } from './components/query3/query3.component';
import { Query4Component } from './components/query4/query4.component';
import { Query5Component } from './components/query5/query5.component';


const routes: Routes = [
  { path: 'query1', component: Query1Component },
  { path: 'query2', component: Query2Component },
  { path: 'query3', component: Query3Component },
  { path: 'query4', component: Query4Component },
  { path: 'query5', component: Query5Component }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
