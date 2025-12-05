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
    # Usar nl2br para preservar saltos de línea (convierte \n en <br>)
    extensions_list = ['extra', 'codehilite', 'tables', 'fenced_code', 'toc']
    try:
        # Intentar agregar nl2br si está disponible
        extensions_list.append('nl2br')
        md = markdown.Markdown(extensions=extensions_list)
        html_content = md.convert(md_content)
    except Exception:
        # Si nl2br no está disponible, usar sin esa extensión
        # y procesar manualmente los saltos de línea
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'fenced_code', 'toc'])
        html_content = md.convert(md_content)
        # Convertir saltos de línea dentro de párrafos en <br>
        # Solo dentro de tags <p>, no en otros elementos
        def replace_newlines_in_paragraphs(match):
            content = match.group(1)
            # Reemplazar \n con <br> pero preservar \n\n como separadores de párrafo
            content = re.sub(r'(?<!\n)\n(?!\n)', '<br>', content)
            return f'<p>{content}</p>'
        html_content = re.sub(r'<p>(.*?)</p>', replace_newlines_in_paragraphs, html_content, flags=re.DOTALL)
    
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
    
    # Remover atributos border de las tablas HTML y agregar estilos inline
    def fix_table_borders(html):
        # Remover atributo border de las tablas
        html = re.sub(r'<table\s+([^>]*?)\s*border\s*=\s*["\']?\d+["\']?([^>]*)>', 
                     r'<table \1\2>', html, flags=re.IGNORECASE)
        html = re.sub(r'<table\s+border\s*=\s*["\']?\d+["\']?([^>]*)>', 
                     r'<table\1>', html, flags=re.IGNORECASE)
        
        # Agregar bordes inline a todas las celdas th y td
        def add_border_to_cell(match):
            full_tag = match.group(0)
            # Si ya tiene style, agregar border al final
            if 'style=' in full_tag.lower():
                result = re.sub(r'(style\s*=\s*["\'])([^"\']*)(["\'])', 
                               r'\1\2; border: 1.5px solid #000 !important; \3', 
                               full_tag, flags=re.IGNORECASE)
                return result
            else:
                # Agregar style completo
                return full_tag.replace('>', ' style="border: 1.5px solid #000 !important;">')
        
        # Aplicar a todas las celdas
        html = re.sub(r'<(th|td)([^>]*)>', add_border_to_cell, html, flags=re.IGNORECASE)
        
        return html
    
    html_content = fix_table_borders(html_content)
    
    # Eliminar todos los tags <hr> (líneas horizontales) del HTML
    html_content = re.sub(r'<hr\s*/?>', '', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<hr\s+[^>]*>', '', html_content, flags=re.IGNORECASE)
    
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
            p {{
                white-space: pre-line;
                margin: 1em 0;
            }}
            /* Evitar que las tablas hereden white-space: pre-line */
            table p {{
                white-space: normal;
                margin: 0;
            }}
            /* Controlar saltos de línea dentro de las celdas */
            table td, table th {{
                line-height: 1.4;
            }}
            /* Limitar saltos de línea excesivos en tablas */
            table br {{
                display: block;
                content: "";
                margin-top: 0.3em;
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
            /* Estilos de tabla - máxima especificidad */
            table, table[border], table * {{
                border-collapse: collapse !important;
                border-spacing: 0 !important;
            }}
            table {{
                width: 100% !important;
                margin: 1em 0 !important;
                font-size: 0.9em !important;
                border: 2px solid #000 !important;
            }}
            /* Bordes para TODAS las celdas - máxima prioridad */
            table th,
            table td,
            table[border] th,
            table[border] td,
            th[style*="border"],
            td[style*="border"] {{
                border-top: 1.5px solid #000 !important;
                border-right: 1.5px solid #000 !important;
                border-bottom: 1.5px solid #000 !important;
                border-left: 1.5px solid #000 !important;
                padding: 8px !important;
                text-align: left !important;
                white-space: normal !important;
                vertical-align: top !important;
            }}
            th {{
                background-color: #3498db !important;
                color: white !important;
                font-weight: bold !important;
            }}
            tr {{
                border: none !important;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2 !important;
            }}
            /* Asegurar bordes incluso en celdas con rowspan/colspan */
            th[rowspan],
            td[rowspan],
            th[colspan],
            td[colspan],
            table th[rowspan],
            table td[rowspan],
            table th[colspan],
            table td[colspan] {{
                border-top: 1.5px solid #000 !important;
                border-right: 1.5px solid #000 !important;
                border-bottom: 1.5px solid #000 !important;
                border-left: 1.5px solid #000 !important;
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
                display: none !important;
                border: none !important;
                margin: 0 !important;
                padding: 0 !important;
                height: 0 !important;
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
