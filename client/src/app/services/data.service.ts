import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { Data } from '../models/data'


@Injectable({
  providedIn: 'root'
})
export class DataService {

  url:string = 'http://127.0.0.1:5000/'; // api rest
  url_test_post:string = 'http://127.0.0.1:5000/api/v1/post_data';
  url_test_get:string = 'https://viacep.com.br/ws/56600000/json'

  constructor(private http: HttpClient) {
  }

  getData(): Observable<any[]> {
    return this.http.get<any[]>(this.url_test_get)
      .pipe(
        retry(2),
        catchError(this.handleError))
  }

  postData(file: any, data: File, options: object): any {
    this.http.post<any>(this.url_test_post, data, options).toPromise().then(
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
