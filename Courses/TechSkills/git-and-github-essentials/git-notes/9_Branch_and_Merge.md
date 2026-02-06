
# 🌿 BRANCH & MERGE

Permiten aislar el trabajo en diferentes líneas de desarrollo sin afectar la rama principal.
Cada rama es una línea de tiempo independiente donde puedes experimentar, desarrollar o corregir errores.

![Static Badge](https://img.shields.io/badge/git-branch-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-checkout-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-switch-teal?logo=git)
![Static Badge](https://img.shields.io/badge/git-merge-yellow?logo=git)

---

- [🌿 BRANCH \& MERGE](#-branch--merge)
  - [🌱 `git branch` — Crear y listar ramas](#-git-branch--crear-y-listar-ramas)
  - [🧠 **Convenciones de nombres de ramas**](#-convenciones-de-nombres-de-ramas)
  - [🔄 `git switch` y `git checkout` — Moverte entre ramas](#-git-switch-y-git-checkout--moverte-entre-ramas)
  - [🧬 `git merge` — Unir ramas](#-git-merge--unir-ramas)

---

## 🌱 `git branch` — Crear y listar ramas

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
---

## 🧠 **Convenciones de nombres de ramas**

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
---

## 🔄 `git switch` y `git checkout` — Moverte entre ramas

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
---

## 🧬 `git merge` — Unir ramas

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

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
