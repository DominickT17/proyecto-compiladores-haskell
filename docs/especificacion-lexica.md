# Especificación léxica de Haskell

## 1. Propósito

Este documento define los elementos léxicos que deberá reconocer el analizador
desarrollado para el proyecto del curso de Compiladores.

La especificación servirá como base para escribir posteriormente las
expresiones regulares y acciones del archivo Flex.

## 2. Análisis léxico

El análisis léxico es la fase del compilador encargada de leer el código fuente
como una secuencia de caracteres y agruparlos en unidades con significado.

Estas unidades se clasifican mediante tokens y posteriormente pueden ser
utilizadas por las demás fases del compilador.

## 3. Lexema

Un lexema es la secuencia exacta de caracteres encontrada en el código fuente.

Por ejemplo, en la instrucción:

```haskell
edad = 20
```

se encuentran los siguientes lexemas:

- `edad`
- `=`
- `20`

## 4. Token

Un token es la categoría que se asigna a un lexema reconocido por el
analizador léxico.

Para el ejemplo anterior se pueden asignar las siguientes categorías:

| Lexema | Token |
|---|---|
| `edad` | IDENTIFICADOR |
| `=` | OPERADOR_ASIGNACION |
| `20` | NUMERO_ENTERO |

El lexema representa el texto exacto encontrado en el código, mientras que el
token representa la clasificación de ese texto.

## 5. Alcance inicial

El analizador léxico recibirá archivos fuente escritos en Haskell y deberá
identificar inicialmente las siguientes categorías:

- Palabras reservadas.
- Identificadores.
- Números enteros.
- Números decimales.
- Cadenas de texto.
- Caracteres.
- Valores booleanos.
- Operadores.
- Símbolos de agrupación.
- Separadores.
- Comentarios.
- Caracteres no reconocidos.

Cada categoría será documentada antes de escribir las expresiones regulares y
acciones correspondientes en Flex.
## 6. Palabras reservadas

Las palabras reservadas son términos que forman parte de la sintaxis del lenguaje Haskell. Estas palabras poseen un significado especial y no deben utilizarse como nombres de variables, funciones o tipos.

Algunas palabras reservadas que reconocerá inicialmente el analizador son:

- `module`
- `where`
- `import`
- `data`
- `type`
- `class`
- `instance`
- `if`
- `then`
- `else`
- `let`
- `in`
- `case`
- `of`
- `do`

Por ejemplo:

```haskell
module Principal where

main = do
    let edad = 20
    if edad >= 18
        then print "Mayor de edad"
        else print "Menor de edad"
```

En este ejemplo, los lexemas `module`, `where`, `do`, `let`, `if`, `then` y `else` se clasifican como palabras reservadas.
## 7. Identificadores

Los identificadores son nombres utilizados para representar variables, funciones, tipos y constructores dentro de un programa.

Inicialmente, el analizador reconocerá dos clases de identificadores.

### 7.1 Identificadores de variables y funciones

Comienzan con una letra minúscula o un guion bajo. Después pueden contener letras, números, apóstrofes y guiones bajos.

Ejemplos:

- `edad`
- `calcularTotal`
- `numero1`
- `_resultado`
- `valorFinal`

Estos lexemas se clasificarán mediante el token:

```text

Los identificadores de variables y funciones comienzan normalmente con una letra minúscula o con un guion bajo.

Después del primer carácter pueden contener letras, números, guiones bajos y apóstrofes.

Ejemplos válidos:

```haskell
edad
calcularTotal
numero1
_valor
nombreCompleto'
```

Estos lexemas serán clasificados con el token:

```text
IDENTIFICADOR
```

Una expresión regular inicial para representar esta categoría será:

```text
[a-z_][a-zA-Z0-9_']*
```

Esta expresión indica que el identificador debe comenzar con una letra minúscula o con un guion bajo. Después puede contener letras mayúsculas, letras minúsculas, números, guiones bajos o apóstrofes.

### 7.2 Identificadores de tipos y constructores

En Haskell, los nombres de tipos y constructores comienzan normalmente con una letra mayúscula.

Ejemplos:

```haskell
Persona
Estudiante
Resultado
UsuarioActivo
```

Estos lexemas serán clasificados inicialmente con el token:

```text
IDENTIFICADOR_TIPO
```

La expresión regular inicial será:

```text
[A-Z][a-zA-Z0-9_']*
```

Por ejemplo:

```haskell
data Persona = Persona String Int
```

En esta instrucción, el lexema `Persona` comienza con una letra mayúscula y puede representar un tipo o un constructor.

## 8. Literales

Un literal es un valor escrito directamente dentro del código fuente.

El analizador reconocerá inicialmente literales enteros, decimales, caracteres y cadenas.

### 8.1 Literales enteros

Los literales enteros representan números sin parte decimal.

Ejemplos:

```haskell
0
18
250
2026
```

Estos lexemas serán clasificados con el token:

```text
ENTERO
```

La expresión regular inicial será:

```text
[0-9]+
```

El signo negativo se analizará inicialmente como un operador separado del número.

Por ejemplo:

```haskell
edad = -20
```

Puede producir los siguientes elementos:

| Lexema | Token |
|---|---|
| `edad` | `IDENTIFICADOR` |
| `=` | `OPERADOR_ASIGNACION` |
| `-` | `OPERADOR_ARITMETICO` |
| `20` | `ENTERO` |

### 8.2 Literales decimales

Los literales decimales contienen una parte entera, un punto y una parte decimal.

Ejemplos:

```haskell
3.14
18.5
100.25
```

Estos lexemas serán clasificados con el token:

```text
DECIMAL
```

La expresión regular inicial será:

```text
[0-9]+\.[0-9]+
```

Por ejemplo:

```haskell
precio = 25.50
```

El lexema `25.50` será reconocido como un literal decimal.

### 8.3 Literales de carácter

Un literal de carácter representa un solo carácter escrito entre comillas simples.

Ejemplos:

```haskell
'A'
'b'
'7'
```

Estos lexemas serán clasificados con el token:

```text
CARACTER
```

Una representación inicial de esta categoría será:

```text
'[^']'
```

Por ejemplo:

```haskell
inicial = 'D'
```

El lexema `'D'` será reconocido como un literal de carácter.

### 8.4 Literales de cadena

Una cadena es una secuencia de caracteres escrita entre comillas dobles.

Ejemplos:

```haskell
"Hola"
"Compiladores"
"Mayor de edad"
```

Estos lexemas serán clasificados con el token:

```text
CADENA
```

Una representación inicial será:

```text
\"[^\"]*\"
```

Por ejemplo:

```haskell
mensaje = "Hola mundo"
```

El lexema `"Hola mundo"` será reconocido como una cadena.