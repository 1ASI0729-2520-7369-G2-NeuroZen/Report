#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para convertir README.md a PDF con imagenes incluidas usando Playwright
"""

import markdown
import os
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

def convert_markdown_to_pdf(md_file, pdf_file):
    """Convierte un archivo Markdown a PDF con imagenes incluidas"""
    
    # Leer el archivo markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convertir markdown a HTML
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'fenced_code', 'toc'])
    html_content = md.convert(md_content)
    
    # Obtener la ruta base para las imagenes
    base_path = Path(md_file).parent.absolute()
    
    # Convertir rutas relativas de imagenes a rutas absolutas
    def convert_image_paths(html):
        # Convertir rutas en tags <img>
        def replace_img(match):
            src = match.group(1)
            if not src.startswith('http') and not os.path.isabs(src):
                # Es una ruta relativa, convertir a absoluta
                img_path = base_path / src
                if img_path.exists():
                    return f'<img src="{img_path.as_uri()}"'
            return match.group(0)
        
        # Reemplazar en tags <img src="...">
        html = re.sub(r'<img\s+src=["\']([^"\']+)["\']', replace_img, html)
        
        # También convertir rutas en markdown images ![alt](path)
        # Estas ya fueron convertidas por markdown, pero por si acaso
        return html
    
    html_content = convert_image_paths(html_content)
    
    # Crear HTML completo con estilos CSS
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 100%;
                padding: 20px;
            }}
            h1, h2, h3, h4, h5, h6 {{
                color: #2c3e50;
                margin-top: 1.5em;
                margin-bottom: 0.5em;
            }}
            h1 {{ font-size: 2em; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; }}
            h2 {{ font-size: 1.5em; border-bottom: 1px solid #95a5a6; padding-bottom: 0.3em; }}
            h3 {{ font-size: 1.3em; }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: 'Courier New', monospace;
                font-size: 0.9em;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 1em;
                border-radius: 5px;
                overflow-x: auto;
                border-left: 4px solid #3498db;
            }}
            pre code {{
                background-color: transparent;
                padding: 0;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin: 1em 0;
                font-size: 0.9em;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: 1em auto;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                margin: 1em 0;
                padding-left: 1em;
                color: #555;
            }}
            ul, ol {{
                margin: 1em 0;
                padding-left: 2em;
            }}
            li {{
                margin: 0.5em 0;
            }}
            a {{
                color: #3498db;
                text-decoration: none;
            }}
            hr {{
                border: none;
                border-top: 2px solid #ecf0f1;
                margin: 2em 0;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Guardar HTML temporal
    html_file = "temp_readme.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    # Convertir HTML a PDF usando Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Usar ruta absoluta para el HTML
        html_path = base_path / html_file
        page.goto(f"file:///{html_path.as_posix()}")
        # Esperar a que las imagenes se carguen
        page.wait_for_load_state('networkidle')
        page.pdf(path=pdf_file, format='A4', margin={'top': '2cm', 'right': '2cm', 'bottom': '2cm', 'left': '2cm'})
        browser.close()
    
    # Eliminar archivo temporal
    if os.path.exists(html_file):
        os.remove(html_file)
    
    print(f"PDF generado exitosamente: {pdf_file}")

if __name__ == "__main__":
    md_file = "README.md"
    pdf_file = "README.pdf"
    
    if not os.path.exists(md_file):
        print(f"Error: No se encontro el archivo {md_file}")
        exit(1)
    
    print(f"Convirtiendo {md_file} a PDF...")
    print("Instalando navegador de Playwright si es necesario...")
    
    # Instalar navegadores de Playwright si es necesario
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            p.chromium.launch()
    except Exception:
        print("Instalando Chromium para Playwright...")
        os.system("python -m playwright install chromium")
    
    convert_markdown_to_pdf(md_file, pdf_file)
