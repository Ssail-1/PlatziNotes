
# 🌐 Advanced Remotes — Forks, Upstream & Synchronization

![Static Badge](https://img.shields.io/badge/git-remote-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-fetch--upstream-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-rebase--upstream-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-push--origin-purple?logo=git)

---

- [🌐 Advanced Remotes — Forks, Upstream \& Synchronization](#-advanced-remotes--forks-upstream--synchronization)
  - [🧩 ¿Qué es un *remote*?](#-qué-es-un-remote)
  - [🔗 Conectar el repo original (upstream)](#-conectar-el-repo-original-upstream)
  - [🔄 Actualizar tu fork con los cambios del original](#-actualizar-tu-fork-con-los-cambios-del-original)
  - [📤 Subir los cambios actualizados a tu fork](#-subir-los-cambios-actualizados-a-tu-fork)
  - [🧠 ¿Cuándo usar *merge* vs *rebase* en forks?](#-cuándo-usar-merge-vs-rebase-en-forks)
  - [🧹 Limpiar ramas remotas obsoletas](#-limpiar-ramas-remotas-obsoletas)
  - [🧭 Flujo visual](#-flujo-visual)
  - [💡 Buenas prácticas](#-buenas-prácticas)

---

## 🧩 ¿Qué es un *remote*?

Un **remote** es una referencia a un repositorio alojado en otro lugar (GitHub, GitLab, etc.).
Normalmente tu repo tiene:

* `origin` → apunta al repositorio principal (tu fork o el que creaste).
* `upstream` → apunta al repositorio original del que hiciste fork (por ejemplo, `Ssail-1/PlatziNotes` cuando trabajas desde `decktSsail`).

---

## 🔗 Conectar el repo original (upstream)

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

```bash
origin   git@github.com-decktSsail:decktSsail/PlatziNotes.git (fetch)
origin   git@github.com-decktSsail:decktSsail/PlatziNotes.git (push)
upstream git@github.com-Ssail:Ssail-1/PlatziNotes.git (fetch)
upstream git@github.com-Ssail:Ssail-1/PlatziNotes.git (push)
```

---

## 🔄 Actualizar tu fork con los cambios del original

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

## 📤 Subir los cambios actualizados a tu fork

Una vez sincronizado tu `main` local:

```bash
git push origin main
```

Así tu fork en GitHub queda actualizado con el original.

---

## 🧠 ¿Cuándo usar *merge* vs *rebase* en forks?

| Acción                     | Cuándo usar                                        | Resultado                    |
| -------------------------- | -------------------------------------------------- | ---------------------------- |
| `git merge upstream/main`  | Cuando no te importa dejar un commit de merge.     | Mantiene historia completa.  |
| `git rebase upstream/main` | Cuando quieres mantener historial lineal y limpio. | Tus commits quedan al final. |

💬 En proyectos colaborativos grandes, lo normal es usar `rebase` antes de un Pull Request.

---

## 🧹 Limpiar ramas remotas obsoletas

```bash
git fetch --prune upstream
git fetch --prune origin
```

💡 Elimina referencias de ramas que ya fueron borradas en los repos remotos.

---

## 🧭 Flujo visual

```mermaid
flowchart TD
  A[Repositorio Original (Ssail-1)] -->|fork| B[Fork (decktSsail)]
  B -->|clone| C[Local VM]
  A -->|fetch upstream| C
  C -->|merge/rebase upstream/main| B
  B -->|push origin main| D[GitHub Fork Actualizado]
```

---

## 💡 Buenas prácticas

* Usa nombres claros: `origin` (tu fork) y `upstream` (original).
* Haz `fetch upstream` periódicamente para mantener tu fork al día.
* Rebase antes de enviar PRs para evitar conflictos.
* Nunca hagas push al `upstream` (solo lees de él).
* Verifica tus remotos con `git remote -v` antes de ejecutar un push.

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
