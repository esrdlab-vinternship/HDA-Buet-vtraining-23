import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query9',
  templateUrl: './query9.component.html',
  styleUrls: ['./query9.component.css']
})
export class Query9Component implements OnInit {

  data_all:any[] = [];
  items: string[]  = [];
  barisal_total_sales:any[] = [];
  chittagong_total_sales:any[] = [];
  dhaka_total_sales:any[] = [];
  khulna_total_sales:any[] = [];
  rajshahi_total_sales:any[] = [];
  rangpur_total_sales:any[] = [];
  sylhet_total_sales:any[] = [];


  chartData: ChartDataset[] = [
    {
      type: "bar",
      label: 'BARISAL',
      data: this.barisal_total_sales
    },
    {
      type: "bar",
      label: 'CHITTAGONG',
      data: this.chittagong_total_sales
    },
    {
      type: "bar",
      label: 'DHAKA',
      data: this.dhaka_total_sales
    },
    {
      type: "bar",
      label: 'KHULNA',
      data: this.khulna_total_sales
    },
    {
      type: "bar",
      label: 'RAJSHAHI',
      data: this.rajshahi_total_sales
    },
    {
      type: "bar",
      label: 'RANGPUR',
      data: this.rangpur_total_sales
    },
    {
      type: "bar",
      label: 'SYLHET',
      data: this.sylhet_total_sales
    }
  ];
  chartLabels: string[] = this.items;
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
    this.query9Data();
  }


  query9Data(): void{
    this.queryService.getQuery9().subscribe((data:any)=>{


      for(const d of data){
        console.log(d)
        this.items.push(d.item)

        for(const q of d.Sales)
        {
          if(q.division == 'BARISAL')
          {
            this.barisal_total_sales.push(q.total_sales)
          }
          if(q.division == 'CHITTAGONG')
          {
            this.chittagong_total_sales.push(q.total_sales)
          }
          if(q.division == 'DHAKA')
          {
            this.dhaka_total_sales.push(q.total_sales)
          }
          if(q.division == 'KHULNA')
          {
            this.khulna_total_sales.push(q.total_sales)
          }
          if(q.division == 'RAJSHAHI')
          {
            this.rajshahi_total_sales.push(q.total_sales)
          }
          if(q.division == 'RANGPUR')
          {
            this.rangpur_total_sales.push(q.total_sales)
          }
          if(q.division == 'SYLHET')
          {
            this.sylhet_total_sales.push(q.total_sales)
          }
        }


      }
      this.data_all = data;
    })
  }

}
