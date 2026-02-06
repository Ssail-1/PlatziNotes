
# 🌿 Branches (atajos prácticos y pro tips)

![Static Badge](https://img.shields.io/badge/git-branch-green?logo=git)
![Static Badge](https://img.shields.io/badge/git-switch-teal?logo=git)
![Static Badge](https://img.shields.io/badge/git-merge-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-push--u-blue?logo=git)

---

- [🌿 Branches (atajos prácticos y pro tips)](#-branches-atajos-prácticos-y-pro-tips)
  - [📋 Listado y navegación](#-listado-y-navegación)
  - [🌱 Crear y entrar (formas equivalentes)](#-crear-y-entrar-formas-equivalentes)
  - [✏️ Renombrar rama](#️-renombrar-rama)

---

## 📋 Listado y navegación

```bash
git branch           # Lista ramas locales ( * = actual )
git branch -r        # Ramas remotas
git branch -a        # Todas (locales + remotas)
git switch main      # Cambiar de rama (moderno)
git checkout main    # Cambiar de rama (clásico)
```

## 🌱 Crear y entrar (formas equivalentes)

```bash
git switch -c feature/x          # crea y entra (-c = create)
git checkout -b feature/x        # clásico
git branch feature/x && git switch feature/x  # crear y luego entrar
```

## ✏️ Renombrar rama

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
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
