from pathlib import Path
import re

# =========================
# Configuración
# =========================

ARCHIVO_README = Path("github-essentials-notes.md")
ARCHIVOS_EXCLUIDOS = {"github-essentials-notes.md", "INDICE.md", "pendientes.md"}
PATRON_NOMBRE_MD = re.compile(r"^\d+_.+\.md$")

MARCADOR_INICIO = "<!-- INDEX_START -->"
MARCADOR_FIN = "<!-- INDEX_END -->"


# =========================
# Funciones
# =========================

def clave_de_orden(archivo_md: Path):
    """
    Extrae el número inicial del archivo (ej: 12_git_merge.md → 12)
    para poder ordenarlos correctamente.
    """
    coincidencia = re.match(r"^(\d+)_", archivo_md.name)
    numero = int(coincidencia.group(1)) if coincidencia else 10**9
    return (numero, archivo_md.name.lower())


# =========================
# Lógica principal
# =========================

carpeta_actual = Path(".")

# 1. Obtener archivos markdown válidos
archivos_md = [
    archivo for archivo in carpeta_actual.glob("*.md")
    if archivo.name not in ARCHIVOS_EXCLUIDOS
    and PATRON_NOMBRE_MD.match(archivo.name)
]

# 2. Ordenarlos por número
archivos_md = sorted(archivos_md, key=clave_de_orden)

# 3. Construir las líneas del índice
lineas_indice = [
    f'[{archivo.stem}]({archivo.name} "{archivo.stem}")'
    for archivo in archivos_md
]

bloque_indice = "\n".join(lineas_indice)

# 4. Validar README
if not ARCHIVO_README.exists():
    raise FileNotFoundError("README.md no existe en esta carpeta.")

contenido_readme = ARCHIVO_README.read_text(encoding="utf-8")

if MARCADOR_INICIO not in contenido_readme or MARCADOR_FIN not in contenido_readme:
    raise ValueError("Faltan los marcadores INDEX_START o INDEX_END en README.md.")

# 5. Insertar el índice entre los marcadores
nuevo_readme = (
    contenido_readme.split(MARCADOR_INICIO)[0]
    + MARCADOR_INICIO
    + "\n\n"
    + bloque_indice
    + "\n\n"
    + MARCADOR_FIN
    + contenido_readme.split(MARCADOR_FIN)[1]
)

ARCHIVO_README.write_text(nuevo_readme, encoding="utf-8")

print("✅ Índice insertado correctamente en README.md")
