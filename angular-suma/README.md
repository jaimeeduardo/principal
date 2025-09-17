# Ejemplo de suma de dos números con Angular

Este directorio contiene un componente de Angular que suma dos números en tiempo real y muestra el resultado en pantalla.

## Archivos principales

- `sum.component.ts`: Lógica del componente con las propiedades `numberA` y `numberB`, junto a un _getter_ `total` que calcula la suma.
- `sum.component.html`: Plantilla que dibuja los campos numéricos y el resultado.
- `sum.component.css`: Estilos sencillos para presentar el formulario.

## Uso dentro de un proyecto Angular

1. Copia los archivos dentro de tu proyecto, por ejemplo en `src/app/sum/`.
2. Registra el componente en tu módulo (ej. `AppModule`). Si usas la clase tal cual, añade el módulo `FormsModule` para trabajar con los inputs si prefieres usar `ngModel`. En este ejemplo usamos enlaces de eventos, por lo que no es obligatorio.

```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { SumComponent } from './sum/sum.component';

@NgModule({
  declarations: [SumComponent],
  imports: [BrowserModule],
  bootstrap: [SumComponent],
})
export class AppModule {}
```

3. Añade la etiqueta del componente en la plantilla donde quieras mostrar el formulario, por ejemplo en `app.component.html`:

```html
<app-suma></app-suma>
```

Al ejecutar tu aplicación (`ng serve`), verás dos campos numéricos que se suman automáticamente.
