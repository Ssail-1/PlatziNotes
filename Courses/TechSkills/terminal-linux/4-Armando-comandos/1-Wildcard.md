
# Wildcard

Las wildcards (comodines) en Linux son símbolos especiales que permiten hacer búsquedas o trabajar con patrones en archivos y directorios desde la terminal.  
Son caracteres que ***sustituyen*** una o varias ***partes del nombre de un archivo/directorio*** cuando usas comandos como `ls`, `cp`, `rm`, `find`, etc

| Wildcard  | Significado             | Ejemplo            | Coincidencias                              |
| --------- | ----------------------- | ------------------ | ------------------------------------------ |
| `*`       | Cero o más caracteres   | `ls *.txt`         | `notas.txt`, `data.txt`, `prueba.txt`      |
| `?`       | Exactamente un carácter | `ls file?.csv`     | `file1.csv`, `fileA.csv` (no `file10.csv`) |
| `[abc]`   | Un carácter de la lista | `ls file[123].txt` | `file1.txt`, `file2.txt`, `file3.txt`      |
| `[a-z]`   | Rango de caracteres     | `ls file[a-c].txt` | `filea.txt`, `fileb.txt`, `filec.txt`      |
| `[!abc]`  | Niega la lista          | `ls file[!1].txt`  | `file2.txt`, `file3.txt` (no `file1.txt`)  |
| `{x,y,z}` | Expansión de opciones   | `ls *.{jpg,png}`   | `foto.jpg`, `imagen.png`                   |

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
