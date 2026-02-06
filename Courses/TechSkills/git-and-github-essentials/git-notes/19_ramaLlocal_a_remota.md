
# 🔗 Tracking (conectar tu rama local con la remota)

## Primera vez que empujas una rama nueva

```bash
git push -u origin feature/x   # -u = set-upstream (queda vinculada)
# Luego ya basta con:
git push
git pull
```

## Ver / cambiar upstream

```bash
git branch -vv                          # muestra tracking de cada rama
git branch --set-upstream-to=origin/feature/x
```

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
