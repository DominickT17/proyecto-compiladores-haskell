import os
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generar_reporte2(
    ruta_salida,
    tokens,
    archivo_fuente
):
    documento = SimpleDocTemplate(
        ruta_salida,
        pagesize=letter
    )

    estilos = getSampleStyleSheet()
    contenido = []

    # Título principal
    titulo = Paragraph(
        "Reporte 2 - Tokens y Tabla de Símbolos",
        estilos["Title"]
    )

    contenido.append(titulo)
    contenido.append(Spacer(1, 15))

    # Información del archivo analizado
    nombre_archivo = os.path.basename(archivo_fuente)

    contenido.append(
        Paragraph(
            f"Archivo analizado: {nombre_archivo}",
            estilos["Normal"]
        )
    )

    fecha_generacion = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    contenido.append(
        Paragraph(
            f"Fecha de generación: {fecha_generacion}",
            estilos["Normal"]
        )
    )

    contenido.append(Spacer(1, 20))

    # Tabla de lexemas encontrados
    contenido.append(
        Paragraph(
            "Lexemas encontrados",
            estilos["Heading2"]
        )
    )

    contenido.append(Spacer(1, 8))

    datos_tokens = [
        ["Token", "Lexema", "Línea"]
    ]

    for token in tokens:
        datos_tokens.append([
            token["token"],
            token["lexema"],
            token["linea"]
        ])

    tabla_tokens = Table(
        datos_tokens,
        colWidths=[150, 270, 60],
        repeatRows=1
    )

    tabla_tokens.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("ALIGN", (2, 1), (2, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5)
        ])
    )

    contenido.append(tabla_tokens)
    contenido.append(Spacer(1, 20))

    # -----------------------------
    # Tabla de símbolos
    # -----------------------------

    contenido.append(
        Paragraph(
            "Tabla de Símbolos",
            estilos["Heading2"]
        )
    )

    contenido.append(Spacer(1, 8))

    datos_simbolos = [
        ["Lexema", "Token", "Primera línea"]
    ]

    simbolos_vistos = set()

    for token in tokens:
        if token["token"] in (
            "IDENTIFICADOR",
            "CONSTRUCTOR"
        ):
            clave = (
                token["lexema"],
                token["token"]
            )

            if clave not in simbolos_vistos:
                simbolos_vistos.add(clave)

                datos_simbolos.append([
                    token["lexema"],
                    token["token"],
                    token["linea"]
                ])

    # Si no se encontraron símbolos
    if len(datos_simbolos) == 1:
        datos_simbolos.append([
            "No se encontraron símbolos",
            "-",
            "-"
        ])

    tabla_simbolos = Table(
        datos_simbolos,
        colWidths=[220, 180, 80],
        repeatRows=1
    )

    tabla_simbolos.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("ALIGN", (2, 1), (2, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5)
        ])
    )

    contenido.append(tabla_simbolos)

    # Crear físicamente el PDF
    documento.build(contenido)