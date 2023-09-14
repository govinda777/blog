---
layout: post
title: Autocomplet in grid
date: 2023-09-14
categories: Artigo
---

<p align="center">
<img src="{{ site.baseurl }}/images/2023-09-14-Autocomplet-in-grid.png" height="50%" width="50%" alt="Unform" />
</p>

# Como implementar um auto-complete com Angular 10 em um grid

Neste tutorial, você aprenderá a implementar um recurso de auto-complete em um grid usando Angular 10. Vamos usar o pacote Angular Material para facilitar o processo.

## Pré-requisitos:

- Ter o Node.js e o npm instalados.
- Ter o Angular CLI instalado. Se não tiver, instale-o com `npm install -g @angular/cli`.

## Passos:

### 1. Crie um novo projeto Angular:

```bash
ng new angular-autocomplete-grid
cd angular-autocomplete-grid
```

### 2. Instale o Angular Material:

```bash
ng add @angular/material
```

Siga as instruções para escolher um tema e configurar gestos e animações.

### 3. Importe os módulos necessários:

No arquivo `app.module.ts`, importe os módulos necessários:

```typescript
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatInputModule } from '@angular/material/input';
import { MatTableModule } from '@angular/material/table';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    // ... seus componentes aqui
  ],
  imports: [
    // ... outros módulos aqui
    MatAutocompleteModule,
    MatInputModule,
    MatTableModule,
    ReactiveFormsModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

### 4. Implemente o auto-complete no grid:

No seu componente, por exemplo `app.component.ts`:

```typescript
import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  myControl = new FormControl();
  options: string[] = ['Opção 1', 'Opção 2', 'Opção 3'];
  filteredOptions: Observable<string[]>;

  ngOnInit() {
    this.filteredOptions = this.myControl.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value))
    );
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    return this.options.filter(option => option.toLowerCase().includes(filterValue));
  }
}
```

No seu template, `app.component.html`:

```html
<mat-form-field>
  <input type="text" placeholder="Escolha uma opção" matInput [matAutocomplete]="auto" [formControl]="myControl">
  <mat-autocomplete #auto="matAutocomplete">
    <mat-option *ngFor="let option of filteredOptions | async" [value]="option">
      {{option}}
    </mat-option>
  </mat-autocomplete>
</mat-form-field>

<mat-table [dataSource]="options">
  <!-- Seu grid aqui -->
</mat-table>
```

### 5. Estilize conforme necessário:

Ajuste o CSS no arquivo `app.component.css` para que o grid e o auto-complete se ajustem ao design desejado.

### 6. Execute o projeto:

```bash
ng serve
```

Agora, ao acessar `http://localhost:4200/`, você verá um campo de auto-complete acima de um grid. À medida que você digita no campo, as opções que correspondem ao texto inserido serão exibidas.

Espero que este tutorial tenha sido útil! Com esses passos, você deve ser capaz de implementar um recurso de auto-complete em um grid usando Angular 10 e Angular Material.