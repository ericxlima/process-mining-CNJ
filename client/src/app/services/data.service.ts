import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { Data } from '../models/data'


@Injectable({
  providedIn: 'root'
})
export class DataService {

  url_post_api:string = 'http://127.0.0.1:5000/api/v1/post_data';
  url_get_img:string = 'http://127.0.0.1:5000/api/v1/<link>'

  response:any = 'aqui';

  constructor(private http: HttpClient) {
  }

  getData(): Observable<any[]> {
    return this.http.get<any[]>(this.url_get_img)
      .pipe(
        retry(2),
        catchError(this.handleError))
  }

  postData(file: any, data: File, options: object): Observable<any[]> {
    return this.http.post<any[]>(this.url_post_api, data, options).pipe(
      retry(2),
      catchError(this.handleError))
    
    // .subscribe((response:any)=>{
    //   console.log('response URI SERVER:' + response.uri)

    //   return response.uri
    // })
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
