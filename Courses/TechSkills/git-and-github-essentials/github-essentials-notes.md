
# **Sección II: GitHub — Colaboración y Herramientas en la Nube.**

## Configuración de SSH en GitHub

<Noa>Aqui me gustaria que expliques porque es importante, en que casos se usa comunmente y lo importante que creas y si el proceso no es tan bueno mejoralo, tambien explica lo que significan los parametros, o que significa cada comando, es algo que ya te habia dicho al inicio pero por si acaso. </Noa>

Para configurar SSH en GitHub, sigue estos pasos:

1. Genera una clave SSH:

    - Abre tu terminal.
    - Ejecuta: ssh-keygen -t ed25519 -C "<tu_correo@example.com>" y sigue las instrucciones para crear la clave.

2. Inicia el agente SSH:

    - Ejecuta: eval "$(ssh-agent -s)".
    - Luego, agrega tu clave privada: ssh-add ~/.ssh/id_ed25519.

3. |Copia la clave pública:

    - Usa cat ~/.ssh/id_ed25519.pub para visualizarla y cópiala.

4. Añade la clave a GitHub:

    - Ve a GitHub, en "Settings" > "SSH and GPG keys", y selecciona "New SSH key". Pega tu clave pública.

5. Prueba la conexión:

    - Ejecuta: ssh -T <git@github.com>. Deberías ver un mensaje de éxito.

Con esto, habrás configurado SSH para GitHub de forma segura y eficiente.

Usar SSH para interactuar con GitHub es una excelente forma de aumentar la seguridad y mejorar la comodidad en el manejo de repositorios. A continuación, te explicamos el paso a paso para generar y configurar tus llaves SSH en distintos sistemas operativos y cómo integrarlas en tu perfil de GitHub para mejorar la experiencia de clonación y autenticación.

¿Por qué es mejor usar SSH en lugar de HTTPS para GitHub?
Seguridad adicional: SSH permite autenticar la computadora específica que accede a los repositorios sin necesidad de ingresar una contraseña cada vez.
Comodidad: Evita la necesidad de escribir tu contraseña en cada operación con GitHub, agilizando el flujo de trabajo.
¿Cómo generar una llave SSH en Windows y Linux?
Instalar WSL si estás en Windows (opcional si usas Linux nativo).
Verificar que no tienes llaves previas: Ve al menú de “Code” en GitHub y verifica que la opción de SSH no tenga llaves configuradas.
Generar la llave SSH: En la terminal, usa el comando:
ssh-keygen -t ed25519 -C "<tu_correo@example.com>"
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
ssh -T <git@github.com>
Escribe “yes” para confirmar la conexión.
Aparecerá un mensaje de GitHub que confirma la autenticidad.
¿Cómo clonar un repositorio usando SSH?
En GitHub, selecciona el repositorio deseado, elige la opción de clonación por SSH y copia la URL.
En la terminal, ejecuta:
git clone <git@github.com>:usuario/repositorio.git
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
    - Título: Una breve descripción.
    - Descripción: Detalles del problema, pasos para reproducirlo, etc.  

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

- Document Report: Para señalar errores en la documentación.
- Mejores prácticas: Para sugerir mejoras en la estructura del código.

Estas plantillas permiten a los colaboradores elegir el tipo de Issue que mejor se adapta al problema y agilizan la gestión del repositorio.

## Uso de Pull Request en GitHub para colaboración efectiva

Colaborar en GitHub requiere evitar modificar directamente la rama principal, lo que podría causar conflictos con el trabajo de otros compañeros. En su lugar, trabajar en ramas individuales y fusionarlas mediante Pull Requests (PR) es clave para un flujo de trabajo colaborativo y seguro.

### ¿Por qué evitar cambios directos en la rama principal?

Realizar cambios directamente en la rama principal (main) puede sobrescribir el trabajo no sincronizado de otros colaboradores. Este error común se evita al:

- Crear una rama separada para cada contribuyente.
- Fusionar cambios mediante una revisión en el Pull Request, antes de unirlos a la rama principal.

### ¿Cómo funciona un Pull Request?

1. Crear una Rama Nueva: Al iniciar cambios, crea una rama local específica. Por ejemplo, developer01.
2. Subir la Rama a GitHub: Usa git push -u origin  para subir tu rama.
3. Notificar al Equipo: Al crear un Pull Request, notificas al equipo sobre tus cambios, lo que permite una revisión colaborativa (Code Review).

### ¿Qué papel juega la revisión de código?

El Code Review en los Pull Requests permite:

- Evaluar y comentar los cambios antes de fusionarlos.
- Aumentar la calidad y la visibilidad de los cambios propuestos.

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

🚀 Resultado: Un equipo bien organizad











o y un código de mejor calidad.

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

- Dentro de tu proyecto vinculado, crea actividades como “Actualizar archivo HTML,” “Actualizar archivo CSS,” o “Actualizar archivo JavaScript.”

- Marca el estado de cada tarea: en progreso, pendiente o completada.
- Usa la sección “Insights” para ver un gráfico del estado de las actividades y medir la eficacia del equipo.

### ¿Cómo automatizar los cambios de estado en actividades?

- Entra en los flujos de trabajo (Workflows) seleccionando los tres puntos en la esquina superior de tu proyecto.

- Configura las reglas, por ejemplo, para que un issue o pull request cerrado cambie automáticamente el estado de la actividad a “Hecho.”
- Personaliza otros workflows como el cambio de estado cuando un pull request es aprobado, asegurando que la automatización se adapte a tus necesidades.

### ¿Cómo crear y enlazar un issue desde una actividad?

1. Selecciona una actividad como “Actualizar archivo CSS,” presiona los tres puntos y conviértela en un issue en el repositorio.
2. Crea una nueva rama desde la sección de ramas, nómbrala de forma clara, y agrega los cambios necesarios en el archivo, por ejemplo, un nuevo archivo style.css.
3. Guarda los cambios, crea un pull request y describe los cambios. Usa la palabra clave closes seguido del número de issue para que GitHub lo cierre automáticamente cuando se apruebe el pull request.

### ¿Qué ventajas ofrece el flujo automatizado en GitHub?

Con esta automatización:

- El estado de las tareas se actualiza solo, sin necesidad de hacerlo manualmente.
- Los workflows pueden expandirse para notificar por Slack, Teams o correo electrónico cada vez que un pull request se cierra, facilitando la comunicación y el seguimiento en equipo.
- GitHub Projects, junto con estas integraciones, permite un flujo de trabajo robusto y ágil.

||  ## Recursos ecenciales de MarkDown para Documentación efectiva
||  
||  ### Herramientas útiles para documentación
||  
||  [MarkDown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
||  
||  [Simple Icons](https://simpleicons.org/)
||  
||  [Sintaxis de escritura y formartos basicos](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
||  
||  [Static Badge](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
||  
||  [Documentacion de Curso que hize de MD en youtube](Aqui deberia ir la ruta para el curso de MD que hize cuando lo suba a un repositorio de GitHub)
||  
||  ### Extenciones para Visual Estudio Code
||  
||  > [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
||  
||  > [Markdown Preview Mermaid Suppor](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
||  
||  <!-- Aquí ya me siento bueno en markdown, así que solo pondre las herramientas que considere muy interesantes-->
||  
||  <Noa> Los comentarios que ponga en html <!-- comentario --> esos dejalos y este tema dejalo como esta o checa tu si quieres poner algo necesario, o ya se, ayudame poniendo los temas que necesito para aprender Mermaid, ese no lo se usar y se me hace muy interesante, en la uni hice un proyecto donde use 100% mermaid para hacer los diagramas y fuaa!, me volo la cabeza pero no tenia tiempo para detenerme a saber como funcionaba. </Noa>
||  
||  ## Creación de una Portada de Perfil en GitHub con Markdown
||  
||  Aprender a crear una portada atractiva y funcional en GitHub usando Markdown no solo mejora la presentación profesional de un perfil, sino que también permite personalizarlo con elementos visuales, enlaces y badges que muestran actividad e información de contacto. Aquí encontrarás un paso a paso para utilizar Markdown y hacer que tu perfil destaque.
||  
||  ### Herramientas de apoyo
||  
||  [Sintaxis de escritura y formartos basicos](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
||  
||  [Static Badge](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
||  
||  ### ¿Cómo iniciar el repositorio especial en GitHub?
||  
||  - Crear un repositorio: Ve a la sección de repositorios y crea uno nuevo usando el mismo nombre que tu nombre de usuario en GitHub; esto permite que el repositorio funcione como portada.
||  
||  - Descripción y visibilidad: Añade una descripción breve (ej. “Portada de perfil”), hazlo público y agrega un archivo README.md. Esto es esencial para que el contenido sea visible en tu perfil.
||  
||  - Clonación del repositorio: Clona el repositorio usando git clone en la terminal. La opción HTTPS es conveniente para nuevos perfiles, aunque SSH es más seguro.
||  
||  ### ¿Cómo personalizar el README con Markdown?
||  
||  Markdown facilita la creación de secciones y elementos visuales. Puedes agregar:
||  
||  - Títulos y subtítulos: Usa #, ## o ### según la jerarquía. Por ejemplo, ## Contacto.
||  - Enlaces y badges: Incluye enlaces usando [Texto](URL). Para badges, visita shields.io donde encontrarás diferentes opciones (ej. actividad de commits, sitios web).
||  - Iconos y emojis: Puedes agregar emojis como :computer: o :pencil: para destacar roles o actividades.
||  
||  ### ¿Cómo previsualizar y ajustar el archivo en Visual Studio Code?
||  
||  - Vista previa de Markdown: Selecciona Open Preview en la esquina superior derecha para ver cómo se verán los cambios en GitHub.
||  - Extensiones recomendadas: Markdown Lint ayuda a mejorar el estilo al sugerir tips sobre el formato, como evitar espacios en blanco innecesarios.
||  - Limpieza del código: Markdown Lint también ayuda a mantener el archivo ordenado eliminando líneas en blanco que no son necesarias.
||  
||  ### ¿Cómo añadir y ajustar badges en el perfil de GitHub?
||  
||  1. Visita shields.io y busca categorías de badges como:
||      - Website: Permite agregar un enlace a tu sitio web.
||      - Actividad de Commits: Muestra la frecuencia de tus commits en GitHub. Puedes seleccionar el intervalo: weekly, monthly, yearly, o total.
||  
||  2. Insertar badges en Markdown: Selecciona “Markdown” en shields.io para obtener el código y pégalo en el README.md.
||  3. Prueba de visualización: Asegúrate de que los badges se muestren correctamente en Visual Studio Code.
||  
||  ### ¿Qué estrategias aplicar para mejorar la portada en GitHub?
||  
||  - Referencias a otros repositorios: Examina perfiles de otros usuarios o proyectos con buena documentación. Visualiza su archivo README.md en modo “RAW” para ver el código en Markdown.
||  
||  - Explora y adapta: La práctica es clave; revisa diferentes perfiles para encontrar ideas y técnicas que puedas adaptar.
||  
---
---
---
---
---
---
---
