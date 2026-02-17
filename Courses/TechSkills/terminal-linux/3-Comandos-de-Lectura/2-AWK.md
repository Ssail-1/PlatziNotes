
# AWK

>Procesador de texto orientado a columnas  

**awk** es un minilenguaje de programación dentro de la terminal, hecho para procesar y analizar texto en columnas. Usada con `.csv`, `.log` y cualquier tipo de archivo tabular.  

Ejemplos...

| Comando | Acción |
| ------- | ------ |
| `awk -F, '{print $1}' archivo.csv` | Imprime la primera columna |
| `awk -F, '$3 > 25 {print $2, $3}' archivo.csv` | Muestra Mostrar primera columna (CSV) |
| `awk -F, '{print $1,$2}' archivo.csv`                     | Mostrar columnas 1 y 2 |
| `awk -F, '$3 > 25 {print $2,$3}' archivo.csv`             | Filtrar por condición |
| `awk 'END {print NR}' archivo`                            | Contar líneas |
| `awk -F, 'NR>1 {s+=$3} END {print s/(NR-1)}' archivo.csv` | Promedio de columna numérica |

* usa IA para saber utilizarla.

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
