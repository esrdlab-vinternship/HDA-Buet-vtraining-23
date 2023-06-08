import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query8',
  templateUrl: './query8.component.html',
  styleUrls: ['./query8.component.css']
})
export class Query8Component implements OnInit {

  data_all: any[] = [];
  item_name: any[] = [];
  quarter: any[] = [];
  sales: any[] = [];



  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query8Data();
  }

  query8Data(): void {
    this.queryService.getQuery8().subscribe((data: any) => {
        for (const d of data) {
          // console.log(d)
          this.item_name.push(d.item_name)
          this.quarter.push(d.quarter)
          this.sales.push(d.sales)

        }
        this.data_all = data;
      }
    )
  }

}
