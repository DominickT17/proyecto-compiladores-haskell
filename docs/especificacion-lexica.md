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
## 9. Operadores

Los operadores son símbolos que permiten realizar cálculos, comparaciones y otras operaciones dentro del código fuente.

El analizador deberá revisar primero los operadores formados por varios caracteres. Esto evita que, por ejemplo, el lexema `==` sea reconocido como dos símbolos `=` separados.

### 9.1 Operadores aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas.

| Lexema | Descripción |
|---|---|
| `+` | Suma |
| `-` | Resta o signo negativo |
| `*` | Multiplicación |
| `/` | División |
| `^` | Potencia |

Estos lexemas serán clasificados inicialmente con el token:

```text
OPERADOR_ARITMETICO
```

Ejemplo:

```haskell
resultado = numero1 + numero2 * 5
```

En este caso, los lexemas `+` y `*` se clasifican como operadores aritméticos.

### 9.2 Operadores relacionales

Los operadores relacionales permiten comparar dos valores.

| Lexema | Descripción |
|---|---|
| `==` | Igual que |
| `/=` | Diferente de |
| `<` | Menor que |
| `<=` | Menor o igual que |
| `>` | Mayor que |
| `>=` | Mayor o igual que |

Estos lexemas serán clasificados con el token:

```text
OPERADOR_RELACIONAL
```

Ejemplo:

```haskell
edad >= 18
```

El lexema `>=` será reconocido como un solo operador relacional.

### 9.3 Operadores lógicos

Los operadores lógicos permiten combinar expresiones booleanas.

| Lexema | Descripción |
|---|---|
| `&&` | Conjunción lógica |
| `||` | Disyunción lógica |

Estos lexemas serán clasificados con el token:

```text
OPERADOR_LOGICO
```

Ejemplo:

```haskell
edad >= 18 && activo == True
```

### 9.4 Operadores y símbolos especiales de Haskell

Haskell utiliza algunos operadores y símbolos con significados particulares.

| Lexema | Descripción inicial |
|---|---|
| `=` | Definición o asociación de un nombre con una expresión |
| `::` | Declaración de tipo |
| `->` | Separación entre parámetros y resultados o ramas |
| `<-` | Obtención de un valor dentro de una expresión monádica |
| `=>` | Restricción o contexto de tipos |
| `:` | Construcción de listas |
| `++` | Concatenación de listas |

Estos elementos serán clasificados inicialmente con el token:

```text
OPERADOR_ESPECIAL
```

Ejemplo:

```haskell
sumar :: Int -> Int -> Int
sumar a b = a + b
```

En este ejemplo, `::`, `->` y `=` son elementos especiales de la sintaxis de Haskell.

> En Haskell, el símbolo `=` no representa una asignación mutable como en otros lenguajes. Se utiliza para definir nombres, funciones o valores.

## 10. Símbolos de agrupación

Los símbolos de agrupación permiten delimitar expresiones, listas y otras estructuras.

| Lexema | Token |
|---|---|
| `(` | `PARENTESIS_ABRE` |
| `)` | `PARENTESIS_CIERRA` |
| `[` | `CORCHETE_ABRE` |
| `]` | `CORCHETE_CIERRA` |
| `{` | `LLAVE_ABRE` |
| `}` | `LLAVE_CIERRA` |

Ejemplo:

```haskell
numeros = [1, 2, 3]
resultado = (5 + 3) * 2
```

Los corchetes delimitan la lista y los paréntesis agrupan la operación aritmética.

## 11. Separadores

Los separadores permiten dividir elementos dentro del código fuente.

| Lexema | Token |
|---|---|
| `,` | `COMA` |
| `;` | `PUNTO_Y_COMA` |
| `.` | `PUNTO` |

Ejemplo:

```haskell
numeros = [10, 20, 30]
```

Las comas separan los elementos de la lista.

El punto y coma puede utilizarse para separar expresiones escritas en una misma línea, aunque Haskell utiliza normalmente la indentación para organizar los bloques.

## 12. Espacios y saltos de línea

Los espacios, tabulaciones y saltos de línea permiten separar los elementos del código fuente.

Los espacios y tabulaciones no producirán tokens, pero serán utilizados para evitar que dos lexemas consecutivos se interpreten como uno solo.

Los saltos de línea tampoco producirán un token en la primera versión del analizador, pero se utilizarán para llevar el control del número de línea.

Elementos que se ignorarán:

```text
Espacio
Tabulación
Retorno de carro
Salto de línea
```

El analizador deberá incrementar un contador cada vez que encuentre un salto de línea.

## 13. Comentarios

Los comentarios contienen explicaciones para el programador y no forman parte de las instrucciones que se ejecutan.

### 13.1 Comentarios de una línea

En Haskell, un comentario de una línea comienza con dos guiones.

Ejemplo:

```haskell
-- Este es un comentario
edad = 20
```

El comentario se extiende desde `--` hasta el final de la línea.

Estos lexemas serán clasificados inicialmente con el token:

```text
COMENTARIO_LINEA
```

### 13.2 Comentarios de bloque

Los comentarios de bloque comienzan con `{-` y terminan con `-}`.

Ejemplo:

```haskell
{-
Este comentario
ocupa varias líneas.
-}
```

Estos lexemas serán clasificados inicialmente con el token:

```text
COMENTARIO_BLOQUE
```

La primera versión del analizador reconocerá comentarios de bloque simples. El manejo de comentarios anidados podrá evaluarse durante la implementación en Flex.

## 14. Caracteres no reconocidos

Cualquier carácter que no pertenezca a una categoría definida será reportado como un error léxico.

Estos caracteres serán clasificados con el token:

```text
CARACTER_NO_RECONOCIDO
```

El analizador mostrará como mínimo:

- El carácter encontrado.
- La línea donde apareció.
- Una descripción indicando que no pertenece al lenguaje reconocido.

Ejemplo de salida:

```text
Error léxico: carácter no reconocido '#' en la línea 4.
```

Esta regla deberá colocarse al final de las reglas de Flex para ejecutarse únicamente cuando ninguna regla anterior coincida.