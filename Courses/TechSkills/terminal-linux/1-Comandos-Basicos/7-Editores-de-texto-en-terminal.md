
# 📝 Editores de texto en la terminal: Vim y Nano

Editar archivos desde la terminal es útil en servidores o sistemas sin interfaz gráfica. Los editores más comunes son **Vim** y **Nano**.

---

## 📌 Vim

Vim (*Vi IMproved*) es un editor **muy potente y configurable**, pero con una curva de aprendizaje más complicada.

Abrir archivo:

```bash
vim archivo.txt
```

### Modos de Vim

* **Modo comando** (por defecto) → navegar, borrar, guardar.
* **Modo inserción** → escribir texto (`i` para entrar, `ESC` para salir).

### Comandos básicos

| Comando | Acción                   |
| ------- | ------------------------ |
| `i`     | Entrar en modo inserción |
| `ESC`   | Volver al modo comando   |
| `:w`    | Guardar cambios          |
| `:q`    | Salir                    |
| `:wq`   | Guardar y salir          |
| `:q!`   | Salir sin guardar        |
| `dd`    | Eliminar línea actual    |
| `gg`    | Ir al inicio del archivo |
| `:n`    | Ir a la línea `n`        |

---

## 📌 Nano

Nano es un editor **sencillo y directo**, ideal para principiantes.

Abrir archivo:

```bash
nano archivo.txt
```

### Comandos básicos

| Comando    | Acción                   |
| ---------- | ------------------------ |
| `Ctrl + O` | Guardar cambios          |
| `Ctrl + X` | Salir                    |
| `Ctrl + K` | Cortar línea             |
| `Ctrl + U` | Pegar                    |
| `Ctrl + G` | Ayuda / menú de comandos |

👉 La gran ventaja: en la parte inferior de Nano siempre ves los atajos.

---

## 📌 Tabla comparativa

| Editor     | Características                                | Ventajas                                        | Desventajas                         | Uso común                                  |
| ---------- | ---------------------------------------------- | ----------------------------------------------- | ----------------------------------- | ------------------------------------------ |
| **Vi**     | Editor clásico, muy básico                     | Siempre está instalado en cualquier Linux/Unix  | Poco amigable, comandos limitados   | Uso mínimo en emergencias                  |
| **Vim**    | Versión mejorada de Vi, altamente configurable | Rápido, potente, con plugins y comunidad enorme | Difícil de aprender, curva empinada | Desarrolladores, admins avanzados          |
| **Neovim** | Fork moderno de Vim                            | Más integración con IDEs, soporte extendido     | No siempre instalado por defecto    | Desarrolladores que buscan personalización |
| **Nano**   | Simple y directo                               | Fácil de usar, comandos visibles en pantalla    | Menos potente, menos personalizable | Usuarios principiantes, ediciones rápidas  |

---

## 📌 ¿Cuál aprender?

* **Nano** → si quieres algo rápido, simple y siempre comprensible.
* **Vim** → si te interesa velocidad, automatización, plugins y trabajar como pro en servidores (pero prepárate para aprender más).
* **Vim** → lo mínimo que debes saber porque **siempre viene preinstalado** en todos los sistemas Unix/Linux.
* **Neovim** → si algún día quieres un Vim más moderno, pero no es obligatorio.

👉 En la práctica: **Nano es el más fácil y más parecido a editores simples preinstalados** (como Notepad).
👉 **Vim es el más usado en entornos profesionales**, aunque Nano es más común entre principiantes.

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
