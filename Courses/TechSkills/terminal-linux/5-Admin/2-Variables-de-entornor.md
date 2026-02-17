# 🌍 Variables de Entorno en Linux

Las **variables de entorno** almacenan información clave del sistema y la shell. Permiten configurar cómo se ejecutan programas y comandos.

Se acceden usando el signo **`$`** seguido del nombre:

```bash
echo $SHELL   # Muestra la shell actual (ej: /bin/bash)
```

---

## 📌 Variables importantes

| Variable            | Significado                                    |
| ------------------- | ---------------------------------------------- |
| `PWD`               | Ruta del directorio actual                     |
| `PATH`              | Directorios donde el sistema busca ejecutables |
| `SHELL`             | Ruta del intérprete en uso                     |
| `LANG` o `LANGUAGE` | Idioma y codificación del sistema              |
| `HOME`              | Directorio personal del usuario                |

---

## 📌 Crear variables de entorno

### 🔹 Variables temporales (solo duran la sesión)

```bash
MYVAR="Hola Linux"
echo $MYVAR     # → Hola Linux
```

### 🔹 Variables globales (disponibles para otros procesos)

```bash
export MYVAR="Hola Linux"
```

⚠️ Estas desaparecen al cerrar la terminal.

---

## 📌 Variables permanentes

Para que se carguen en cada sesión, debes añadirlas al archivo de configuración de tu shell:

### En Bash

```bash
echo 'export MYVAR="Hola Linux"' >> ~/.bashrc
source ~/.bashrc
```

### En Zsh

```bash
echo 'export MYVAR="Hola Linux"' >> ~/.zshrc
source ~/.zshrc
```

---

## 📌 Gestión y consulta

| Comando         | Uso                                                     |
| --------------- | ------------------------------------------------------- |
| `echo $VAR`     | Ver el valor de una variable                            |
| `env`           | Listar todas las variables de entorno                   |
| `printenv`      | Listar variables exportadas                             |
| `set`           | Ver todas las variables (incluye locales de shell)      |
| `unset VAR`     | Eliminar variable temporal                              |
| `cat ~/.bashrc` | Confirmar que tus variables permanentes estén guardadas |

---

## ⚡ Ejemplo práctico

1. Crear variable temporal:

   ```bash
   saludo="Hola Mundo"
   echo $saludo
   ```

2. Exportar como global:

   ```bash
   export saludo="Hola Mundo"
   ```

3. Hacerla permanente:

   ```bash
   echo 'export saludo="Hola Mundo"' >> ~/.bashrc
   source ~/.bashrc
   ```

---

## 🚀 Tips

* Mantén tus **scripts y configuraciones** en variables para mayor flexibilidad.
* No modifiques el **PATH** a la ligera, mejor **añade rutas al final**:

  ```bash
  export PATH=$PATH:/home/luis/bin
  ```

* Usa `env | less` para navegar entre todas las variables.

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
