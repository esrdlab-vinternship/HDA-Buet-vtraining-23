import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

const baseUrl = 'http://127.0.0.1:5000/api'

@Injectable({
  providedIn: 'root'
})
export class QueryService {

  constructor(private http: HttpClient) { }

  getQuery1() : Observable<any> {
    return this.http.get(`${baseUrl}/query1`);
  }

  getQuery2() : Observable<any> {
    return this.http.get(`${baseUrl}/query2`);
  }

  getQuery3() : Observable<any> {
    return this.http.get(`${baseUrl}/query3`);
  }

  getQuery4() : Observable<any> {
    return this.http.get(`${baseUrl}/query4`);
  }

  getQuery5() : Observable<any> {
    return this.http.get(`${baseUrl}/query5`);
  }
}
