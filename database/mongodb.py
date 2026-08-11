import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

URI_MONGODB = os.getenv("MONGODB_URI")

NOMBRE_BASE_DATOS = "analizador_haskell"
NOMBRE_COLECCION = "tabla_simbolos"


def obtener_coleccion():
    if not URI_MONGODB:
        raise Exception(
            "No se encontró la variable MONGODB_URI en el archivo .env"
        )

    cliente = MongoClient(
        URI_MONGODB,
        serverSelectionTimeoutMS=5000
    )

    cliente.admin.command("ping")

    base_datos = cliente[NOMBRE_BASE_DATOS]
    coleccion = base_datos[NOMBRE_COLECCION]

    return cliente, coleccion


def guardar_tabla_simbolos(tokens, archivo_fuente):
    cliente, coleccion = obtener_coleccion()

    try:
        simbolos = []
        simbolos_vistos = set()

        for token in tokens:
            if token["token"] in (
                "IDENTIFICADOR",
                "CONSTRUCTOR"
            ):
                clave = (
                    token["lexema"],
                    token["token"]
                )

                if clave not in simbolos_vistos:
                    simbolos_vistos.add(clave)
                
                simbolos.append({
                    "lexema": token["lexema"],
                    "token": token["token"],
                    "linea": int(token["linea"]),
                    "archivo": archivo_fuente
                })

        if not simbolos:
            return 0

        coleccion.delete_many({
            "archivo": archivo_fuente
        })

        resultado = coleccion.insert_many(simbolos)

        return len(resultado.inserted_ids)

    finally:
        cliente.close()