# 🆕 `git init`

Inicializa un directorio vacío como **repositorio Git**.

![Static Badge](https://img.shields.io/badge/git-init-blue?logo=git)

---

- [🆕 `git init`](#-git-init)
  - [⚙️ **Cómo definir siempre `main` como predeterminado:**](#️-cómo-definir-siempre-main-como-predeterminado)
  - [⚙️ **Cómo renombrar la rama actual a `main`:**](#️-cómo-renombrar-la-rama-actual-a-main)

---

```bash
git init
```

📌 **Qué hace:**

- Crea una carpeta oculta llamada `.git` que guarda todo el historial de versiones.
- Inicia la rama principal. Antiguamente se llamaba **master**, ahora por convención se usa **main**.

🔎 **Explicación del cambio de nombre de la rama:**

- `master` era el nombre por defecto, pero muchas comunidades lo reemplazaron por `main` para hacerlo más inclusivo y claro.
- **main** = rama principal, la base del proyecto.

## ⚙️ **Cómo definir siempre `main` como predeterminado:**

```bash
git config --global init.defaultBranch main
```

## ⚙️ **Cómo renombrar la rama actual a `main`:**

```bash
git branch -m main
```

- `git branch` → gestiona ramas.
- `-m` → move/rename (renombra la rama actual).
- `main` → el nuevo nombre.

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
