
# Guía rapida Markdown

## _Indice_

<p align="right">
  <a href="README.md">- 🔄 Regresar</a>
<p>

- [Guía rapida Markdown](#guía-rapida-markdown)
  - [_Indice_](#indice)
  - [__Titulos #__](#titulos-)
  - [Propiedades de texto](#propiedades-de-texto)
  - [Listas ordenadas y desordenadas](#listas-ordenadas-y-desordenadas)
  - [Enlaces](#enlaces)
  - [Blaquote](#blaquote)
  - [Lineas divisorias](#lineas-divisorias)
  - [Pegar Codigo](#pegar-codigo)
    - [Linea de codigo](#linea-de-codigo)
    - [Bloque de codigo](#bloque-de-codigo)
  - [Tablas](#tablas)
    - [Tabla normal](#tabla-normal)
    - [Tabla con alineaciones](#tabla-con-alineaciones)
  - [Insertar imagenes](#insertar-imagenes)
    - [Mediante Hipervinculo](#mediante-hipervinculo)
    - [Localmente](#localmente)

## __Titulos #__

<!-- Headings -->
```markdown
# H1 Markdown

## H2

### H3

#### H4
```

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## Propiedades de texto
<!-- Tipos de textos -->
```md
This is an *italic* text

This is an **Strong** text

Este es un ~~text~~ tachado
```

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## Listas ordenadas y desordenadas

Simbolos ( *, +, -)

```md
UL Unordered list

* Elemento 1
* Elemento 2
    * Subelemento 2.1
+ Elemento 3
    1. Sub elemento 3.1 (Usa tabulador)
- Elemento 4

 OL Ordered list

 1. Item 1
    1. subitem 1.1 (Usa tabulador)
 2. Item 2
```

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## Enlaces

```md
[Enlace](www.vatosconsesos.com)

[Enlace con preview](vatosconsesos.com "Titulo preview")  

Enlace limpio  
 <https://www.youtube.com>
```

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## Blaquote

> this is a quote

```md
> this is a quote
```

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## Lineas divisorias

```md
--- guion
```

---

```md
___ guion bajo
```

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## Pegar Codigo

Se usan las comillas invertidas (__``__) [Alt + 96]

### Linea de codigo

`console.log('Hello world)`

```md
`console.log('Hello world)`
```

### Bloque de codigo

```javascript
var sumar2 = function(numero) {
    return numero + 2;
}
console.log('Hello world')
```

```md
    ```javascript
    var sumar2 = function(numero) {
        return numero + 2;
    }
    console.log('Hello world')
    ```
```

>[!note]
>Al final de las primeras tre comillas le indicas a md el lenguaje que es, algunos IDE como GitHub le da colores
>
> [Triple comilla][Nombre del lenguaje]
>
> codigo
>
> [Triple comilla]

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## Tablas

### Tabla normal

|   ID  |   Campo 1     |   Campo 2     |
| ----- | ------------- | ------------- |
| 1 | Registro numero  1 | Registro numero 2|
| 2 | ... | lll |
| 2 | Ultimo Registro | NULL RELLENAR CAMPO |

```md
|   ID  |   Campo 1     |   Campo 2     |
| ----- | ------------- | ------------- |
| 1 | Registro numero  1 | Registro numero 2|
| 2 | ... | lll |
| 2 | Ultimo Registro | NULL RELLENAR CAMPO |
```

### Tabla con alineaciones

|   ID_USER  |   Campo 1     |   Campo 2     |
| :----- | :-------------: | -------------:|
| 1 | Registro numero  1 | Registro numero 2|
| 2 | ... | lll |
| 2 | Ultimo Registro | NULL RELLENAR CAMPO |
| __Izquierda...__ | __Centrado__ | __Derecha__ |

```md
|   ID_USER  |   Campo 1     |   Campo 2     |
| :----- | :-------------: | -------------:|
| 1 | Registro numero  1 | Registro numero 2|
| 2 | ... | lll |
| 2 | Ultimo Registro | NULL RELLENAR CAMPO |
| __Izquierda__ | __Centrado__ | __Derecha__ |
```

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## Insertar imagenes

### Mediante Hipervinculo

![Visual estudio code logo](https://www.330ohms.com/cdn/shop/articles/thumbnail_visualstudiocode_01_1200x675.png?v=1722326500 "VSC logo url")

```md
![Visual estudio code logo](https://www.330ohms.com/cdn/shop/articles/thumbnail_visualstudiocode_01_1200x675.png?v=1722326500 "VSC logo url")

```

### Localmente

```md
![Visual Estudio Code](logoVSC.png "Logo guardado VSC localmente")
```

![Visual Estudio Code](logoVSC.png "Logo guardado VSC localmente")

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>
