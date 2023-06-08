import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query5',
  templateUrl: './query5.component.html',
  styleUrls: ['./query5.component.css']
})
export class Query5Component implements OnInit {

  data_all: any[] = [];
  division: any[] = [];
  year: any[] = [];
  sales: any[] = [];
  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query5Data();
  }

  query5Data(): void {
    this.queryService.getQuery5().subscribe((data: any) => {
        for (const d of data) {
          // console.log(d)
          this.division.push(d.division)
          this.year.push(d.year)
          this.sales.push(d.sales)
        }
        this.data_all = data;
      }
    )
  }

}
