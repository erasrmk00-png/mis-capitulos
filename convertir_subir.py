import os

# Carpeta donde están los archivos .txt
carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Archivos")

# 1. Borrar todos los .html existentes
for f in os.listdir(carpeta):
    if f.endswith(".html"):
        os.remove(os.path.join(carpeta, f))
        print(f"Eliminado: {f}")

# 2. Convertir todos los .txt en .html
txt_files = [f for f in os.listdir(carpeta) if f.endswith(".txt")]

for archivo in txt_files:
    ruta_txt = os.path.join(carpeta, archivo)
    nombre_base = os.path.splitext(archivo)[0]

    with open(ruta_txt, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Dividir en párrafos por saltos dobles
    parrafos = contenido.split("\n\n")

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>{nombre_base}</title>
  <style>
    body {{ font-family: Arial, sans-serif; background: #fdfdfd; color: #333; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; }}
    p {{ margin-bottom: 15px; }}
  </style>
</head>
<body>
"""

    for p in parrafos:
        p = p.strip().replace("\n", " ")
        if p:
            html += f"  <p>{p}</p>\n"

    html += "</body>\n</html>"

    ruta_html = os.path.join(carpeta, nombre_base + ".html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Convertido: {archivo} → {nombre_base}.html")

# 3. Generar index.html con enlaces a todos los .html
html_files = [f for f in os.listdir(carpeta) if f.endswith(".html") and f != "index.html"]

index_html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Índice de capítulos</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f9f9f9; color: #333; }
    h2 { text-align: center; margin-top: 30px; }
    ul { list-style: none; padding: 0; max-width: 600px; margin: 30px auto; }
    li { margin: 10px 0; }
    a { text-decoration: none; color: #0066cc; font-size: 18px; }
    a:hover { text-decoration: underline; }
    .container { text-align: center; }
  </style>
</head>
<body>
  <h2>Capítulos disponibles</h2>
  <div class="container">
    <ul>
"""

for archivo in sorted(html_files):
    nombre_base = os.path.splitext(archivo)[0]
    index_html += f'      <li><a href="{archivo}">{nombre_base}</a></li>\n'

index_html += """    </ul>
  </div>
</body>
</html>
"""

ruta_index = os.path.join(carpeta, "index.html")
with open(ruta_index, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Generado: index.html con enlaces a todos los capítulos")
