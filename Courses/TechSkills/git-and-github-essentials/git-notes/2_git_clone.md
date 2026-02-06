# 📥 `git clone [url]`

Clona (descarga) un repositorio existente desde una URL remota.

![Static Badge](https://img.shields.io/badge/git-clone-green?logo=github)

---

```bash
git clone git@github.com:usuario/repositorio.git
```

📌 **Qué hace:**

- Copia todos los archivos, ramas e historial de commits.
- Te da una copia idéntica para trabajar en tu máquina.

🛠️ **Parámetros comunes:**

- `[url]` → Dirección del repositorio (HTTPS o SSH).
- `[directorio]` *(opcional)* → Nombre de la carpeta destino.

Ejemplo:

```bash
git clone git@github.com:Ssail-1/PlatziNotes.git mi-carpeta-local
```

👉 Esto clona el repo en una carpeta llamada `mi-carpeta-local` en lugar de usar el nombre original.

---

### 📖 Resumen visual con Mermaid

```mermaid
flowchart TD
  A[Directorio vacío] --> B[Repositorio Git (.git)] C[Repositorio remoto en GitHub] --> D[Copia local idéntica]
```

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
