import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AddTutorialComponent} from "./components/add-tutorial/add-tutorial.component";
import {Query1Component} from "./components/query1/query1.component";
import {Query2Component} from "./components/query2/query2.component";
import {Query7Component} from "./components/query7/query7.component";
import {NewComponentComponent} from "./components/new-component/new-component.component";

const routes: Routes = [
  {path: 'first-component', component: AddTutorialComponent},
  {path: 'query1', component: Query1Component},
  {path: 'query2', component: Query2Component},
  {path: 'query7', component: Query7Component},
  {path: 'new-com', component: NewComponentComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
