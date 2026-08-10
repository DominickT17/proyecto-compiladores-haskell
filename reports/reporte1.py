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

def generar_reporte1(
    ruta_salida,
    estadisticas,
    palabras_reservadas,
    archivo_fuente
):
    documento = SimpleDocTemplate(
        ruta_salida,
        pagesize=letter
    )

    estilos = getSampleStyleSheet()
    contenido = []

    titulo = Paragraph(
        "Reporte 1 - Análisis Léxico de Haskell",
        estilos["Title"]
    )

    contenido.append(titulo)
    contenido.append(Spacer(1, 15))

    contenido.append(
        Paragraph(
            f"Archivo analizado: {archivo_fuente}",
            estilos["Normal"]
        )
    )

    contenido.append(Spacer(1, 15))

    datos_estadisticas = [
        ["Estadisticas", "Cantidad"],
        ["Lienas", estadisticas.get("lineas", "0")],
        ["Caracteres", estadisticas.get("caracteres", "0")],
        ["Enteros", estadisticas.get("enteros", "0")],
        ["Flotantes", estadisticas.get("flotantes", "0")],
        [
            "Identificadores",
            estadisticas.get("identificadores", "0")
        ],
        ["Booleanos", estadisticas.get("booleanos", "0")],
        ["Operadores", estadisticas.get("operadores", "0")]
    ]

    tabla_estadisticas = Table(
        datos_estadisticas,
        colWidths=[250, 150]
    )

    tabla_estadisticas.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7)
        ])
    )

    contenido.append(
        Paragraph(
            "Resumen del archivo",
            estilos["Heading2"]
        )
    )

    contenido.append(Spacer(1, 8))
    contenido.append(tabla_estadisticas)
    contenido.append(Spacer(1, 20))

    contenido.append(
        Paragraph(
            "Palabras reservadas por frecuencia",
            estilos["Heading2"]
        )
    )

    contenido.append(Spacer(1, 8))

    datos_palabras = [
        ["Palabra reservada", "Cantidad"]
    ]

    for palabra in palabras_reservadas:
        datos_palabras.append([
            palabra["palabra"],
            palabra["cantidad"]
        ])

    tabla_palabras =Table(
        datos_palabras,
        colWidths=[250, 150]
    )

    tabla_palabras.setStyle(
        TableStyle([
            ("BACKGOUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("ALGIN", (1, 1), (1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7)
        ])
    )

    contenido.append(tabla_palabras)

    documento.build(contenido)
