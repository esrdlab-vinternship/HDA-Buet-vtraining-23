import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query10',
  templateUrl: './query10.component.html',
  styleUrls: ['./query10.component.css']
})
export class Query10Component implements OnInit {

  data_all:any[] = [];
  store_keys: string[]  = [];
  month_1_avg_sales:any[] = [];
  month_2_avg_sales:any[] = [];
  month_3_avg_sales:any[] = [];
  month_4_avg_sales:any[] = [];
  month_5_avg_sales:any[] = [];
  month_6_avg_sales:any[] = [];
  month_7_avg_sales:any[] = [];
  month_8_avg_sales:any[] = [];
  month_9_avg_sales:any[] = [];
  month_10_avg_sales:any[] = [];
  month_11_avg_sales:any[] = [];
  month_12_avg_sales:any[] = [];








  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: '1',
      data: this.month_1_avg_sales
    },
    {
      type: "bar",
      label: '2',
      data: this.month_2_avg_sales
    },
    {
      type: "bar",
      label: '3',
      data: this.month_3_avg_sales
    },
    {
      type: "bar",
      label: '4',
      data: this.month_4_avg_sales
    },
    {
      type: "bar",
      label: '5',
      data: this.month_5_avg_sales
    },
    {
      type: "bar",
      label: '6',
      data: this.month_6_avg_sales
    },
    {
      type: "bar",
      label: '7',
      data: this.month_7_avg_sales
    },
    {
      type: "bar",
      label: '8',
      data: this.month_8_avg_sales
    },
    {
      type: "bar",
      label: '9',
      data: this.month_9_avg_sales
    },
    {
      type: "bar",
      label: '10',
      data: this.month_10_avg_sales
    },
    {
      type: "bar",
      label: '11',
      data: this.month_11_avg_sales
    },
    {
      type: "bar",
      label: '12',
      data: this.month_12_avg_sales
    }
  ];
  chartLabels: string[] = this.store_keys;
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
    this.query10Data();
  }


  query10Data(): void{
    this.queryService.getQuery10().subscribe((data:any)=>{


      for(const d of data){
        console.log(d)
        this.store_keys.push(d.store_key)

        for(const q of d.Sales)
        {
          if(q.month == 1)
          {
            this.month_1_avg_sales.push(q.avg_sales)
          }
          if(q.month == 2)
          {
            this.month_2_avg_sales.push(q.avg_sales)
          }
          if(q.month == 3)
          {
            this.month_3_avg_sales.push(q.avg_sales)
          }
          if(q.month == 4)
          {
            this.month_4_avg_sales.push(q.avg_sales)
          }
          if(q.month == 5)
          {
            this.month_5_avg_sales.push(q.avg_sales)
          }
          if(q.month == 6)
          {
            this.month_6_avg_sales.push(q.avg_sales)
          }
          if(q.month == 7)
          {
            this.month_7_avg_sales.push(q.avg_sales)
          }
          if(q.month == 8)
          {
            this.month_8_avg_sales.push(q.avg_sales)
          }
          if(q.month == 9)
          {
            this.month_9_avg_sales.push(q.avg_sales)
          }
          if(q.month == 10)
          {
            this.month_10_avg_sales.push(q.avg_sales)
          }
          if(q.month == 11)
          {
            this.month_11_avg_sales.push(q.avg_sales)
          }
          if(q.month == 12)
          {
            this.month_12_avg_sales.push(q.avg_sales)
          }
        }


      }
      this.data_all = data;
    })
  }

}
