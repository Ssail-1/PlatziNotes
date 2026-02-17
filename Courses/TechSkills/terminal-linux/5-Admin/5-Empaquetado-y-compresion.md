
# 📦 Empaquetado y Compresión en Linux (TAR y GZIP)

En Linux, **empaquetar** y **comprimir** no son lo mismo:

* **Empaquetar (TAR)** → Junta varios archivos/carpetas en uno solo (`.tar`).
* **Comprimir (GZIP)** → Reduce el tamaño de un archivo (`.gz`).

👉 Muchas veces se combinan: **`.tar.gz`** → empaquetado + comprimido.

---

## 📌 Empaquetar con `tar`

```bash
tar -cvf textos.tar textos/
```

* **c** → create (crear).
* **v** → verbose (mostrar progreso).
* **f** → file (nombre del archivo resultante).

👉 Resultado: `textos.tar` contiene la carpeta `textos/`.

---

## 📌 Comprimir con `gzip`

```bash
gzip textos.tar
```

👉 Genera `textos.tar.gz` (más ligero).

---

## 📌 Desempaquetar y descomprimir

### Opción 1: en dos pasos

```bash
gunzip textos.tar.gz      # Descomprime → textos.tar
tar -xvf textos.tar       # Extrae carpeta textos/
```

### Opción 2: en un solo paso (más común)

```bash
tar -xzvf textos.tar.gz
```

* **x** → extract (extraer).
* **z** → gzip (descomprimir).
* **v** → verbose (mostrar).
* **f** → file (archivo de entrada).

⚠️ **Precaución:**
Antes de extraer (`tar -xvf` o `tar -xzvf`), **elimina la carpeta original** si aún existe en la misma ubicación con el mismo nombre, de lo contrario se mezclarán archivos o se sobrescribirán.

```bash
rm -r textos/
tar -xzvf textos.tar.gz
```

---

## 📌 Crear y extraer sin compresión

* Empaquetar sin comprimir:

  ```bash
  tar -cvf backup.tar carpeta/
  ```

* Extraer sin comprimir:

  ```bash
  tar -xvf backup.tar
  ```

---

## 📌 Extra tips

* Ver contenido sin extraer:

  ```bash
  tar -tvf archivo.tar
  ```

* Comprimir varias carpetas en un solo `.tar.gz`:

  ```bash
  tar -czvf proyecto.tar.gz carpeta1/ carpeta2/
  ```

* Extraer en una ruta específica:

  ```bash
  tar -xzvf proyecto.tar.gz -C /home/luis/descargas/
  ```

---

## 🚀 Resumen rápido

* **Crear TAR** → `tar -cvf archivo.tar carpeta/`
* **Comprimir TAR** → `gzip archivo.tar` → `archivo.tar.gz`
* **Extraer TAR** → `tar -xvf archivo.tar`
* **Extraer TAR.GZ** → `tar -xzvf archivo.tar.gz`
* **Ver contenido** → `tar -tvf archivo.tar`

---

* **Qué es cada uno**.
* **Comandos básicos**.
* **Tabla comparativa Vim vs Nano vs Vi vs Neovim**.
* **Consejo práctico** sobre cuál aprender según tu contexto.

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
