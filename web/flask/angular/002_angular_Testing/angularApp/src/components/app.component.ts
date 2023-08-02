import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div>Angular Test App</div>
    <hr />

    <!-- Angular Routes -->
    <router-outlet></router-outlet>
  `,
  styleUrls: []
})
export class AppComponent {
  
}
