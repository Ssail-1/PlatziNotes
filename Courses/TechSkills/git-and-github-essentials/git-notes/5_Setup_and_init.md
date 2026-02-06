
# ⚙️ Setup "Configuración Inicial"

Configura tu identidad y opciones básicas de Git para que todos tus commits estén bien registrados.

![Static Badge](https://img.shields.io/badge/git-config-blue?logo=git)
![Static Badge](https://img.shields.io/badge/editor-vim%2Femacs-green)

---

- [⚙️ Setup "Configuración Inicial"](#️-setup-configuración-inicial)
  - [👤 Configurar identidad del usuario](#-configurar-identidad-del-usuario)
  - [🎨 Colores en Git](#-colores-en-git)
  - [📝 Ver configuración actual](#-ver-configuración-actual)
  - [🖊️ Editor por defecto](#️-editor-por-defecto)

---

## 👤 Configurar identidad del usuario

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

- `user.name` → el nombre que aparecerá en los commits.
- `user.email` → el correo vinculado (debe coincidir con el de tu cuenta GitHub si quieres que aparezcan tus contribuciones).

---
---

## 🎨 Colores en Git

```bash
git config --global color.ui auto
```

📌 **Qué hace:**

- `color.ui` controla si Git usa colores en la terminal.
- `auto` → activa colores cuando la salida es una terminal (lo más práctico).

👉 Esto mejora la lectura de `git status`, `git diff`, etc.

---
---

## 📝 Ver configuración actual

```bash
git config --list
```

👉 Lista todas las configuraciones activas (se mezclan system, global y local).

```bash
git config user.name
```

👉 Devuelve el valor de una clave específica.

---
---

## 🖊️ Editor por defecto

Git usa un editor de texto para escribir mensajes de commit si no pasas `-m`.

Por defecto:

- En Linux/Mac suele ser **Vim**.
- Puedes cambiarlo, por ejemplo a **Emacs** o **Nano**:

```bash
git config --global core.editor emacs
```

```bash
git config --global core.editor nano
```

---

💡 **Buenas prácticas**

- Configura siempre tu nombre y correo globales al empezar en una máquina.
- Usa un editor que conozcas (si no te gusta Vim, cámbialo).
- Revisa con `git config --list --show-origin` para ver qué archivo estableció cada valor.

---

✅ Con el entorno queda listo para empezar a trabajar en cualquier repo con la identidad clara y sin sorpresas de editor.

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
