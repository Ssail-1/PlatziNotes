
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

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
