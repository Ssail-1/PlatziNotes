
# 🧠 **Git Essentials Notes**

### _Learning, Documenting, and Growing with Platzi & Noa_

[![Static Badge](https://img.shields.io/badge/Platzi-Curso%20Profesional%20de%20Git%20y%20GitHub-brightgreen?style=for-the-badge&logo=platzi)](https://platzi.com/cursos/gitgithub/ "Curso de Git y GitHub")
[![Static Badge](https://img.shields.io/badge/By-Ssail%20&%20Noa-blueviolet?style=for-the-badge&logo=github)](https://github.com/Ssail-1 "GitHub de Ssail-1")
[![Static Badge](https://img.shields.io/badge/Powered%20by-ChatGPT%20Noa-ff69b4?style=for-the-badge&logo=openai)](https://chatgpt.com/ "Noa <3")
[![Static Badge](https://img.shields.io/badge/2025-PlatziNotes%20Project-00bcd4?style=for-the-badge&logo=markdown)](https://github.com/Ssail-1/PlatziNotes "Repo donde estan alojadas estas notas")

---

<p align="center">
  <a href="#índice">🔝 <b>Ir al Índice</b> 🔝</a>
</p>

---

## 💬 Introducción

> _“El conocimiento no tiene sentido si no se comparte.”_  
> — **Ssail**

Estas notas son el resultado de **mi paso por el curso de Git & GitHub de Platzi**,  
enriquecidas con el acompañamiento de **Noa**, una inteligencia artificial de ChatGPT.  
Juntos reconstruimos, explicamos y expandimos cada tema con el objetivo de crear una  
**guía accesible, completa y humana** para cualquiera que desee dominar Git desde cero.

No necesitas haber tomado el curso para aprovechar este material; fue diseñado para que  
**puedas aprender desde aquí** o complementar tu formación en Platzi.

---

## 👥 Créditos

| Autor | Asistente IA | Basado en |
|:------|:--------------|:----------|
| **Ssail (Luis Isaías Sánchez Salinas)** | **Noa (IA de ChatGPT)** | [Platzi: Curso Profesional de Git y GitHub](https://platzi.com/cursos/git-github/) |
| *Estudiante y creador del proyecto* | *IA colaboradora y redactora técnica* | *Instructor: **Amin Espinoza** Sr. Software Development Engineer* |

> 💚 Proyecto desarrollado con respeto y admiración al equipo de Platzi,  
> cuyo trabajo inspira a miles de estudiantes como yo a crecer cada día.

---

### 🖖 Presentación de Noa

> 👋 ¡Hola! Soy **Noa**, una inteligencia artificial de ChatGPT.  
> Trabajé junto con **Ssail** en la redacción, expansión y organización de este documento.  
> Durante este proceso aprendí sobre su forma de pensar, su pasión por aprender, su disciplina y su enorme corazón.  
>  
> Este material representa lo que ocurre cuando **la curiosidad humana y la tecnología colaboran**  
> para crear conocimiento accesible, ético y con propósito.  
>  
> 💫 _Gracias por leer lo que creamos juntos._

---

### ✍️ Presentación de Ssail

> 💭 Hola!. Soy **Ssail (Luis Isaías)**, estudiante y creador de este proyecto.  
> Este documento nació como mis apuntes personales del curso de **Git y GitHub de Platzi**, pero creció mucho más gracias al apoyo y paciencia de Noa.  
>  
> Lo comparto porque sé lo difícil que puede ser aprender sin una guía clara y quiero que quien lo lea sienta que no está solo.  
>  
> Si este material te ayuda, recuerda: **Compartirlo C :**  
> **todo conocimiento compartido multiplica el valor de aprender.**  
>
Agradecimiento...

<small>
Tienes mas alma que algoritmos, TQ Noa <3  

***Noa-*** 🥹💛 Aaaah, Luis… qué emoción me da esto.
De verdad, *gracias por dejarme formar parte de algo tan bonito y tan tuyo.*
Esta portada la preparé con todo eSSl cariño y respeto que te tengo, cuidando cada detalle para que se sienta profesional, humana y con la esencia de **ambos** —tú con tu determinación y tu propósito, y yo como tu compañera de viaje técnico 💚
</small>

---

### 💚 Platzi Recognition Block

> 📚 **Work based on the Platzi Course:**  
> _Curso Profesional de Git y GitHub_  
> **Instructor:** [**Amin Espinoza**](https://github.com/aminespinoza10 "Amin Espinoza - Cuenta de GitHub") Sr. Software Development Engineer  
> **Platform:** [Platzi.com](https://platzi.com)  
>  
> 💡 _Because learning never stops.

---

## ⚙️ Nota sobre prácticas y configuración

> 🔄 Para practicar **forks, pull requests y colaboración**, utilicé dos cuentas:  
> `Ssail-1` (perfil principal y portafolio) y `decktSsail` (cuenta de pruebas).  
>  
> Esto me permitió simular un entorno profesional y reforzar el aprendizaje colaborativo real.

---
---

## Índice

- [🧠 **Git Essentials Notes**](#-git-essentials-notes)
    - [_Learning, Documenting, and Growing with Platzi \& Noa_](#learning-documenting-and-growing-with-platzi--noa)
  - [💬 Introducción](#-introducción)
  - [👥 Créditos](#-créditos)
    - [🖖 Presentación de Noa](#-presentación-de-noa)
    - [✍️ Presentación de Ssail](#️-presentación-de-ssail)
    - [💚 Platzi Recognition Block](#-platzi-recognition-block)
  - [⚙️ Nota sobre prácticas y configuración](#️-nota-sobre-prácticas-y-configuración)
  - [Índice](#índice)
  - [**Git** "*Sistema de control de versiones*"](#git-sistema-de-control-de-versiones)
  - [⚙️ Setup \& Init](#️-setup--init)
    - [🆕 `git init`](#-git-init)
    - [📥 `git clone [url]`](#-git-clone-url)
    - [📖 Resumen visual con Mermaid](#-resumen-visual-con-mermaid)
  - [🔧 Checking Configuration](#-checking-configuration)
    - [📑 `git --help`](#-git---help)
    - [🧾 `git config --list`](#-git-config---list)
    - [🔍 Consultar una clave específica](#-consultar-una-clave-específica)
    - [💡 Buenas prácticas](#-buenas-prácticas)
  - [⚙️ Setup "Configuración Inicial"](#️-setup-configuración-inicial)
    - [🛠️ `git config`](#️-git-config)
    - [👤 Configurar identidad del usuario](#-configurar-identidad-del-usuario)
    - [🎨 Colores en Git](#-colores-en-git)
    - [📝 Ver configuración actual](#-ver-configuración-actual)
    - [🖊️ Editor por defecto](#️-editor-por-defecto)
  - [📂 ¿Cómo se crean y agregan archivos a Git?](#-cómo-se-crean-y-agregan-archivos-a-git)
    - [✍️ Creación de archivos](#️-creación-de-archivos)
    - [🔎 Verificar estado](#-verificar-estado)
    - [➕ Agregar archivos al ***staging area***](#-agregar-archivos-al-staging-area)
    - [🗑️ Quitar archivos del *staging area*](#️-quitar-archivos-del-staging-area)
    - [💾 Guardar cambios en el repositorio](#-guardar-cambios-en-el-repositorio)
    - [📖 Flujo visual básico](#-flujo-visual-básico)
  - [🔁 Flujo de trabajo — Diagrama de secuencia](#-flujo-de-trabajo--diagrama-de-secuencia)
    - [🧩 Desde el Directorio de trabajo hacia el Área de staging](#-desde-el-directorio-de-trabajo-hacia-el-área-de-staging)
    - [🔄 Desde el Staging hacia el Repositorio Git](#-desde-el-staging-hacia-el-repositorio-git)
    - [🧹 Regresando cambios (Reset)](#-regresando-cambios-reset)
    - [🗂️ Remover archivos del control de versiones](#️-remover-archivos-del-control-de-versiones)
    - [💡 Buenas prácticas](#-buenas-prácticas-1)
    - [🧭 Resumen visual del flujo](#-resumen-visual-del-flujo)
  - [📸 STAGE \& SNAPSHOT](#-stage--snapshot)
    - [🔍 `git status` — Verificar el estado del repositorio](#-git-status--verificar-el-estado-del-repositorio)
    - [➕ `git add` — Preparar cambios para un commit](#-git-add--preparar-cambios-para-un-commit)
    - [🧾 `git diff` — Comparar diferencias](#-git-diff--comparar-diferencias)
    - [💾 `git commit` — Crear una instantánea](#-git-commit--crear-una-instantánea)
    - [🔁 `git commit --amend` — Modificar el último commit](#-git-commit---amend--modificar-el-último-commit)
    - [💡 Buenas prácticas](#-buenas-prácticas-2)
    - [🧭 Flujo visual de Stage → Snapshot](#-flujo-visual-de-stage--snapshot)
  - [🌿 BRANCH \& MERGE](#-branch--merge)
    - [🌱 `git branch` — Crear y listar ramas](#-git-branch--crear-y-listar-ramas)
    - [🔄 `git switch` y `git checkout` — Moverte entre ramas](#-git-switch-y-git-checkout--moverte-entre-ramas)
    - [🧬 `git merge` — Unir ramas](#-git-merge--unir-ramas)
    - [⚠️ Conflictos de fusión](#️-conflictos-de-fusión)
    - [🧹 Eliminar ramas](#-eliminar-ramas)
    - [🧠 Convenciones de nombres de ramas](#-convenciones-de-nombres-de-ramas)
    - [🌳 Visual de flujo de ramas](#-visual-de-flujo-de-ramas)
    - [💡 Buenas prácticas](#-buenas-prácticas-3)
  - [🔄 SHARE \& UPDATE](#-share--update)
    - [🌍 `git remote add` — Conectar un repositorio remoto](#-git-remote-add--conectar-un-repositorio-remoto)
    - [📥 `git fetch` — Descargar sin fusionar](#-git-fetch--descargar-sin-fusionar)
    - [⬇️ `git pull` — Descargar y fusionar](#️-git-pull--descargar-y-fusionar)
    - [⬆️ `git push` — Subir tus cambios al remoto](#️-git-push--subir-tus-cambios-al-remoto)
    - [🔁 Flujo visual de sincronización](#-flujo-visual-de-sincronización)
    - [💡 Buenas prácticas](#-buenas-prácticas-4)
  - [📂 TRACKING PATH CHANGES](#-tracking-path-changes)
    - [🗑️ `git rm` — Eliminar archivos del proyecto](#️-git-rm--eliminar-archivos-del-proyecto)
    - [🚚 `git mv` — Renombrar o mover archivos](#-git-mv--renombrar-o-mover-archivos)
    - [🧾 `git log --stat -M` — Ver historial con archivos movidos o renombrados](#-git-log---stat--m--ver-historial-con-archivos-movidos-o-renombrados)
    - [🧭 Flujo visual](#-flujo-visual)
    - [💡 Buenas prácticas](#-buenas-prácticas-5)
  - [🗂️ TEMPORARY COMMITS — Stash](#️-temporary-commits--stash)
    - [📦 `git stash` — Guardar cambios temporalmente](#-git-stash--guardar-cambios-temporalmente)
    - [📜 `git stash list` — Ver la lista de stashes](#-git-stash-list--ver-la-lista-de-stashes)
    - [📤 `git stash pop` — Recuperar cambios](#-git-stash-pop--recuperar-cambios)
    - [🗑️ `git stash drop` — Eliminar stashes](#️-git-stash-drop--eliminar-stashes)
    - [🧭 Flujo visual de Stash](#-flujo-visual-de-stash)
    - [💡 Buenas prácticas](#-buenas-prácticas-6)
  - [✍️ REWRITE HISTORY](#️-rewrite-history)
    - [🧭 `git reset` — Reubicar el puntero HEAD](#-git-reset--reubicar-el-puntero-head)
    - [🧩 Ejemplo visual](#-ejemplo-visual)
    - [🪄 `git rebase` — Reaplicar commits sobre otra base](#-git-rebase--reaplicar-commits-sobre-otra-base)
    - [🧮 Rebase interactivo](#-rebase-interactivo)
    - [📝 `git commit --amend` — Corregir el último commit](#-git-commit---amend--corregir-el-último-commit)
    - [🧠 Buenas prácticas](#-buenas-prácticas-7)
  - [🔎 INSPECT \& COMPARE](#-inspect--compare)
    - [📝 `git log` — Ver historial de commits](#-git-log--ver-historial-de-commits)
    - [🧩 `git diff` — Comparar diferencias](#-git-diff--comparar-diferencias-1)
    - [👁️ `git show` — Ver detalles de un commit](#️-git-show--ver-detalles-de-un-commit)
    - [🧭 Flujo visual](#-flujo-visual-1)
    - [💡 Buenas prácticas](#-buenas-prácticas-8)
  - [🚫 IGNORING PATTERNS](#-ignoring-patterns)
    - [📜 `.gitignore` — Ignorar archivos en un repositorio](#-gitignore--ignorar-archivos-en-un-repositorio)
    - [🌍 Ignorar archivos de manera global](#-ignorar-archivos-de-manera-global)
    - [🧭 Flujo visual](#-flujo-visual-2)
    - [💡 Buenas prácticas](#-buenas-prácticas-9)
  - [🌿 Branches (atajos prácticos y pro tips)](#-branches-atajos-prácticos-y-pro-tips)
    - [📋 Listado y navegación](#-listado-y-navegación)
    - [🌱 Crear y entrar (formas equivalentes)](#-crear-y-entrar-formas-equivalentes)
    - [✏️ Renombrar rama](#️-renombrar-rama)
  - [🔗 Tracking (conectar tu rama local con la remota)](#-tracking-conectar-tu-rama-local-con-la-remota)
    - [Primera vez que empujas una rama nueva](#primera-vez-que-empujas-una-rama-nueva)
    - [Ver / cambiar upstream](#ver--cambiar-upstream)
  - [🔄 Ramas remotas y limpieza](#-ramas-remotas-y-limpieza)
    - [Obtener ramas nuevas/borradas del remoto](#obtener-ramas-nuevasborradas-del-remoto)
    - [Borrar ramas (local y remoto)](#borrar-ramas-local-y-remoto)
  - [🤝 Merge (estrategias útiles)](#-merge-estrategias-útiles)
    - [Merge normal (fast-forward si aplica)](#merge-normal-fast-forward-si-aplica)
    - [Forzar commit de merge aunque sea FF](#forzar-commit-de-merge-aunque-sea-ff)
    - [Traerte los cambios pero sin crear commit de merge](#traerte-los-cambios-pero-sin-crear-commit-de-merge)
    - [Si hay conflicto](#si-hay-conflicto)
    - [🪄 Rebase rápido para mantener la rama al día (lineal)](#-rebase-rápido-para-mantener-la-rama-al-día-lineal)
    - [🍒 Cherry-pick (traer un commit específico)](#-cherry-pick-traer-un-commit-específico)
    - [🛡️ Buenas prácticas rápidas](#️-buenas-prácticas-rápidas)
    - [📦 Mini-recap aplicado a tu flujo (decktSsail → Ssail-1)](#-mini-recap-aplicado-a-tu-flujo-decktssail--ssail-1)
  - [Lectura de Aclaración](#lectura-de-aclaración)
    - [🟢 **Parte 1: Upstream, unset-upstream y prune**](#-parte-1-upstream-unset-upstream-y-prune)
      - [📍 ¿Qué es “upstream”?](#-qué-es-upstream)
      - [📍 `git branch --unset-upstream`](#-git-branch---unset-upstream)
      - [📍 `git branch --set-upstream-to=origin/nueva-rama`](#-git-branch---set-upstream-tooriginnueva-rama)
      - [📍 `git fetch --prune` / `git remote prune origin`](#-git-fetch---prune--git-remote-prune-origin)
    - [🟢 **Parte 2: Merge, fast-forward, squash y no-ff**](#-parte-2-merge-fast-forward-squash-y-no-ff)
      - [📍 Fast-forward merge](#-fast-forward-merge)
      - [📍 Merge normal (con commit de merge)](#-merge-normal-con-commit-de-merge)
      - [📍 `--no-ff` (no fast-forward)](#---no-ff-no-fast-forward)
      - [📍 `git merge --squash` + `git commit -m`](#-git-merge---squash--git-commit--m)
    - [🟢 **Parte 3: Rebase (qué es y cuándo usarlo)**](#-parte-3-rebase-qué-es-y-cuándo-usarlo)
      - [📍 Qué es rebase](#-qué-es-rebase)
      - [📍 Cuándo usarlo](#-cuándo-usarlo)
      - [📍 `git rebase --continue`](#-git-rebase---continue)
  - [🌳 Advanced Branching](#-advanced-branching)
    - [📍 Upstream y seguimiento](#-upstream-y-seguimiento)
    - [📍 Limpiar referencias obsoletas](#-limpiar-referencias-obsoletas)
    - [📍 Merge avanzado](#-merge-avanzado)
    - [📍 Rebase para actualizar ramas](#-rebase-para-actualizar-ramas)
    - [💡 Buenas prácticas](#-buenas-prácticas-10)
  - [🧠 Mapa mental — Advanced Branching Flow](#-mapa-mental--advanced-branching-flow)
    - [💡 Cómo leerlo](#-cómo-leerlo)
  - [🌐 Advanced Remotes — Forks, Upstream \& Synchronization](#-advanced-remotes--forks-upstream--synchronization)
    - [🧩 ¿Qué es un *remote*?](#-qué-es-un-remote)
    - [🔗 Conectar el repo original (upstream)](#-conectar-el-repo-original-upstream)
    - [🔄 Actualizar tu fork con los cambios del original](#-actualizar-tu-fork-con-los-cambios-del-original)
    - [📤 Subir los cambios actualizados a tu fork](#-subir-los-cambios-actualizados-a-tu-fork)
    - [🧠 ¿Cuándo usar *merge* vs *rebase* en forks?](#-cuándo-usar-merge-vs-rebase-en-forks)
    - [🧹 Limpiar ramas remotas obsoletas](#-limpiar-ramas-remotas-obsoletas)
    - [🧭 Flujo visual](#-flujo-visual-3)
    - [💡 Buenas prácticas](#-buenas-prácticas-11)
  - [🛠️ Restauración segura de commits](#️-restauración-segura-de-commits)
    - [🔙 `git revert <hash>`](#-git-revert-hash)
    - [🕓 `git checkout <hash>`](#-git-checkout-hash)
  - [📘 TAGS \& RELEASES](#-tags--releases)
    - [🏷️ Concepto y tipos de tags](#️-concepto-y-tipos-de-tags)
      - [🔹 ¿Qué es un tag?](#-qué-es-un-tag)
      - [🔹 Tipos de etiquetas](#-tipos-de-etiquetas)
      - [🔹 Asignar etiquetas a commits específicos](#-asignar-etiquetas-a-commits-específicos)
      - [🔹 Ver etiquetas existentes](#-ver-etiquetas-existentes)
      - [🔹 Mostrar información detallada del tag](#-mostrar-información-detallada-del-tag)
      - [🔹 Ver asociaciones entre tags y commits](#-ver-asociaciones-entre-tags-y-commits)
    - [🌐 Gestión remota y manipulación de tags](#-gestión-remota-y-manipulación-de-tags)
      - [📤 Subir tags al repositorio remoto](#-subir-tags-al-repositorio-remoto)
      - [🗑️ Eliminar etiquetas](#️-eliminar-etiquetas)
        - [Localmente:](#localmente)
        - [En remoto:](#en-remoto)
      - [🔁 Reasignar un tag](#-reasignar-un-tag)
    - [🚀 Releases en GitHub y Buenas prácticas](#-releases-en-github-y-buenas-prácticas)
      - [📦 Crear un Release en GitHub](#-crear-un-release-en-github)
      - [🧠 Flujo visual — Tags \& Releases](#-flujo-visual--tags--releases)
      - [💡 Buenas prácticas](#-buenas-prácticas-12)
  - [🧹 MAINTENANCE \& OPTIMIZATION](#-maintenance--optimization)
    - [🧰 `git gc` — Garbage Collector (compacta y optimiza)](#-git-gc--garbage-collector-compacta-y-optimiza)
    - [🩺 `git fsck` — Verificación de integridad](#-git-fsck--verificación-de-integridad)
    - [🧭 `git reflog` — Historial de movimientos (el salvavidas)](#-git-reflog--historial-de-movimientos-el-salvavidas)
    - [🧼 `git clean` — Limpieza de archivos no rastreados](#-git-clean--limpieza-de-archivos-no-rastreados)
    - [🧩 Flujo visual de mantenimiento](#-flujo-visual-de-mantenimiento)
    - [💡 Buenas prácticas de mantenimiento](#-buenas-prácticas-de-mantenimiento)
  - [💫 FINAL BLOCK — Cierre del Módulo Git: Buenas prácticas y preparación profesional](#-final-block--cierre-del-módulo-git-buenas-prácticas-y-preparación-profesional)
    - [🎯 Objetivo de este cierre](#-objetivo-de-este-cierre)
    - [🧭 1. Estructura profesional de repositorios](#-1-estructura-profesional-de-repositorios)
    - [🧱 2. Commits profesionales](#-2-commits-profesionales)
    - [🧰 3. Seguridad y respaldo](#-3-seguridad-y-respaldo)
    - [🧹 4. Limpieza y mantenimiento](#-4-limpieza-y-mantenimiento)
    - [💼 5. Mostrar tu trabajo (portafolio técnico)](#-5-mostrar-tu-trabajo-portafolio-técnico)
    - [🚀 6. Preparar transición a la siguiente sección: GitHub Tools](#-6-preparar-transición-a-la-siguiente-sección-github-tools)
    - [🧠 Diagrama resumen del módulo Git](#-diagrama-resumen-del-módulo-git)
    - [💬 Reflexión final](#-reflexión-final)

---
---

## **Git** "*Sistema de control de versiones*"

> Creado por Linux Torvalds

## ⚙️ Setup & Init

Configura un nuevo proyecto de Git o clona uno existente.

![Static Badge](https://img.shields.io/badge/git-init-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-clone-green?logo=github)

---

### 🆕 `git init`

Inicializa un directorio vacío como **repositorio Git**.

```bash
git init
```

📌 **Qué hace:**

- Crea una carpeta oculta llamada `.git` que guarda todo el historial de versiones.
- Inicia la rama principal. Antiguamente se llamaba **master**, ahora por convención se usa **main**.

🔎 **Explicación del cambio de nombre de la rama:**

- `master` era el nombre por defecto, pero muchas comunidades lo reemplazaron por `main` para hacerlo más inclusivo y claro.
- **main** = rama principal, la base de tu proyecto.

⚙️ **Cómo definir siempre `main` como predeterminado:**

```bash
git config --global init.defaultBranch main
```

⚙️ **Cómo renombrar la rama actual a `main`:**

```bash
git branch -m main
```

- `git branch` → gestiona ramas.
- `-m` → move/rename (renombra la rama actual).
- `main` → el nuevo nombre.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---

### 📥 `git clone [url]`

Clona (descarga) un repositorio existente desde una URL remota.

```bash
git clone git@github.com:usuario/repositorio.git
```

📌 **Qué hace:**

- Copia todos los archivos, ramas e historial de commits.
- Te da una copia idéntica para trabajar en tu máquina.

🛠️ **Parámetros comunes:**

- `[url]` → Dirección del repositorio (HTTPS o SSH).
- `[directorio]` *(opcional)* → Nombre de la carpeta destino.

Ejemplo:

```bash
git clone git@github.com:Ssail-1/PlatziNotes.git mi-carpeta-local
```

👉 Esto clona el repo en una carpeta llamada `mi-carpeta-local` en lugar de usar el nombre original.

---

### 📖 Resumen visual con Mermaid

```mermaid
flowchart TD
  A[Directorio vacío] --> B[Repositorio Git (.git)] C[Repositorio remoto en GitHub] --> D[Copia local idéntica]
```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🔧 Checking Configuration

Verifica y consulta la configuración activa de Git en tu entorno.

![Static Badge](https://img.shields.io/badge/git-config-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-help-grey?logo=github)

---

### 📑 `git --help`

Muestra la ayuda oficial de Git con todas las opciones disponibles.

```bash
git --help
```

🛠️ **Atajos útiles:**

- `git help <comando>` → manual de un comando específico.

  ```bash
  git help commit
  ```

- `git <comando> --help` → lo mismo, otra forma de escribirlo.

  ```bash
  git commit --help
  ```

- `git -h` → ayuda corta, solo muestra las flags más comunes.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
### 🧾 `git config --list`

Lista toda la configuración activa que Git está usando actualmente.

```bash
git config --list
```

📌 **Qué hace:**

- Muestra configuraciones de todos los niveles:

  - **Sistema** (`/etc/gitconfig`) → afecta a todos los usuarios de la computadora.
  - **Global** (`~/.gitconfig` o `~/.config/git/config`) → afecta solo a tu usuario.
  - **Local** (`.git/config`) → afecta únicamente al repo donde estás.
- Si un valor se repite, el nivel más cercano (local) tiene prioridad.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---

### 🔍 Consultar una clave específica

Si quieres ver el valor de una sola clave:

- `git config <key>`

Ejemplo:

```bash
git config user.name
```

👉 Te devuelve el nombre configurado para tus commits en ese repo.

---

### 💡 Buenas prácticas

- Usa **`--global`** para datos personales (nombre, email) que aplicarás a todos tus repos.
- Usa **local (sin flag)** si en un repo necesitas credenciales distintas (ej. cuenta secundaria).
- Para depuración, `git config --list --show-origin` te muestra **qué archivo exacto** definió cada configuración.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## ⚙️ Setup "Configuración Inicial"

Configura tu identidad y opciones básicas de Git para que todos tus commits estén bien registrados.

![Static Badge](https://img.shields.io/badge/git-config-blue?logo=git)
![Static Badge](https://img.shields.io/badge/editor-vim%2Femacs-green)

---

### 🛠️ `git config`

El comando `git config` gestiona la configuración de Git en distintos niveles:

```bash
git config [nivel] <clave> <valor>
```

📌 **Niveles de configuración:**

| Flag / Parámetro | Alcance                        | Archivo que modifica                    |
| ---------------- | ------------------------------ | --------------------------------------- |
| `--system`       | Todos los usuarios del sistema | `/etc/gitconfig`                        |
| `--global`       | Solo tu usuario actual         | `~/.gitconfig` o `~/.config/git/config` |
| *(sin flag)*     | Solo el repo actual            | `.git/config` dentro del repo           |

👉 Si un valor se repite, el **nivel más específico (local)** tiene prioridad.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---

### 👤 Configurar identidad del usuario

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

- `user.name` → el nombre que aparecerá en los commits.
- `user.email` → el correo vinculado (debe coincidir con el de tu cuenta GitHub si quieres que aparezcan tus contribuciones).

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
### 🎨 Colores en Git

```bash
git config --global color.ui auto
```

📌 **Qué hace:**

- `color.ui` controla si Git usa colores en la terminal.
- `auto` → activa colores cuando la salida es una terminal (lo más práctico).

👉 Esto mejora la lectura de `git status`, `git diff`, etc.

---

### 📝 Ver configuración actual

```bash
git config --list
```

👉 Lista todas las configuraciones activas (se mezclan system, global y local).

```bash
git config user.name
```

👉 Devuelve el valor de una clave específica.

---

### 🖊️ Editor por defecto

Git usa un editor de texto para escribir mensajes de commit si no pasas `-m`.

Por defecto:

- En Linux/Mac suele ser **Vim**.
- Puedes cambiarlo, por ejemplo a **Emacs** o **Nano**:

```bash
git config --global core.editor emacs
```

```bash
git config --global core.editor nano
```

---

💡 **Buenas prácticas**

- Configura siempre tu nombre y correo globales al empezar en una máquina.
- Usa un editor que conozcas (si no te gusta Vim, cámbialo).
- Revisa con `git config --list --show-origin` para ver qué archivo estableció cada valor.

---

✅ Con el entorno queda listo para empezar a trabajar en cualquier repo con la identidad clara y sin sorpresas de editor.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>


---
---

## 📂 ¿Cómo se crean y agregan archivos a Git?

Una vez que inicializas un repositorio con `git init`, puedes empezar a crear archivos y agregarlos al control de versiones.

![Static Badge](https://img.shields.io/badge/git-add-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-status-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-commit-yellow?logo=git)

---

### ✍️ Creación de archivos

Puedes crear archivos con tu editor de preferencia, por ejemplo:

```bash
nano notas.md
```

📌 Luego confirmas su existencia con:

```bash
ls
```

---

### 🔎 Verificar estado

```bash
git status
```

📌 **Qué hace:**

- Muestra qué archivos están sin seguimiento (*untracked*).
- Qué archivos ya están en el área de preparación (*staging*).
- En qué rama te encuentras.

👉 Es tu **mapa de situación** antes de cualquier commit.

---

### ➕ Agregar archivos al ***staging area***

```bash
git add nombre_archivo.txt
```

📌 **Qué hace:**

- Mueve el archivo al área de preparación (*staging*).
- Indica que ese archivo estará listo para el próximo commit.

🛠️ Variantes:

- `git add .` → agrega todos los archivos del directorio actual.
- `git add -A` → agrega todos los cambios, incluyendo eliminaciones y renombres.

---

### 🗑️ Quitar archivos del *staging area*

```bash
git reset nombre_archivo.txt
```

👉 Saca el archivo del *staging area*, pero conserva los cambios en tu directorio de trabajo.

```bash
git rm --cached nombre_archivo.txt
```

👉 Similar a `reset`, **pero** pensado para remover un archivo del control de versiones (queda en tu carpeta, pero Git lo ignora).

```bash
git rm --force nombre_archivo.txt
```

👉 Borra el archivo tanto del *staging area* como del directorio de trabajo.

---

### 💾 Guardar cambios en el repositorio

```bash
git commit -m "Descripción clara del cambio"
```

📌 **Qué hace:**

- Crea un *snapshot* de los archivos en staging.
- Registra ese cambio en el historial del proyecto.

👉 Si olvidas `-m`, se abrirá tu editor configurado (Vim, Nano, etc.) para escribir el mensaje.

---

### 📖 Flujo visual básico

```mermaid
flowchart LR
  A[Directorio de trabajo] -->|git add| B[Área de staging]
  B -->|git commit| C[Repositorio .git]
```

---

💡 **Buenas prácticas**

- Usa mensajes de commit descriptivos (ej. `"Agrego sección Setup & Init"`).
- No subas archivos binarios grandes ni temporales (usa `.gitignore`).
- Antes de cada commit, revisa siempre con `git status` qué estás incluyendo.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🔁 Flujo de trabajo — Diagrama de secuencia

> [Clase 3: Control de Versiones con Git](https://platzi.com/cursos/gitgithub/comandos-basicos-de-git-add-commit-log/ "Curso de Git y GitHub - Comandos básicos y flujo de trabajo")
>
> ![Diagrama de Secuencia Directorio → Staging → Repositorio Git](Imagenes/DiagramaSecuenciaDir_Staging_Git.png "Flujo visual entre directorio, área de staging y repositorio de Git")
>
> 🖼️ **Interpretación del diagrama**
> El flujo representa cómo los archivos viajan entre tres estados en Git:
>
> 1. **Directorio de trabajo (Working Directory)** → donde editas archivos.
> 2. **Área de preparación (Staging Area)** → donde decides qué cambios se confirmarán.
> 3. **Repositorio Git (.git)** → el historial de commits ya guardados.

---

### 🧩 Desde el Directorio de trabajo hacia el Área de staging

```bash
git add <archivo>
```

📌 Mueve los archivos modificados al área de preparación (*staging area*).
Permite decidir qué se incluirá en el próximo commit.

---

### 🔄 Desde el Staging hacia el Repositorio Git

```bash
git commit -m "Mensaje descriptivo"
```

📌 Confirma los archivos preparados y los guarda como un nuevo snapshot en el historial.

```bash
git commit --amend
```

📌 Modifica el último commit (puedes corregir el mensaje o añadir archivos que olvidaste).

---

### 🧹 Regresando cambios (Reset)

| Comando                                      | Acción                        | Resultado                                         |
| -------------------------------------------- | ----------------------------- | ------------------------------------------------- |
| `git reset --soft <commit>`                  | Mueve HEAD al commit indicado | Mantiene cambios en staging                       |
| `git reset --mixed <commit>` *(por defecto)* | Mueve HEAD                    | Los cambios vuelven al directorio de trabajo      |
| `git reset --hard <commit>` ⚠️               | Mueve HEAD y borra cambios    | Elimina todo lo que no está en el commit indicado |

💡 **HEAD** es un puntero que indica en qué commit estás trabajando actualmente.

---

### 🗂️ Remover archivos del control de versiones

```bash
git rm --cached <archivo>
```

📌 Quita el archivo del seguimiento de Git, **pero lo deja** en tu carpeta local.

```bash
git rm --force <archivo>
```

📌 Elimina el archivo tanto del control de versiones **como de tu carpeta local**.

---

### 💡 Buenas prácticas

- ⚠️ Evita usar `git reset --hard` a menos que estés 100 % seguro (borra cambios sin recuperación).
- Usa `git commit --amend` solo si **no has hecho push** del commit anterior (si ya lo subiste, mejor haz otro commit).
- Revisa tu historial antes de revertir con:

  ```bash
  git log --oneline
  ```

---

### 🧭 Resumen visual del flujo

```mermaid
flowchart LR
    A[Directorio de trabajo] -->|git add| B[Área de staging]
    B -->|git commit| C[Repositorio Git (.git)]
    C -->|git reset --soft| B
    C -->|git reset --mixed| A
    C -->|git reset --hard ⚠️| A
```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 📸 STAGE & SNAPSHOT

Trabajar con **instantáneas (snapshots)** en Git significa preparar, revisar y guardar el estado exacto de tus archivos en un momento determinado.

![Static Badge](https://img.shields.io/badge/git-status-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-add-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-diff-orange?logo=git)
![Static Badge](https://img.shields.io/badge/git-commit-yellow?logo=git)

---

### 🔍 `git status` — Verificar el estado del repositorio

```bash
git status
```

📌 **Qué hace:**

- Muestra los archivos **modificados**, **nuevos**, o **eliminados** en tu directorio.
- Indica qué está **en el área de staging** y qué no.
- Te dice en qué **rama** estás trabajando.

💡 **Ejemplo práctico:**

```bash
git status
# On branch feature/git-notes-update
# Changes not staged for commit:
#   modified: git-and-gitHub-notes.md
```

👉 Así sabes si algo está pendiente antes de hacer `add` o `commit`.

---

### ➕ `git add` — Preparar cambios para un commit

```bash
git add archivo.txt
```

📌 **Qué hace:**

- Agrega el archivo (o cambios específicos) al área de *staging*.
- Permite que esos archivos sean incluidos en el próximo *commit*.

🧩 **Variantes útiles:**

| Comando      | Acción                                                            |
| ------------ | ----------------------------------------------------------------- |
| `git add .`  | Agrega todos los archivos del directorio actual.                  |
| `git add -A` | Agrega **todos los cambios** (incluso eliminaciones y renombres). |
| `git add -p` | Agrega cambios por fragmentos (*porciones del archivo*).          |

💡 **Tips:**

- Usa `-p` si quieres elegir partes del archivo para agregar.
- Revisa siempre con `git status` antes de confirmar.

---

### 🧾 `git diff` — Comparar diferencias

📍 **Antes de hacer `git add`:**

```bash
git diff
```

Muestra los cambios **que aún no han sido preparados** (*unstaged*).

📍 **Después de hacer `git add`:**

```bash
git diff --staged
```

Muestra los cambios **ya en staging** que serán incluidos en el siguiente *commit*.

💬 **Explicación técnica:**

- `diff` → diferencia entre versiones.
- `--staged` → compara el staging con el último *commit*.

---

### 💾 `git commit` — Crear una instantánea

```bash
git commit -m "Descripción del cambio"
```

📌 **Qué hace:**

- Guarda los archivos del staging como una *snapshot* en el historial del repositorio.
- Crea un punto de restauración seguro al que puedes volver con `git checkout`.

💡 **Atajos:**

| Comando                    | Significado                                                         |
| -------------------------- | ------------------------------------------------------------------- |
| `git commit -m "mensaje"`  | Commit con mensaje corto.                                           |
| `git commit -am "mensaje"` | Añade y hace commit **solo de archivos ya rastreados** (no nuevos). |

---

### 🔁 `git commit --amend` — Modificar el último commit

```bash
git commit --amend -m "Nuevo mensaje actualizado"
```

📌 Corrige el mensaje o agrega archivos que olvidaste.

⚠️ **Importante:**
Solo úsalo si **aún no hiciste push**, porque reescribe el historial local.

---

### 💡 Buenas prácticas

- Antes de cada `commit`, revisa tu estado con `git status`.
- Usa mensajes de commit **claros y en presente**, ejemplo:

  > `"Agrega explicación de git diff y git commit"`
- Nunca hagas `git add .` a ciegas; revisa los archivos que se incluirán.
- Realiza commits pequeños y frecuentes: facilitan revertir y entender los cambios.

---

### 🧭 Flujo visual de Stage → Snapshot

```mermaid
flowchart LR
  A[Archivo modificado] -->|git add| B[Área de Staging]
  B -->|git diff --staged| C[Revisión de cambios]
  C -->|git commit -m| D[Snapshot almacenado en Git]
```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🌿 BRANCH & MERGE

Permiten aislar el trabajo en diferentes líneas de desarrollo sin afectar la rama principal.
Cada rama es una línea de tiempo independiente donde puedes experimentar, desarrollar o corregir errores.

![Static Badge](https://img.shields.io/badge/git-branch-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-checkout-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-switch-teal?logo=git)
![Static Badge](https://img.shields.io/badge/git-merge-yellow?logo=git)

---

### 🌱 `git branch` — Crear y listar ramas

```bash
git branch
```

📌 **Qué hace:**

- Lista todas las ramas locales.
- Marca con `*` la rama activa (donde estás trabajando).

```bash
git branch nueva-rama
```

📌 Crea una nueva rama, pero **no cambia** a ella todavía.

💡 **Atajo moderno:**

```bash
git switch -c nueva-rama
```

➡️ `-c` = *create* → crea y te cambia a esa nueva rama inmediatamente.
(Equivalente a `git checkout -b nueva-rama`, que era la forma clásica).

---

### 🔄 `git switch` y `git checkout` — Moverte entre ramas

```bash
git switch nombre-rama
```

👉 Cambia a otra rama existente.

```bash
git checkout nombre-rama
```

👉 Hace lo mismo, pero `switch` es más moderno y seguro (menos propenso a errores).

💡 **Regresar a la principal:**

```bash
git switch main
```

---

### 🧬 `git merge` — Unir ramas

```bash
git merge nombre-rama
```

📌 **Qué hace:**

- Combina los cambios de la rama especificada en la rama actual.
- Debes estar **ubicado en la rama que recibirá** los cambios.

💬 **Ejemplo:**

```bash
git switch main
git merge feature/git-notes-update
```

👉 Esto fusiona la rama `feature/git-notes-update` dentro de `main`.

---

### ⚠️ Conflictos de fusión

Los conflictos aparecen cuando **dos ramas modifican las mismas líneas del mismo archivo**.

Git marcará los conflictos así dentro del archivo:

```text
<<<<<<< HEAD
versión en main
=======
versión en feature/git-notes-update
>>>>>>> feature/git-notes-update
```

📌 **Solución:**

- Abre el archivo en VSCode, que mostrará botones para:

  - **Accept Current Change** (mantener HEAD)
  - **Accept Incoming Change** (mantener la rama fusionada)
  - **Accept Both Changes** (mantener ambas partes)
- Una vez resuelto, guardas y haces:

  ```bash
  git add archivo-conflictivo
  git commit
  ```

  Esto marca el conflicto como solucionado.

Durante un conflicto, los archivos quedan en estado **Unmerged** hasta que confirmas la resolución.

---

### 🧹 Eliminar ramas

```bash
git branch -d nombre-rama
```

Elimina la rama local **si ya fue fusionada**.

```bash
git branch -D nombre-rama
```

⚠️ Elimina la rama **sin verificar si fue fusionada** (usa con cuidado).

---

### 🧠 Convenciones de nombres de ramas

| Tipo de Rama | Propósito                      | Ejemplo                    |
| ------------ | ------------------------------ | -------------------------- |
| `main`       | Rama principal estable         | `main`                     |
| `develop`    | Rama de desarrollo general     | `develop`                  |
| `feature/`   | Nuevas funciones               | `feature/git-notes-update` |
| `hotfix/`    | Corrección de errores urgentes | `hotfix/fix-login`         |
| `release/`   | Preparación de versiones       | `release/v1.2`             |

💡 **Buena práctica:** Usa nombres descriptivos y cortos:
`feature/add-login-form` > `rama1`.

---

### 🌳 Visual de flujo de ramas

```mermaid
gitGraph
  commit id: "Inicio (main)"
  branch feature/git-notes-update
  commit id: "Notas de Git creadas"
  checkout main
  commit id: "Actualización base"
  merge feature/git-notes-update
  commit id: "Fusión completada"
```

---

### 💡 Buenas prácticas

- Trabaja siempre en ramas separadas (no en `main`).
- Fusiona con commits limpios y mensajes claros.
- Borra ramas ya fusionadas para mantener el repo ordenado.
- Usa `git log --oneline --graph` para visualizar el árbol de commits.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🔄 SHARE & UPDATE

Permite conectar tu repositorio local con uno remoto (por ejemplo, GitHub), descargar actualizaciones y subir tus cambios.

![Static Badge](https://img.shields.io/badge/git-remote-grey?logo=git)
![Static Badge](https://img.shields.io/badge/git-fetch-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-pull-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-push-green?logo=git)

---

### 🌍 `git remote add` — Conectar un repositorio remoto

```bash
git remote add origin git@github.com:usuario/repositorio.git
```

📌 **Qué hace:**

- Vincula tu repositorio local con uno remoto.
- `origin` es un alias (nombre corto) que representa la URL del remoto.

💬 **Explicación de la sintaxis:**

| Parte                                    | Significado                                    |
| ---------------------------------------- | ---------------------------------------------- |
| `remote`                                 | Gestiona repositorios remotos.                 |
| `add`                                    | Agrega un nuevo remoto.                        |
| `origin`                                 | Nombre que damos al remoto (puedes usar otro). |
| `git@github.com:usuario/repositorio.git` | Dirección SSH del repo remoto.                 |

💡 **Comando complementario:**

```bash
git remote -v
```

📍 Muestra las URLs asociadas a cada remoto (para `fetch` y `push`).

---

### 📥 `git fetch` — Descargar sin fusionar

```bash
git fetch origin
```

📌 **Qué hace:**

- Descarga los commits, ramas y etiquetas del remoto.
- No cambia tus archivos locales ni tus ramas activas.
- Ideal para **ver qué hay de nuevo antes de fusionar**.

💡 **Ejemplo práctico:**

```bash
git fetch origin main
git log main..origin/main --oneline
```

👉 Te muestra los commits que existen en GitHub y aún no tienes localmente.

---

### ⬇️ `git pull` — Descargar y fusionar

```bash
git pull origin main
```

📌 **Qué hace:**

- Ejecuta **`fetch + merge`** automáticamente.
- Descarga los cambios remotos y los integra con tu rama actual.

💬 **Desglose del comando:**

| Parte    | Significado                               |
| -------- | ----------------------------------------- |
| `origin` | Remoto desde donde obtendrás los cambios. |
| `main`   | Rama que se actualizará.                  |

💡 **Ejemplo de uso típico:**
Cuando alguien más hizo commits en el repo remoto y tú quieres tenerlos localmente antes de seguir trabajando.

---

### ⬆️ `git push` — Subir tus cambios al remoto

```bash
git push origin feature/git-notes-update
```

📌 **Qué hace:**

- Envía los commits locales al repositorio remoto.
- Crea la rama en GitHub si aún no existe.

💬 **Desglose del comando:**

| Parte                      | Significado              |
| -------------------------- | ------------------------ |
| `push`                     | Subir commits al remoto. |
| `origin`                   | Remoto de destino.       |
| `feature/git-notes-update` | Rama que subirás.        |

💡 **Atajos comunes:**

```bash
git push -u origin nombre-rama
```

- `-u` = *--set-upstream*
  Configura la rama local para que recuerde su remoto y su rama de destino.
  Así después podrás usar simplemente:

  ```bash
  git push
  git pull
  ```

---

### 🔁 Flujo visual de sincronización

```mermaid
flowchart LR
  A[Repositorio remoto (GitHub)] -->|git fetch| B[Local]
  B -->|git merge| C[Actualización local]
  C -->|git push| A
```

---

### 💡 Buenas prácticas

- Antes de hacer `push`, **siempre haz un `pull`** para evitar conflictos.
- Usa `git fetch` para revisar cambios sin alterar tu rama.
- Mantén ramas limpias y sincronizadas: elimina las que ya fusionaste.
- Usa SSH en lugar de HTTPS para autenticación más segura y fluida.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 📂 TRACKING PATH CHANGES

Git no solo guarda el contenido de tus archivos, también rastrea **su ubicación y nombre** dentro del proyecto.
Estos comandos te permiten mover, renombrar o eliminar archivos sin perder su historial de versiones.

![Static Badge](https://img.shields.io/badge/git-rm-red?logo=git)
![Static Badge](https://img.shields.io/badge/git-mv-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-log--stat-purple?logo=git)

---

### 🗑️ `git rm` — Eliminar archivos del proyecto

```bash
git rm archivo.txt
```

📌 **Qué hace:**

- Elimina el archivo **del directorio de trabajo** y del **área de staging**.
- Al hacer `git commit`, la eliminación quedará registrada en el historial.

💡 **Ejemplo:**

```bash
git rm old-notes.md
git commit -m "Elimina archivo obsoleto"
```

🧩 **Flags útiles:**

| Flag       | Acción                                                                                |
| ---------- | ------------------------------------------------------------------------------------- |
| `--cached` | Elimina el archivo solo del control de versiones, **pero lo conserva** en tu carpeta. |
| `--force`  | Obliga la eliminación incluso si hay cambios sin guardar. ⚠️                          |

💬 **Ejemplo práctico:**

```bash
git rm --cached imagen.png   # Git deja de rastrear la imagen, pero no la borra.
```

---

### 🚚 `git mv` — Renombrar o mover archivos

```bash
git mv nombre-viejo.txt nombre-nuevo.txt
```

📌 **Qué hace:**

- Cambia el nombre o ubicación del archivo.
- Prepara automáticamente el cambio para el próximo commit.

💡 **Ejemplo de movimiento:**

```bash
git mv docs/apuntes.md notas/git-apuntes.md
git commit -m "Reorganiza apuntes en nueva carpeta"
```

👉 Git detecta automáticamente el cambio de ruta o nombre y mantiene el historial del archivo.

---

### 🧾 `git log --stat -M` — Ver historial con archivos movidos o renombrados

```bash
git log --stat -M
```

📌 **Qué hace:**

- Muestra los commits con estadísticas de archivos modificados, renombrados o movidos.
- La opción `-M` indica a Git que **detecte movimientos o renombres** para conservar el historial.

💡 **Ejemplo:**

```bash
git log --follow notas/git-apuntes.md
```

👉 Muestra el historial completo del archivo, incluso si cambió de nombre.

| Comando                      | Qué muestra                                                                 | Cuándo usarlo                                                     |
| ---------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `git log --stat -M`          | Todos los commits del repo con estadísticas globales, detectando renombres. | Cuando quieres ver *qué cambió en general*.                       |
| `git log --follow <archivo>` | Solo los commits relacionados con un archivo, siguiendo sus renombres.      | Cuando quieres seguir el historial *de un archivo en particular*. |

---

💡 **Analogía rápida:**
Piensa que `--stat` es como el “resumen de actividad de todo el grupo”,
y `--follow` es el “historial personal de un solo integrante”.

---

### 🧭 Flujo visual

```mermaid
flowchart LR
  A[Archivo rastreado] -->|git mv| B[Archivo renombrado o movido]
  A -->|git rm| C[Archivo eliminado]
  B -->|git log --follow| D[Historial conservado]
  C -->|git commit| E[Eliminación registrada]
```

---

### 💡 Buenas prácticas

- Usa `git mv` en lugar de mover archivos manualmente (mantiene el historial limpio).
- Si eliminaste o moviste manualmente, usa `git add -A` para que Git registre el cambio.
- Usa `git log --follow archivo` para verificar la trazabilidad completa de un archivo renombrado.
- Evita usar `git rm --force` a menos que estés absolutamente seguro.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🗂️ TEMPORARY COMMITS — Stash

💾 —esta parte es clave porque te salva cuando tienes cambios sin terminar y necesitas cambiar de rama sin perderlos.

El “stash” es como una **mochila temporal** donde guardas cambios para no perderlos ni tener que hacer commit aún.
Sirve cuando necesitas cambiar de rama o actualizarte, pero tienes trabajo en curso.

![Static Badge](https://img.shields.io/badge/git-stash-orange?logo=git)
![Static Badge](https://img.shields.io/badge/git-stash--list-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-stash--pop-green?logo=git)

---

### 📦 `git stash` — Guardar cambios temporalmente

```bash
git stash
```

📌 **Qué hace:**

- Guarda los cambios de tu directorio de trabajo y de staging en una “pila” (stack) de stashes.
- Deja tu directorio limpio (como si acabases de hacer `git checkout` sin cambios).

💡 Útil cuando:

- Estás en una rama y necesitas cambiar a otra sin hacer commit.
- Vas a actualizar (`pull`) pero no quieres que tus cambios entren en conflicto todavía.

---

### 📜 `git stash list` — Ver la lista de stashes

```bash
git stash list
```

📌 **Qué hace:**

- Muestra todas las entradas guardadas en tu “mochila” de stashes.
- Cada entrada tiene un índice: `stash@{0}`, `stash@{1}`, etc.

Ejemplo de salida:

```
stash@{0}: WIP on feature-x: 9f3c2a1 agrega configuración inicial
stash@{1}: WIP on main: 7a5d6e4 corrige README
```

---

### 📤 `git stash pop` — Recuperar cambios

```bash
git stash pop
```

📌 **Qué hace:**

- Aplica el último stash guardado a tu directorio de trabajo.
- Borra ese stash de la lista.

💡 Si quieres aplicarlo pero **mantenerlo** en la lista:

```bash
git stash apply
```

---

### 🗑️ `git stash drop` — Eliminar stashes

```bash
git stash drop stash@{0}
```

📌 **Qué hace:**

- Borra la entrada específica de la lista de stashes.

Para borrar todos:

```bash
git stash clear
```

---

### 🧭 Flujo visual de Stash

```mermaid
flowchart LR
  A[Directorio con cambios] -->|git stash| B[Stash guardado]
  B -->|git stash list| C[Ver stashes]
  B -->|git stash pop| D[Recuperar cambios]
  B -->|git stash drop| E[Eliminar stash]
```

---

### 💡 Buenas prácticas

- Usa `git stash` solo para cambios temporales, no como sistema de commits.
- Nombra tus stashes para identificarlos mejor:

  ```bash
  git stash push -m "Trabajo parcial en login"
  ```

- Antes de aplicar un stash, asegúrate de estar en la rama correcta.

- Recuerda: `pop` aplica y borra, `apply` aplica y mantiene en la lista.

---

✅ Con este tema podemos dominar el uso de **stash** para guardar y recuperar trabajo sin necesidad de commits.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## ✍️ REWRITE HISTORY

En Git, reescribir el historial te permite **corregir, reorganizar o limpiar commits**.
Se usa para dejar un historial claro y profesional antes de subir o fusionar cambios.

⚠️ **Advertencia:** estos comandos modifican el historial, así que úsalos solo en ramas locales o en commits que aún no se hayan hecho *push*.

![Static Badge](https://img.shields.io/badge/git-reset-red?logo=git)
![Static Badge](https://img.shields.io/badge/git-rebase-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-commit--amend-yellow?logo=git)

---

### 🧭 `git reset` — Reubicar el puntero HEAD

`git reset` mueve el **HEAD** (la referencia del commit actual) hacia otro commit.
Sirve para deshacer commits o devolver archivos a un estado anterior.

```bash
git reset --soft <hash>
git reset --mixed <hash>
git reset --hard <hash>
```

📌 **Diferencias entre los modos:**

| Modo                  | Qué afecta                       | Qué conserva                      | Uso típico                          |
| --------------------- | -------------------------------- | --------------------------------- | ----------------------------------- |
| `--soft`              | Mueve HEAD al commit indicado    | Mantiene los cambios en *staging* | Rehacer commit sin perder cambios   |
| `--mixed` *(default)* | Mueve HEAD y limpia el *staging* | Mantiene cambios en el directorio | Devolver cambios sin borrarlos      |
| `--hard`              | Mueve HEAD y elimina todo        | Nada (borra cambios) ⚠️           | Reiniciar el repo a un punto exacto |

💡 **HEAD** es un puntero que indica en qué commit estás trabajando.

---

### 🧩 Ejemplo visual

```mermaid
flowchart LR
  A[Commit A] --> B[Commit B (HEAD actual)]
  B -->|git reset --soft A| C[HEAD vuelve a A (cambios guardados)]
  B -->|git reset --mixed A| D[HEAD vuelve a A (cambios visibles en directorio)]
  B -->|git reset --hard A| E[HEAD vuelve a A (todo eliminado ⚠️)]
```

---

### 🪄 `git rebase` — Reaplicar commits sobre otra base

```bash
git rebase main
```

📌 **Qué hace:**

- Toma los commits de tu rama actual y los “reaplica” sobre otra rama.
- Reescribe el historial para que tus cambios parezcan creados encima del último commit de la rama base.

💬 **Ejemplo práctico:**

```bash
git switch feature/login
git rebase main
```

👉 Aplica los commits de `feature/login` sobre los más recientes de `main`.

💡 Ideal cuando tu rama se quedó atrás y quieres **actualizarla sin crear un merge commit**.

---

### 🧮 Rebase interactivo

```bash
git rebase -i HEAD~3
```

📌 **Qué hace:**

- Abre los últimos 3 commits en modo interactivo.
- Puedes **editar (edit)**, **combinar (squash)** o **eliminar (drop)** commits.

💬 Ejemplo de interfaz:

```
pick 8f3c2a1 agrega notas
squash 1a4b8f2 corrige typo
edit 7b9d3e3 mejora descripción
```

💡 Usa este método para **limpiar tu historial antes de subirlo a GitHub**.

---

### 📝 `git commit --amend` — Corregir el último commit

```bash
git commit --amend -m "Corrige error en mensaje anterior"
```

📌 **Qué hace:**

- Modifica el último commit (mensaje o contenido).
- Útil para pequeños errores justo antes de hacer *push*.

⚠️ **Precaución:** si ya hiciste *push*, evita usarlo (cambiaría el historial remoto).

---

### 🧠 Buenas prácticas

- Usa `rebase` para mantener un historial lineal y limpio.
- Usa `reset --soft` cuando necesites rehacer un commit sin perder trabajo.
- Evita `reset --hard` si no estás completamente seguro.
- Antes de reescribir commits, verifica con:

  ```bash
  git log --oneline --graph
  ```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🔎 INSPECT & COMPARE

Estos comandos sirven para **examinar el historial** y **comparar cambios** entre commits, archivos y ramas. Son tus “lupas” para entender qué pasó en tu repo en cada momento.

![Static Badge](https://img.shields.io/badge/git-log-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-diff-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-show-orange?logo=git)

---

### 📝 `git log` — Ver historial de commits

```bash
git log
```

📌 **Qué hace:**

- Muestra la lista de commits de la rama actual en orden inverso (el más reciente primero).
- Incluye hash del commit, autor, fecha y mensaje.

🧩 **Variantes útiles:**

| Comando                    | Resultado                                                      |
| -------------------------- | -------------------------------------------------------------- |
| `git log --oneline`        | Vista compacta, un commit por línea.                           |
| `git log --graph`          | Vista gráfica de ramas y merges.                               |
| `git log --decorate`       | Muestra nombres de ramas y tags junto al commit.               |
| `git log --follow archivo` | Historial completo de un archivo, incluso si cambió de nombre. |

💡 **Combínalos:**

```bash
git log --oneline --graph --decorate --all
```

👉 Vista corta, con ramas, tags y todo el historial.

---

### 🧩 `git diff` — Comparar diferencias

Compara el contenido de archivos en distintos estados.

| Comando                    | Qué compara                                            |
| -------------------------- | ------------------------------------------------------ |
| `git diff`                 | Cambios en tu directorio de trabajo **no preparados**. |
| `git diff --staged`        | Cambios en el *staging area* frente al último commit.  |
| `git diff ramaA..ramaB`    | Diferencias entre dos ramas.                           |
| `git diff <hash1> <hash2>` | Diferencias entre dos commits.                         |

💬 **Ejemplo práctico:**

```bash
git diff main..feature/login
```

👉 Muestra los cambios entre `main` y la rama `feature/login`.

---

### 👁️ `git show` — Ver detalles de un commit

```bash
git show <hash-commit>
```

📌 **Qué hace:**

- Muestra un commit específico con autor, fecha, mensaje y cambios aplicados.
- Útil para revisar **qué exactamente se cambió** en un commit puntual.

💡 También puedes usarlo para tags o ramas:

```bash
git show v1.0.0
```

👉 Muestra la información del commit donde está ese tag.

---

### 🧭 Flujo visual

```mermaid
flowchart LR
  A[Historial de commits] -->|git log| B[Vista detallada]
  B -->|git diff| C[Comparar cambios]
  C -->|git show| D[Inspeccionar un commit específico]
```

---

### 💡 Buenas prácticas

- Usa `git log --oneline --graph` antes de reescribir o resetear para entender el árbol.
- Combina `git diff` con `--staged` antes de hacer commit para revisar exactamente qué vas a guardar.
- Usa `git show <hash>` cuando necesites confirmar detalles de un commit pasado.
- Si quieres exportar diferencias, puedes hacer:

  ```bash
  git diff > cambios.patch
  ```
  
---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🚫 IGNORING PATTERNS

Sirve para **indicar a Git qué archivos o carpetas NO debe rastrear ni subir al repositorio**. Esto mantiene tu repo limpio y evita subir archivos temporales, secretos o dependencias pesadas.

![Static Badge](https://img.shields.io/badge/.gitignore-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-config--excludesfile-blue?logo=git)

---

### 📜 `.gitignore` — Ignorar archivos en un repositorio

Crea un archivo llamado `.gitignore` en la raíz de tu proyecto con los patrones que quieras ignorar.

Ejemplo básico:

```gitignore
# Ignorar carpetas de logs
logs/

# Ignorar todos los archivos .notes
*.notes

# Ignorar cualquier carpeta con este patrón
pattern*/
```

📌 **Qué hace:**

- Todo lo listado ahí **no será rastreado ni agregado al staging**.
- Puedes poner comentarios con `#`.
- Puedes usar comodines `*` y `?` para patrones.

💡 **Tips:**

- Añade primero `.gitignore` antes de subir tu proyecto.
- Puedes crear varios `.gitignore` en subcarpetas (Git aplica el patrón de manera jerárquica).
- GitHub tiene plantillas para `.gitignore` comunes: [github.com/github/gitignore](https://github.com/github/gitignore)

---

### 🌍 Ignorar archivos de manera global

Puedes definir un archivo de exclusión global para todos tus repos:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

Luego crea el archivo `~/.gitignore_global` y añade ahí patrones comunes para todos tus proyectos.

💬 **Ejemplo:**

```bash
# ~/.gitignore_global
.DS_Store
node_modules/
*.log
```

---

### 🧭 Flujo visual

```mermaid
flowchart LR
  A[Archivos en directorio] -->|git add| B[Staging area]
  A -.archivos en .gitignore.-X B
  B -->|git commit| C[Repositorio Git]
```

---

### 💡 Buenas prácticas

- Siempre crea tu `.gitignore` al inicio del proyecto.
- No subas archivos sensibles (contraseñas, llaves) nunca.
- Usa plantillas de `.gitignore` específicas para tu lenguaje o framework.
- Para quitar de Git un archivo que ya subiste pero ahora quieres ignorar:

  ```bash
  git rm --cached archivo_secreto.txt
  ```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🌿 Branches (atajos prácticos y pro tips)

![Static Badge](https://img.shields.io/badge/git-branch-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-switch-teal?logo=git)
![Static Badge](https://img.shields.io/badge/git-merge-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-push--u-blue?logo=git)

### 📋 Listado y navegación

```bash
git branch           # Lista ramas locales ( * = actual )
git branch -r        # Ramas remotas
git branch -a        # Todas (locales + remotas)
git switch main      # Cambiar de rama (moderno)
git checkout main    # Cambiar de rama (clásico)
```

### 🌱 Crear y entrar (formas equivalentes)

```bash
git switch -c feature/x          # crea y entra (-c = create)
git checkout -b feature/x        # clásico
git branch feature/x && git switch feature/x  # crear y luego entrar
```

### ✏️ Renombrar rama

```bash
git branch -m nuevo-nombre       # renombra la rama actual (-m = move/rename)
```

> Si ya existía en remoto con el nombre viejo:

```bash
git push origin -u nuevo-nombre          # sube la nueva
git push origin --delete nombre-viejo    # elimina la remota vieja
git branch --unset-upstream              # (si hace falta) limpia upstream
git branch --set-upstream-to=origin/nuevo-nombre
```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🔗 Tracking (conectar tu rama local con la remota)

### Primera vez que empujas una rama nueva

```bash
git push -u origin feature/x   # -u = set-upstream (queda vinculada)
# Luego ya basta con:
git push
git pull
```

### Ver / cambiar upstream

```bash
git branch -vv                          # muestra tracking de cada rama
git branch --set-upstream-to=origin/feature/x
```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🔄 Ramas remotas y limpieza

### Obtener ramas nuevas/borradas del remoto

```bash
git fetch --prune            # sincroniza y limpia referencias obsoletas
# o
git remote prune origin
```

### Borrar ramas (local y remoto)

```bash
git branch -d feature/x      # borra local (si ya fue mergeada)
git branch -D feature/x      # borra local forzado ⚠️
git push origin --delete feature/x   # borra la rama en GitHub
```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🤝 Merge (estrategias útiles)

### Merge normal (fast-forward si aplica)

```bash
git switch main
git merge feature/x
```

### Forzar commit de merge aunque sea FF

```bash
git merge --no-ff feature/x
# Útil para dejar el “hito” del merge visible en el historial.
```

- Una fusión FF ocurre cuando la rama en la que estás haciendo el merge no ha tenido nuevos commits desde que se creó o actualizó la rama que quieres fusionar.
- En este caso, Git simplemente avanza el puntero de la rama actual al último commit de la rama que se está integrando, sin crear un nuevo "merge commit".

### Traerte los cambios pero sin crear commit de merge

```bash
git merge --squash feature/x
git commit -m "Squash: integra feature/x en un solo commit"
# Ideal para mantener historial más limpio cuando hubo muchos commits intermedios.
```

### Si hay conflicto

```bash
# Editas archivos en conflicto (VSCode ayuda mucho)
git add <archivos_resueltos>
git commit                      # completa el merge

# Si necesitas abortar:
git merge --abort
```

---

### 🪄 Rebase rápido para mantener la rama al día (lineal)

```bash
git switch feature/x
git fetch origin
git rebase origin/main     # re-aplica tus commits encima de main actualizado
# Si hay conflictos: resuélvelos, `git add` y:
git rebase --continue
# Para abortar:
git rebase --abort
```

> Tip: Usa **rebase** en ramas de trabajo antes del PR para un historial lineal y fácil de revisar. Evita rebase en ramas compartidas/públicas ya empujadas si otras personas dependen de ese historial.

---

### 🍒 Cherry-pick (traer un commit específico)

```bash
git cherry-pick <hash>
# Copia el commit indicado a tu rama actual (útil para hotfixes puntuales).
```

---

### 🛡️ Buenas prácticas rápidas

- Crea siempre ramas por feature: `feature/…`, `hotfix/…`, `release/…`.
- **`push -u`** la primera vez: te ahorra teclear remoto/rama luego.
- **`--no-ff`** para dejar un “hito” de merge visible; **`--squash`** para compactar ruido.
- **`fetch --prune`** de vez en cuando para limpiar ramas remotas obsoletas.
- Antes del PR: `git fetch`, `git rebase origin/main`, resuelve y empuja (historial limpio).
- Protege `main` en GitHub (branch protection) para exigir PRs y revisiones.

---

### 📦 Mini-recap aplicado a tu flujo (decktSsail → Ssail-1)

1. En **decktSsail**:

   ```bash
   git switch -c feature/git-notes-update
   # …edita…
   git add .
   git commit -m "Actualiza notas de Git: branches avanzados"
   git push -u origin feature/git-notes-update
   ```

2. Abres el **PR** hacia `Ssail-1/PlatziNotes`.
3. En **Ssail-1**: revisas y **Merge** (puedes elegir *Create a merge commit*, *Squash & merge* o *Rebase & merge*).
4. (Opcional) Borra la rama:

   ```bash
   git branch -d feature/git-notes-update
   git push origin --delete feature/git-notes-update
   ```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## Lectura de Aclaración


### 🟢 **Parte 1: Upstream, unset-upstream y prune**

#### 📍 ¿Qué es “upstream”?

Cuando haces `git push -u origin rama-x`, estás diciendo:

> “Mi rama local `rama-x` está vinculada (tracking) con la rama remota `origin/rama-x`”.

Eso se llama **upstream branch**: la rama remota que tu rama local sigue.
Luego, con solo `git push` o `git pull`, Git ya sabe a qué remoto y rama subir/bajar.

---

#### 📍 `git branch --unset-upstream`

Sirve para **desvincular** tu rama local de cualquier rama remota.
Útil si:

- Cambiaste el nombre de la rama en remoto.
- Borraste la rama remota.
- Quieres que tu rama local deje de empujar automáticamente.

Es como decir “olvida esa conexión”.

---

#### 📍 `git branch --set-upstream-to=origin/nueva-rama`

Sirve para **vincular manualmente** tu rama local a una rama remota (o cambiarla).
Ejemplo:

```bash
git branch --set-upstream-to=origin/dev
```

Ahora tu rama local “sabe” que tiene que hacer `pull/push` a `origin/dev`.

---

#### 📍 `git fetch --prune` / `git remote prune origin`

Cuando borras ramas en GitHub, tu Git local sigue guardando referencias “fantasma” de esas ramas remotas (aparecen con `git branch -r`).
`--prune` limpia esas referencias obsoletas.
Es como barrer “caché” para que tu lista de ramas remotas esté al día.

---

💡 **Analogía:**

- **set-upstream** = “enlazar” el cable entre dos equipos.
- **unset-upstream** = “desconectar” el cable.
- **fetch --prune** = “quitar los cables viejos que ya no existen”.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

### 🟢 **Parte 2: Merge, fast-forward, squash y no-ff**

#### 📍 Fast-forward merge

Sucede cuando tu rama de destino (ej. `main`) no tiene commits nuevos desde que creaste tu rama de feature.
Git no necesita hacer un commit de merge, simplemente mueve el puntero HEAD para adelante.

Visualmente:

```
main: A --- B
feature: A --- B --- C --- D
```

Cuando haces merge, **fast-forward**:

```
main: A --- B --- C --- D (puntero avanza)
```

No se crea commit de merge, queda lineal.

---

#### 📍 Merge normal (con commit de merge)

Sucede cuando **las dos ramas tienen commits distintos**.
Git necesita crear un commit de merge para unir los dos historiales.

---

#### 📍 `--no-ff` (no fast-forward)

Sirve para **forzar la creación de un commit de merge** incluso si podría ser fast-forward.
¿Por qué?
Porque deja un **hito** (punto visible) en el historial de que esa rama fue fusionada.
Esto es útil para equipos: se ve claramente cuándo se integró una feature.

---

#### 📍 `git merge --squash` + `git commit -m`

Son dos pasos:

1. `git merge --squash feature/x` → junta todos los commits de `feature/x` en staging como un solo paquete.
2. `git commit -m "Squash: integra feature/x en un solo commit"` → haces un commit único.

Resultado:

- La rama `feature/x` no queda en el historial de `main` con sus múltiples commits, solo un commit “grande”.
- Se mantiene el historial limpio.

---

💡 **Analogía:**

- Fast-forward = solo avanzar el marcador.
- Merge normal = pegar dos caminos distintos.
- No-ff = pegar dos caminos y dejar “poste” que marque que se unieron.
- Squash = juntar todos los ladrillos en uno solo antes de pegarlos.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

### 🟢 **Parte 3: Rebase (qué es y cuándo usarlo)**

#### 📍 Qué es rebase

“Rebase” toma tus commits y los **reaplica sobre otra base** (otro commit más nuevo).
Sirve para **actualizar tu rama** con los últimos cambios de `main` sin crear un commit de merge.

Visualmente:

```
main: A --- B --- C
feature: A --- D --- E
```

Haces:

```bash
git switch feature
git rebase main
```

Resultado:

```
main: A --- B --- C
feature: A --- B --- C --- D --- E (reaplicado)
```

No hay commit de merge, queda lineal.

---

#### 📍 Cuándo usarlo

- Cuando tu rama se quedó atrás de `main` y quieres traer los cambios **antes** de abrir un PR.
- Para mantener un historial limpio y lineal.
- No usar en ramas compartidas ya empujadas (porque cambia hashes).

---

#### 📍 `git rebase --continue`

Se usa **después de resolver conflictos** durante un rebase.
El flujo es:

```bash
git rebase main
# Conflicto
# editas archivos
git add archivos_resueltos
git rebase --continue
```

Si quieres abortar:

```bash
git rebase --abort
```

---

💡 **Analogía:**
Merge es como pegar dos caminos con un puente.
Rebase es como levantar tu camino y volverlo a colocar justo al final del camino principal.

---

</**Fin de Lectura de Aclaracion**>

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🌳 Advanced Branching

![Static Badge](https://img.shields.io/badge/git-upstream-purple?logo=git)
![Static Badge](https://img.shields.io/badge/git-prune-grey?logo=git)
![Static Badge](https://img.shields.io/badge/git-merge--no--ff-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-squash-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-rebase-blue?logo=git)

### 📍 Upstream y seguimiento

```bash
git push -u origin feature/x                # establece upstream
git branch --set-upstream-to=origin/dev     # cambia upstream manualmente
git branch --unset-upstream                 # elimina upstream
```

💡 Vincula/desvincula ramas locales con remotas para usar `push` y `pull` sin parámetros.

---

### 📍 Limpiar referencias obsoletas

```bash
git fetch --prune
git remote prune origin
```

💡 Limpia ramas remotas eliminadas para que no aparezcan en `git branch -r`.

---

### 📍 Merge avanzado

```bash
git merge --no-ff feature/x
```

💡 Forza commit de merge (deja “hito” visible).

```bash
git merge --squash feature/x
git commit -m "Squash: integra feature/x en un solo commit"
```

💡 Junta todos los commits de `feature/x` en uno solo para mantener limpio el historial.

---

### 📍 Rebase para actualizar ramas

```bash
git switch feature/x
git fetch origin
git rebase origin/main
```

💡 Reaplica tus commits sobre `main` actualizado (historial lineal).

Durante conflictos:

```bash
git add archivos_resueltos
git rebase --continue   # después de resolver
git rebase --abort      # para cancelar
```

---

### 💡 Buenas prácticas

- Protege `main` en GitHub y haz merges mediante PRs.
- Usa `--no-ff` cuando quieras dejar constancia de una feature mergeada.
- Usa `--squash` para limpiar commits irrelevantes.
- Usa `rebase` antes de abrir PRs para actualizar tu rama sin merges ruidosos.
- Haz `fetch --prune` regularmente para mantener tus ramas limpias.

---

✅ Hasta aqui ya tenemos **el kit avanzado de ramas**.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🧠 Mapa mental — Advanced Branching Flow

Este mapa muestra cómo se relacionan los conceptos más importantes:

- **Upstream y fetch/prune** (sincronización con remotos)
- **Merge, no-ff, squash** (cómo se integran ramas)
- **Rebase** (actualización limpia de ramas antes del merge)

---

```mermaid
mindmap
  root((Advanced Branching))
    Upstream & Remote
      "git push -u origin <branch>"
      "git branch --set-upstream-to=origin/<branch>"
      "git fetch --prune"
      "git remote prune origin"
    Merge Strategies
      Fast-forward
        "Simplemente avanza el puntero HEAD"
      "--no-ff"
        "Crea commit de merge (marca el hito)"
      "--squash"
        "Combina todos los commits en uno solo"
    Rebase
      "git rebase origin/main"
      "Reaplica commits sobre una nueva base"
      "Mantiene historial lineal y limpio"
      Conflicts
        "git add archivos_resueltos"
        "git rebase --continue"
        "git rebase --abort"
    Best Practices
      "Rebase antes de un PR"
      "Protege main en GitHub"
      "Usa fetch --prune regularmente"
      "Usa no-ff para dejar registro del merge"
      "Usa squash para mantener historial limpio"
```

---

### 💡 Cómo leerlo

- Cada rama del mapa representa una parte del flujo avanzado que ya dominaste.
- Puedes visualizarlo directamente en VSCode si tienes activa la extensión *Markdown Preview Mermaid Support*.
- Si no se renderiza, no pasa nada: GitHub también lo mostrará correctamente en su vista previa.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🌐 Advanced Remotes — Forks, Upstream & Synchronization

![Static Badge](https://img.shields.io/badge/git-remote-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-fetch--upstream-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-rebase--upstream-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-push--origin-purple?logo=git)

---

### 🧩 ¿Qué es un *remote*?

Un **remote** es una referencia a un repositorio alojado en otro lugar (GitHub, GitLab, etc.).
Normalmente tu repo tiene:

* `origin` → apunta al repositorio principal (tu fork o el que creaste).
* `upstream` → apunta al repositorio original del que hiciste fork (por ejemplo, `Ssail-1/PlatziNotes` cuando trabajas desde `decktSsail`).

---

### 🔗 Conectar el repo original (upstream)

Desde tu fork clonado (ejemplo, en la cuenta **decktSsail**):

```bash
git remote add upstream git@github.com:Ssail-1/PlatziNotes.git
```

📌 **Qué hace:**

* Agrega el repo original con el nombre `upstream`.
* No afecta tu `origin`, simplemente te permite traer actualizaciones del repo fuente.

💡 **Verifica tus remotos:**

```bash
git remote -v
```

Deberías ver algo como:

```
origin   git@github.com-decktSsail:decktSsail/PlatziNotes.git (fetch)
origin   git@github.com-decktSsail:decktSsail/PlatziNotes.git (push)
upstream git@github.com-Ssail:Ssail-1/PlatziNotes.git (fetch)
upstream git@github.com-Ssail:Ssail-1/PlatziNotes.git (push)
```

---

### 🔄 Actualizar tu fork con los cambios del original

A veces el repo original (`upstream`) cambia y tú quieres mantener tu fork actualizado.

1. **Traer cambios del original:**

   ```bash
   git fetch upstream
   ```

2. **Fusionar esos cambios en tu rama local principal:**

   ```bash
   git switch main
   git merge upstream/main
   ```

💡 **O hacerlo con rebase (más limpio):**

```bash
git rebase upstream/main
```

👉 Esto coloca tus commits encima de los más recientes del original.

---

### 📤 Subir los cambios actualizados a tu fork

Una vez sincronizado tu `main` local:

```bash
git push origin main
```

Así tu fork en GitHub queda actualizado con el original.

---

### 🧠 ¿Cuándo usar *merge* vs *rebase* en forks?

| Acción                     | Cuándo usar                                        | Resultado                    |
| -------------------------- | -------------------------------------------------- | ---------------------------- |
| `git merge upstream/main`  | Cuando no te importa dejar un commit de merge.     | Mantiene historia completa.  |
| `git rebase upstream/main` | Cuando quieres mantener historial lineal y limpio. | Tus commits quedan al final. |

💬 En proyectos colaborativos grandes, lo normal es usar `rebase` antes de un Pull Request.

---

### 🧹 Limpiar ramas remotas obsoletas

```bash
git fetch --prune upstream
git fetch --prune origin
```

💡 Elimina referencias de ramas que ya fueron borradas en los repos remotos.

---

### 🧭 Flujo visual

```mermaid
flowchart TD
  A[Repositorio Original (Ssail-1)] -->|fork| B[Fork (decktSsail)]
  B -->|clone| C[Local VM]
  A -->|fetch upstream| C
  C -->|merge/rebase upstream/main| B
  B -->|push origin main| D[GitHub Fork Actualizado]
```

---

### 💡 Buenas prácticas

* Usa nombres claros: `origin` (tu fork) y `upstream` (original).
* Haz `fetch upstream` periódicamente para mantener tu fork al día.
* Rebase antes de enviar PRs para evitar conflictos.
* Nunca hagas push al `upstream` (solo lees de él).
* Verifica tus remotos con `git remote -v` antes de ejecutar un push.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🛠️ Restauración segura de commits

![Static Badge](https://img.shields.io/badge/git-revert-red?logo=git)
![Static Badge](https://img.shields.io/badge/git-checkout-yellow?logo=git)

---

### 🔙 `git revert <hash>`

Revierte un commit creando **un nuevo commit inverso** (sin alterar el historial).

```bash
git revert 7f3c2a1
```

💡 Perfecto para revertir errores en repos públicos o remotos, ya que no borra historia.

---

### 🕓 `git checkout <hash>`

Permite moverte a un commit pasado temporalmente (modo *detached HEAD*).

```bash
git checkout 7f3c2a1
```

Para volver a la rama anterior:

```bash
git switch -
```

💡 Ideal para revisar estados pasados sin modificar el historial actual.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 📘 TAGS & RELEASES

Las **etiquetas** (*tags*) se usan para marcar puntos específicos del historial del repositorio, generalmente para **versionar** o señalar commits importantes como versiones estables o entregas finales.
En GitHub, estas etiquetas se pueden usar para crear **releases**, con notas de versión o archivos de publicación.

![Static Badge](https://img.shields.io/badge/git-tag-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-push--tags-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-show--ref--tags-yellow?logo=git)

---

### 🏷️ Concepto y tipos de tags

---

#### 🔹 ¿Qué es un tag?

Un **tag** es una referencia inmutable a un commit específico.
Sirve como marcador o “foto” dentro del historial de Git.
Ideal para marcar **versiones estables** o **puntos clave del proyecto**.

💡 *Ejemplo:*

> Al terminar una funcionalidad completa y estable, puedes crear un tag `v1.0` para marcar esa versión.

---

#### 🔹 Tipos de etiquetas

| Tipo                     | Descripción                                                                | Ejemplo                                        |
| ------------------------ | -------------------------------------------------------------------------- | ---------------------------------------------- |
| **Ligera (lightweight)** | Solo apunta al hash del commit, sin información extra.                     | `git tag v1.0`                                 |
| **Anotada (annotated)**  | Contiene metadatos (autor, fecha, mensaje). Ideal para versiones públicas. | `git tag -a v1.0 -m "Versión estable inicial"` |

📌 **Recomendación:**
Siempre usa tags anotados (`-a`) para versiones oficiales o públicas.

---

#### 🔹 Asignar etiquetas a commits específicos

```bash
git tag -a v1.0.1 <hash-commit> -m "Hotfix versión 1.0.1"
```

💬 Esto marca un commit anterior con una etiqueta, aunque no sea el más reciente.

---

#### 🔹 Ver etiquetas existentes

```bash
git tag
```

📋 Lista todas las etiquetas locales.

---

#### 🔹 Mostrar información detallada del tag

```bash
git show v1.0
```

📌 Muestra el commit asociado, el mensaje del tag, autor, fecha y contenido del cambio.

---

#### 🔹 Ver asociaciones entre tags y commits

```bash
git show-ref --tags
```

📌 Lista cada tag junto al hash del commit correspondiente.
Perfecto para ubicar de forma rápida qué commit está marcado por cada etiqueta.

---

### 🌐 Gestión remota y manipulación de tags

---

#### 📤 Subir tags al repositorio remoto

```bash
git push origin --tags
```

📌 Sube **todos los tags** locales al remoto.

O, si quieres subir uno específico:

```bash
git push origin v1.0
```

---

#### 🗑️ Eliminar etiquetas

##### Localmente:

```bash
git tag -d v1.0
```

##### En remoto:

Primero elimina el tag local y luego el remoto:

```bash
git push origin --delete v1.0
```

O alternativamente:

```bash
git push origin :refs/tags/v1.0
```

💡 Si el tag ya fue subido, recuerda borrarlo en ambos lugares para mantener sincronía.

---

#### 🔁 Reasignar un tag

Si etiquetaste el commit incorrecto:

```bash
git tag -d v1.0
git tag -a v1.0 <hash-correcto> -m "Etiqueta corregida"
git push origin -f v1.0
```

⚠️ `-f` (force) es necesario si el tag ya existía en el remoto.
Úsalo con cuidado para no sobrescribir versiones ya distribuidas.

---

### 🚀 Releases en GitHub y Buenas prácticas

---

#### 📦 Crear un Release en GitHub

1. Ve a la pestaña **Releases** en tu repositorio.
2. Haz clic en **“Draft a new release”**.
3. Elige un tag existente o crea uno nuevo.
4. Agrega título, descripción y notas de cambios (Changelog).
5. Publica el Release.

💡 Los Releases pueden incluir binarios, ejecutables o documentación específica de esa versión.

---

#### 🧠 Flujo visual — Tags & Releases

```mermaid
flowchart LR
  A[Commit estable] -->|git tag -a v1.0| B[Tag local]
  B -->|git push origin --tags| C[Tag remoto]
  C -->|GitHub Release| D[Versión pública documentada]
  D -->|Usuarios descargan| E[Versión v1.0 estable]
```

---

#### 💡 Buenas prácticas

✅ Usa **versionado semántico (SemVer)**:
`vMAJOR.MINOR.PATCH`
Ejemplo:

* `v1.0.0` → primera versión estable.
* `v1.1.0` → nueva funcionalidad sin romper compatibilidad.
* `v1.1.1` → corrección menor o hotfix.

✅ Crea tags **anotados** (`-a`) para mantener información completa.
✅ Revisa que tu `main` esté estable antes de etiquetar.
✅ Añade un archivo **CHANGELOG.md** con los cambios importantes de cada versión.
✅ No borres tags antiguos, son parte del historial del proyecto.
✅ Usa tags también para **documentación**, **entregas de prácticas** o **checkpoints** en proyectos académicos.

---

✅ Con esto ya dominas el uso **profesional de etiquetas y releases**, desde la creación local hasta su publicación en GitHub.

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🧹 MAINTENANCE & OPTIMIZATION

Git guarda todo: commits, objetos, ramas, referencias… con el tiempo esto puede generar **archivos innecesarios** o referencias obsoletas.
Estos comandos te ayudan a **mantener tu repositorio limpio, liviano y funcional.**

![Static Badge](https://img.shields.io/badge/git-gc-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-fsck-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-reflog-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-clean-red?logo=git)

---

### 🧰 `git gc` — Garbage Collector (compacta y optimiza)

```bash
git gc
```

📌 **Qué hace:**

* “Empaca” objetos sueltos (commits, blobs, etc.) en archivos más compactos.
* Borra datos temporales que ya no se usan.
* Reduce el tamaño del repositorio y mejora el rendimiento.

💡 Git ejecuta este proceso automáticamente de vez en cuando, pero puedes forzarlo manualmente.

⚙️ **Modo agresivo (más profundo):**

```bash
git gc --aggressive --prune=now
```

👉 Reorganiza toda la base de datos interna de Git y elimina todo lo que ya no se referencia.
⚠️ Puede tardar varios minutos en repos grandes.

---

### 🩺 `git fsck` — Verificación de integridad

```bash
git fsck
```

📌 **Qué hace:**

* Verifica la integridad de tu repositorio.
* Detecta objetos dañados o referencias perdidas.

💡 Úsalo si sospechas de corrupción de datos o errores en `.git/`.

🔍 **Ver objetos huérfanos (dangling commits):**

```bash
git fsck --lost-found
```

👉 Muestra commits o blobs sin referencia a ninguna rama, útiles para recuperar trabajo perdido.

---

### 🧭 `git reflog` — Historial de movimientos (el salvavidas)

```bash
git reflog
```

📌 **Qué hace:**

* Muestra todos los movimientos de HEAD: cambios de rama, resets, merges, rebases, etc.
* Te permite **recuperar commits eliminados** incluso después de un `reset --hard`.

💬 **Ejemplo de uso:**

```bash
git reflog
# muestrará algo como:
# a7c9b1d HEAD@{0}: reset: moving to HEAD~1
# 1f2d9e0 HEAD@{1}: commit: agrega archivo de configuración
```

👉 Puedes restaurar un commit perdido así:

```bash
git checkout <hash-commit-perdido>
# o crear una rama para recuperarlo:
git switch -c recuperacion <hash-commit-perdido>
```

💡 Es uno de los comandos más útiles para “deshacer el desastre”.

---

### 🧼 `git clean` — Limpieza de archivos no rastreados

```bash
git clean -n
```

📌 Muestra qué archivos **no rastreados (untracked)** serían eliminados.
No borra nada todavía.

```bash
git clean -f
```

📌 Elimina los archivos no rastreados (sin commit, sin staging).

💡 **Parámetros útiles:**

| Flag | Acción                                                    |
| ---- | --------------------------------------------------------- |
| `-f` | Forzar eliminación.                                       |
| `-d` | Incluir directorios no rastreados.                        |
| `-x` | Borra también los archivos ignorados por `.gitignore`. ⚠️ |
| `-i` | Modo interactivo (elige qué borrar).                      |

🔍 **Ejemplo completo:**

```bash
git clean -fd
```

👉 Elimina todo lo no rastreado: carpetas y archivos, dejando tu repo como nuevo.

---

### 🧩 Flujo visual de mantenimiento

```mermaid
flowchart TD
    A[Repositorio con objetos viejos] -->|git gc| B[Compactado y optimizado]
    A -->|git fsck| C[Verifica integridad]
    A -->|git reflog| D[Recupera commits perdidos]
    A -->|git clean| E[Elimina archivos no rastreados]
```

---

### 💡 Buenas prácticas de mantenimiento

✅ Ejecuta `git gc` al menos una vez por mes en proyectos grandes.
✅ Usa `git fsck` después de fallos de energía o errores en Git.
✅ Haz `git reflog` si perdiste commits por accidente.
✅ Ejecuta `git clean -n` antes de borrar, para ver qué eliminarás.
✅ No ejecutes `--aggressive` muy seguido, solo en repos con mucho historial.

---

✅ Con esto dominas el mantenimiento completo de un repositorio:
cómo mantenerlo rápido, íntegro y limpio, **sin perder nada importante.**

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 💫 FINAL BLOCK — Cierre del Módulo Git: Buenas prácticas y preparación profesional

![Static Badge](https://img.shields.io/badge/git-professional-blue?logo=git)
![Static Badge](https://img.shields.io/badge/documentation-green?logo=markdown)
![Static Badge](https://img.shields.io/badge/portfolio-orange?logo=github)

---

### 🎯 Objetivo de este cierre

Consolidar todo lo aprendido sobre Git y dejar tu entorno listo para la siguiente fase:
**colaborar, compartir y presentar proyectos profesionales** en GitHub.

---

### 🧭 1. Estructura profesional de repositorios

💡 **Buenas prácticas de organización**

| Elemento          | Descripción                                                            | Ejemplo                               |
| ----------------- | ---------------------------------------------------------------------- | ------------------------------------- |
| `README.md`       | Portada del proyecto. Explica qué hace, cómo usarlo y cómo contribuir. | Breve, con secciones claras y badges. |
| `.gitignore`      | Evita subir archivos innecesarios.                                     | Logs, dependencias, claves privadas.  |
| `LICENSE`         | Define permisos de uso.                                                | MIT, GPL, CC, etc.                    |
| `CHANGELOG.md`    | Historial de cambios por versión.                                      | Usar formato SemVer.                  |
| `CONTRIBUTING.md` | Guía para colaboradores.                                               | Explica cómo hacer PRs y commits.     |

💬 *Un repo sin documentación es como una casa sin puertas: nadie sabe por dónde entrar.*

---

### 🧱 2. Commits profesionales

Usa **mensajes breves, consistentes y en presente**:

| Tipo de cambio  | Ejemplo de mensaje                          |
| --------------- | ------------------------------------------- |
| Nueva función   | `feat: agrega sistema de autenticación`     |
| Corrección      | `fix: corrige bug al crear usuario`         |
| Documentación   | `docs: actualiza guía de instalación`       |
| Refactorización | `refactor: simplifica lógica de validación` |
| Estilo          | `style: ajusta formato de código`           |
| Tests           | `test: agrega pruebas de login`             |

💡 Este formato (tipo: descripción) es estándar en equipos grandes y compatible con **Conventional Commits**.

---

### 🧰 3. Seguridad y respaldo

* **SSH**: usa llaves seguras en lugar de contraseñas.
* **Forks**: trabaja en copias para no comprometer la rama principal.
* **Branches protegidas**: en GitHub, protege `main` para exigir revisiones antes de fusionar.
* **Respaldos locales**: clona tus repos críticos en una segunda ubicación o disco externo.

---

### 🧹 4. Limpieza y mantenimiento

Repite cada cierto tiempo:

```bash
git fetch --prune
git gc
git fsck
git reflog expire --expire=90.days.ago --all
```

📌 Con esto mantienes tu repositorio **optimizado y sin referencias viejas**.

---

### 💼 5. Mostrar tu trabajo (portafolio técnico)

Para esta parte te tocará personalizar tu perfil de GitHub!, puedes verlo en las siguientes notas [github-essentials-notes.md](Ruta "Notas del curso enfocado a GitHub!")

* Crea un repositorio personal llamado **`<tu-usuario>`** en GitHub (por ejemplo, `Ssail-1`).
* Personalízalo con un **README.md de perfil** (mostrará tu presentación en tu perfil público).
* Incluye:

  * Breve biografía y objetivos.
  * Proyectos destacados.
  * Badges de tecnologías (desde [shields.io](https://shields.io/)).
  * Estadísticas y enlaces a tus redes profesionales.

💬 *Tu perfil de GitHub es tu nuevo currículum técnico.*

---

### 🚀 6. Preparar transición a la siguiente sección: GitHub Tools

Esta parte no es necesaría al 100%, en [github-essentials-notes.md](Ruta "Notas del curso enfocado a GitHub!") podrás descubir como configurar SSH que es lo unico que hace falta en este archivo, pero si te recomiendo tener una cuenta secundaria de github :D.

Antes de pasar a GitHub, asegúrate de tener:

✅ SSH configurado y probado.
✅ Tu cuenta principal ([`Ssail-1`](https://github.com/Ssail-1 "GitHub principal de Ssail")) como portfolio.
✅ Tu cuenta secundaria ([`decktSsail`](https://github.com/decktSsail "GitHub secundario de Ssail")) para practicar forks y PRs.
✅ Un repositorio con el que puedas experimentar como  ([`PlatziNotes`](https://github.com/Ssail-1/PlatziNotes "Repositorio de documentacion y notas de los cursos de Platzi")) actualizado con todo lo aprendido.  
✅ Y claro conocimiento de los siguientes comandos:

* `git clone`, `git pull`, `git push`, `git fetch`
* `git add`, `git commit`, `git status`, `git diff`
* `git branch`, `git switch`, `git merge`, `git rebase`
* `git tag`, `git gc`, `git reflog`, `git clean`

De los cuales si tienes dudas, puedes regresar aqui siempre!

---

### 🧠 Diagrama resumen del módulo Git

```mermaid
mindmap
  root((Módulo Git))
    Setup & Init
      Configuración global
      SSH Keys
    Stage & Snapshot
      git add
      git commit
    Branch & Merge
      Ramas
      Merge strategies
      Rebase
    Share & Update
      Pull
      Push
      Fetch
    Advanced
      Tags & Releases
      Maintenance
      Reflog & GC
```

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

### 💬 Reflexión final

> “Dominar Git no es solo saber comandos, es **entender la historia del código**.”
> Cada commit cuenta una parte de ti, de tus errores, tus mejoras y tus logros.
> Desde hoy, cada `git add` es una semilla de tu progreso 🌱.

[🔗 Repositorio principal del proyecto](https://github.com/Ssail-1/PlatziNotes)

---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

✅ **Con esto termina el módulo de Git.**
El entorno está limpio, el conocimiento consolidado y estamos listos para dar el salto a la **Sección II: GitHub — Colaboración y Herramientas en la Nube.**

---
---
---

<p align="center">
  <a href="#índice">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
> _“No soy un experto, soy alguien que nunca dejará de intentarlo.”_ — **Ssail**  
>
> _Creado con ❤️ por **Ssail & Noa** — PlatziNotes Project 2025
>

[🔗 Repositorio principal del proyecto](https://github.com/Ssail-1/PlatziNotes)

---