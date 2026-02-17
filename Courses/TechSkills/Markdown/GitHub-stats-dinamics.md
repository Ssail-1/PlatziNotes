
# 📊 GitHub Stats Dinámicas

Las estadísticas dinámicas permiten mostrar información actualizada automáticamente en tu README.

Se generan usando servicios externos que leen tu perfil público.

---

## 1️⃣ GitHub Readme Stats (Estadísticas generales)

Servicio más usado:

```md
https://github-readme-stats.vercel.app
```

### 📌 Estructura básica

```md
https://github-readme-stats.vercel.app/api
?username=TUUSUARIO
&show_icons=true
&theme=tokyonight
```

#### 🧪 Ejemplo

```html
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=anuraghazra&show_icons=true&theme=tokyonight" />
</p>
```

### 🔧 Parámetros importantes

| Parámetro            | Qué hace               |
| -------------------- | ---------------------- |
| `username`           | Tu usuario de GitHub   |
| `show_icons=true`    | Muestra iconos         |
| `theme=`             | Cambia el tema visual  |
| `hide=`              | Oculta métricas        |
| `count_private=true` | Incluye repos privados |

---

## 2️⃣ Lenguajes más usados

Se usa el mismo servicio pero otro endpoint:

```md
https://github-readme-stats.vercel.app/api/top-langs/
```

### 🧪 Ejemplo

```html
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=anuraghazra&layout=compact&theme=tokyonight" />
</p>
```

### 📌 Parámetros útiles

| Parámetro        | Función             |
| ---------------- | ------------------- |
| `layout=compact` | Diseño compacto     |
| `langs_count=8`  | Número de lenguajes |
| `theme=`         | Cambia tema         |

---

## 3️⃣ GitHub Streak (Racha de contribuciones)

Servicio:

```md
https://github-readme-streak-stats.herokuapp.com
```

### 🧪 Ejemplo

```html
<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=anuraghazra&theme=tokyonight" />
</p>
```

Muestra:

* Días consecutivos de commits
* Mejor racha
* Total de contribuciones

---

## 🎨 Temas populares actuales

Algunos themes modernos que se ven bien en 2026:

* `tokyonight`
* `radical`
* `github_dark`
* `dracula`
* `transparent`
* `onedark`
* `nightowl`

---

## 💡 Diseño Profesional (Importante)

Regla de oro:

No pongas las 3 tarjetas gigantes una debajo de otra.

Mejor algo así:

```html
<p align="center">
  <img src="STATS_URL" />
  <img src="LANGS_URL" />
</p>

<p align="center">
  <img src="STREAK_URL" />
</p>
```

Eso hace que se vea limpio.

---

## 🧠 Para pensar

Estas cards son:

* SVG dinámicos
* Renderizados por Vercel
* Personalizables
* Ligeros
* Automáticos

Pero…

No sustituyen proyectos reales.

Son complemento visual.

---

## 🚀 Extra avanzado

Existe también:

### 🏆 GitHub Trophies

Servicio:

```md
https://github-profile-trophy.vercel.app
```

Ejemplo:

```html
<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=anuraghazra&theme=tokyonight" />
</p>
```

---
