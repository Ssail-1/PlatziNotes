
# 📦 Gestión de Paquetes con APT (Debian/Ubuntu)

**APT (Advanced Package Tool)** es el administrador de paquetes en distribuciones basadas en **Debian** como Ubuntu. Permite instalar, actualizar, buscar y eliminar software fácilmente desde la terminal.

---

## 📌 Comandos básicos de APT

| Comando                           | Acción                                                    |
| --------------------------------- | --------------------------------------------------------- |
| `sudo apt update`                 | Actualiza la lista de paquetes disponibles (repositorios) |
| `sudo apt upgrade`                | Actualiza los paquetes instalados a la última versión     |
| `sudo apt install nombre-paquete` | Instala un paquete                                        |
| `sudo apt remove nombre-paquete`  | Elimina un paquete (mantiene archivos de config)          |
| `sudo apt purge nombre-paquete`   | Elimina un paquete y sus configuraciones                  |
| `sudo apt show nombre-paquete`    | Muestra info detallada de un paquete                      |
| `apt list --installed`            | Lista paquetes instalados                                 |
| `apt list --upgradeable`          | Muestra qué paquetes tienen actualización disponible      |
| `sudo apt autoremove`             | Elimina dependencias que ya no se usan                    |
| `sudo apt clean`                  | Limpia la caché de paquetes descargados                   |

---

## 📌 Flujo de actualización recomendado

1. **Actualizar lista de paquetes**

   ```bash
   sudo apt update
   ```

2. **Actualizar paquetes instalados**

   ```bash
   sudo apt upgrade
   ```

3. (Opcional) **Eliminar dependencias obsoletas**

   ```bash
   sudo apt autoremove
   ```

---

## 📌 Instalación de paquetes

Ejemplo: instalar **Neofetch** (muestra info del sistema):

```bash
sudo apt install neofetch
neofetch
```

👉 Una vez instalado, el programa queda disponible como comando.

---

## 📌 Eliminación de paquetes

* Remover solo el paquete:

  ```bash
  sudo apt remove nombre-paquete
  ```

* Remover con archivos de configuración:

  ```bash
  sudo apt purge nombre-paquete
  ```

---

## 📌 Diferencias con otros manejadores

* **Debian/Ubuntu** → `apt`
* **Red Hat/Fedora** → `dnf` o `yum`
* **Arch Linux** → `pacman`
* **macOS** → No tiene nativo, pero se usa **Homebrew**.

---

## ⚡ Tips prácticos

* Siempre usa `sudo` con `apt`.
* Después de instalar o borrar mucho software, limpia espacio:

  ```bash
  sudo apt autoremove && sudo apt clean
  ```

* Puedes combinar instalación múltiple:

  ```bash
  sudo apt install git curl htop
  ```

* Usa `apt-cache search palabra` (o `apt search palabra`) para buscar paquetes.

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
