import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query6',
  templateUrl: './query6.component.html',
  styleUrls: ['./query6.component.css']
})
export class Query6Component implements OnInit {

  data_all:any[] = [];
  stores: string[]  = [];
  total_quantity: any[] = [];
  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: 'Sales in Taka',
      data: this.total_quantity
    }
  ];
  chartLabels: string[] = this.stores;
  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    // ⤵️ Remove the grids
    // scales: {
    //   xAxis: {
    //     display: false,
    //     grid: {
    //       drawBorder: false // removes random border at bottom
    //     }
    //   },
    //   yAxis: {
    //     display: false
    //   }
    // },

    plugins: {
      legend: {
        display: true,
        labels: {
          color: 'rgb(14,38,3)'
        }
      },

      tooltip: {
        // ⤵️ tooltip main styles
        backgroundColor: '#ffeaff',
        displayColors: false, // removes unnecessary legend
        padding: 10,

        // ⤵️ title
        titleColor: '#0b4ad2',
        titleFont: {
          size: 18
        },

        // ⤵️ body
        bodyColor: '#2D2F33',
        bodyFont: {
          size: 13
        }
      }
    }
  };

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.query6Data();
  }

  query6Data(): void{
    this.queryService.getQuery6().subscribe((data:any)=>{

      for(const d of data){
        console.log(d);
       // this.trans_type.push(d.trans_type)
        //this.total_sales.push(d.total_sales)
      }
      this.data_all = data;
    })
  }

}
