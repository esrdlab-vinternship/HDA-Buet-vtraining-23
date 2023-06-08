import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query9',
  templateUrl: './query9.component.html',
  styleUrls: ['./query9.component.css']
})

export class Query9Component implements OnInit {

  data_all:any[] = [];
  item: any[]  = [];
  sales_Khulna: any[]=[]
  sales_Barisal: any[]=[]
  sales_Dhaka: any[]=[]
  sales_Chittagong: any[]=[]
  sales_Rajshahi: any[]=[]
  sales_Sylhet: any[]=[]
  sales_Rangpur: any[]=[]

  chartData: ChartDataset[] = [
    {
      label: "Khulna",
      type:"bar",
      backgroundColor: "pink",
      borderColor: "red",
      borderWidth: 1,
      data: this.sales_Khulna
    },
    {
      label: "Dhaka",
      type:"bar",
      backgroundColor: "lightblue",
      borderColor: "blue",
      borderWidth: 1,
      data: this.sales_Dhaka
    },
    {
      label: "Barisal",
      type:"bar",
      backgroundColor: "lightgreen",
      borderColor: "green",
      borderWidth: 1,
      data: this.sales_Barisal
    },
    {
      label: "Rangpur",
      type:"bar",
      backgroundColor: "lavender",
      borderColor: "purple",
      borderWidth: 1,
      data: this.sales_Rangpur
    },
    {
      label: "Rajshahi",
      type:"bar",
      backgroundColor: "lightsalmon",
      borderColor: "orange",
      borderWidth: 1,
      data: this.sales_Rajshahi
    },
    {
      label: "Sylhet",
      type:"bar",
      backgroundColor: "lightcyan",
      borderColor: "cyan",
      borderWidth: 1,
      data: this.sales_Sylhet
    },
    {
      label: "Chittagong",
      type:"bar",
      backgroundColor: "lightyellow",
      borderColor: "yellow",
      borderWidth: 1,
      data: this.sales_Chittagong
    }
  ];
  chartLabels: string[] = this.item;
  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,


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
      //console.log(data);
      //data= data.slice(0, 100);

      for(const d of data){
        this.item.push(d.item)
        if(d.division == "KHULNA")
        {
          this.sales_Khulna.push(d.sales)
        }
        if(d.division == "DHAKA")
        {
          this.sales_Dhaka.push(d.sales)
        }
        if(d.division == "BARISAL")
        {
          this.sales_Barisal.push(d.sales)
        }
        if(d.division == "RAJSHAHI")
        {
          this.sales_Rajshahi.push(d.sales)
        }
        if(d.division == "SYLHET")
        {
          this.sales_Sylhet.push(d.sales)
        }
        if(d.division == "RANGPUR")
        {
          this.sales_Rangpur.push(d.sales)
        }
        if(d.division == "CHITTAGONG")
        {
          this.sales_Chittagong.push(d.sales)
        }
      }
      this.data_all = data;
    })
  }

}
