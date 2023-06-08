import {Component, OnInit} from '@angular/core';
import {ChartDataset, ChartOptions} from "chart.js";
import {QueryService} from "../../services/query.service";
import {query} from "@angular/animations";
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-query10',
  templateUrl: './query10.component.html',
  styleUrls: ['./query10.component.css']
})
export class Query10Component implements OnInit {

  data_all: any[] = [];
  store_ID: any[] = [];
  month1_avgSales: any[] = [];
  month2_avgSales: any[] = [];
  month3_avgSales: any[] = [];
  month4_avgSales: any[] = [];
  month5_avgSales: any[] = [];
  month6_avgSales: any[] = [];
  month7_avgSales: any[] = [];
  month8_avgSales: any[] = [];
  month9_avgSales: any[] = [];
  month10_avgSales: any[] = [];
  month11_avgSales: any[] = [];
  month12_avgSales: any[] = [];


  chartData: ChartDataset[] = [
    {
      label: "January",
      type:"bar",
      backgroundColor: "pink",
      borderColor: "red",
      borderWidth: 1,
      data: this.month1_avgSales
    },
    {
      label: "February",
      type:"bar",
      backgroundColor: "lightblue",
      borderColor: "blue",
      borderWidth: 1,
      data: this.month2_avgSales
    },
    {
      label: "March",
      type:"bar",
      backgroundColor: "lightgreen",
      borderColor: "green",
      borderWidth: 1,
      data: this.month3_avgSales
    },
    {
      label: "April",
      type:"bar",
      backgroundColor: "lavender",
      borderColor: "purple",
      borderWidth: 1,
      data: this.month4_avgSales
    },
    {
      label: "May",
      type:"bar",
      backgroundColor: "lightsalmon",
      borderColor: "orange",
      borderWidth: 1,
      data: this.month5_avgSales
    },
    {
      label: "June",
      type:"bar",
      backgroundColor: "lightcyan",
      borderColor: "cyan",
      borderWidth: 1,
      data: this.month6_avgSales
    },
    {
      label: "July",
      type:"bar",
      backgroundColor: "lightyellow",
      borderColor: "yellow",
      borderWidth: 1,
      data: this.month7_avgSales
    },
    {
      label: "August",
      type:"bar",
      backgroundColor: "lightskyblue",
      borderColor: "skyblue",
      borderWidth: 1,
      data: this.month8_avgSales
    },
    {
      label: "September",
      type:"bar",
      backgroundColor: "lightgoldenrodyellow",
      borderColor: "goldenrod-yellow",
      borderWidth: 1,
      data: this.month9_avgSales
    },
    {
      label: "October",
      type:"bar",
      backgroundColor: "lightcoral",
      borderColor: "coral",
      borderWidth: 1,
      data: this.month10_avgSales
    },
    {
      label: "November",
      type:"bar",
      backgroundColor: "paleturquoise",
      borderColor: "turquoise",
      borderWidth: 1,
      data: this.month11_avgSales
    },
    {
      label: "December",
      type:"bar",
      backgroundColor: "lightpink",
      borderColor: "pink",
      borderWidth: 1,
      data: this.month12_avgSales
    }
  ];
  chartLabels: string[] = this.store_ID;
  chartOptions: ChartOptions = {

    // ⤵️ Fill the wrapper
    responsive: true,
    maintainAspectRatio: true,

    plugins: {
      legend: {
        display: true
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

  constructor(private queryService: QueryService, private http: HttpClient) {
  }

  ngOnInit() {
    this.query10Data();
  }

  query10Data(): void {
    this.queryService.getQuery10().subscribe((data: any) => {
        for (const d of data) {
          // console.log(d)
          this.store_ID.push(d.store_ID)
          if(d.month == "1")
          {
            this.month1_avgSales.push(d.average_sales)
          }
          if(d.month == "2")
          {
            this.month2_avgSales.push(d.average_sales)
          }
          if(d.month == "3")
          {
            this.month3_avgSales.push(d.average_sales)
          }
          if(d.month == "4")
          {
            this.month4_avgSales.push(d.average_sales)
          }
          if(d.month == "5")
          {
            this.month5_avgSales.push(d.average_sales)
          }
          if(d.month == "6")
          {
            this.month6_avgSales.push(d.average_sales)
          }
          if(d.month == "7")
          {
            this.month7_avgSales.push(d.average_sales)
          }
          if(d.month == "8")
          {
            this.month8_avgSales.push(d.average_sales)
          }
          if(d.month == "9")
          {
            this.month9_avgSales.push(d.average_sales)
          }
          if(d.month == "10")
          {
            this.month10_avgSales.push(d.average_sales)
          }
          if(d.month == "11")
          {
            this.month11_avgSales.push(d.average_sales)
          }
          if(d.month == "12")
          {
            this.month12_avgSales.push(d.average_sales)
          }
        }
        this.data_all = data;
      }
    )
  }

}
