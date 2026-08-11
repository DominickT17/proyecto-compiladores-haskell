# Analizador Léxico de Haskell

Proyecto académico desarrollado para el curso de Compiladores.

El proyecto consiste en un analizador léxico para el lenguaje Haskell desarrollado con **Flex**, integrado con una interfaz gráfica desarrollada en **Python con Tkinter**.

La aplicación permite analizar archivos fuente `.hs`, identificar los diferentes componentes léxicos, visualizar los resultados, generar reportes en PDF y almacenar la tabla de símbolos en MongoDB Atlas.

## Responsables del repositorio

- **Dóminick Ricardo Cifuentes Tomás**
  - Carnet: 202408077
- **Yeisson Alexander Poroj Toc**
  - Carnet: 2002408068
- **Sandra Paola Gomez Diaz**
  - Carnet: 202408023

---

## Funcionalidades

El sistema permite:

- Seleccionar archivos fuente de Haskell (`.hs`).
- Visualizar el código fuente seleccionado.
- Ejecutar el analizador léxico desarrollado con Flex.
- Mostrar los tokens encontrados junto con:
  - Token
  - Lexema
  - Número de línea
- Reconocer palabras reservadas de Haskell.
- Reconocer identificadores y constructores.
- Reconocer números enteros.
- Reconocer números flotantes.
- Reconocer valores booleanos.
- Reconocer cadenas y caracteres.
- Reconocer operadores de Haskell.
- Mostrar estadísticas generales del análisis.
- Mostrar frecuencia de palabras reservadas.
- Generar reportes en formato PDF.
- Generar una tabla de símbolos.
- Guardar la tabla de símbolos en MongoDB Atlas.

---

## Tecnologías utilizadas

- Flex
- C
- Python 3
- Tkinter
- ReportLab
- PyMongo
- MongoDB Atlas
- python-dotenv
- Git
- GitHub

---

## Estructura del proyecto

```text
proyecto-compiladores-haskell/
│
├── database/
│   └── mongodb.py
│
├── docs/
│
├── gui/
│   └── app.py
│
├── lexer/
│   └── haskell_lexer.l
│
├── output/
│
├── reports/
│   ├── reporte1.py
│   └── reporte2.py
│
├── samples/
│
├── tests/
│
├── .env.example
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt
```

---

## Requisitos

Para ejecutar el proyecto se necesita:

- Python 3
- Flex
- GCC
- Make
- Tkinter
- Acceso a MongoDB Atlas

En Ubuntu se pueden instalar las herramientas principales con:

## Estado del proyecto

**Proyecto finalizado.**

Funcionalidades implementadas:

- [x] Repositorio creado en GitHub.
- [x] Repositorio clonado mediante SSH.
- [x] Entorno de trabajo preparado en Ubuntu.
- [x] Definición de lexemas y tokens.
- [x] Analizador léxico desarrollado con Flex.
- [x] Integración del lexer con Python.
- [x] Interfaz gráfica desarrollada con Tkinter.
- [x] Visualización del código fuente.
- [x] Visualización de tokens, lexemas y líneas.
- [x] Generación de estadísticas del análisis.
- [x] Generación del Reporte 1 en PDF.
- [x] Generación del Reporte 2 en PDF.
- [x] Generación de tabla de símbolos.
- [x] Persistencia de la tabla de símbolos en MongoDB Atlas.
- [x] Configuración mediante variables de entorno.
- [x] Compilación mediante Makefile.
- [x] Programa Haskell de prueba con más de 75 líneas.
- [x] Pruebas integrales del analizador.

---

## Programa Haskell de prueba

### Desarrolladora del programa de prueba

**Nombre:** Sandra Paola Gomez Diaz  
**Carné:** 202408023

### Contenido del programa

El archivo utilizado para las pruebas se encuentra en:

```text
samples/programa_completo.hs
```

El programa incluye:

- Palabras reservadas de Haskell.
- Identificadores repetidos.
- Números enteros.
- Números flotantes.
- Valores booleanos `True` y `False`.
- Cadenas de texto.
- Caracteres.
- Comentarios.
- Listas.
- Funciones.
- Condicionales.
- Pattern matching.
- Recursividad.
- Operadores aritméticos.
- Operadores lógicos.
- Operadores de comparación.

El programa representa un sistema sencillo de estudiantes y calificaciones utilizado como código fuente de prueba para el analizador léxico.

---

## Pruebas integrales

Se agregó documentación para comprobar el funcionamiento del analizador utilizando el programa Haskell completo.

Archivos relacionados:

- `samples/programa_completo.hs`
- `tests/validacion_programa_completo.md`
- `docs/guia_programa_prueba.md`

Estas pruebas permiten verificar que el analizador reconozca correctamente los diferentes lexemas presentes en el código fuente y genere los tokens y estadísticas correspondientes.

Aspectos verificados:

- [x] Programa Haskell de prueba con más de 75 líneas.
- [x] Inclusión de enteros, flotantes, booleanos y cadenas.
- [x] Inclusión de identificadores y palabras reservadas.
- [x] Inclusión de más de 10 operadores.
- [x] Documentación de la prueba integral del lexer.
- [x] Archivo de validación del programa Haskell.
