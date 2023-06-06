import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";
import {ChartDataset, ChartOptions} from "chart.js";

@Component({
  selector: 'app-query8',
  templateUrl: './query8.component.html',
  styleUrls: ['./query8.component.css']
})
export class Query8Component implements OnInit {

  data_all:any[] = [];
  Q1_dataset:any[] = [];
  Q2_dataset:any[] = [];
  Q3_dataset:any[] = [];
  Q4_dataset:any[] = [];
  items :string[] =[];





  chartData: ChartDataset[] = [
    {
      type: 'scatter',
      label: 'Q1',
      data: this.Q1_dataset
    },
    {
      type: 'scatter',
      label: 'Q2',
      data: this.Q2_dataset
    },
    {
      type: 'scatter',
      label: 'Q3',
      data: this.Q3_dataset
    },
    {
      type: 'scatter',
      label: 'Q4',
      data: this.Q4_dataset
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
    this.query8Data();
  }

  query8Data(): void{
    this.queryService.getQuery8().subscribe((data:any)=>{

      for(const d of data){
        console.log(d);
        this.items.push(d.item_name)

        if(d.quarter == "Q1")
        {
          const coordinate = { x: 0, y: 0 };
          coordinate.x = d.item_name
          coordinate.y = d.total_price
          this.Q1_dataset.push(coordinate)
        }

        if(d.quarter == "Q2")
        {
          const coordinate = { x: 0, y: 0 };
          coordinate.x = d.item_name
          coordinate.y = d.total_price
          this.Q2_dataset.push(coordinate)
        }

        if(d.quarter == "Q3")
        {
          const coordinate = { x: 0, y: 0 };
          coordinate.x = d.item_name
          coordinate.y = d.total_price
          this.Q3_dataset.push(coordinate)
        }
        if(d.quarter == "Q4")
        {
          const coordinate = { x: 0, y: 0 };
          coordinate.x = d.item_name
          coordinate.y = d.total_price
          this.Q4_dataset.push(coordinate)
        }


      }
      this.data_all = data;
    })
  }

}
