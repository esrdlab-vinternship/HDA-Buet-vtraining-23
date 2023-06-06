import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query4',
  templateUrl: './query4.component.html',
  styleUrls: ['./query4.component.css']
})
export class Query4Component implements OnInit {

  data_all: any[] = [];

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.query4Data();
  }

  query4Data(): void{
    this.queryService.getQuery4().subscribe((data:any)=>{

      for(const d of data){
        console.log(d);
      }
      this.data_all = data

    })
  }

}
