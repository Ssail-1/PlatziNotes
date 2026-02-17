
# Como identificar que es exactamente un comando

En Linux, los comandos pueden pertenecer a distintas categorías:

* **Binarios compilados** → Programas creados en lenguajes como C o C++.
* **Scripts** → Archivos ejecutables en lenguajes como Shell, Python o JavaScript.
* **Alias** → Comandos personalizados definidos por el usuario.
* **Utilidades del sistema** → Herramientas esenciales que vienen con el SO.
---

📌 Comandos útiles para identificar comandos

| Comando           | Uso principal                                                         | Ejemplo         | Salida esperada                               |
| ----------------- | --------------------------------------------------------------------- | --------------- | --------------------------------------------- |
| `type comando`    | Indica si un comando es alias, función, palabra reservada o binario   | `type ls`       | `ls is /usr/bin/ls`                           |
| `which comando`   | Muestra la ruta del ejecutable que se ejecutará                       | `which python3` | `/usr/bin/python3`                            |
| `whereis comando` | Muestra todas las ubicaciones relacionadas (binarios, manpages, etc.) | `whereis ls`    | `ls: /usr/bin/ls /usr/share/man/man1/ls.1.gz` |
| `whatis comando`  | Devuelve una breve descripción del comando                            | `whatis grep`   | `grep (1) - print lines matching a pattern`   |


🚀 Ejemplo práctico
---
```bash
type grep
which grep
whereis grep
whatis grep
```

Salida típica:

```
grep is /usr/bin/grep
/usr/bin/grep
grep: /usr/bin/grep /usr/share/man/man1/grep.1.gz
grep (1) - print lines matching a pattern
```

---

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
