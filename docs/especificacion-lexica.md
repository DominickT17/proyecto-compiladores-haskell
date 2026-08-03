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