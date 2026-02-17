
# Grep

El comando grep (Global Regular Expression Print) es una herramienta poderosa para buscar patrones de texto en archivos.

**Sintaxis básica:** 
> `grep [opciones] patrón [archivo(s)]`

## Opciones comunes

| Flag | Descripción |
| ---- | ----------- |
|-i |Ignora mayúsculas/minúsculas|
|-r |Búsqueda recursiva en directorios|
|-l |Solo muestra nombres de archivos (no el contenido)|
|-n |Muestra números de línea|
|-v |Muestra líneas que NO coinciden con el patrón |
|-c |Cuenta el número de coincidencias |
|-A n|Muestra n líneas después de la coincidencia |
|-B n| Muestra n líneas antes de la coincidencia |

## Casos de uso comunes

+ Búsqueda de texto en archivos: `grep "error" archivo.log`
+ Búsqueda recursiva en directorios: `grep -r "función" /ruta/proyecto`
+ Filtrar salida de otros comandos: `ls -la | grep ".txt"`
+ Contar ocurrencias: `grep -c "warning" archivo.log`

| Comando                    | Acción                  |
| -------------------------- | ----------------------- |
| `grep "texto" archivo`     | Buscar texto            |
| `grep -i "texto"`          | Ignorar mayúsculas      |
| `grep -n "texto"`          | Mostrar número de línea |
| `grep -r "texto" carpeta/` | Buscar en toda carpeta  |

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
