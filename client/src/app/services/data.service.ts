import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { Data } from '../models/data'


@Injectable({
  providedIn: 'root'
})
export class DataService {

  url = 'http://127.0.0.1:5000/'; // api rest
  url_test_post = 'http://127.0.0.1:5000/api/v1/post_data';
  url_test_get = 'https://viacep.com.br/ws/56600000/json'
  constructor(private httpClient: HttpClient) { }

  // Headers
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/csv' })
  }

  getData(): Observable<any[]> {
    return this.httpClient.get<any[]>(this.url_test_get)
      .pipe(
        retry(2),
        catchError(this.handleError))
  }

  postData(file:any): any {
    const headers = {
      'Access-Control-Allow-Origin': 'True',
      'Accept': 'application/csv',
      'Content-Type': 'application/csv',
      'cache': 'false',
      'method': 'POST',
      'dataType': 'csv',
    }
    this.httpClient.post<any>(this.url_test_post, file, {headers}).toPromise().then(
      data=>{console.log(data)}
    )

  }

  handleError(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Erro ocorreu no lado do client
      errorMessage = error.error.message;
    } else {
      // Erro ocorreu no lado do servidor
      errorMessage = `Error Code: ${error.status}, ` + `message: ${error.message}`;
    }
    console.log(errorMessage);
    return throwError(errorMessage);
  };

}
