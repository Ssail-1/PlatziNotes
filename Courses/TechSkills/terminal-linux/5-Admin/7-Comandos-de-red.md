# 🌐 Comandos de Red en la Terminal (Linux)

Los comandos de red permiten **verificar conectividad, diagnosticar problemas y comunicarse con servicios web** directamente desde la terminal.

---

## 📌 Consultar interfaces y direcciones IP

```bash
ip a
```

Muestra interfaces de red y direcciones IP.

* `lo` → loopback (127.0.0.1).
* `eth0` / `wlan0` → red cableada o WiFi.

👉 Reemplazo moderno de `ifconfig`.

---

## 📌 Revisar tabla de ruteo

```bash
ip r
```

Muestra la tabla de rutas del sistema:

* `default via` → puerta de enlace por defecto (generalmente tu router).
* Otras rutas locales → cómo el sistema envía paquetes a distintas redes.

---

## 📌 Probar conectividad con `ping`

```bash
ping www.google.com
```

Envía paquetes ICMP para verificar si un host responde.

* `Ctrl + C` → detener y mostrar resumen.
* `-c 5` → limitar número de intentos:

  ```bash
  ping -c 5 8.8.8.8
  ```

👉 Útil para ver si hay internet o si un servidor remoto está activo.

---

## 📌 Consultar nombres de dominio con `nslookup` / `dig`

* **nslookup**:

  ```bash
  nslookup www.google.com
  ```

* **dig** (más detallado, requiere instalación):

  ```bash
  dig www.google.com
  ```

👉 Útil para diagnosticar problemas de DNS.

---

## 📌 Descargar contenido con `curl`

Cliente HTTP muy flexible.

* Descargar HTML:

  ```bash
  curl www.google.com
  ```

* Guardar a archivo:

  ```bash
  curl www.google.com > index.html
  ```

* Probar API REST (ejemplo GET con JSON):

  ```bash
  curl -H "Accept: application/json" https://api.github.com/users/octocat
  ```

👉 Muy usado en desarrollo y testing de **APIs**.

---

## 📌 Descargar archivos con `wget`

```bash
wget https://example.com/archivo.zip
```

👉 Baja archivos directo a tu carpeta actual.

* Continuar descarga interrumpida:

  ```bash
  wget -c https://example.com/archivo.zip
  ```

---

## 📌 Analizar rutas con `traceroute`

```bash
traceroute www.google.com
```

Muestra el camino que siguen los paquetes hasta el destino.
👉 Identifica en qué “salto” se corta la conexión.

*(En Ubuntu instálalo con `sudo apt install traceroute`)*

---

## 📌 Escanear puertos con `nmap`

```bash
nmap localhost
```

* Ver puertos abiertos y servicios activos.
* Ejemplo:

  ```bash
  nmap -p 22,80,443 servidor.com
  ```

👉 Útil para seguridad y administración de servidores.

*(Instalación: `sudo apt install nmap`)*

---

## 📌 Otras utilidades prácticas

* **`netstat` (o `ss`)** → Ver conexiones activas y puertos en escucha:

  ```bash
  ss -tuln
  ```

* **`telnet` o `nc` (netcat)** → Probar conexión a un puerto:

  ```bash
  nc -zv github.com 443
  ```

  👉 Útil para comprobar si puedes conectar a GitHub vía HTTPS/SSH.

---

## 🚀 Resumen rápido

| Comando              | Uso principal                   |
| -------------------- | ------------------------------- |
| `ip a`               | Ver interfaces y direcciones IP |
| `ip r`               | Ver tabla de rutas              |
| `ping host`          | Probar conectividad             |
| `nslookup/dig`       | Resolver DNS                    |
| `curl`               | Peticiones HTTP / APIs          |
| `wget`               | Descargar archivos              |
| `traceroute`         | Ver camino de paquetes          |
| `nmap`               | Escanear puertos y servicios    |
| `ss -tuln`           | Conexiones y puertos en escucha |
| `nc -zv host puerto` | Probar conexión a un puerto     |

---

## 📌 Relación con Git/GitHub

Estos comandos ayudan a:

* Ver si tienes **internet y DNS funcional** (`ping`, `nslookup`).
* Probar si GitHub responde en sus puertos (`nc github.com 22` para SSH, `nc github.com 443` para HTTPS).
* Usar `curl` para probar la **API de GitHub** (ejemplo: usuarios, repositorios).
* Con `wget` puedes hasta bajar releases directamente.

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
