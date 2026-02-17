# Reglas para GitHub

GitHub Flavored Markdown

## _Indice_

<p align="right">
  <a href="README.md">- 🔄 Regresar</a>
<p>

- [Reglas para GitHub](#reglas-para-github)
  - [_Indice_](#indice)
  - [✅ Checklists (Tareas interactivas)](#-checklists-tareas-interactivas)
  - [🚨 Alertas (GitHub flavored)](#-alertas-github-flavored)
  - [🔗 Menciones y referencias automáticas](#-menciones-y-referencias-automáticas)
  - [📎 Enlaces internos a archivos](#-enlaces-internos-a-archivos)
  - [🏷 Emojis compatibles](#-emojis-compatibles)
  - [📊 Tablas compatibles](#-tablas-compatibles)
  - [📌 Colapsables (Muy útil y poco usado)](#-colapsables-muy-útil-y-poco-usado)
  - [🖼 Imágenes centradas (HTML permitido)](#-imágenes-centradas-html-permitido)
  - [🧩 Comentarios invisibles](#-comentarios-invisibles)

## ✅ Checklists (Tareas interactivas)

Permiten marcar tareas directamente desde el navegador.

```md
- [x] Tarea completada
- [ ] Tarea pendiente
```

Ejemplo:

* [x] Configurar proyecto
* [ ] Escribir documentación
* [ ] Subir cambios

⚠ Importante:
Debe haber un espacio entre `[ ]`.

Incorrecto:

```md
- [] Tarea
```

Correcto:

```md
- [ ] Tarea
```

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## 🚨 Alertas (GitHub flavored)

```md
>[!NOTE]
> Información útil
```

Las puedes modificar.

>[!NOTE] (Nota): Información útil.
> `>[!NOTE] (Nota): Información útil.`
---
>[!TIP] (Consejo): Consejos útiles.
> `>[!TIP] (Consejo): Consejos útiles.`
---
>[!IMPORTANT] (Importante): Información crucial.
> `>[!IMPORTANT] (Importante): Información crucial.`
---
>[!WARNING] (Advertencia): Información urgente.
> `>[!WARNING] (Advertencia): Información urgente.`
---
>[!CAUTION] (Precaución): Riesgos o consecuencias negativas.
> `>[!CAUTION] (Precaución): Riesgos o consecuencias negativas.`

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## 🔗 Menciones y referencias automáticas

GitHub convierte automáticamente:

```md
@usuario
#123
```

* `@usuario` → Menciona persona
* `#123` → Referencia un Issue o Pull Request
* `usuario/repo#45` → Referencia externa

Muy útil en documentación colaborativa.

---

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## 📎 Enlaces internos a archivos

```md
[Guía](./Guia-rapida-markdown.md)
```

Buenas prácticas:

* Usar rutas relativas
* No usar rutas absolutas del sistema
* Mantener nombres consistentes

---

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## 🏷 Emojis compatibles

GitHub soporta sintaxis tipo:

```md
:rocket:
:fire:
:warning:
:bulb:
:construction:
```

Ejemplo:

:rocket: Proyecto listo
:construction: En desarrollo

Puedes ver la lista completa aquí:
[https://github.com/ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet)

---

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## 📊 Tablas compatibles

GitHub respeta alineaciones:

```md
| ID | Nombre | Estado |
|:---|:------:|------:|
| 1 | Luis | Activo |
```

* `:---` → izquierda
* `:---:` → centrado
* `---:` → derecha

---

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## 📌 Colapsables (Muy útil y poco usado)

Esto es oro para READMEs largos.

```html
<details>
<summary>Click para ver más</summary>

Contenido oculto aquí.

Puede incluir:
- Código
- Tablas
- Imágenes

</details>
```

Ejemplo funcional:

<details>
<summary>Ejemplo</summary>

Este contenido está colapsado.

</details>

Perfecto para:

* Logs largos
* Instalaciones opcionales
* Explicaciones extendidas

---

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>

## 🖼 Imágenes centradas (HTML permitido)

GitHub permite HTML básico.

```html
<p align="center">
  <img src="logo.png" width="200" />
</p>
```

Puedes controlar:

* width
* align
* style básico

---

## 🧩 Comentarios invisibles

No se renderizan en GitHub.

```html
<!-- Esto no se mostrará -->
```

Muy útil para:

* Notas internas
* Recordatorios
* Organización

---

<p align="right">
  <a href="#indice">- 📝 Indice</a>
<p>
