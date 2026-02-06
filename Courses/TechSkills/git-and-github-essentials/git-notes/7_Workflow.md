
# 🔁 Flujo de trabajo — Diagrama de secuencia

- [🔁 Flujo de trabajo — Diagrama de secuencia](#-flujo-de-trabajo--diagrama-de-secuencia)
  - [🧩 Desde el Directorio de trabajo hacia el Área de staging](#-desde-el-directorio-de-trabajo-hacia-el-área-de-staging)
  - [🔄 Desde el Staging hacia el Repositorio Git](#-desde-el-staging-hacia-el-repositorio-git)
  - [🧹 Regresando cambios (Reset)](#-regresando-cambios-reset)
  - [🗂️ Remover archivos del control de versiones](#️-remover-archivos-del-control-de-versiones)
  - [💡 Buenas prácticas](#-buenas-prácticas)
  - [🧭 Resumen visual del flujo](#-resumen-visual-del-flujo)

---

> [Clase 3: Control de Versiones con Git](https://platzi.com/cursos/gitgithub/comandos-basicos-de-git-add-commit-log/ "Curso de Git y GitHub - Comandos básicos y flujo de trabajo")
>
> ![Diagrama de Secuencia Directorio → Staging → Repositorio Git](../Imagenes/DiagramaSecuenciaDir_Staging_Git.png "Flujo visual entre directorio, área de staging y repositorio de Git")
>
> 🖼️ **Interpretación del diagrama**
> El flujo representa cómo los archivos viajan entre tres estados en Git:
>
> 1. **Directorio de trabajo (Working Directory)** → donde editas archivos.
> 2. **Área de preparación (Staging Area)** → donde decides qué cambios se confirmarán.
> 3. **Repositorio Git (.git)** → el historial de commits ya guardados.

---
---

## 🧩 Desde el Directorio de trabajo hacia el Área de staging

```bash
git add <archivo>
```

📌 Mueve los archivos modificados al área de preparación (*staging area*).
Permite decidir qué se incluirá en el próximo commit.

---
---

## 🔄 Desde el Staging hacia el Repositorio Git

```bash
git commit -m "Mensaje descriptivo"
```

📌 Confirma los archivos preparados y los guarda como un nuevo snapshot en el historial.

```bash
git commit --amend
```

📌 Modifica el último commit (puedes corregir el mensaje o añadir archivos que olvidaste).

---
---

## 🧹 Regresando cambios (Reset)

| Comando                                      | Acción                        | Resultado                                         |
| -------------------------------------------- | ----------------------------- | ------------------------------------------------- |
| `git reset --soft <commit>`                  | Mueve HEAD al commit indicado | Mantiene cambios en staging                       |
| `git reset --mixed <commit>` *(por defecto)* | Mueve HEAD                    | Los cambios vuelven al directorio de trabajo      |
| `git reset --hard <commit>` ⚠️               | Mueve HEAD y borra cambios    | Elimina todo lo que no está en el commit indicado |

💡 **HEAD** es un puntero que indica en qué commit estás trabajando actualmente.

---
---

## 🗂️ Remover archivos del control de versiones

```bash
git rm --cached <archivo>
```

📌 Quita el archivo del seguimiento de Git, **pero lo deja** en tu carpeta local.

```bash
git rm --force <archivo>
```

📌 Elimina el archivo tanto del control de versiones **como de tu carpeta local**.

---

## 💡 Buenas prácticas

- ⚠️ Evita usar `git reset --hard` a menos que estés 100 % seguro (borra cambios sin recuperación).
- Usa `git commit --amend` solo si **no has hecho push** del commit anterior (si ya lo subiste, mejor haz otro commit).
- Revisa tu historial antes de revertir con:

  ```bash
  git log --oneline
  ```

---

## 🧭 Resumen visual del flujo

```mermaid
flowchart LR
    A[Directorio de trabajo] -->|git add| B[Área de staging]
    B -->|git commit| C[Repositorio Git (.git)]
    C -->|git reset --soft| B
    C -->|git reset --mixed| A
    C -->|git reset --hard ⚠️| A
```

---

<p align="center">
  <a href="git-essentials-notes.md">🔝 <b>Volver al Índice</b> 🔝</a>
</p>

---
