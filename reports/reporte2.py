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

    contenido.append(
        Paragraph(
            "Reporte 2 - Tokens y Tabla de Símbolos",
            estilos["Title"]
        )
    )

    contenido.append(Spacer(1, 15))

    contenido.append(
        Paragraph(
            f"Archivo analizado: {archivo_fuente}",
            estilos["Normal"]
        )
    )

    contenido.append(Spacer(1, 15))

    # Tabla de tokens
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
            ("BACKGROUND", (0,0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("ALIGN", (2, 1), (2, -1), "CENTER"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5)
        ])
    )

    contenido.append(tabla_tokens)
    contenido.append(Spacer(1, 20))

    # Tabla de símbolos
    contenido.append(
        Paragraph(
            "Tabla de Símbolos",
            estilos["Heading2"]
        )
    )

    contenido.append(Spacer(1, 8))

    datos_simbolos = [
        ["Lexema", "Token", "Línea"]
    ]

    for token in tokens:
        if token["token"] in (
            "IDENTIFICADOR",
            "CONSTRUCTOR"
        ):
            datos_simbolos.append([
                token["lexema"],
                token["token"],
                token["linea"]
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
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5)
        ])
    )

    contenido.append(tabla_simbolos)

    documento.build(contenido)



