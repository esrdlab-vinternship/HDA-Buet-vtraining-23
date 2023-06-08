import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query6',
  templateUrl: './query6.component.html',
  styleUrls: ['./query6.component.css']
})
export class Query6Component implements OnInit {

  data_all: any[] = [];
  store_ID: any[] = [];
  item: any[] = [];
  quantity: any[] = [];



  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query6Data();
  }

  query6Data(): void {
    this.queryService.getQuery6().subscribe((data: any) => {
        for (const d of data) {
          // console.log(d)
          this.store_ID.push(d.store_ID)
          this.item.push(d.item)
          this.quantity.push(d.quantity)

        }
        this.data_all = data;
      }
    )
  }

}
