# Analizador Léxico de Haskell

Proyecto académico desarrollado para el curso de Compiladores.

El proyecto consiste en un analizador léxico para el lenguaje Haskell desarrollado con **Flex**, integrado con una interfaz gráfica desarrollada en **Python con Tkinter**.

La aplicación permite analizar archivos fuente `.hs`, identificar los diferentes componentes léxicos, visualizar los resultados, generar reportes en PDF y almacenar la tabla de símbolos en MongoDB Atlas.

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

```bash
sudo apt update
sudo apt install flex gcc make python3 python3-venv python3-tk
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
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

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Las principales dependencias de Python son:

- ReportLab
- PyMongo
- python-dotenv

---

## Compilar el analizador léxico

El proyecto incluye un `Makefile` para facilitar la compilación.

Ejecutar:

```bash
make lexer
```

Este comando utiliza Flex y GCC para generar el ejecutable del analizador a partir de:

```text
lexer/haskell_lexer.l
```

También puede utilizarse:

```bash
make clean
```

para eliminar los archivos generados durante la compilación.

---

## Configuración de MongoDB Atlas

Por seguridad, las credenciales de MongoDB no están almacenadas en el repositorio.

El proyecto incluye:

```text
.env.example
```

Crear un archivo llamado:

```text
.env
```

en la raíz del proyecto.

Agregar la cadena de conexión:

```text
MONGODB_URI=mongodb+srv://USUARIO:CONTRASENA@CLUSTER.mongodb.net/?appName=AnalizadorHaskell
```

Reemplazar los valores por las credenciales correspondientes de MongoDB Atlas.

> El archivo `.env` está incluido en `.gitignore` y no debe subirse al repositorio.

---

## Ejecutar la aplicación

Después de activar el entorno virtual y compilar el lexer:

```bash
make run
```

También puede ejecutarse directamente:

```bash
python gui/app.py
```

---

## Flujo de uso

1. Ejecutar la aplicación.
2. Presionar **Abrir archivo**.
3. Seleccionar un archivo Haskell `.hs`.
4. Presionar **Analizar código**.
5. Revisar los tokens y estadísticas obtenidas.
6. Generar el **Reporte 1** o **Reporte 2**.
7. Seleccionar el nombre y ubicación del archivo PDF.
8. Utilizar **Guardar MongoDB** para almacenar la tabla de símbolos.

---

## Reportes

### Reporte 1 - Estadísticas del análisis

Contiene información general del archivo analizado:

- Cantidad de líneas.
- Cantidad de caracteres.
- Enteros.
- Flotantes.
- Identificadores.
- Booleanos.
- Operadores.
- Palabras reservadas ordenadas por frecuencia.
- Archivo analizado.
- Fecha y hora de generación.

### Reporte 2 - Tokens y tabla de símbolos

Contiene:

- Token.
- Lexema.
- Número de línea.
- Tabla de símbolos.
- Identificadores.
- Constructores.
- Primera línea de aparición de cada símbolo.
- Archivo analizado.
- Fecha y hora de generación.

Los reportes son generados en formato PDF utilizando ReportLab.

---

## MongoDB Atlas

La aplicación utiliza MongoDB Atlas para almacenar la tabla de símbolos obtenida durante el análisis.

Cada símbolo almacena información como:

```text
lexema
token
linea
archivo
```

El sistema evita almacenar repetidamente los mismos símbolos de un análisis y permite mantener la información asociada al archivo fuente.

---

## Analizador léxico

El analizador fue desarrollado utilizando Flex y reconoce diferentes categorías léxicas de Haskell, incluyendo:

- Palabras reservadas.
- Identificadores.
- Constructores.
- Enteros.
- Decimales.
- Booleanos.
- Cadenas.
- Caracteres.
- Operadores.
- Símbolos de agrupación.
- Separadores.
- Comentarios.

Además, genera estadísticas que posteriormente son utilizadas por la interfaz gráfica y los reportes.

---

## Manejo de seguridad

El proyecto utiliza variables de entorno para proteger la cadena de conexión de MongoDB Atlas.

Los siguientes archivos y directorios no deben almacenarse en el repositorio:

```text
.env
.venv/
__pycache__/
*.pyc
lexer/lex.yy.c
lexer/haskell_lexer
```

Estos elementos están controlados mediante `.gitignore`.

---

## Autores

Proyecto desarrollado de forma colaborativa por los integrantes del equipo para el curso de Compiladores.

---

## Estado del proyecto

**Proyecto finalizado.**

Funcionalidades implementadas:

- Analizador léxico con Flex.
- Integración del lexer con Python.
- Interfaz gráfica.
- Visualización de código fuente.
- Visualización de tokens.
- Estadísticas.
- Reporte 1.
- Reporte 2.
- Tabla de símbolos.
- Persistencia en MongoDB Atlas.
- Configuración mediante variables de entorno.
- Compilación mediante Makefile.