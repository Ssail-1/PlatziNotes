from pathlib import Path
import re

README = Path("README.md")

INDEX_START = "<!-- INDEX_START -->"
INDEX_END = "<!-- INDEX_END -->"

# Carpetas tipo: "1-Comandos-Basicos", "2-Manipulacion-de-archivos", etc.
PATRON_CARPETA = re.compile(r"^(\d+)-(.+)$")

# Archivos tipo: "0-Comandos-utiles.md", "1-Despliegue-de-informacion.md", etc.
PATRON_ARCHIVO = re.compile(r"^(\d+)-(.+)\.md$", re.IGNORECASE)

def title_case_humano(texto: str) -> str:
    """Convierte 'Comandos-Basicos' -> 'Comandos basicos' (suave, sin inventar acentos)."""
    texto = texto.replace("-", " ").replace("_", " ").strip()
    # Capitaliza primera letra, deja lo demás igual (para no romper acrónimos tipo APT, AWK)
    return texto[:1].upper() + texto[1:]

def sort_key_num(nombre: str, patron: re.Pattern):
    m = patron.match(nombre)
    return int(m.group(1)) if m else 10**9

def build_index_block(base_dir: Path) -> str:
    """
    Genera el índice agrupado por carpetas numeradas.
    Cada carpeta se vuelve un subtítulo, y los archivos se listan con links relativos.
    """
    carpetas = [d for d in base_dir.iterdir() if d.is_dir() and PATRON_CARPETA.match(d.name)]
    carpetas.sort(key=lambda d: sort_key_num(d.name, PATRON_CARPETA))

    lineas = []

    for carpeta in carpetas:
        m_carpeta = PATRON_CARPETA.match(carpeta.name)
        nombre_modulo = m_carpeta.group(2) if m_carpeta else carpeta.name
        titulo_modulo = title_case_humano(nombre_modulo)

        # Título del módulo (como tu ejemplo: "Comandos basicos")
        lineas.append(f"### {titulo_modulo}\n")

        # Buscar archivos .md dentro, ordenados por número
        archivos = [f for f in carpeta.iterdir() if f.is_file() and f.suffix.lower() == ".md" and PATRON_ARCHIVO.match(f.name)]
        archivos.sort(key=lambda f: sort_key_num(f.name, PATRON_ARCHIVO))

        for archivo in archivos:
            m_arch = PATRON_ARCHIVO.match(archivo.name)
            titulo_raw = m_arch.group(2) if m_arch else archivo.stem
            titulo_leccion = title_case_humano(titulo_raw)

            # Link relativo tipo: ./1-Comandos-Basicos/0-Comandos-utiles.md
            link = f"./{carpeta.name}/{archivo.name}"
            lineas.append(f'- [{titulo_leccion}]({link} "{titulo_leccion}")')

        lineas.append("")  # línea en blanco entre módulos

    return "\n".join(lineas).strip() + "\n"

def insert_between_markers(text: str, block: str) -> str:
    if INDEX_START not in text or INDEX_END not in text:
        raise ValueError("README.md no tiene los marcadores INDEX_START / INDEX_END")

    before = text.split(INDEX_START)[0]
    after = text.split(INDEX_END)[1]
    return before + INDEX_START + "\n" + block + INDEX_END + after

def main():
    if not README.exists():
        raise FileNotFoundError("No existe README.md en esta carpeta.")

    contenido = README.read_text(encoding="utf-8")
    bloque = build_index_block(Path("."))

    nuevo = insert_between_markers(contenido, bloque)
    README.write_text(nuevo, encoding="utf-8")

    print("✅ Índice generado e insertado en README.md")

if __name__ == "__main__":
    main()
