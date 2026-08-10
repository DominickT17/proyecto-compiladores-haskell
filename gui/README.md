# Interfaz Gráfica - Analizador Léxico de Haskell

Interfaz gráfica desarrollada con Python y Tkinter para el Proyecto Corto #1
del curso de Compiladores.

## Desarrollador de la interfaz

- Nombre: Yeisson Alexander Poroj Toc
- Carné: 202408068

## Funcionalidades implementadas

La interfaz permite actualmente:

- Seleccionar archivos Haskell con extensión `.hs`.
- Mostrar la ruta del archivo seleccionado.
- Visualizar el código fuente Haskell.
- Validar que el archivo seleccionado sea `.hs`.
- Mostrar una tabla con Token, Lexema y Línea.
- Cargar tokens simulados desde `mock_tokens.json`.
- Evitar resultados duplicados al realizar varios análisis.
- Mostrar estadísticas del archivo.
- Contar líneas y caracteres.
- Mostrar estadísticas simuladas de:
  - Enteros.
  - Flotantes.
  - Identificadores.
  - Booleanos.
  - Operadores.
- Mostrar mensajes de estado y validaciones.

## Ejecución

Desde la raíz del proyecto ejecutar:

```bash
python3 gui/app.py