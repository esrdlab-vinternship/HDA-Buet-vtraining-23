import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query9',
  templateUrl: './query9.component.html',
  styleUrls: ['./query9.component.css']
})
export class Query9Component implements OnInit {

  data_all: any[] = [];
  division_data: string[]  = [];
  item_data: string[]  = [];
  quantity_data: any[] = [];
  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: 'Quantity',
      data: this.quantity_data,
    }
  ];
  chartLabels: string[] = this.item_data;
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
    this.getQuery9Data();
  }

  getQuery9Data(): void{
    this.queryService.getQuery9().subscribe((data:any)=>{
      console.log(data);
      for(const d of data){
        //console.log(d.trans_type, d.sales)
        this.division_data.push(d.division)
        this.item_data.push(d.item_name)
        this.quantity_data.push(d.quantity)
      }
      //console.log(this.trans_type_data, this.sales_data);
      this.data_all = data;
    })
}

}
