
# 🔀 Redirecciones en la terminal Linux

En Linux, la **entrada (stdin)**, la **salida (stdout)** y los **errores (stderr)** se pueden redirigir con operadores.

* **`0` → stdin (entrada estándar)**
* **`1` → stdout (salida estándar, por defecto)**
* **`2` → stderr (errores estándar)**

---

## 📌 Operadores básicos

| Operador | Uso                                | Ejemplo                              | Explicación                        |        |                                              |
| -------- | ---------------------------------- | ------------------------------------ | ---------------------------------- | ------ | -------------------------------------------- |
| `>`      | Redirigir salida (sobrescribe)     | `ls > lista.txt`                     | Guarda salida en `lista.txt`       |        |                                              |
| `>>`     | Redirigir salida (agrega al final) | `echo "hola" >> lista.txt`           | Añade texto sin borrar lo anterior |        |                                              |
| `2>`     | Redirigir solo errores             | `ls carpetaInexistente 2> error.log` | Guarda los errores en `error.log`  |        |                                              |
| `&>`     | Redirigir salida y errores         | `comando &> salida.log`              | Todo va a `salida.log`             |        |                                              |
| `2>&1`   | Unir errores en la salida normal   | `comando > salida.log 2>&1`          | Guarda salida + errores juntos     |        |                                              |
| `<`      | Usar un archivo como entrada       | `sort < datos.txt`                   | Ordena el contenido de `datos.txt` |        |                                              |
| \`       | \` (pipe)                          | Conectar comandos (output → input)   | \`ls                               | less\` | Usa la salida de `ls` como entrada en `less` |

---

## 🐮 Ejemplo divertido con `lolcat` y `cowsay`

```bash
echo "Linux es poder" | cowsay | lolcat
```

👉 `echo` manda texto → `cowsay` lo convierte en vaca parlante → `lolcat` lo colorea 🌈.
Esto es el **pipe (`|`)** en acción.

---

## 🚀 Casos prácticos

* Guardar solo errores de un script:

  ```bash
  ./script.sh 2> errores.log
  ```

* Guardar salida y errores juntos:

  ```bash
  ./script.sh > salida.log 2>&1
  ```

* Filtrar y mostrar con paginador:

  ```bash
  dmesg | grep error | less
  ```

* Añadir al final de un log sin borrar lo anterior:

  ```bash
  echo "Nueva entrada" >> registro.log
  ```

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
