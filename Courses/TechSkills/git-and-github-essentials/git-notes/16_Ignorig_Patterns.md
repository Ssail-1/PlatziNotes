
# 🚫 IGNORING PATTERNS

Sirve para **indicar a Git qué archivos o carpetas NO debe rastrear ni subir al repositorio**. Esto mantiene tu repo limpio y evita subir archivos temporales, secretos o dependencias pesadas.

![Static Badge](https://img.shields.io/badge/.gitignore-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-config--excludesfile-blue?logo=git)

---

- [🚫 IGNORING PATTERNS](#-ignoring-patterns)
  - [📜 `.gitignore` — Ignorar archivos en un repositorio](#-gitignore--ignorar-archivos-en-un-repositorio)
  - [🌍 Ignorar archivos de manera global](#-ignorar-archivos-de-manera-global)
  - [🧭 Flujo visual](#-flujo-visual)
  - [💡 Buenas prácticas](#-buenas-prácticas)

---

## 📜 `.gitignore` — Ignorar archivos en un repositorio

Crea un archivo llamado `.gitignore` en la raíz de tu proyecto con los patrones que quieras ignorar.

Ejemplo básico:

```gitignore
# Ignorar carpetas de logs
logs/

# Ignorar todos los archivos .notes
*.notes

# Ignorar cualquier carpeta con este patrón
pattern*/

# Ignorar Entornos virtuales
.venv
venv
```

📌 **Qué hace:**

- Todo lo listado ahí **no será rastreado ni agregado al staging**.
- Puedes poner comentarios con `#`.
- Puedes usar comodines `*` y `?` para patrones.

💡 **Tips:**

- Añade primero `.gitignore` antes de subir tu proyecto.
- Puedes crear varios `.gitignore` en subcarpetas (Git aplica el patrón de manera jerárquica).
- GitHub tiene plantillas para `.gitignore` comunes: [github.com/github/gitignore](https://github.com/github/gitignore)

---
---

## 🌍 Ignorar archivos de manera global

Puedes definir un archivo de exclusión global para todos tus repos:

```bash
git config --global core.excludesfile ~/.gitignore_global
```

Luego crea el archivo `~/.gitignore_global` y añade ahí patrones comunes para todos tus proyectos.

💬 **Ejemplo:**

```bash
# ~/.gitignore_global
.DS_Store
node_modules/
*.log
```

---

## 🧭 Flujo visual

```mermaid
flowchart LR
  A[Archivos en directorio] -->|git add| B[Staging area]
  A -.archivos en .gitignore.-X B
  B -->|git commit| C[Repositorio Git]
```

---

## 💡 Buenas prácticas

- Siempre crea tu `.gitignore` al inicio del proyecto.
- No subas archivos sensibles (contraseñas, llaves) nunca.
- Usa plantillas de `.gitignore` específicas para tu lenguaje o framework.
- Para quitar de Git un archivo que ya subiste pero ahora quieres ignorar:

  ```bash
  git rm --cached archivo_secreto.txt
  ```

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
