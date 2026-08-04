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