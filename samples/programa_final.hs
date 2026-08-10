module ProgramaFinal where

import Prelude
import qualified Prelude as P hiding (map)

-- Archivo final para validar el analizador lexico
-- Incluye palabras reservadas, literales, operadores e identificadores

type Edad = Int
type Nombre = String

newtype Codigo = Codigo Int

data Persona = Persona Nombre Edad deriving (Show)

class Describible a where
    describir :: a -> String

instance Describible Persona where
    describir persona = "Persona registrada"

default (Int)

infix 4 ===
infixl 7 ***
infixr 5 +++

(===) :: Int -> Int -> Bool
a === b = a == b

(***) :: Int -> Int -> Int
a *** b = a * b

(+++) :: [a] -> [a] -> [a]
listaA +++ listaB = listaA ++ listaB

edadBase = 18
edadMinima = 1
edadMaxima = 99

precio = 25.75
descuento = 5.50

activo = True
finalizado = False

nombre = "Dominick"
mensajeAdulto = "Mayor de edad"
mensajeMenor = "Menor de edad"

inicial = 'D'
salto = '\n'

suma = edadBase + 2
resta = edadMaxima - edadBase
producto = edadBase * 2
division = edadMaxima / 3

esMayor = edadBase >= 18
esMenor = edadBase < 18

esValida =
    edadBase >= edadMinima &&
    edadBase <= edadMaxima

esEspecial =
    activo || finalizado

esIgual =
    edadBase == 18

esDistinta =
    edadBase /= edadMaxima

listaUno = [1, 2, 3]
listaDos = [4, 5, 6]

listaCompleta =
    listaUno ++ listaDos

primerElemento =
    listaCompleta !! 0

clasificarEdad edad =
    if edad >= 18
    then mensajeAdulto
    else mensajeMenor

clasificarNumero numero =
    case numero of
        0 -> "cero"
        1 -> "uno"
        _ -> "otro"

calcular edad =
    let doble = edad * 2
        triple = edad * 3
    in doble + triple

comparar a b =
    if a > b
    then a
    else b

crearPersona =
    Persona nombre edadBase

crearCodigo =
    Codigo 202408077

usarDo = do
    valor <- return edadBase
    otro <- return edadMaxima
    return (valor + otro)

usarCase persona =
    case persona of
        Persona n e -> n

foreign import ccall "abs" c_abs :: Int -> Int

pruebaUno = edadBase
pruebaDos = edadBase
pruebaTres = nombre
pruebaCuatro = nombre
pruebaCinco = nombre

principal = do
    resultado <- return (calcular edadBase)
    texto <- return (clasificarEdad resultado)
    return texto