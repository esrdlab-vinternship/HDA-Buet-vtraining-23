import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query3',
  templateUrl: './query3.component.html',
  styleUrls: ['./query3.component.css']
})
export class Query3Component implements OnInit {

  data_all: any[] = [];

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.query3Data();
  }

  query3Data(): void{
    this.queryService.getQuery3().subscribe((data:any)=>{

      for(const d of data){
        console.log(d);
      }
      this.data_all = data

    })
  }

}
