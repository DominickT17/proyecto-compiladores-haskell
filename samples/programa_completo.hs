module Main where

import Data.List (intercalate)

-- Sistema sencillo de estudiantes y calificaciones
-- Archivo diseñado para probar diferentes tokens del lexer

data Estudiante = Estudiante
    {
        nombre :: String,
        edad :: Int,
        promedio :: Float,
        activo :: Bool,
        seccion :: Char
    }
    deriving (Show)

estudiantes :: [Estudiante]
estudiantes =
    [
        Estudiante "Ana Lopez" 19 88.5 True 'A',
        Estudiante "Carlos Ruiz" 17 72.0 True 'B',
        Estudiante "Maria Perez" 21 94.3 True 'A',
        Estudiante "Luis Gomez" 18 61.5 False 'C',
        Estudiante "Sofia Diaz" 20 79.8 True 'B',
        Estudiante "Pedro Morales" 22 55.4 False 'C'
    ]

obtenerNombre :: Estudiante -> String
obtenerNombre estudiante = nombre estudiante

obtenerPromedio :: Estudiante -> Float
obtenerPromedio estudiante = promedio estudiante

esMayorDeEdad :: Estudiante -> Bool
esMayorDeEdad estudiante = edad estudiante >= 18

estaAprobado :: Estudiante -> Bool
estaAprobado estudiante = promedio estudiante >= 60.0

esSobresaliente :: Estudiante -> Bool
esSobresaliente estudiante = promedio estudiante > 90.0

filtrarAprobados :: [Estudiante] -> [Estudiante]
filtrarAprobados lista = filter estaAprobado lista

buscarEstudiante :: String -> [Estudiante] -> Maybe Estudiante
buscarEstudiante _ [] = Nothing
buscarEstudiante buscado (estudiante:resto)
    | nombre estudiante == buscado = Just estudiante
    | otherwise = buscarEstudiante buscado resto

contarActivos :: [Estudiante] -> Int
contarActivos [] = 0
contarActivos (estudiante:resto)
    | activo estudiante = 1 + contarActivos resto
    | otherwise = contarActivos resto

calcularPromedio :: [Float] -> Float
calcularPromedio [] = 0.0
calcularPromedio notas =
    sum notas / fromIntegral (length notas)

promedioGeneral :: [Estudiante] -> Float
promedioGeneral lista =
    calcularPromedio (map promedio lista)

clasificarPromedio :: Estudiante -> String
clasificarPromedio estudiante =
    case promedio estudiante of
        nota | nota >= 90.0 -> "Excelente"
        nota | nota >= 75.0 -> "Bueno"
        nota | nota >= 60.0 -> "Aprobado"
        _ -> "Reprobado"

compararEdad :: Estudiante -> String
compararEdad estudiante =
    if edad estudiante < 18
        then "Menor de edad"
        else "Mayor o igual a 18"

necesitaRevision :: Estudiante -> Bool
necesitaRevision estudiante =
    promedio estudiante < 60.0 || activo estudiante == False

estadoCompleto :: Estudiante -> String
estadoCompleto estudiante =
    let { aprobado = estaAprobado estudiante; vigente = activo estudiante }
    in if aprobado && vigente
        then "Aprobado y activo"
        else "Requiere revision"

ajustarPromedio :: Estudiante -> Float
ajustarPromedio estudiante
    | promedio estudiante /= 0.0 = promedio estudiante + 2.0
    | otherwise = promedio estudiante

calcularDiferencia :: Estudiante -> Estudiante -> Float
calcularDiferencia primero segundo =
    promedio primero - promedio segundo

calcularDoble :: Int -> Int
calcularDoble numero = numero * 2

estaEnRango :: Estudiante -> Bool
estaEnRango estudiante =
    promedio estudiante >= 60.0 && promedio estudiante <= 100.0

sumaRecursiva :: [Int] -> Int
sumaRecursiva [] = 0
sumaRecursiva (x:xs) = x + sumaRecursiva xs

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

listaNombres :: [Estudiante] -> String
listaNombres lista =
    intercalate ", " (map nombre lista)

mostrarResumen :: Estudiante -> String
mostrarResumen estudiante =
    nombre estudiante
    ++ " | promedio: "
    ++ show (promedio estudiante)
    ++ " | seccion: "
    ++ [seccion estudiante]

resumenConWhere :: Estudiante -> String
resumenConWhere estudiante =
    nombreActual ++ " -> " ++ estado
    where
        nombreActual = nombre estudiante
        estado = clasificarPromedio estudiante

main :: IO ()
main = do
    putStrLn "=== Sistema de estudiantes y calificaciones ==="
    putStrLn ("Nombres: " ++ listaNombres estudiantes)
    putStrLn ("Total: " ++ show (length estudiantes))
    putStrLn ("Activos: " ++ show (contarActivos estudiantes))
    putStrLn ("Promedio general: " ++ show (promedioGeneral estudiantes))
    putStrLn ("Suma [1,2,3,4,5]: " ++ show (sumaRecursiva [1,2,3,4,5]))
    putStrLn ("Factorial de 5: " ++ show (factorial 5))
    putStrLn "--- Resumenes ---"
    mapM_ (putStrLn . mostrarResumen) estudiantes
    putStrLn "--- Busqueda ---"
    case buscarEstudiante "Maria Perez" estudiantes of
        Just estudiante -> putStrLn (resumenConWhere estudiante)
        Nothing -> putStrLn "Estudiante no encontrado"