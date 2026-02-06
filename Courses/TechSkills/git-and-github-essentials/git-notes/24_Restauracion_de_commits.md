
# 🛠️ Restauración segura de commits

![Static Badge](https://img.shields.io/badge/git-revert-red?logo=git)
![Static Badge](https://img.shields.io/badge/git-checkout-yellow?logo=git)

---

- [🛠️ Restauración segura de commits](#️-restauración-segura-de-commits)
  - [🔙 `git revert <hash>`](#-git-revert-hash)
  - [🕓 `git checkout <hash>`](#-git-checkout-hash)

---

## 🔙 `git revert <hash>`

Revierte un commit creando **un nuevo commit inverso** (sin alterar el historial).

```bash
git revert 7f3c2a1
```

💡 Perfecto para revertir errores en repos públicos o remotos, ya que no borra historia.

---

## 🕓 `git checkout <hash>`

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
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
