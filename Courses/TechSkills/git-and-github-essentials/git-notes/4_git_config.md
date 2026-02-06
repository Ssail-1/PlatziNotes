
# 🧾 `git config --list`

Verifica y consulta la configuración activa de Git en tu entorno.

![Static Badge](https://img.shields.io/badge/git-config-yellow?logo=git)

Lista toda la configuración activa que Git está usando actualmente.

---

- [🧾 `git config --list`](#-git-config---list)
  - [🔍 Consultar una clave específica](#-consultar-una-clave-específica)
    - [💡 Buenas prácticas](#-buenas-prácticas)

---

```bash
git config --list
```

📌 **Qué hace:**

- Muestra configuraciones de todos los niveles:

  - **Sistema** (`/etc/gitconfig`) → afecta a todos los usuarios de la computadora.
  - **Global** (`~/.gitconfig` o `~/.config/git/config`) → afecta solo a tu usuario.
  - **Local** (`.git/config`) → afecta únicamente al repo donde estás.
- Si un valor se repite, el nivel más cercano (local) tiene prioridad.

## 🔍 Consultar una clave específica

Si quieres ver el valor de una sola clave:

- `git config <key>`

Ejemplo:

```bash
git config user.name
```

👉 Te devuelve el nombre configurado para tus commits en ese repo.

---

### 💡 Buenas prácticas

- Usa **`--global`** para datos personales (nombre, email) que aplicarás a todos tus repos.
- Usa **local (sin flag)** si en un repo necesitas credenciales distintas (ej. cuenta secundaria).
- Para depuración, `git config --list --show-origin` te muestra **qué archivo exacto** definió cada configuración.

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
