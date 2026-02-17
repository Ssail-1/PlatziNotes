
# 🏷️ Alias en Linux

Los **alias** permiten crear **comandos personalizados** o **atajos** para no tener que escribir instrucciones largas.

---

## 📌 Alias temporales

* Se crean con el comando `alias`.
* **Solo duran mientras la sesión actual está abierta** (si cierras la terminal, se pierden).

### Sintaxis

```bash
alias nombre='comando'
```

### Ejemplos

```bash
alias cls='clear'                 # Limpiar pantalla
alias ll='ls -lh --color=auto'    # Listar con formato largo y legible
alias gs='git status'             # Atajo para git status
```

👉 Comprobar alias activos:

```bash
alias
```

👉 Eliminar un alias temporal:

```bash
unalias nombre
```

---

## 📌 Alias permanentes 

Para que el alias quede guardado y se cargue cada vez que abras la terminal, debes **editar el archivo de configuración del shell** ***".bashrc"***. 
### En Bash

Para saber que shell tienes...  

```bash      
	  echo shell
```

Si es bash, continua con esto:
1. Edita el archivo:

	Se encuentra en la carpeta del usuario ~  
	Recargamos el archivo
   ```bash
   source ~/.bashrc 
   ```
* Para visualizar el archivo puedes usar 
	`cat .bashrc | less`

2. Agrega los alias al final, por ejemplo:

   ```bash
   echo alias cls="clear" >> .bashrc
   ```

## 📦 Buenas prácticas

* Usa nombres cortos y fáciles de recordar.
* Evita sobreescribir comandos importantes como `rm`, a menos que lo hagas con seguridad:

  ```bash
  alias rm='rm -i'   # Preguntar antes de borrar
  ```
* Puedes organizarlos por categorías (navegación, git, redes).


---
Recuerda: 
* `alias` → crea alias temporal.
* `unalias` → elimina alias temporal.
* `~/.bashrc` (o `~/.zshrc`) → guardar alias permanentes.
* `source ~/.bashrc` → recargar cambios sin reiniciar terminal.

---

<p align="center">
  <a href="../README.md"> <b>🔄 Regresar</b> </a>
</p>

---
