import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";

const baseUrl = 'http://127.0.0.1:5000/api'
const baseUrlOther = 'http://127.0.0.1:5000/api1'

@Injectable({
  providedIn: 'root'
})
export class QueryService {

  constructor(private http: HttpClient) {
  }

  getQuery1(): Observable<any> {
    return this.http.get<any>(`${baseUrl}/q1`);
  }

  getQuery2(): Observable <any> {
    return this.http.get<any>(`${baseUrl}/q2`);
  }

  getQuery3(): Observable <any> {
    return this.http.get<any>(`${baseUrl}/q3`);
  }

  getQuery4(): Observable <any> {
    return this.http.get<any>(`${baseUrl}/q4`);
  }

  getQuery5(): Observable <any> {
    return this.http.get<any>(`${baseUrl}/q5`);
  }

  getQuery6(): Observable <any> {
    return this.http.get<any>(`${baseUrl}/q6`);
  }
  
  getQuery7(days?:any): Observable <any> {
    const headers = { 'content-type': 'application/json'}
    const body=JSON.stringify({'days': days});
    return this.http.post(`${baseUrl}/q7`, body,{'headers':headers})
  }

  getQuery8(): Observable <any> {
    return this.http.get<any>(`${baseUrl}/q8`);
  }

  getHello(): Observable<any>{
    return this.http.get(`${baseUrl}/hello`)
  }
}
