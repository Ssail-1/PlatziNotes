# 🔐 Gestión de Permisos en Archivos y Directorios (Linux)

Los permisos en Linux definen **quién puede leer, escribir o ejecutar** un archivo o directorio. Se dividen en tres niveles de usuarios:

* **u** → usuario (propietario)
* **g** → grupo
* **o** → otros (resto de usuarios/procesos)
* **a** → todos

Cada archivo/directorio tiene 3 tipos de permisos:

| Permiso   | Letra | Valor numérico | Significado                                           |
| --------- | ----- | -------------- | ----------------------------------------------------- |
| Lectura   | `r`   | 4              | Ver el contenido del archivo o listar directorio      |
| Escritura | `w`   | 2              | Modificar archivo o agregar/eliminar en un directorio |
| Ejecución | `x`   | 1              | Ejecutar archivo o acceder a un directorio            |

---

## 📌 Visualizar permisos

Comando:

```bash
ls -la # l -> long list ; a -> all
```

Ejemplo de salida:

```
-rwxrw-r--
```

Interpretación:

* **rwx** → el usuario puede leer, escribir y ejecutar.
* **rw-** → el grupo puede leer y escribir.
* **r--** → otros solo pueden leer.

---

## 📌 Cambiar permisos con `chmod`

### 🔹 Modo simbólico

```bash
chmod u+x script.sh   # Añade ejecución al usuario
chmod g-w archivo.txt # Quita escritura al grupo
chmod o+r archivo.txt # Da lectura a otros
```

### 🔹 Modo numérico

La suma binaria define los permisos:

* 4 = lectura (r)
* 2 = escritura (w)
* 1 = ejecución (x)

Ejemplos:

```bash
chmod 644 archivo.txt   # u=rw, g=r, o=r
chmod 755 script.sh     # u=rwx, g=rx, o=rx
chmod 700 privado.txt   # u=rwx, g=---, o=---
```

⚠️ Evita usar `777` (todos tienen todos los permisos). Es un riesgo de seguridad.

---

## 📌 Cambios recursivos

Aplicar permisos a todos los archivos dentro de un directorio:

```bash
chmod -R 755 carpeta/
```

⚠️ Úsalo con precaución, puede afectar archivos sensibles.

**Mejor práctica:** combinar con `find`:

```bash
find carpeta/ -type f -exec chmod 644 {} \;   # Solo archivos
find carpeta/ -type d -exec chmod 755 {} \;   # Solo directorios
```

---

## 📌 Comandos relacionados

| Comando                       | Uso                       |
| ----------------------------- | ------------------------- |
| `chmod`                       | Cambiar permisos          |
| `chown usuario:grupo archivo` | Cambiar propietario       |
| `chgrp grupo archivo`         | Cambiar grupo propietario |

---

## ⚡ Tips prácticos

* Mantén permisos al **mínimo necesario**.
* Para scripts compartidos, usa `755`.
* Para archivos de texto comunes, `644` es suficiente.
* Usa `chown` junto con `chmod` para gestionar permisos de forma completa.

---

![Ejemplo de asignacion de permisos 755 y 644](asignacionDePermisosLinux.png "Ejemplo de asignacion de permisos 755 y 644")

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
