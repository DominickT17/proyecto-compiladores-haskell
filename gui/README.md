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


## Instalacion

### 1. Crear entorno virtual

```bash
python3 .m venv .venv
source .venv/bin/activate

### 2. Instalar dependencias

Las dependencias necesarias se encuentran en `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 3. Compilar el analizador léxico

El analizador fue desarrollado utilizando Flex. Para compilarlo:

```bash
make lexer
```

Este comando genera el ejecutable necesario para que la interfaz pueda comunicarse con el analizador léxico.

### 4. Configurar MongoDB Atlas

Crear un archivo `.env` en la raíz del proyecto tomando como referencia `.env.example`.

```text
MONGODB_URI=mongodb+srv://USUARIO:CONTRASENA@CLUSTER.mongodb.net/
```

El archivo `.env` contiene las credenciales de conexión y no debe subirse al repositorio.

### 5. Ejecutar la aplicación

Con el entorno virtual activado:

```bash
make run
```

También puede ejecutarse directamente con:

```bash
python gui/app.py
```

## Funcionalidades principales

- Selección y visualización de archivos Haskell.
- Análisis léxico mediante Flex.
- Identificación de tokens, lexemas y números de línea.
- Conteo de palabras reservadas.
- Estadísticas de enteros, flotantes, identificadores, booleanos y operadores.
- Generación de reportes en formato PDF.
- Generación de tabla de símbolos.
- Almacenamiento de la tabla de símbolos en MongoDB Atlas.