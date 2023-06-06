import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query5',
  templateUrl: './query5.component.html',
  styleUrls: ['./query5.component.css']
})
export class Query5Component implements OnInit {

  data_all: any[] = [];

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.query5Data();
  }

  query5Data(): void{
    this.queryService.getQuery5().subscribe((data:any)=>{

      for(const d of data){
        console.log(d);
      }
      this.data_all = data

    })
  }

}
