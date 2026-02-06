
# 🤝 Merge (estrategias útiles)

---

- [🤝 Merge (estrategias útiles)](#-merge-estrategias-útiles)
  - [Merge normal (fast-forward si aplica)](#merge-normal-fast-forward-si-aplica)
  - [Forzar commit de merge aunque sea FF](#forzar-commit-de-merge-aunque-sea-ff)
  - [Traerte los cambios pero sin crear commit de merge](#traerte-los-cambios-pero-sin-crear-commit-de-merge)
  - [Si hay conflicto](#si-hay-conflicto)
  - [🪄 Rebase rápido para mantener la rama al día (lineal)](#-rebase-rápido-para-mantener-la-rama-al-día-lineal)
  - [🍒 Cherry-pick (traer un commit específico)](#-cherry-pick-traer-un-commit-específico)
  - [🛡️ Buenas prácticas rápidas](#️-buenas-prácticas-rápidas)
  - [📦 Mini-recap aplicado a tu flujo (decktSsail → Ssail-1)](#-mini-recap-aplicado-a-tu-flujo-decktssail--ssail-1)

---

## Merge normal (fast-forward si aplica)

```bash
git switch main
git merge feature/x
```

## Forzar commit de merge aunque sea FF

```bash
git merge --no-ff feature/x
# Útil para dejar el “hito” del merge visible en el historial.
```

- Una fusión FF ocurre cuando la rama en la que estás haciendo el merge no ha tenido nuevos commits desde que se creó o actualizó la rama que quieres fusionar.
- En este caso, Git simplemente avanza el puntero de la rama actual al último commit de la rama que se está integrando, sin crear un nuevo "merge commit".

## Traerte los cambios pero sin crear commit de merge

```bash
git merge --squash feature/x
git commit -m "Squash: integra feature/x en un solo commit"
# Ideal para mantener historial más limpio cuando hubo muchos commits intermedios.
```

## Si hay conflicto

```bash
# Editas archivos en conflicto (VSCode ayuda mucho)
git add <archivos_resueltos>
git commit                      # completa el merge

# Si necesitas abortar:
git merge --abort
```

---

## 🪄 Rebase rápido para mantener la rama al día (lineal)

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

## 🍒 Cherry-pick (traer un commit específico)

```bash
git cherry-pick <hash>
# Copia el commit indicado a tu rama actual (útil para hotfixes puntuales).
```

---

## 🛡️ Buenas prácticas rápidas

- Crea siempre ramas por feature: `feature/…`, `hotfix/…`, `release/…`.
- **`push -u`** la primera vez: te ahorra teclear remoto/rama luego.
- **`--no-ff`** para dejar un “hito” de merge visible; **`--squash`** para compactar ruido.
- **`fetch --prune`** de vez en cuando para limpiar ramas remotas obsoletas.
- Antes del PR: `git fetch`, `git rebase origin/main`, resuelve y empuja (historial limpio).
- Protege `main` en GitHub (branch protection) para exigir PRs y revisiones.

---

## 📦 Mini-recap aplicado a tu flujo (decktSsail → Ssail-1)

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
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
