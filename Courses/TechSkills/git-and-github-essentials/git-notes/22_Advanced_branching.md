
# 🌳 Advanced Branching

![Static Badge](https://img.shields.io/badge/git-upstream-purple?logo=git)
![Static Badge](https://img.shields.io/badge/git-prune-grey?logo=git)
![Static Badge](https://img.shields.io/badge/git-merge--no--ff-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-squash-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-rebase-blue?logo=git)

---

- [🌳 Advanced Branching](#-advanced-branching)
  - [📍 Upstream y seguimiento](#-upstream-y-seguimiento)
  - [📍 Limpiar referencias obsoletas](#-limpiar-referencias-obsoletas)
  - [📍 Merge avanzado](#-merge-avanzado)
  - [📍 Rebase para actualizar ramas](#-rebase-para-actualizar-ramas)
  - [💡 Buenas prácticas](#-buenas-prácticas)
  - [🧠 Mapa mental — Advanced Branching Flow](#-mapa-mental--advanced-branching-flow)
    - [💡 Cómo leerlo](#-cómo-leerlo)

---

## 📍 Upstream y seguimiento

```bash
git push -u origin feature/x                # establece upstream
git branch --set-upstream-to=origin/dev     # cambia upstream manualmente
git branch --unset-upstream                 # elimina upstream
```

💡 Vincula/desvincula ramas locales con remotas para usar `push` y `pull` sin parámetros.

---

## 📍 Limpiar referencias obsoletas

```bash
git fetch --prune
git remote prune origin
```

💡 Limpia ramas remotas eliminadas para que no aparezcan en `git branch -r`.

---

## 📍 Merge avanzado

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

## 📍 Rebase para actualizar ramas

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

## 💡 Buenas prácticas

- Protege `main` en GitHub y haz merges mediante PRs.
- Usa `--no-ff` cuando quieras dejar constancia de una feature mergeada.
- Usa `--squash` para limpiar commits irrelevantes.
- Usa `rebase` antes de abrir PRs para actualizar tu rama sin merges ruidosos.
- Haz `fetch --prune` regularmente para mantener tus ramas limpias.

---

✅ Hasta aqui ya tenemos **el kit avanzado de ramas**.

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

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
<!-- Aun no se utlizar bien mermaid
Lo corregire despues -->
---

### 💡 Cómo leerlo

- Cada rama del mapa representa una parte del flujo avanzado.
- Puedes visualizarlo directamente en VSCode si tienes activa la extensión *Markdown Preview Mermaid Support*.
- Si no se renderiza, no pasa nada: GitHub también lo mostrará correctamente en su vista previa.

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
