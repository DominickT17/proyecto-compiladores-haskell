# Plan inicial del proyecto

## 1. Nombre del proyecto

Analizador léxico de código fuente Haskell.

## 2. Descripción

El proyecto consiste en desarrollar una aplicación capaz de recibir un archivo
fuente escrito en Haskell y realizar su análisis léxico.

Durante el análisis se identificarán los lexemas encontrados, el tipo de token
al que pertenece cada uno y la información necesaria para construir una tabla
de símbolos.

## 3. Objetivo general

Desarrollar un analizador léxico para archivos escritos en Haskell utilizando
Flex como generador del analizador.

## 4. Componentes previstos

El proyecto estará formado por los siguientes componentes:

1. Un archivo de entrada escrito en Haskell.
2. Un analizador léxico desarrollado mediante Flex y lenguaje C.
3. Una salida estructurada con los tokens encontrados.
4. Una tabla de símbolos.
5. Una interfaz gráfica para seleccionar y analizar archivos.
6. Reportes en formato PDF.
7. Almacenamiento de información mediante MongoDB.
8. Archivos de prueba para verificar el funcionamiento del analizador.

## 5. Alcance inicial

La primera etapa se enfocará en estudiar y definir los elementos léxicos que
deben reconocerse en Haskell.

Entre los elementos previstos se encuentran:

- Palabras reservadas.
- Identificadores.
- Números enteros.
- Números decimales.
- Cadenas de texto.
- Caracteres.
- Valores booleanos.
- Operadores.
- Signos de agrupación.
- Separadores.
- Comentarios.
- Espacios y saltos de línea.
- Caracteres no reconocidos.

La lista definitiva será establecida en la especificación léxica antes de
comenzar la implementación completa en Flex.

## 6. Organización del repositorio

La estructura inicial prevista es la siguiente:

- `docs`: documentación y especificaciones.
- `lexer`: archivos relacionados con Flex y C.
- `samples`: archivos Haskell utilizados como entrada.
- `gui`: código de la interfaz gráfica.
- `database`: integración con MongoDB.
- `output`: archivos generados por el programa.
- `tests`: pruebas del analizador.

Las carpetas serán agregadas al repositorio cuando contengan archivos
relacionados con un avance real del proyecto.

## 7. Forma de trabajo

El desarrollo se realizará mediante Git y GitHub.

Cada avance deberá cumplir con el siguiente procedimiento:

1. Actualizar la rama principal.
2. Crear una rama específica para la tarea.
3. Realizar cambios pequeños y relacionados.
4. Revisar los archivos modificados.
5. Probar el funcionamiento del avance.
6. Crear commits con mensajes descriptivos.
7. Subir la rama a GitHub.
8. Revisar los cambios antes de integrarlos en `main`.

## 8. Organización del equipo

El proyecto será desarrollado por tres integrantes.

Cada integrante trabajará desde su propia cuenta de GitHub y deberá participar
mediante commits, ramas y operaciones de actualización del repositorio.

Los nombres, carnets, usuarios de GitHub y responsabilidades específicas serán
agregados cuando se complete la organización del equipo.

## 9. Estado actual

- Repositorio creado y conectado con GitHub.
- Entorno de trabajo preparado en Ubuntu.
- Documentación inicial agregada.
- Planificación inicial en desarrollo.
- Especificación léxica pendiente.
- Implementación del lexer pendiente.
- Interfaz gráfica pendiente.
- Reportes PDF pendientes.
- Integración con MongoDB pendiente.