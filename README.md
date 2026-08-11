# Analizador Léxico de Haskell

## Integrantes

- **Dóminick Ricardo Cifuentes Tomás**  
  Carné: 202408077

- **Yeisson Alexander Poroj Toc**  
  Carné: 202408068

- **Sandra Paola Gomez Diaz**  
  Carné: 202408023

---

## Descripción del proyecto

Proyecto académico desarrollado para el curso de Compiladores.

El sistema consiste en un analizador léxico para el lenguaje de programación **Haskell**, desarrollado utilizando **Flex** e integrado con una interfaz gráfica creada en **Python con Tkinter**.

La aplicación permite seleccionar archivos fuente con extensión `.hs`, ejecutar el análisis léxico, visualizar los lexemas encontrados, generar estadísticas, crear reportes en formato PDF y almacenar la tabla de símbolos en una base de datos no relacional utilizando MongoDB Atlas.

---

## Funcionalidades

El proyecto permite:

- Seleccionar archivos Haskell con extensión `.hs`.
- Mostrar el código fuente dentro de la interfaz.
- Ejecutar el analizador léxico desarrollado con Flex.
- Mostrar cada lexema encontrado.
- Mostrar el token correspondiente a cada lexema.
- Mostrar el número de línea en el que fue encontrado.
- Reconocer palabras reservadas de Haskell.
- Reconocer identificadores.
- Reconocer constructores.
- Reconocer números enteros.
- Reconocer números flotantes.
- Reconocer valores booleanos.
- Reconocer cadenas.
- Reconocer caracteres.
- Reconocer comentarios.
- Reconocer símbolos de agrupación.
- Reconocer separadores.
- Reconocer más de 10 operadores.
- Mostrar estadísticas generales del archivo.
- Mostrar la frecuencia de palabras reservadas.
- Generar el Reporte 1 en formato PDF.
- Generar el Reporte 2 en formato PDF.
- Generar una tabla de símbolos.
- Guardar la tabla de símbolos en MongoDB Atlas.
- Evitar duplicados de símbolos al almacenar nuevamente un mismo archivo.

---

## Tecnologías utilizadas

- Flex
- C
- GCC
- Python 3
- Tkinter
- ReportLab
- PyMongo
- MongoDB Atlas
- python-dotenv
- Make
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
│   └── guia_programa_prueba.md
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
│   ├── ejemplo_basico.hs
│   └── programa_completo.hs
│
├── tests/
│   └── validacion_programa_completo.md
│
├── .env.example
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt
```

---

## Requisitos

Para ejecutar el proyecto en Ubuntu se necesita:

- Python 3
- Flex
- GCC
- Make
- Tkinter
- Acceso a MongoDB Atlas

Las herramientas principales pueden instalarse con:

```bash
sudo apt update
sudo apt install flex gcc make python3 python3-venv python3-tk
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone git@github.com:DominickT17/proyecto-compiladores-haskell.git
cd proyecto-compiladores-haskell
```

### 2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

### 3. Instalar las dependencias de Python

```bash
pip install -r requirements.txt
```

Las dependencias principales son:

- `reportlab`
- `pymongo`
- `python-dotenv`

---

## Compilación del analizador léxico

El proyecto incluye un `Makefile` para simplificar la compilación del lexer.

Ejecutar:

```bash
make lexer
```

Este comando utiliza Flex y GCC para generar el ejecutable del analizador a partir de:

```text
lexer/haskell_lexer.l
```

Para eliminar los archivos generados durante la compilación puede utilizarse:

```bash
make clean
```

---

## Configuración de MongoDB Atlas

La tabla de símbolos se almacena en MongoDB Atlas.

Las credenciales de conexión no se incluyen directamente en el repositorio.

El proyecto contiene:

```text
.env.example
```

Debe crearse un archivo llamado:

```text
.env
```

en la raíz del proyecto.

Dentro debe agregarse la cadena de conexión correspondiente:

```text
MONGODB_URI=mongodb+srv://USUARIO:CONTRASENA@CLUSTER.mongodb.net/?appName=AnalizadorHaskell
```

Los valores deben reemplazarse por las credenciales reales de MongoDB Atlas.

> El archivo `.env` se encuentra protegido mediante `.gitignore` y no debe subirse al repositorio.

---

## Ejecución de la aplicación

Después de activar el entorno virtual y compilar el lexer:

```bash
make run
```

También puede ejecutarse directamente con:

```bash
python gui/app.py
```

---

## Flujo de uso

1. Ejecutar la aplicación.
2. Presionar **Abrir archivo**.
3. Seleccionar un archivo Haskell con extensión `.hs`.
4. Presionar **Analizar código**.
5. Revisar el código fuente cargado.
6. Revisar los tokens, lexemas y líneas encontrados.
7. Revisar las estadísticas obtenidas.
8. Generar el **Reporte 1**.
9. Generar el **Reporte 2**.
10. Seleccionar el nombre y ubicación de los archivos PDF.
11. Presionar **Guardar MongoDB** para almacenar la tabla de símbolos.

---

## Analizador léxico

El analizador fue desarrollado utilizando Flex.

Reconoce las siguientes categorías léxicas:

- Palabras reservadas.
- Identificadores.
- Constructores.
- Números enteros.
- Números decimales.
- Valores booleanos.
- Cadenas.
- Caracteres.
- Comentarios.
- Operadores.
- Símbolos de agrupación.
- Separadores.

Entre los operadores reconocidos se encuentran:

- `=`
- `+`
- `-`
- `*`
- `/`
- `^`
- `>`
- `<`
- `>=`
- `<=`
- `==`
- `/=`
- `&&`
- `||`
- `++`
- `!!`
- `->`
- `<-`
- `::`

Además, el lexer genera estadísticas que son utilizadas posteriormente por la interfaz gráfica y los reportes.

---

## Estadísticas generadas

Después del análisis se muestran:

- Cantidad de líneas.
- Cantidad de caracteres.
- Cantidad de números enteros.
- Cantidad de números flotantes.
- Cantidad de identificadores.
- Cantidad de valores booleanos.
- Cantidad de operadores.

También se obtiene el conteo de palabras reservadas encontradas y su frecuencia.

---

## Reporte 1

El Reporte 1 contiene:

- Nombre del archivo analizado.
- Fecha y hora de generación.
- Cantidad de líneas.
- Cantidad de caracteres.
- Cantidad de enteros.
- Cantidad de flotantes.
- Cantidad de identificadores.
- Cantidad de booleanos.
- Cantidad de operadores.
- Palabras reservadas encontradas.
- Frecuencia de cada palabra reservada.

Las palabras reservadas se muestran según la frecuencia obtenida durante el análisis.

El reporte se genera en formato PDF utilizando ReportLab.

---

## Reporte 2

El Reporte 2 contiene:

- Nombre del archivo analizado.
- Fecha y hora de generación.
- Token.
- Lexema.
- Número de línea.
- Tabla de símbolos.

La tabla de símbolos incluye identificadores y constructores encontrados durante el análisis, evitando repetir innecesariamente el mismo símbolo.

El reporte se genera en formato PDF utilizando ReportLab.

---

## Tabla de símbolos

La tabla de símbolos utiliza información obtenida directamente del lexer.

Cada símbolo contiene información como:

```text
Lexema
Token
Primera línea de aparición
```

Los identificadores y constructores son considerados símbolos del programa analizado.

---

## MongoDB Atlas

La aplicación utiliza una base de datos no relacional en MongoDB Atlas.

La base de datos utilizada es:

```text
analizador_haskell
```

La colección utilizada es:

```text
tabla_simbolos
```

Cada documento puede almacenar:

```text
lexema
token
linea
archivo
```

Antes de guardar nuevamente los símbolos correspondientes a un mismo archivo, se eliminan los registros anteriores asociados a ese archivo para evitar duplicaciones innecesarias.

---

## Programa Haskell de prueba

El archivo principal utilizado para realizar las pruebas integrales se encuentra en:

```text
samples/programa_completo.hs
```

Este archivo contiene más de 75 líneas de código Haskell y fue preparado para cubrir las distintas categorías requeridas por el proyecto.

Incluye:

- Palabras reservadas.
- Identificadores repetidos.
- Enteros.
- Flotantes.
- Valores booleanos `True` y `False`.
- Cadenas.
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

El programa representa un sistema sencillo de estudiantes y calificaciones utilizado como entrada para probar el analizador.

---

## Pruebas integrales

La documentación de las pruebas se encuentra en:

```text
tests/validacion_programa_completo.md
```

También se incluye:

```text
docs/guia_programa_prueba.md
```

Estas pruebas permiten verificar el funcionamiento del lexer utilizando el programa Haskell completo.

Se validó:

- [x] Archivo Haskell con más de 75 líneas.
- [x] Palabras reservadas.
- [x] Identificadores.
- [x] Enteros.
- [x] Flotantes.
- [x] Booleanos.
- [x] Cadenas.
- [x] Más de 10 operadores.
- [x] Visualización de tokens.
- [x] Estadísticas.
- [x] Reporte 1.
- [x] Reporte 2.
- [x] Tabla de símbolos.
- [x] MongoDB Atlas.

---

## Seguridad

El proyecto utiliza variables de entorno para proteger la cadena de conexión con MongoDB Atlas.

Los siguientes archivos y directorios no deben subirse al repositorio:

```text
.env
.venv/
venv/
__pycache__/
*.pyc
*.pyo
lexer/lex.yy.c
lexer/haskell_lexer
```

Estos elementos están configurados dentro de `.gitignore`.

---

## Estado del proyecto

**Proyecto finalizado.**

Se encuentran implementadas las funcionalidades solicitadas:

- [x] Analizador léxico con Flex.
- [x] Interfaz gráfica.
- [x] Apertura de archivos Haskell.
- [x] Visualización de código fuente.
- [x] Tokens específicos.
- [x] Lexemas y líneas.
- [x] Estadísticas.
- [x] Conteo de palabras reservadas.
- [x] Reporte 1.
- [x] Reporte 2.
- [x] Tabla de símbolos.
- [x] MongoDB Atlas.
- [x] Archivo Haskell de más de 75 líneas.
- [x] Configuración mediante variables de entorno.
- [x] Dependencias mediante `requirements.txt`.
- [x] Compilación mediante `Makefile`.
- [x] Documentación del proyecto.