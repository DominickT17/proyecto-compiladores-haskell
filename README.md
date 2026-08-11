# Analizador léxico de Haskell

Proyecto corto del curso de Compiladores orientado al análisis léxico de archivos escritos en el lenguaje Haskell.

## Datos académicos

- Universidad: Universidad Mesoamericana
- Sede: Quetzaltenango
- Curso: Compiladores
- Sección: E
- Docente: Ing. Erick Juan José de Paz Rivera
- Lenguaje asignado: Haskell

## Responsables del repositorio

- Dóminick Ricardo Cifuentes Tomás
- Carnet: 202408077
- Yeisson Alexander Poroj Toc
- Carnet: 2002408068
- Sandra Paola Gomez Diaz
- 202408023


## Objetivo general

Desarrollar un analizador léxico que procese archivos fuente escritos en Haskell e identifique los diferentes lexemas y tokens presentes en el código.

El proyecto utilizará Flex para generar el analizador léxico y posteriormente integrará una interfaz gráfica, reportes en PDF y almacenamiento de la tabla de símbolos en MongoDB.

## Tecnologías previstas

- Flex
- Lenguaje C
- Python
- MongoDB
- Git y GitHub
- Visual Studio Code
- Haskell como lenguaje analizado

# Interfaz gráfica - Analizador lexico

Este directorio contiene la interfaz gráfica del analizador lexico de Haskell, desarrollada utilizando python y tkinter

## Desarrollador de la interfaz

- Nombre: Yeisson Alexander Poroj Toc
- Carnet: 202408068

## FUncionamiento 

La interfaz permitirá: 

- Seleccionar archivos de código fuente haskell
- Visualizar el código fuente
- Ejecutar el analisis léxico
- Mostrar los tokens encontrados
- MOstrar las estadísticas obtenidas durante el análisis

## Estado actual

- [x] Repositorio creado en GitHub
- [x] Repositorio clonado mediante SSH
- [x] Entorno de trabajo preparado en Ubuntu
- [ ] Definición formal de lexemas y tokens
- [ ] Desarrollo del analizador con Flex
- [ ] Desarrollo de la interfaz gráfica
- [ ] Generación de reportes PDF
- [ ] Integración con MongoDB

      
## Desarrolladora del programa de prueba

Nombre: Sandra Paola Gomez Diaz
Carnet:202408023

## Contenido del programa

El archivo utilizado para las pruebas se encuentra en:

`samples/programa_completo.hs`

El programa incluye:

- Palabras reservadas de Haskell
- Identificadores repetidos
- Números enteros
- Números flotantes
- Valores booleanos `True` y `False`
- Cadenas de texto
- Caracteres
- Comentarios
- Listas
- Funciones
- Condicionales
- Pattern matching
- Recursividad
- Operadores aritméticos
- Operadores lógicos
- Operadores de comparación

El programa representa un sistema sencillo de estudiantes y calificaciones, utilizado únicamente como código fuente de prueba para el analizador léxico.

## Pruebas integrales

También se agregó documentación para comprobar el funcionamiento del lexer utilizando el programa Haskell completo.

Archivos relacionados:

- `samples/programa_completo.hs`
- `tests/validacion_programa_completo.md`
- `docs/guia_programa_prueba.md`

La prueba permite verificar que el analizador reconozca correctamente los diferentes lexemas presentes en el código fuente y genere los tokens y estadísticas correspondientes
- [x] Programa Haskell de prueba con más de 75 líneas
- [x] Inclusión de enteros, flotantes, booleanos y cadenas
- [x] Inclusión de identificadores y palabras reservadas
- [x] Inclusión de más de 10 operadores
- [x] Documentación de la prueba integral del lexer
- [x] Archivo de validación del programa Haskell
