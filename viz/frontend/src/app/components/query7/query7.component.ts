import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup} from "@angular/forms";
import {QueryService} from "../../services/query.service";

@Component({
  selector: 'app-query7',
  templateUrl: './query7.component.html',
  styleUrls: ['./query7.component.css']
})
export class Query7Component implements OnInit {

  private days_input: any;

  query7From = new FormGroup({
    days: new FormControl(''),
  });

  constructor(private queryService: QueryService) {
  }

  data_all: any[] = [];

  // @ts-ignore
  dtOptions: DataTables.Settings = {};



  ngOnInit(): void {
    this.dtOptions = {
      pagingType: 'full_numbers'
    };
  }

  search() {
    this.days_input = this.query7From.value.days
    this.queryService.getQuery7(this.days_input).subscribe((data: any) => {
      for (const d of data) {
        console.log(d)
      }
      this.data_all = data;
    })
  }

}
