
# 🔄 SHARE & UPDATE

Permite conectar tu repositorio local con uno remoto (por ejemplo, GitHub), descargar actualizaciones y subir tus cambios.

![Static Badge](https://img.shields.io/badge/git-remote-grey?logo=git)
![Static Badge](https://img.shields.io/badge/git-fetch-blue?logo=git)
![Static Badge](https://img.shields.io/badge/git-pull-yellow?logo=git)
![Static Badge](https://img.shields.io/badge/git-push-green?logo=git)

---

- [🔄 SHARE \& UPDATE](#-share--update)
  - [🌍 `git remote add` — Conectar un repositorio remoto](#-git-remote-add--conectar-un-repositorio-remoto)
  - [Verificando el origen del repo](#verificando-el-origen-del-repo)
  - [📥 `git fetch` — Descargar sin fusionar](#-git-fetch--descargar-sin-fusionar)
  - [⬇️ `git pull` — Descargar y fusionar](#️-git-pull--descargar-y-fusionar)
  - [⬆️ `git push` — Subir tus cambios al remoto](#️-git-push--subir-tus-cambios-al-remoto)
  - [🔁 Flujo visual de sincronización](#-flujo-visual-de-sincronización)
  - [💡 Buenas prácticas](#-buenas-prácticas)

---

## 🌍 `git remote add` — Conectar un repositorio remoto

```bash
git remote add origin git@github.com:usuario/repositorio.git
```

📌 **Qué hace:**

- Vincula tu repositorio local con uno remoto.
- `origin` es un alias (nombre corto) que representa la URL del remoto.

💬 **Explicación de la sintaxis:**

| Parte                                    | Significado                                    |
| ---------------------------------------- | ---------------------------------------------- |
| `remote`                                 | Gestiona repositorios remotos.                 |
| `add`                                    | Agrega un nuevo remoto.                        |
| `origin`                                 | Nombre que damos al remoto (puedes usar otro). |
| `git@github.com:usuario/repositorio.git` | Dirección SSH del repo remoto.                 |

---
---

## Verificando el origen del repo

```bash
git remote -v
```

📍 Muestra las URLs asociadas a cada remoto (para `fetch` y `push`).

---
---

## 📥 `git fetch` — Descargar sin fusionar

```bash
git fetch origin
```

📌 **Qué hace:**

- Descarga los commits, ramas y etiquetas del remoto.
- No cambia tus archivos locales ni tus ramas activas.
- Ideal para **ver qué hay de nuevo antes de fusionar**.

💡 **Ejemplo práctico:**

```bash
git fetch origin main
git log main..origin/main --oneline
```

👉 Te muestra los commits que existen en GitHub y aún no tienes localmente.

---
---

## ⬇️ `git pull` — Descargar y fusionar

```bash
git pull origin main
```

📌 **Qué hace:**

- Ejecuta **`fetch + merge`** automáticamente.
- Descarga los cambios remotos y los integra con tu rama actual.

💬 **Desglose del comando:**

| Parte    | Significado                               |
| -------- | ----------------------------------------- |
| `origin` | Remoto desde donde obtendrás los cambios. |
| `main`   | Rama que se actualizará.                  |

💡 **Ejemplo de uso típico:**
Cuando alguien más hizo commits en el repo remoto y tú quieres tenerlos localmente antes de seguir trabajando.

---
---

## ⬆️ `git push` — Subir tus cambios al remoto

```bash
git push origin feature/git-notes-update
```

📌 **Qué hace:**

- Envía los commits locales al repositorio remoto.
- Crea la rama en GitHub si aún no existe.

💬 **Desglose del comando:**

| Parte                      | Significado              |
| -------------------------- | ------------------------ |
| `push`                     | Subir commits al remoto. |
| `origin`                   | Remoto de destino.       |
| `feature/git-notes-update` | Rama que subirás.        |

💡 **Atajos comunes:**

```bash
git push -u origin nombre-rama
```

- `-u` = *--set-upstream*
  Configura la rama local para que recuerde su remoto y su rama de destino.
  Así después podrás usar simplemente:

  ```bash
  git push
  git pull
  ```

---
---

## 🔁 Flujo visual de sincronización

```mermaid
flowchart LR
  A[Repositorio remoto (GitHub)] -->|git fetch| B[Local]
  B -->|git merge| C[Actualización local]
  C -->|git push| A
```

---

## 💡 Buenas prácticas

- Antes de hacer `push`, **siempre haz un `pull`** para evitar conflictos.
- Usa `git fetch` para revisar cambios sin alterar tu rama.
- Mantén ramas limpias y sincronizadas: elimina las que ya fusionaste.
- Usa SSH en lugar de HTTPS para autenticación más segura y fluida.

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
