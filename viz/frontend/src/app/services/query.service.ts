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
    return this.http.get<any>(`${baseUrl}/query1`);
  }

  getQuery2(): Observable <any> {
    return this.http.get<any>(`${baseUrl}/query2`);
  }
  getQuery7(days?:any): Observable <any> {
    const headers = { 'content-type': 'application/json'}
    const body=JSON.stringify({'days': days});
    return this.http.post(`${baseUrlOther}/query7`, body,{'headers':headers})
  }

  getHello(): Observable<any>{
    return this.http.get(`${baseUrl}/hello`)
  }
}
