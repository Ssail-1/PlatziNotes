
# ✍️ REWRITE HISTORY

En Git, reescribir el historial te permite **corregir, reorganizar o limpiar commits**.
Se usa para dejar un historial claro y profesional antes de subir o fusionar cambios.

⚠️ **Advertencia:** estos comandos modifican el historial, así que úsalos solo en **ramas locales** o en commits que aún no se hayan hecho *push*.

![Static Badge](https://img.shields.io/badge/git-reset-red?logo=git)
![Static Badge](https://img.shields.io/badge/git-rebase-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-commit--amend-yellow?logo=git)

---

- [✍️ REWRITE HISTORY](#️-rewrite-history)
  - [🧭 `git reset` — Reubicar el puntero HEAD](#-git-reset--reubicar-el-puntero-head)
    - [🧩 Ejemplo visual](#-ejemplo-visual)
  - [🪄 `git rebase` — Reaplicar commits sobre otra base](#-git-rebase--reaplicar-commits-sobre-otra-base)
    - [💬 **Ejemplo práctico:**](#-ejemplo-práctico)
    - [🧮 Rebase interactivo](#-rebase-interactivo)
  - [📝 `git commit --amend` — Corregir el último commit](#-git-commit---amend--corregir-el-último-commit)
  - [🧠 Buenas prácticas](#-buenas-prácticas)

---

## 🧭 `git reset` — Reubicar el puntero HEAD

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
---

## 🪄 `git rebase` — Reaplicar commits sobre otra base

```bash
git rebase main
```

📌 **Qué hace:**

- Toma los commits de tu rama actual y los “reaplica” sobre otra rama.
- Reescribe el historial para que tus cambios parezcan creados encima del último commit de la rama base.

### 💬 **Ejemplo práctico:**

```bash
git switch feature/login
git rebase main
```

👉 Aplica los commits de `feature/login` sobre los más recientes de `main`.

💡 Ideal cuando tu rama se quedó atrás y quieres **actualizarla sin crear un merge commit**.

---
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

## 📝 `git commit --amend` — Corregir el último commit

```bash
git commit --amend -m "Corrige error en mensaje anterior"
```

📌 **Qué hace:**

- Modifica el último commit (mensaje o contenido).
- Útil para pequeños errores justo antes de hacer *push*.

⚠️ **Precaución:** si ya hiciste *push*, evita usarlo (cambiaría el historial remoto).

---

## 🧠 Buenas prácticas

- Usa `rebase` para mantener un historial lineal y limpio.
- Usa `reset --soft` cuando necesites rehacer un commit sin perder trabajo.
- Evita `reset --hard` si no estás completamente seguro.
- Antes de reescribir commits, verifica con:

  ```bash
  git log --oneline --graph
  ```

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
