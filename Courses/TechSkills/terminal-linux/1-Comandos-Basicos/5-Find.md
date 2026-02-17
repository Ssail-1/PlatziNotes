
# Find

Sirve para buscar archivos y directorios con diferentes criterios: nombre, extensión, fecha, tamaño, permisos, dueño, etc.

**Sintaxis general**  
`find [ruta] [opciones] [expresión]`

## Opciones comunes

| Flag | Descripción |
| ---- | ----------- |
|-name:| Busca por nombre de archivo (acepta wildcards)|
|-type:| Busca por tipo (f=archivo, d=directorio)|
|-size:| Busca por tamaño|
|-mtime:| Busca por tiempo de modificación|
|-user: |Busca por propietario|
|-exec: |Ejecuta un comando sobre los archivos encontrados|
|-not, -and, -or| Operadores lógicos|

## Casos de uso comunes

+ Buscar archivos por nombre: `find /home -name "*.txt"`
+ Buscar directorios: `find /var -type d -name "log*"`
+ Buscar archivos modificados en los últimos 7 días: `find /home -mtime -7`
+ Buscar archivos grandes: `find /var -size +10M`
+ Ejecutar comando en archivos encontrados: `find . -name "*.tmp" -exec rm {} \\;`
+ Buscar archivos con permisos específicos: `find /etc -perm 644`

| Comando | Acción |
| ------- | ------ |
| `find . -name "archivo.txt"` | Buscar archivo exacto |
| `find . -name "*.txt"` | Buscar todos los `.txt` |
| `find . -iname "*.txt"` | Buscar ignorando mayúsculas/minúsculas |
| `find /home -name "data*"` | Buscar archivos que empiezan con `data` |
| `find . -type d -name "*"` | Busca todos los directiorios a partir de la ubicación actual |
| `find . -type f -size +1M` | Encuentra los archivos que pesen mas de un megabyte |

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
