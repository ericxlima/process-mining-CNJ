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
  constructor(private httpClient: HttpClient) { }

  // Headers
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/csv' })
  }

  getData(): Observable<Data[]> {
    return this.httpClient.get<Data[]>(this.url)
      .pipe(
        retry(2),
        catchError(this.handleError))
  }

  // getDataByCase(Case: number): Observable<Data> {
  //   return this.httpClient.get<Data>(this.url + '/' + Case)
  //     .pipe(
  //       retry(2),
  //       catchError(this.handleError)
  //     )
  // }

  // saveData(data: Data): Observable<Data> {
  //   return this.httpClient.post<Data>(this.url, JSON.stringify(data), this.httpOptions)
  //     .pipe(
  //       retry(2),
  //       catchError(this.handleError)
  //     )
  // }

  // updateData(data: Data): Observable<Data> {
  //   return this.httpClient.put<Data>(this.url + '/' + data.Case, JSON.stringify(data), this.httpOptions)
  //     .pipe(
  //       retry(1),
  //       catchError(this.handleError)
  //     )
  // }

  // deleteData(data: Data) {
  //   return this.httpClient.delete<Data>(this.url + '/' + data.Case, this.httpOptions)
  //     .pipe(
  //       retry(1),
  //       catchError(this.handleError)
  //     )
  // }

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
