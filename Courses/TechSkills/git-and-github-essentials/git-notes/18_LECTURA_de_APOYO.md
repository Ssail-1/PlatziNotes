# Lectura de Aclaración

## Indice

- [Lectura de Aclaración](#lectura-de-aclaración)
  - [Indice](#indice)
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

## 🟢 **Parte 1: Upstream, unset-upstream y prune**

### 📍 ¿Qué es “upstream”?

Cuando haces `git push -u origin rama-x`, estás diciendo:

> “Mi rama local `rama-x` está vinculada (tracking) con la rama remota `origin/rama-x`”.

Eso se llama **upstream branch**: la rama remota que tu rama local sigue.
Luego, con solo `git push` o `git pull`, Git ya sabe a qué remoto y rama subir/bajar.

---
---
### 📍 `git branch --unset-upstream`

Sirve para **desvincular** tu rama local de cualquier rama remota.
Útil si:

- Cambiaste el nombre de la rama en remoto.
- Borraste la rama remota.
- Quieres que tu rama local deje de empujar automáticamente.

Es como decir “olvida esa conexión”.

---

### 📍 `git branch --set-upstream-to=origin/nueva-rama`

Sirve para **vincular manualmente** tu rama local a una rama remota (o cambiarla).
Ejemplo:

```bash
git branch --set-upstream-to=origin/dev
```

Ahora tu rama local “sabe” que tiene que hacer `pull/push` a `origin/dev`.

---

### 📍 `git fetch --prune` / `git remote prune origin`

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
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🟢 **Parte 2: Merge, fast-forward, squash y no-ff**

### 📍 Fast-forward merge

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

### 📍 Merge normal (con commit de merge)

Sucede cuando **las dos ramas tienen commits distintos**.
Git necesita crear un commit de merge para unir los dos historiales.

---

### 📍 `--no-ff` (no fast-forward)

Sirve para **forzar la creación de un commit de merge** incluso si podría ser fast-forward.
¿Por qué?
Porque deja un **hito** (punto visible) en el historial de que esa rama fue fusionada.
Esto es útil para equipos: se ve claramente cuándo se integró una feature.

---

### 📍 `git merge --squash` + `git commit -m`

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
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
---

## 🟢 **Parte 3: Rebase (qué es y cuándo usarlo)**

### 📍 Qué es rebase

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
feature: A --- B --- C --- D --- E (reapl
### 📍 Upstream y seguimiento

```bash
git push -u origin feature/x                # establece upstream
git branch --set-upstream-to=origin/dev     # cambia upstream manualmente
git branch --unset-upstream                 # elimina upstream
```

💡 Vincula/desvincula ramas locales con remotas para usar `push` y `pull` sin parámetros.icado)
```

No hay commit de merge, queda lineal.

---

### 📍 Cuándo usarlo

- Cuando tu rama se quedó atrás de `main` y quieres traer los cambios **antes** de abrir un PR.
- Para mantener un historial limpio y lineal.
- No usar en ramas compartidas ya empujadas (porque cambia hashes).

---

### 📍 `git rebase --continue`

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

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
