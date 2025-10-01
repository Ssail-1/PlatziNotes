Hola Noa, este es el apunte que estoy realizando, ire dandole la estructura y la información, a lo largo del documento te dejare indicaciones para que puedas mejorar el trabajo o darle el formato que te pido y sabras donde estaran las intrucciones porque te lo dejare indicado así: <Noa>Instrucciones</Noa>

<Noa> Estas son las primeras instrucciones, quiero que del siguiente apunte hagas lo siguiente:
* Le des un mejor formato que el que tengo, tienes la libertad de mejorarlo con el objetivo de que sea un material de aprendizaje esmerado en hacerlo profundo pero eficiente para aprender desde las bases.
* Quiero que de los comandos me des si tienes otra descripción o lo puedes mejorar esta bien, tambien quiero que de los comandos me vayas diciendo que significa cada cosa, ejemplo: git diff --staged, osea que significa diff o --staged, ten en cuenta que no se ingles y si escalamos esto, muchas personas no saben ingles y se ahorra mucho tiempo si te ponen que signica en español o si no tiene una traduccion directa o su traducción es confusa puedes tu decir a que se refiere o su traducción mas acercada.
*Siento que yo entiendo si me explican a profundidad cada cosa y me desespera que aveces no y tengo que estar buscando a que se refieren las cosas. Por ejemplo en la parte que hablo de config global yo busque y encontre que se podia acceder a diferentes configuraciones en archivos diferentes, etc, y en el curso solo dijeron git config --global podemos poner username y useremail y ya, pero no fue mas allá, chance mas adelante lo diga, pero a mi se me complica entender porque entiendo lo que hace pero es como si me dejara con preguntas que no me respondio y eso me aflije porque me detiene, y ya cuando empeze a leer fue como haaa, ya entiendo y fue mas facil entender el concepto, el royo es que yo aprendo así, entonces si me ayudas a facilitar eso, estaría sensacional.
* Hay algunos comandos que solo fueron mencionados como: "--soft -> permite eliminar los archivos
--mixed -> regresa los commits" pero no se adentro, donde veas que hay alguna mencion pero no se aonda correctamente, me gustaría que tu lo complementaras
* Poco a poco estoy viendo que hay comandos para repositorios locales y remotos y son comandos diferentes, me gustaría que si no los tengo anotados tu los vayas anexando y pongas eficientemente que unos son locales y otros remotos
* Tambien quiero que me vayas complementando el trabajo con buenas practicas o estanderas para llamar ramas, como Development para donde estamos desarrollando, main que es la principal, Hotfix para llamar a la rama en la que estamos solucionando un error, etc.
</Noa>

> Trabajo basado en:  
> | Titulo | Profesor | 
> | ------ | -------- |
> |[Curso de Git y GitHub](https://platzi.com/cursos/gitgithub/ "Curso de Git y GitHub") | Amin Espinoza |   
> |[Curso de Configuración de Entorno en Linux](https://platzi.com/cursos/entorno-linux/ "Curso de Configuración de Entorno en Linux") | Enrique devars |

Fuentes usadas: 
https://education.github.com/git-cheat-sheet-education.pdf 

by ssail
---

# Apuntes Git y GitHub
**Git**
---  
    "Sistema de control de versiones"
> Creado por Linux Torvalds

## Setup & INIT

Se inicia un repositorio con el comando **git init**, que crea una carpeta oculta llamada .git en el directorio de trabajo.

### git init
`git init` -> Inicializa un directorio como un repositorio git  
+ Crea la rama/branck inical **"master"** por defecto 

<Noa> Aqui no entendi porque cambio la rama, a que se refiere, le cambio el nombre o creo un archivo, osea que royo con eso, y si lo cambio porque ese nombre, es una convención? y si lo es, de que o de donde? </Noa> 
> Cambio de rama principal como **main**
1. Cambia la configuración global escribiendo `git config --global init.defaultBranch main`.
2. Actualiza la rama en el proyecto actual con `git branch -m main`.

### git clone [url]
Recuperar un repositorio completo desde una ubicación alojada a través de URL

## Checking Configuration
`git --help`

    Despliega el manual de comandos

`git config --list`  

    Muestra la configuración completa y activa en el entrono de git esto es a nivel del sistema, global y local
- `git config "key"` -> Comprueba el valor que tomo una clave especifica

## Setup  

### git config
+ Es una herramienta para configurar y controlar el aspecto y funcionamientode Git dependiendo de la flag o parametro

| Flags / Parametros | Accede o modifica | Ruta |
| --- | --- | --- |
| --global | Archivo especifico de tu usuario | `~/.gitconfig` o `~/.config/git/config` |
| --system | Usuarios del sistema y todos sus repositorios | /etc/gitconfig |
| Archivo config en el directorio de git | Especifico del repositorio actual | .git/config |   

Cada nivel sobreescribe los valores del nivel anterior    

---


```shell
git config --global user.name "username" 
```
```shell
git config --global user.email "user email"
```
```shell
git config --global color.ui auto
``` 
<Noa> Esta no se para que es: git config --global color.ui auto </Noa>


### Editor
Se usa el editor por defecto, generalmente **Vim** o **Emacs** para sistemas basados en Unix como Linux y Mac.

Cambio a emacs
> ` $ git config --global core.editor emacs`





## ¿Cómo se crean y agregan archivos a Git?

Para crear un archivo desde la terminal, utiliza un editor como nano. Una vez creado, puedes verificar su existencia y estado con **`git status`**, que te mostrará el archivo como no registrado. Para incluirlo en el área de ***staging***, donde estará listo para el *commit*, usa `git add` nombre_del_archivo.txt. 
* Esta área de staging es un “limbo” donde decides qué archivos entrarán en el control de versiones.

Diagrama de secuencia 
---
[Clase 3](https://platzi.com/cursos/gitgithub/comandos-basicos-de-git-add-commit-log/ "Control de Versiones con Git: Comandos Básicos y flujo de Trabajo")  
![Diagrama de Secuencia Directorio -> Staging -> Repo git](DiagramaSecuenciaDir_Staging_Git.png "Diagrama de Secuencia Directorio -> Staging -> Repo git")

<Noa> En la imagen anterior aparecen comandos que se pueden realizar a nivel de directorio de trabajo como cp, mv, touch, create, rm, delete etc, despues a nivel de area de staging git add para agregar, git rm--cached para sacar un archivo del area de staging y git rm--force que hace lo mismo creo, pero no se la diferencia, y a nivel de repositorio de git git commit, git commit-ammend para ingresar a repo, y git reset--soft que lleva el archivo al area de staging, git reset--mixed lleva el archivo al directorio de trabajo y git reset --hard elimina definitivamente los archivos, te digo esto porque estaria bueno que despues de la imagen hagas una descripción mejor que la que te di para explicar la imagen y ponela con un formato bonito de .md que se vea como pie de foto.
Tambien si en el documento no ves que ponga información de estos comandos, porfa tu agregalos. Los de directorio de trabajo como cp, mv y esos no porfa, porque pues eso es de linea de comandos y estamos en git</Noa>

<Noa> Desde aqui hasta donde te vuelva a indicar, esta es información que saque de un pdf ayuda de gitHub, lo integre porque se me hace mas facil hacer apuntes y me parecio genial porque viene por secciones, no se si es bueno, pero si lo es, me gustaria que lo integraras a este trabajo y si tienes que modificarlo para hacerlo mas digerible sabes que puedes. 
Actualizacion jaja: trata de mejorar demaciado sus definiciones o descripciones porque no son muy buenas, conforme sigo el curso me doy cuenta que a estas tambien les falta mas crema.
Eso de crema es una expreción de ponerle mas crema a los tacos jaja, yo le digo crema porque no me gusta tanto la salsa, le falle a méxico :'v jaja</Noa>  

## 📍 STAGE & SNAPSHOT

*Trabajando con instantáneas y el área de preparación de Git*

* `git status`
  Muestra los archivos modificados en el directorio de trabajo y cuáles están preparados (*staged*) para el próximo commit.

* `git add [archivo]`
  Agrega un archivo (tal como está en ese momento) al área de preparación (*stage*) para incluirlo en el próximo commit.

* `git reset [archivo]`
  Saca un archivo del área de preparación o staging, pero conserva los cambios en el directorio de trabajo. <Noa>Aqui me entro duda es diferente git reset [archivo] que git rm --cached y --force?, explica eso, si es necesario aqui incluye esos dos comandos que te di</Noa> 

* `git diff`
  Muestra las diferencias de lo que ha cambiado pero aún **no** está preparado.

* `git diff --staged`
  Muestra las diferencias de lo que está en el área de preparación pero aún no se ha hecho commit.

* `git commit -m "[mensaje descriptivo]"`
  Guarda los archivos preparados como un nuevo *snapshot* (commit) en la historia del proyecto.

---


## 🌿 BRANCH & MERGE

*Aislar trabajo en ramas, cambiar contexto e integrar cambios*

* `git branch`
  Lista todas las ramas. El `*` indica la rama activa.

* `git branch [nombre-rama]`
  Crea una nueva rama en el commit actual.

* `git checkout [rama]`
  Cambia a otra rama y actualiza el directorio de trabajo.

* `git merge [rama]`
  Fusiona la rama especificada en la actual.

* `git log`
  Muestra todos los commits de la rama actual.

---

## 🔄 SHARE & UPDATE

*Obtener actualizaciones de otros repositorios y actualizar el local*

* `git remote add [alias] [url]`
  Agrega una URL remota con un alias.

* `git fetch [alias]`
  Descarga todas las ramas del repositorio remoto.

* `git merge [alias]/[rama]`
  Fusiona una rama remota en la rama local actual.

* `git push [alias] [rama]`
  Envía los commits locales de una rama al repositorio remoto.

* `git pull`
  Descarga y fusiona cambios del remoto en la rama actual.

---

## 📂 TRACKING PATH CHANGES

*Versionar eliminaciones y cambios de ruta de archivos*

* `git rm [archivo]`
  Elimina el archivo del proyecto y prepara la eliminación para el commit.

* `git mv [ruta-existente] [nueva-ruta]`
  Cambia el nombre o mueve un archivo, y prepara ese cambio para el commit.

* `git log --stat -M`
  Muestra los commits junto con los archivos movidos o renombrados.

---

## 🗂️ TEMPORARY COMMITS (Stash)

*Guardar temporalmente cambios para cambiar de rama*

* `git stash`
  Guarda los cambios modificados o preparados en un “almacén temporal”.

* `git stash list`
  Lista las entradas guardadas en el stash.

* `git stash pop`
  Recupera los cambios guardados y los aplica al directorio de trabajo.

* `git stash drop`
  Descarta los cambios guardados en el stash.

---

## ✍️ REWRITE HISTORY

*Reescribir ramas, actualizar commits y limpiar historial*

* `git rebase [rama]`
  Aplica los commits de la rama actual sobre la rama especificada.

* `git reset --hard [commit]`
  Borra el área de preparación y restaura el directorio de trabajo al estado del commit dado. ⚠️ (peligroso, puede perder cambios).

---

## 🔎 INSPECT & COMPARE

*Examinar logs, diferencias e información de objetos*

* `git log`
  Muestra el historial de commits de la rama activa.

* `git log branchB..branchA`
  Muestra los commits que están en `branchA` pero no en `branchB`.

* `git log --follow [archivo]`
  Muestra el historial de commits de un archivo, incluso si fue renombrado.

* `git diff branchB...branchA`
  Muestra las diferencias entre `branchA` y `branchB`.

* `git show [SHA]`
  Muestra un objeto de Git (commit, archivo, etc.) en un formato legible.

---

## 🚫 IGNORING PATTERNS

*Evitar que ciertos archivos se suban al repositorio*

* `git config --global core.excludesfile [archivo]`
  Define un archivo global de patrones de exclusión para todos los repositorios.

* **Ejemplo de `.gitignore`**

  ```gitignore
  logs/
  *.notes
  pattern*/
  ```

  Guarda un archivo llamado `.gitignore` en tu proyecto para especificar qué archivos o carpetas deben ignorarse.
---
<Noa> De aqui sigo con los apuntes propios y me gustaría que integraras en lo demas en las secciones correspondientes </Noa>

---

`git rm --cached [Archivo]` -> Remueve el archivo del area de staging y pasandolo 

`git rm --force [Archivo]` -> Remueve archivos que el sistema normalmente eliminaria

<Noa>El profe uso estos comandos, no los entendí y me revolví por lo que anteriormente te habia mencionado, agregalos por si despues no los agrego a mis notas, son estos: git rm --force [archivo] ; git commit -ammend ; git reset --soft ; git reset --mixed ; git reset --hard. Y tambien he visto que las flags o parametros tienen acronimos como --force -f, eso me gustaría que explicaras porque y cual conviene usar y si puedes de todos los comandos que estan en este documento pon el comando largo y corto si es que hay, como cuando hicimos el de linea de comandos, me dabas el comando completo y despues me decias que había uno mas corto que hacia lo mismo. </Noa>

---

`git add .` -> Ingresa todos los archivos que se encuentren en el directorio actual.

`git commit -m "Descripcion del cambio"` -> Lleva el archivo al repositorio o control de versiones

## Ramas 
Una rama es un directorio donde creamos trabajamos sobre el trabajo original creando desarrollando versiones que no afectan al flujo principal y así cada desarrollador puede trabajar en conjunto o bien solo uno.

### Rama Principal (Main o Master)
Por defecto git llama Master a la rama principal pero por convención, estandar y buenas practicas le cambiamos el nombre a main y sobre esta podemos crear varias ramas independientes.

Checkout  
Así le llamamos al proceso de crear una rama independiente

Development  
Es el nombre que le asignamos a la rama sobre la que estamos desarrollando.

Hotfix  
Es la forma en la que le llamamos a la rama donde estamos solucionando un bug o un error.

Merge  
Es el proceso de combinar ramas

<Noa> Creo que esta aclaración del Head no va aquí, tambien me gustaria que me dijeras porque ahay que tener en cuenta que al hacer merge puede gerear conflictos que hay que solucionar quien hace el commit, la duda es porque si trabaje sobre un archivo.js ejemplo y al hacer commit, se actualiza en que tiene el mismo nombre o hay que eliminar el que estaba en el repo y dejar el que subimos o como, como que no entiendo cual sería el conflicto. </Noa>
HEAD  
Indica el commit donde estamos trabajando.

+ `git branch <Nombre de rama>` -> Indica en que rama te encuentras con un *  

Crea la rama y te lleva a ella
+ `git checkout -b <Nombre de rama>` 
+ `git switch -c <NameBranch>`

Saltos entre ramas
+ `git checkout <branch>` -> En deshuso 
+ `git switch <branck>` -> forma actual

Unificación de ramas
1. Saltar a la rama donde se unificara para recibir nueva rama
2. `git merge <rama a fucionar>` 

Eliminación de ramas  
`git branch -D <Rama a eliminar>`

---

## Solución de conflictos de fusión
<Noa> Aqui explica lo del conflicto, ya en otra clase explico el profesor sobre el conflicto, este se da cuando dos ramas diferentes hacen cambios distintos a un mismo archivo en las mismas lineas. Al hacer merge git nos avisa de ello y la solución es abrir el archivo y modificarlo como nosotros lo deseemos.
git coloca con caracteres <, >, -, donde hay conflictos y marca los lugares donde se hacen los cambios con punteros como head y developer creo, el archivo se puede abrir en nano pero VSCode nos ayuda a resolver estos conflictos sin necesidad de borrar o escribir mas lineas de codigo  automatizando la solución, explica esto y el proceso de VSCode. Mientras se soluciona el conflicto el archivo se encuentra en un estado llamado **Unmerged** y cuando ya esta solucionado terminados el commit.</Noa>

## Navegación de Historial y Corrección de errores

<Noa> Desarrolla este tema tu Noa, que estoy perdido </Noa>

Para regresar a una verión anterior tenemos varios metodos...

### git revert
`git revert <hash-commit>` -> Revierte los cambios de un commit 

### git reset
`git reset --hard <hash-HEAD>` -> Desecha los cambios locales dejando como cabezera el hash indicado, eliminando archivos e historial que habia despues de hash 

`git reset --soft [hash-commit]` -> permite eliminar los archivos  
`git reset --mixed [hash-commit]` -> regresa los commits  

`git reset` -> puede eliminar todo
<Noa> Explicalo mejor que yo que no entendí </Noa>

## Git checkout para gestion de verisiones y Revición.
```shell
git checkout [hash-commit]
```
Este comando sirve para volver a cualquier version del historial sin afectar la integridad del historial.
* Es este estado temporal puedes hacer pruebas y no afectara la rama principal

### Regresar a rama principal
`git checkout main` 

### Version alterna a partir de un commit
`git switch -c [new-branch-name]`

`git checkout master` <Noa>Este no se si es correcto, mecionaban que era para volver a la ultima version de un archivo, o rama, no se si hay dos comandos diferentes, pero si fuera para un archivo hace falta saber donde se pone el nombre del archivo como argumento, y otra duda, si la rama principal se llama main, entonces va main en lugar de Master?</Noa>



## Tags o Etiquetas
### git tag
Utiles para marcar los commits mas importante. Nos dan una referencia de la evolución del proyecto, tienen mucha funcionalidad en GitHub.

```shell
git tag -a [tag] -m "Descripción o ser del tag"
```
#### Asignando etiquetas 
Se vería algo así:
```shell  
git tag -a [nameTag] [hash-commit] -m "Descripcion mensaje"
```

Publicar un tag en el repositorio remoto:  
`git push origin --tags`


#### Manipulando etiquetas
Mostrar o listar los tags  
+ `git tag` 
+ `git show-ref --tags` -> Lista los tags y muestra que commit esta asociado a cada tag.

`git show <etiqueta>` o `di -> Muestra toda la información asociada a esta etiqueta...

Borrar la etiqueta:  
Localmente ->
+ `git tag -d <etiqueta>` 

Cuando borramos un tag en local, este no se borra en el repositorio remoto. 

Repositorio Remoto ->
1. Borramos el tag localmente
2. Borramos el remoto con: `git push origin :refs/tags/nombre-del-tag`

`git tag -a <etiqueta> <hash de commit> -m "Mensaje de tag"` -> Coloca una etiqueta al commit indicado


`git clone [url]` -> Clona el repositorio en el directorio donde nos encontramos

## Configuración deDDH en GitHub 

<Noa>Aqui me gustaria que expliques porque es importante, en que casos se usa comunmente y lo importante que creas y si el proceso no es tan bueno mejoralo, tambien explica lo que significan los parametros, o que significa cada comando, es algo que ya te habia dicho al inicio pero por si acaso. </Noa>

Para configurar SSH en GitHub, sigue estos pasos:

1. Genera una clave SSH:

    + Abre tu terminal.
    + Ejecuta: ssh-keygen -t ed25519 -C "tu_correo@example.com" y sigue las instrucciones para crear la clave.

2. Inicia el agente SSH:

    + Ejecuta: eval "$(ssh-agent -s)".
    + Luego, agrega tu clave privada: ssh-add ~/.ssh/id_ed25519.

3. |Copia la clave pública:

    + Usa cat ~/.ssh/id_ed25519.pub para visualizarla y cópiala.

4. Añade la clave a GitHub:

    + Ve a GitHub, en "Settings" > "SSH and GPG keys", y selecciona "New SSH key". Pega tu clave pública.

5. Prueba la conexión:

    + Ejecuta: ssh -T git@github.com. Deberías ver un mensaje de éxito.

Con esto, habrás configurado SSH para GitHub de forma segura y eficiente.



Usar SSH para interactuar con GitHub es una excelente forma de aumentar la seguridad y mejorar la comodidad en el manejo de repositorios. A continuación, te explicamos el paso a paso para generar y configurar tus llaves SSH en distintos sistemas operativos y cómo integrarlas en tu perfil de GitHub para mejorar la experiencia de clonación y autenticación.

¿Por qué es mejor usar SSH en lugar de HTTPS para GitHub?
Seguridad adicional: SSH permite autenticar la computadora específica que accede a los repositorios sin necesidad de ingresar una contraseña cada vez.
Comodidad: Evita la necesidad de escribir tu contraseña en cada operación con GitHub, agilizando el flujo de trabajo.
¿Cómo generar una llave SSH en Windows y Linux?
Instalar WSL si estás en Windows (opcional si usas Linux nativo).
Verificar que no tienes llaves previas: Ve al menú de “Code” en GitHub y verifica que la opción de SSH no tenga llaves configuradas.
Generar la llave SSH: En la terminal, usa el comando:
ssh-keygen -t ed25519 -C "tu_correo@example.com"
-t ed25519 establece el nivel de encriptación.
-C añade un comentario con tu correo, útil para identificar la llave en GitHub.
Guardar y proteger la llave:
Usa el nombre por defecto y añade una contraseña segura.
La llave pública se guarda en el directorio .ssh, generalmente nombrada id_ed25519.pub.
Configurar el agente SSH: Activa el agente de SSH y añade la llave privada:
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
¿Cómo añadir la llave SSH a GitHub?
Abrir el archivo de la llave pública (id_ed25519.pub) y copia el contenido.
En GitHub, ve a Settings > SSH and GPG keys > New SSH key y pega la llave.
Nombra la llave de acuerdo a la computadora en la que estás configurándola.
¿Qué pasos adicionales seguir en Mac?
Crear el archivo de configuración SSH: Abre o crea el archivo config dentro del directorio .ssh.

Agregar parámetros específicos de Mac: Añade la configuración para integrar SSH con el sistema Keychain:

Host github.com
   AddKeysToAgent yes
   UseKeychain yes
   IdentityFile ~/.ssh/id_ed25519
Añadir la llave al agente SSH con Keychain: Usa el comando:

ssh-add --apple-use-keychain ~/.ssh/id_ed25519
¿Cómo verificar la conexión con GitHub?
Comprobar autenticación: En la terminal, ejecuta el comando:
ssh -T git@github.com
Escribe “yes” para confirmar la conexión.
Aparecerá un mensaje de GitHub que confirma la autenticidad.
¿Cómo clonar un repositorio usando SSH?
En GitHub, selecciona el repositorio deseado, elige la opción de clonación por SSH y copia la URL.
En la terminal, ejecuta:
git clone git@github.com:usuario/repositorio.git
Esto clona el repositorio sin solicitar contraseña, aprovechando la autenticación SSH.

## Uso de Forks y Estrella en Repositorios de GitHub

<Noa>Este tema no es tan complejo, pegue el apunte del curso, lo puedes resumir o poner solo las cosas importantes</Noa>

Entender el uso de forks y estrellas en GitHub optimiza la gestión de proyectos y recursos al trabajar en esta plataforma. Aquí exploraremos cómo funcionan estos elementos y cómo pueden ayudarte a organizar tus repositorios en función de tus necesidades.

¿Qué es un fork y cómo se utiliza?
Un fork en GitHub es una copia de un repositorio alojado en la cuenta de otra persona y que puedes transferir a tu propia cuenta. Este proceso crea una réplica del repositorio en su estado actual, sin reflejar futuros cambios del original a menos que se sincronice manualmente. Esto permite:

Trabajar de manera independiente en un proyecto sin afectar el repositorio original.
Personalizar el contenido según tus necesidades sin modificar el repositorio fuente.
Crear una base para hacer contribuciones posteriores al repositorio original.
Para crear un fork, debes abrir el repositorio, seleccionar el botón de Fork y seguir los pasos para copiarlo en tu cuenta. Así, GitHub duplicará el repositorio, manteniendo el nombre y descripción del original. Puedes optar por copiar solo la rama principal (main) o todo el proyecto. Luego, desde tu cuenta, podrás modificar el contenido sin interferir con el repositorio original.

¿Qué beneficios aporta usar estrellas en GitHub?
Las estrellas en GitHub funcionan como un sistema de marcado para resaltar los repositorios que deseas tener a mano como referencia o favoritos. Son útiles para:

Crear un índice de repositorios de referencia o inspiración.
Acceder rápidamente a recursos clave desde tu perfil.
Seguir el desarrollo de proyectos importantes para tus intereses.
Al seleccionar la estrella en un repositorio, ésta se ilumina para indicar que has marcado este recurso. Puedes acceder a todos tus repositorios marcados desde la sección de “tus estrellas” en tu perfil. Aquí se listan los proyectos que has destacado, ayudándote a centralizar tus fuentes de consulta.

¿Cómo clonar un repositorio forkeado?
Después de realizar un fork, puedes clonar este repositorio a tu entorno local para trabajar de forma directa en tu equipo. Para hacerlo:

Ve a tu repositorio forkeado.
Selecciona el botón Code y copia la URL del proyecto en formato SSH.
Abre la terminal y usa el comando git clone .
De esta manera, tendrás una versión local del repositorio en la que podrás modificar y gestionar el código. Esta técnica de fork y clonación es útil para personalizar proyectos o experimentar sin afectar el original, ofreciendo flexibilidad para hacer cambios sin alterar el repositorio fuente.

¿Por qué usar forks en lugar de clonar directamente el repositorio original?
Hacer un fork en lugar de una clonación directa del repositorio original permite que trabajes de manera independiente. Puedes hacer ajustes sin el riesgo de cambiar el repositorio base, especialmente útil cuando el original es de terceros o si planeas realizar cambios extensivos. Además, el fork es una base ideal para hacer contribuciones futuras, ya que se puede sincronizar y enviar cambios al proyecto original a través de un proceso estructurado.

## Uso de git pull, git push y git fetch en repositoios de GitHub

### ¿Cómo sincronizar tus repositorios con git pull, git push y git fetch?
La gestión de repositorios es una habilidad esencial en el desarrollo de software moderno. Git y GitHub permiten a los desarrolladores colaborar y sincronizar cambios de manera eficiente. Aquí te explicaremos cómo los comandos git pull, git push y git fetch juegan un papel crucial en este proceso, ayudándote a entender cuándo y cómo utilizarlos para mantener tus repositorios actualizados.

### ¿Cómo usar git pull y git push para mantener tus repositorios sincronizados?
El comando git pull se utiliza para actualizar tu repositorio local con los cambios que se han producido en la nube, específicamente en GitHub. Esta acción es esencial cuando deseas asegurarte de que tu entorno local refleje las últimas modificaciones realizadas en el repositorio compartido.

Por otro lado, git push tiene la función opuesta: permite subir tus cambios locales al repositorio en la nube. Esto es fundamental para colaborar con otros desarrolladores, garantizando que todos los cambios se integren en el proyecto general.

Script de ejemplo para git pull y git push


```
# Para verificar la rama activa y actualizar el repositorio local

$ git branch                # Verifica la rama activa
$ git pull origin main      # Jala los últimos cambios de la rama main en GitHub

# Para subir cambios desde el repositorio local a la nube
$ git add .                 # Prepara los archivos para el commit
$ git commit -m "Descripción del cambio" # Realiza el commit
$ git push origin main      # Sube los cambios a GitHub
```

### ¿Qué es y cómo utilizar git fetch?
El comando git fetch es útil cuando deseas descargar los cambios sin aplicarlos inmediatamente. Difiere de git pull, ya que te permite evaluar primero los cambios antes de fusionarlos con tu rama local. Este enfoque resulta valioso cuando se espera una revisión antes de integrar los cambios en el entorno local.

Ejemplo práctico de git fetch

```
# Descargar cambios sin aplicarlos de inmediato
$ git fetch origin                # Jala los cambios de la rama origen

# Comparar y evaluar diferencias entre ramas
$ git log main..origin/main       # Compara las diferencias entre la rama local y la remota

# Una vez evaluados, fusionar cambios en la rama local
$ git merge origin/main           # Fusiona los cambios evaluados
```

### ¿Cómo elegir entre git pull y git fetch?

git pull: Rápido y directo, ideal cuando se confía en los cambios remotos y se necesita una actualización inmediata de la rama local.
git fetch: Más cauteloso, ofrece una etapa de evaluación antes de integrar los cambios, evitando sincronizaciones no deseadas.
Elige el comando que mejor se adapte a tu situación y flujo de trabajo. Recuerda siempre sincronizar tus cambios entre local y remoto para mantener la integridad del proyecto y facilitar la colaboración.

Con estos comandos como parte de tu arsenal, tendrás la habilidad de mantener tus proyectos bien organizados y listos para la colaboración. Sigue explorando y practicando en diferentes escenarios para reforzar estas habilidades esenciales en el manejo de Git y GitHub. ¡Adelante, y sigue aprendiendo!

<Noa>El profe uso fit [push -u origin main] pero no se porque puso -u </Noa>





## Creación de Plantillas de Issues en GitHub

Usar los Issues de GitHub permite gestionar y documentar problemas en un repositorio, desde errores simples en la redacción hasta defectos complejos en la funcionalidad. Con una interfaz intuitiva, permite que cualquier usuario señale y describa aspectos mejorables, y con plantillas de Issues, mejora la claridad y colaboración en el proceso.

### ¿Qué es un Issue en GitHub?
Un Issue es una forma de señalar problemas o sugerencias dentro de un repositorio. Puede ser usado para:

Notificar errores en la documentación, como faltas de ortografía.
Reportar problemas en el funcionamiento esperado del código.
Informar mejoras o cambios necesarios.
Los Issues permiten una comunicación bidireccional entre los colaboradores y el creador del repositorio, lo que facilita la resolución de problemas.

### ¿Cómo crear un nuevo Issue?
1. En el repositorio de GitHub, selecciona la pestaña Issues.
2. Haz clic en New Issue y describe el problema en dos campos principales:
    + Título: Una breve descripción.
    + Descripción: Detalles del problema, pasos para reproducirlo, etc.  

Es posible agregar elementos adicionales, como asignar el Issue a otra persona o etiquetarlo.

### ¿Cómo crear una plantilla de Issues?
Para facilitar el proceso a otros colaboradores, es útil crear plantillas de Issues. Para hacerlo:

1. Desde el repositorio, abre Visual Studio Code con el comando code ..
2. Crea una carpeta llamada .github y dentro otra carpeta llamada ISSUE_TEMPLATE.
3. Dentro de ISSUE_TEMPLATE, crea un archivo Markdown (por ejemplo, bug_report.md).
4. Copia la estructura de la plantilla, que usualmente incluye secciones como descripción, pasos para reproducir el error y detalles adicionales.

Con esta plantilla, los colaboradores tendrán un formato estándar para reportar problemas, lo que ayuda a una mejor gestión y resolución.

### ¿Cómo sincronizar los cambios en GitHub?
1. Una vez creada la plantilla, verifica que los archivos cambiados estén marcados en verde en Visual Studio Code.
2. Realiza un commit (por ejemplo, “Bug Report agregado”).
3. Sincroniza con el repositorio de GitHub mediante el botón de flecha hacia arriba (push).
4. En GitHub, verifica que la plantilla esté disponible en la sección de Issues.

### ¿Qué ventajas tiene una plantilla de Issues?
Las plantillas simplifican el proceso de documentación de problemas y mejoran la comunicación al estandarizar la información que se solicita a los colaboradores. Esto ayuda a identificar los problemas de forma precisa y rápida.

### ¿Cómo personalizar las plantillas de Issues para casos específicos?
Además de la plantilla básica para bugs, puedes crear plantillas personalizadas como:

+ Document Report: Para señalar errores en la documentación.
+ Mejores prácticas: Para sugerir mejoras en la estructura del código.

Estas plantillas permiten a los colaboradores elegir el tipo de Issue que mejor se adapta al problema y agilizan la gestión del repositorio.


## Uso de Pull Request en GitHub para colaboración efectiva

Colaborar en GitHub requiere evitar modificar directamente la rama principal, lo que podría causar conflictos con el trabajo de otros compañeros. En su lugar, trabajar en ramas individuales y fusionarlas mediante Pull Requests (PR) es clave para un flujo de trabajo colaborativo y seguro.

### ¿Por qué evitar cambios directos en la rama principal?
Realizar cambios directamente en la rama principal (main) puede sobrescribir el trabajo no sincronizado de otros colaboradores. Este error común se evita al:

+ Crear una rama separada para cada contribuyente.
+ Fusionar cambios mediante una revisión en el Pull Request, antes de unirlos a la rama principal.

### ¿Cómo funciona un Pull Request?
1. Crear una Rama Nueva: Al iniciar cambios, crea una rama local específica. Por ejemplo, developer01.
2. Subir la Rama a GitHub: Usa git push -u origin  para subir tu rama.
3. Notificar al Equipo: Al crear un Pull Request, notificas al equipo sobre tus cambios, lo que permite una revisión colaborativa (Code Review).

### ¿Qué papel juega la revisión de código?
El Code Review en los Pull Requests permite:

+ Evaluar y comentar los cambios antes de fusionarlos.
+ Aumentar la calidad y la visibilidad de los cambios propuestos.

Aunque puede ser intimidante al principio, esta práctica asegura transparencia y mejora continua en el equipo.

### ¿Cómo se fusiona un Pull Request?
1. Comparación y Revisión: Una vez que el equipo revisa los cambios y los aprueba, GitHub facilita la fusión con la rama principal.
2. Resolver Conflictos: GitHub verifica automáticamente conflictos potenciales, mostrando una marca verde si está listo para fusionarse sin problemas.
3. Eliminar la Rama: Tras la fusión, se elimina la rama para mantener el repositorio ordenado y listo para nuevas tareas.

### ¿Cómo puedo practicar Pull Requests de forma efectiva?
Para mejorar, colabora con un amigo o colega, practicando la creación y revisión de Pull Requests. Esta interacción entre ramas te ayudará a familiarizarte y a fluir con confianza en el proceso de colaboración en GitHub.

### Pasos que seguí

1. Se crea una nueva rama y se hacen los cambios
2. Se hace un `git add .` y un `git commit -m "mensaje"` o bien un `git commit -am "mensaje"`
3. Subimos los cambios en la nueva rama `git push --set-upstream origin nameBranch` o `git push -u origin nameBranch`
4. En GitHub hacemos un Compare & pull request
5. Esperamos el code review por parte de los colaboradores
6. Una vez cumplido el objetivo de la rama, podemos eliminar esta.










## Gestión de Proyectos con GitHub Projects: Planificación Colaborativa

### Introducción a GitHub Projects 🚀
GitHub Projects es una herramienta integrada en GitHub que permite gestionar proyectos de forma visual y organizada, combinando issues, pull requests y notas en tableros personalizables.

### 🎯 ¿Por qué usar GitHub Projects?
✅ Facilita la planificación y seguimiento del trabajo. ✅ Se integra con Issues y Pull Requests automáticamente. ✅ Permite organizar tareas en tableros estilo Kanban o listas. ✅ Soporta automatización con GitHub Actions. ✅ Ideal para equipos y proyectos individuales.

### 1️⃣ Cómo Crear un GitHub Project

Sigue estos pasos para iniciar un Project en GitHub:

📌 1. Acceder a GitHub Projects
Ve al repositorio donde quieres gestionar el proyecto.
Haz clic en la pestaña "Projects".
Presiona "New project".
📌 2. Elegir el Tipo de Proyecto
Puedes elegir entre:

Table (tablas personalizadas con filtros avanzados).
Board (tablero estilo Kanban, similar a Trello).
Elige el que mejor se adapte a tu flujo de trabajo.

📌 3. Configurar el Proyecto
Asigna un nombre y descripción.
Agrega columnas o estados (Ej: "To Do", "In Progress", "Done").
Agrega Issues o Pull Requests arrastrándolos al tablero.
2️⃣ Uso Básico de GitHub Projects
Una vez creado, puedes gestionar el trabajo de manera eficiente:

📌 1. Agregar Tareas (Items)
Puedes añadir Issues o PRs existentes al proyecto.
También puedes crear notas personalizadas para otras tareas.
📌 2. Organizar el Trabajo con Columnas
To Do → Tareas pendientes.
In Progress → Tareas en desarrollo.
Done → Tareas completadas.
Puedes personalizar columnas según tu flujo de trabajo.

📌 3. Automatizar con GitHub Actions
Puedes configurar automatizaciones como: ✅ Mover un Issue a "In Progress" cuando se asigne. ✅ Marcar como "Done" cuando se cierre un Pull Request.

3️⃣ Ejemplo de Flujo de Trabajo con GitHub Projects
🔹 1. Crear un Issue → Se registra una tarea o bug. 🔹 2. Mover a "In Progress" → Se asigna a un desarrollador. 🔹 3. Crear un Pull Request → Se suben los cambios. 🔹 4. Revisar el Código → Se aprueba el PR. 🔹 5. Fusionar y Cerrar el Issue → Se mueve a "Done".

🚀 Resultado: Un equipo bien organizado y un código de mejor calidad.

🎯 Conclusión
✅ GitHub Projects ayuda a organizar y visualizar tareas en un proyecto. ✅ Se integra con Issues, Pull Requests y GitHub Actions. ✅ Es una herramienta poderosa para equipos y desarrolladores individuales.




## Automatización de flujos de trabajo en GitHub Projects

Automatizar tareas en proyectos de software es esencial para ahorrar tiempo y mejorar la productividad. Con GitHub Projects, puedes configurar flujos de trabajo automáticos que simplifican la gestión y seguimiento de actividades, permitiendo un enfoque directo en el código.

### ¿Cómo vincular y personalizar un proyecto en GitHub?
1. Accede a tu repositorio en GitHub y selecciona la categoría de “Projects.”
2. Si no tienes un proyecto vinculado, selecciona la opción  “Enlazar a un proyecto.”
3. Edita el proyecto sin título agregando un nombre relevante, como “Mi proyecto individual,” y, opcionalmente, una descripción y un README.
4. Guarda los cambios y regresa al repositorio para enlazar este proyecto.

### ¿Cómo gestionar y actualizar actividades dentro del proyecto?
+ Dentro de tu proyecto vinculado, crea actividades como “Actualizar archivo HTML,” “Actualizar archivo CSS,” o “Actualizar archivo JavaScript.”
+ Marca el estado de cada tarea: en progreso, pendiente o completada.
+ Usa la sección “Insights” para ver un gráfico del estado de las actividades y medir la eficacia del equipo.


### ¿Cómo automatizar los cambios de estado en actividades?
+ Entra en los flujos de trabajo (Workflows) seleccionando los tres puntos en la esquina superior de tu proyecto.
+ Configura las reglas, por ejemplo, para que un issue o pull request cerrado cambie automáticamente el estado de la actividad a “Hecho.”
+ Personaliza otros workflows como el cambio de estado cuando un pull request es aprobado, asegurando que la automatización se adapte a tus necesidades.


### ¿Cómo crear y enlazar un issue desde una actividad?

1. Selecciona una actividad como “Actualizar archivo CSS,” presiona los tres puntos y conviértela en un issue en el repositorio.
2. Crea una nueva rama desde la sección de ramas, nómbrala de forma clara, y agrega los cambios necesarios en el archivo, por ejemplo, un nuevo archivo style.css.
3. Guarda los cambios, crea un pull request y describe los cambios. Usa la palabra clave closes seguido del número de issue para que GitHub lo cierre automáticamente cuando se apruebe el pull request.


### ¿Qué ventajas ofrece el flujo automatizado en GitHub?

Con esta automatización:

+ El estado de las tareas se actualiza solo, sin necesidad de hacerlo manualmente.
+ Los workflows pueden expandirse para notificar por Slack, Teams o correo electrónico cada vez que un pull request se cierra, facilitando la comunicación y el seguimiento en equipo.
+ GitHub Projects, junto con estas integraciones, permite un flujo de trabajo robusto y ágil.


## Recursos ecenciales de MarkDown para Documentación efectiva

### Herramientas útiles para documentación 

[MarkDown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

[Simple Icons](https://simpleicons.org/)

[Sintaxis de escritura y formartos basicos](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

[Static Badge](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

[Documentacion de Curso que hize de MD en youtube](Aqui deberia ir la ruta para el curso de MD que hize cuando lo suba a un repositorio de GitHub)

### Extenciones para Visual Estudio Code

> [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

> [Markdown Preview Mermaid Suppor](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

<!-- Aquí ya me siento bueno en markdown, así que solo pondre las herramientas que considere muy interesantes-->

<Noa> Los comentarios que ponga en html <!-- comentario --> esos dejalos y este tema dejalo como esta o checa tu si quieres poner algo necesario, o ya se, ayudame poniendo los temas que necesito para aprender Mermaid, ese no lo se usar y se me hace muy interesante, en la uni hice un proyecto donde use 100% mermaid para hacer los diagramas y fuaa!, me volo la cabeza pero no tenia tiempo para detenerme a saber como funcionaba. </Noa>








## Creación de una Portada de Perfil en GitHub con Markdown

Aprender a crear una portada atractiva y funcional en GitHub usando Markdown no solo mejora la presentación profesional de un perfil, sino que también permite personalizarlo con elementos visuales, enlaces y badges que muestran actividad e información de contacto. Aquí encontrarás un paso a paso para utilizar Markdown y hacer que tu perfil destaque.

### Herramientas de apoyo

[Sintaxis de escritura y formartos basicos](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

[Static Badge](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### ¿Cómo iniciar el repositorio especial en GitHub?

* Crear un repositorio: Ve a la sección de repositorios y crea uno nuevo usando el mismo nombre que tu nombre de usuario en GitHub; esto permite que el repositorio funcione como portada.

* Descripción y visibilidad: Añade una descripción breve (ej. “Portada de perfil”), hazlo público y agrega un archivo README.md. Esto es esencial para que el contenido sea visible en tu perfil.

* Clonación del repositorio: Clona el repositorio usando git clone en la terminal. La opción HTTPS es conveniente para nuevos perfiles, aunque SSH es más seguro.

### ¿Cómo personalizar el README con Markdown?

Markdown facilita la creación de secciones y elementos visuales. Puedes agregar:

* Títulos y subtítulos: Usa #, ## o ### según la jerarquía. Por ejemplo, ## Contacto.
* Enlaces y badges: Incluye enlaces usando [Texto](URL). Para badges, visita shields.io donde encontrarás diferentes opciones (ej. actividad de commits, sitios web).
* Iconos y emojis: Puedes agregar emojis como :computer: o :pencil: para destacar roles o actividades.

### ¿Cómo previsualizar y ajustar el archivo en Visual Studio Code?

* Vista previa de Markdown: Selecciona Open Preview en la esquina superior derecha para ver cómo se verán los cambios en GitHub.
* Extensiones recomendadas: Markdown Lint ayuda a mejorar el estilo al sugerir tips sobre el formato, como evitar espacios en blanco innecesarios.
* Limpieza del código: Markdown Lint también ayuda a mantener el archivo ordenado eliminando líneas en blanco que no son necesarias.

### ¿Cómo añadir y ajustar badges en el perfil de GitHub?

1. Visita shields.io y busca categorías de badges como:
    * Website: Permite agregar un enlace a tu sitio web.
    * Actividad de Commits: Muestra la frecuencia de tus commits en GitHub. Puedes seleccionar el intervalo: weekly, monthly, yearly, o total.

2. Insertar badges en Markdown: Selecciona “Markdown” en shields.io para obtener el código y pégalo en el README.md.
3. Prueba de visualización: Asegúrate de que los badges se muestren correctamente en Visual Studio Code.

### ¿Qué estrategias aplicar para mejorar la portada en GitHub?

* Referencias a otros repositorios: Examina perfiles de otros usuarios o proyectos con buena documentación. Visualiza su archivo README.md en modo “RAW” para ver el código en Markdown.

* Explora y adapta: La práctica es clave; revisa diferentes perfiles para encontrar ideas y técnicas que puedas adaptar.


