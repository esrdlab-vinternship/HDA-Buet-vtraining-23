import { Component, OnInit } from '@angular/core';
import {QueryService} from "../../services/query.service";

@Component({
  selector: 'app-new-component',
  templateUrl: './new-component.component.html',
  styleUrls: ['./new-component.component.css']
})
export class NewComponentComponent implements OnInit {

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.queryService.getHello().subscribe((data: any) => {
      console.log(data)
    })

  }

}
