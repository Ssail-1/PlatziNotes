
# ⚙️ Manejo y Administración de Procesos en Linux

En Linux, cada programa en ejecución es un **proceso**.
Cada proceso tiene un **PID (Process ID)**, estado, usuario propietario y recursos asignados.
Saber **cómo ejecutarlos, listarlos, monitorearlos y matarlos** es fundamental para trabajar en la terminal.

---

## 🔹 Foreground vs Background

* **Foreground** → El proceso ocupa la terminal hasta que termina.
* **Background** → Corre “tras bambalinas” y devuelve el control de la terminal.

Ejemplos:

```bash
sleep 1000        # foreground (bloquea la terminal)
sleep 1000 &      # background (devuelve control de inmediato)
```

---

## 🔹 Control de procesos interactivos

| Comando         | Acción                                              |
| --------------- | --------------------------------------------------- |
| `Ctrl + C`      | Finaliza un proceso en foreground                   |
| `Ctrl + Z`      | Suspende (pause) el proceso en foreground           |
| `jobs`          | Lista procesos en background con su ID (`%1`, `%2`) |
| `fg %ID`        | Trae un proceso suspendido al foreground            |
| `bg %ID`        | Reanuda un proceso en background                    |
| `kill -STOP %1` | Pausa un proceso en background usando su ID         |
| `kill -CONT %1` | Reanuda un proceso pausado en background            |

---

## 🔹 Visualización de procesos con `ps`

El comando **`ps`** (*process status*) muestra una **fotografía** de los procesos activos.
Por sí solo (`ps`), solo enseña procesos de la **sesión actual**.

### Variantes comunes

| Comando  | Uso                                                 |                             |
| -------- | --------------------------------------------------- | --------------------------- |
| `ps`     | Procesos actuales de la terminal activa             |                             |
| `ps -e`  | Todos los procesos del sistema                      |                             |
| `ps -f`  | Formato completo (PID, PPID, tiempo, etc.)          |                             |
| `ps aux` | Lista completa de procesos con detalles (muy usado) |                             |
| \`ps aux | less\`                                              | Lista completa, paginada    |
| \`ps aux | grep -i firefox\`                                   | Filtrar procesos con `grep` |

### ¿Qué significa `aux`?

* **a** → all → muestra procesos de todos los usuarios.
* **u** → user-oriented → incluye el usuario propietario en la lista.
* **x** → muestra procesos que no tienen terminal asociada (ej: servicios).

### Columnas importantes en `ps aux`

| Columna     | Significado                             |
| ----------- | --------------------------------------- |
| **USER**    | Usuario dueño del proceso               |
| **PID**     | Identificador único del proceso         |
| **%CPU**    | Porcentaje de CPU usado                 |
| **%MEM**    | Porcentaje de memoria usada             |
| **VSZ**     | Memoria virtual consumida (KB)          |
| **RSS**     | Memoria física real usada (KB)          |
| **TTY**     | Terminal asociada (o `?` si no tiene)   |
| **STAT**    | Estado del proceso (`R`, `S`, `T`, `Z`) |
| **START**   | Hora o fecha en que inició el proceso   |
| **TIME**    | Tiempo de CPU consumido                 |
| **COMMAND** | El comando que originó el proceso       |

👉 Estados comunes en **STAT**:

* **R** → Running (ejecutando).
* **S** → Sleeping (en espera).
* **T** → Stopped (detenido).
* **Z** → Zombie (terminó pero no liberó recursos).

---

## 🔹 Monitoreo en tiempo real con `top`

El comando `top` muestra procesos **actualizándose en vivo**.

Datos clave:

* **PID, USER, PR/NI, %CPU, %MEM, TIME+, COMMAND**.
* **NI (Nice Value)** → prioridad del proceso.

  * Valores negativos = mayor prioridad.
  * Valores positivos = menor prioridad.

Atajos en `top`:

* `q` → salir.
* `k` → matar proceso (pide PID).
* `h` → ayuda.

---

## 🔹 Htop: monitor avanzado

**htop** es una versión mejorada de `top`.

### Instalación

```bash
sudo apt install htop
```

### Ventajas

* Interfaz gráfica en consola.
* Barras de CPU y memoria.
* Navegación con flechas.
* **F3** → buscar procesos.
* **F5** → ver árbol de procesos.
* **F9** → matar proceso.

👉 En macOS:

```bash
brew install htop
```

---

## 🔹 Finalizar procesos con `kill`

Permite terminar o enviar señales a un proceso usando su **PID**.

### Flujo básico

1. Encontrar PID con `ps aux` o `top`.
2. Enviar señal con `kill`.

Ejemplos:

```bash
kill 1234         # Termina suavemente (SIGTERM)
kill -9 1234      # Mata forzado (SIGKILL)
```

### Señales comunes

| Señal     | Comando                            | Acción                            |
| --------- | ---------------------------------- | --------------------------------- |
| `SIGTERM` | `kill PID`                         | Terminar proceso (suave, default) |
| `SIGKILL` | `kill -9 PID`                      | Matar proceso de inmediato        |
| `SIGSTOP` | `kill -STOP PID` o `kill -STOP %1` | Pausar                            |
| `SIGCONT` | `kill -CONT PID` o `kill -CONT %1` | Reanudar                          |

---

## 🚀 Ejemplo completo

```bash
ps aux | less             # Ver todos los procesos
ps aux | grep firefox     # Buscar PID de Firefox
kill -9 4567              # Matar Firefox con su PID
top                       # Monitorear en tiempo real
htop                      # Monitor gráfico avanzado
```

---

## 🗂️ Guía rápida: ¿Qué hacer si…?

* 🔎 **Ver procesos** → `ps aux` / `top` / `htop`
* 🚫 **Detener rápido** → `Ctrl + C`
* ⏸️ **Pausar sin matar** → `Ctrl + Z` o `kill -STOP %PID`
* ▶️ **Reanudar** → `fg %ID`, `bg %ID`, o `kill -CONT %PID`
* ❌ **Matar** → `kill PID` / `kill -9 PID`
* 📊 **Monitorear consumo** → `top` o `htop`

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
