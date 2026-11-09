import { Component } from '@angular/core';

@Component({
  imports: [],
  selector: 'app-businesses',
  styleUrl: './businesses.css',
  templateUrl: './businesses.html',
})
export class Businesses {

  business_list = [
    {
      "name":"Starbucks",
      "town":"Coleraine",
      "rating": 5
    },
    {
      "name":"Costa",
      "town":"Belfast",
      "rating": 5
    },
    {
      "name":"Nero",
      "town":"London",
      "rating": 4
    },
  ]
}
