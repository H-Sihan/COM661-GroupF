import { Component } from '@angular/core';
import { BusinessData } from '../../services/business-data';
import { RouterLink } from '@angular/router';
import { RouterOutlet, RouterModule } from '@angular/router';

@Component({
  imports: [RouterLink, RouterOutlet, RouterModule],
  providers: [BusinessData],
  selector: 'app-businesses',
  styleUrl: './businesses.css',
  templateUrl: './businesses.html',
})
export class Businesses {

  business_list: any = [ ];
  page: number = 1;

  constructor(private businessData: BusinessData) { }

  ngOnInit() {
    this.business_list = this.businessData.getBusinesses(this.page);
  }

  nextPage(){
    if (this.page < this.businessData.getLastPageNumber()){
      this.page = this.page + 1
      this.business_list = this.businessData.getBusinesses(this.page);
    }
  }
  previousPage() {
    if(this.page > 1){
      this.page = this.page - 1
      this.business_list = this.businessData.getBusinesses(this.page);
    }
  }
}
