# 🖥️ Tmux – Multiplexor de Terminales

**Tmux** (*Terminal Multiplexer*) permite tener **múltiples terminales dentro de una sola ventana**, organizadas en paneles o pestañas (ventanas).
Ideal para trabajar en servidores remotos o cuando necesitas ejecutar varios procesos a la vez.

---

## 📌 Instalación

* En Linux (Debian/Ubuntu):

  ```bash
  sudo apt install tmux
  ```
  
* En macOS (Homebrew):

  ```bash
  brew install tmux
  ```

---

## 📌 Concepto clave: el **prefijo**

Todas las acciones en Tmux comienzan con el **prefijo**:

```s
Ctrl + b
```

(Lo presionas, lo sueltas, y luego das la siguiente tecla de comando).

---

## 📌 Paneles

| Acción                | Combinación        |
| --------------------- | ------------------ |
| Dividir vertical      | `Ctrl+b %`         |
| Dividir horizontal    | `Ctrl+b "`         |
| Cerrar panel          | `exit` o `Ctrl+d`  |
| Moverse entre paneles | `Ctrl+b` + flechas |

---

## 📌 Ventanas

| Acción             | Combinación                |
| ------------------ | -------------------------- |
| Nueva ventana      | `Ctrl+b c`                 |
| Cambiar de ventana | `Ctrl+b` + número (0,1,2…) |
| Renombrar ventana  | `Ctrl+b ,`                 |

---

## 📌 Sesiones

Una de las grandes ventajas de Tmux es que las sesiones **se mantienen aunque cierres la terminal**.

| Acción                        | Comando                       |
| ----------------------------- | ----------------------------- |
| Listar sesiones activas       | `tmux ls`                     |
| Crear nueva sesión            | `tmux new -s nombre`          |
| Adjuntarse a sesión existente | `tmux attach -t nombre`       |
| Detach (salir sin cerrar)     | `Ctrl+b d`                    |
| Eliminar sesión               | `tmux kill-session -t nombre` |

👉 Ejemplo práctico:

```bash
tmux new -s trabajo      # Crear sesión
Ctrl+b %                 # Panel vertical
Ctrl+b "                 # Panel horizontal
Ctrl+b d                 # Salir sin cerrar
tmux attach -t trabajo   # Reanudar
```

---

## 📌 Flujo rápido de uso

1. Inicia una sesión:

   ```bash
   tmux
   ```

2. Divide paneles (`Ctrl+b %` o `Ctrl+b "`).
3. Abre más ventanas (`Ctrl+b c`).
4. Renombra para organizar (`Ctrl+b ,`).
5. Si debes cerrar la terminal → `Ctrl+b d` (detach).
6. Vuelve luego con:

   ```bash
   tmux attach
   ```

---

## 🚀 Resumen práctico

* **Paneles** → Divide y organiza (vertical `%`, horizontal `"`).
* **Ventanas** → Como pestañas (`c`, número, `,`).
* **Sesiones** → Guardan tu trabajo aunque cierres terminal.
* **Prefijo** = `Ctrl+b`.

---

👉 Con Tmux ya no necesitas abrir 10 terminales diferentes, lo controlas todo en una sola.

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
