import os

# Carpeta actual (donde están los .txt)
carpeta_actual = os.path.dirname(os.path.abspath(__file__))

# Listar todos los archivos .txt
archivos = [f for f in os.listdir(carpeta_actual) if f.endswith(".txt")]

for archivo in archivos:
    ruta_txt = os.path.join(carpeta_actual, archivo)
    nombre_base = os.path.splitext(archivo)[0]  # nombre sin extensión

    # Leer contenido del txt
    with open(ruta_txt, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Dividir en párrafos por saltos de línea dobles
    parrafos = contenido.split("\n\n")

    # Crear HTML con formato
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>{nombre_base}</title>
</head>
<body>
"""

    for p in parrafos:
        p = p.strip().replace("\n", " ")
        if p:
            html += f"  <p>{p}</p>\n"

    html += "</body>\n</html>"

    # Guardar archivo HTML con el mismo nombre
    ruta_html = os.path.join(carpeta_actual, nombre_base + ".html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Convertido: {archivo} → {nombre_base}.html")
