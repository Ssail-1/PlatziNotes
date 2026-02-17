
# ⚙️ Operadores de Control en Bash

Los operadores de control permiten ejecutar comandos en **secuencia**, **paralelo**, o **condicionalmente**, dependiendo del resultado del anterior.

---

## 📌 Operadores básicos

| Operador | Uso                                                                    | Ejemplo                   | Explicación                                                        |              |   |                    |                                  |
| -------- | ---------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------ | ------------ | - | ------------------ | -------------------------------- |
| `;`      | Ejecutar comandos en secuencia (independiente del resultado)           | `ls; pwd; date`           | Se ejecutan uno tras otro                                          |              |   |                    |                                  |
| `&&`     | Ejecutar siguiente **solo si el anterior fue exitoso** (`exit code 0`) | `mkdir nueva && cd nueva` | Solo entra a `nueva` si se creó bien|
| `double pipe`| Ejecutar siguiente **solo si el anterior falló** (`exit code ≠ 0`) | `cd carpeta` **double pipe** `echo "No existe"` | Muestra mensaje si falla el `cd` |
| `&`      | Ejecutar en **segundo plano**                                          | `sleep 60 &`              | Ejecuta `sleep` sin bloquear la terminal                           |              |   |                    |                                  |


## 🚀 Combinaciones útiles

* Crear carpeta y entrar en ella (seguro):

  ```bash
  mkdir proyecto && cd proyecto
  ```
* Intentar entrar en carpeta, y si no existe, mostrar error:

  ```bash
  cd carpeta || echo "La carpeta no existe"
  ```
* Ejecutar varios comandos en cadena:

  ```bash
  ls; whoami; date
  ```
* Lanzar procesos en paralelo:

  ```bash
  comando1 & comando2 &
  ```

---

👉 Clave para recordar:

* **`;`** = secuencia simple
* **`&&`** = ejecuta si **éxito**
* **`||`** = ejecuta si **falla**
* **`&`** = segundo plano

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
