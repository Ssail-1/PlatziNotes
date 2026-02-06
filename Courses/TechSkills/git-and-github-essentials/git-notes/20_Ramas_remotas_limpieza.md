
# 🔄 Ramas remotas y limpieza

## Obtener ramas nuevas/borradas del remoto

```bash
git fetch --prune            # sincroniza y limpia referencias obsoletas
# o
git remote prune origin
```

## Borrar ramas (local y remoto)

```bash
git branch -d feature/x      # borra local (si ya fue mergeada)
git branch -D feature/x      # borra local forzado ⚠️
git push origin --delete feature/x   # borra la rama en GitHub
```

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
