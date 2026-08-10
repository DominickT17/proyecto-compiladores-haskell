import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import json
import os
import subprocess

class AnalizadorGUI:

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo Haskell",

            filetypes=[
                ("Archivos Haskell","*.hs"),
                ("Todos los archivos","*.*")
                ]

        )
        
        if archivo:
            if not archivo.endswith(".hs"):
                        messagebox.showwarning(
                            "Archivo no valido",
                            "Debe seleccionar un archivo Haskell con extension .hs"
                        )
                        return
            
            self.archivo_actual = archivo
            self.ruta_archivo.set(archivo)

            try: 
                with open(archivo, "r", encoding="utf-8") as archivo_haskell:
                    contenido = archivo_haskell.read()

                    self.area_codigo.delete("1.0", tk.END)
                    self.area_codigo.insert("1.0", contenido)

                    self.estado.config(
                        text="Estado: Archivo cargado correctamente"
                    )
            except Exception as error:
                self.estado.config(
                    text=f"Estado: Error al abrir el archivo: {error}"
                )
        else:
            self.estado.config(
                text="Estado: Seleccion de archivo canceladada"
            )


    def limpiar_tabla(self):
        for elemento in self.tabla_tokens.get_children():
            self.tabla_tokens.delete(elemento)

    def ejecutar_lexer(self):
        ruta_proyecto = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        ruta_lexer = os.path.join(
             ruta_proyecto,
             "lexer",
             "haskell_lexer"
        )

        resultado = subprocess.run(
            [ruta_lexer, self.archivo_actual],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        if resultado.returncode != 0:
            raise Exception(
                resultado.stderr.strip() or "El lexer terminó con un error."
            )

        return resultado.stdout

    def extraer_tokens_lexer(self, salida):
        tokens = []

        leyendo_tokens = False

        for linea in salida.splitlines():

            if linea.startswith("TOKEN"):
               leyendo_tokens = True
               continue

            if leyendo_tokens and linea.startswith("-"):
               continue

            if linea.startswith("RESUMEN DEL ARCHIVO"):
               break

            if leyendo_tokens and linea.strip():
               partes = linea.rsplit(maxsplit=1)

               if len(partes) != 2:
                  continue

               contenido, numero_linea = partes
               partes_token = contenido.split(maxsplit=1)

            if len(partes_token) != 2:
                continue

            token, lexema = partes_token

            tokens.append({
                "token": token,
                "lexema": lexema.strip(),
                "linea": numero_linea
            })

        return tokens

    def extraer_palabras_reservadas(self, salida):
        palabras = []
        leyendo_palabras = False

        for linea in salida.splitlines():
            linea = linea.strip()

            if linea == "PALABRAS RESERVADAS POR FRECUENCIA":
                leyendo_palabras = True
                continue

            if leyendo_palabras and linea.startswith("-"):
                continue

            if linea == "IDENTIFICADORES POR FRECUENCIA":
                break

            if leyendo_palabras and linea:
                partes = linea.rsplit(maxsplit=1)

                if len(partes) == 2:
                    palabra, cantidad = partes

                    palabras.append({
                        "palabra": palabra.strip(),
                        "cantidad": cantidad.strip()
                    })

        return palabras

    def extraer_estadisticas_lexer(self, salida):
        estadisticas = {}

        leyendo_resumen = False

        for linea in salida.splitlines():
            linea = linea.strip()

            if linea == "RESUMEN DEL ARCHIVO":
                leyendo_resumen = True
                continue

            if leyendo_resumen and linea.startswith("PALABRAS RESERVADAS"):
                break

            if leyendo_resumen and ":" in linea:
                clave, valor = linea.split(":", 1)

                estadisticas[clave.strip().lower()] = valor.strip()

        return estadisticas

    def analizar_codigo(self):
        if not self.archivo_actual:
           messagebox.showwarning(
               "Archivo requerido",
               "Debe seleccionar un archivo Haskell antes de analizar."
           )

           self.estado.config(
               text="Estado: No hay archivo seleccionado."
           ) 
           return

        try:
            salida_lexer = self.ejecutar_lexer()

            tokens = self.extraer_tokens_lexer(salida_lexer)
            estadisticas = self.extraer_estadisticas_lexer(salida_lexer)
            palabras_reservadas = self.extraer_palabras_reservadas(salida_lexer)

            print("PALABRAS RESERVADAS")
            for palabra in palabras_reservadas:
                print(palabra)

            self.limpiar_tabla()

            for token in tokens:
                self.tabla_tokens.insert(
                   "",
                   tk.END,
                   values=(
                       token["token"],
                       token["lexema"],
                       token["linea"]
                   )
                ) 
            self.estadisticas["lineas"].set(
                estadisticas.get("lineas", "0")
            )

            self.estadisticas["caracteres"].set(
                estadisticas.get("caracteres", "0")
            )

            self.estadisticas["enteros"].set(
                estadisticas.get("enteros", "0")
            )

            self.estadisticas["flotantes"].set(
                estadisticas.get("flotantes", "0")
            )

            self.estadisticas["identificadores"].set(
                estadisticas.get("identificadores", "0")
            )

            self.estadisticas["booleanos"].set(
                estadisticas.get("booleanos", "0")
            ) 

            self.estadisticas["operadores"].set(
                estadisticas.get("operadores", "0")
            )

            self.estado.config(
                text="Estado: Análisis léxico completado."
            )

        except Exception as error:
            self.estado.config(
              text=f"Estado: Error durante el análisis: {error}"
        )

    def __init__(self, root):

        self.root = root
        self.archivo_actual = ""

        self.ruta_archivo = tk.StringVar()
        self.ruta_archivo.set("Ningun archivo seleccionado")
        self.root.title("Analizador Lexico de Haskell")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)

        self.crear_componentes()

    def crear_componentes(self):

        titulo = tk.Label(
            self.root,
            text="Analizador Lexico de Haskell",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=15)

        botones = tk.Frame(self.root)
        botones.pack()

        tk.Button(
            botones,
            text="Abrir archivo",
            width=18,
            command=self.abrir_archivo
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            botones,
            text="Analizar código",
            width=18,
            command=self.analizar_codigo
        ).pack(side=tk.LEFT)

        frame_ruta = tk.Frame(self.root)
        frame_ruta.pack(fill="x", padx=20, pady=10)

        tk.Label(
            frame_ruta,
            text="Archivo:"
        ).pack(side=tk.LEFT)

        tk.Entry(
            frame_ruta,
            textvariable=self.ruta_archivo,
            state="readonly"
        ).pack(
            side=tk.LEFT,
            fill="x",
            expand=True,
            padx=(10, 0)
        )

        ttk.Separator(
            self.root, 
            orient="horizontal"
            ).pack(fill="x", pady=15)

        tk.Label(
            self.root,
            text="codigo fuente",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=20, pady=(5, 0))

        self.area_codigo = tk.Text(
            self.root,
            wrap="none",
            height=20
        )

        self.area_codigo.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        tk.Button(
            botones,
            text="Reporte 1",
            width=15,
            state="disabled",
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            botones,
            text="Reporte 2",
            width=15,
            state="disabled"
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            botones,
            text="Guardar MonoBD",
            width=15,
            state="disabled"
        ).pack(side=tk.LEFT, padx=5)

        # Panel de estadísticas
        tk.Label(
           self.root,
           text="Estadísticas:",
           font=("Arial", 11, "bold")
           ).pack(anchor="w", padx=20, pady=(5, 0))

        frame_estadisticas = tk.Frame(self.root)
        frame_estadisticas.pack(
           fill="x",
           padx=20,
           pady=10
        )

        self.estadisticas = {
           "lineas": tk.StringVar(value="0"),
           "caracteres": tk.StringVar(value="0"),
           "enteros": tk.StringVar(value="0"),
           "flotantes": tk.StringVar(value="0"),
           "identificadores": tk.StringVar(value="0"),
           "booleanos": tk.StringVar(value="0"),
           "operadores": tk.StringVar(value="0")
       }

        datos_estadisticas = [
           ("Líneas", "lineas"),
           ("Caracteres", "caracteres"),
           ("Enteros", "enteros"),
           ("Flotantes", "flotantes"),
           ("Identificadores", "identificadores"),
           ("Booleanos", "booleanos"),
           ("Operadores", "operadores")
       ]

        for columna, (texto, clave) in enumerate(datos_estadisticas):
           contenedor = tk.Frame(frame_estadisticas)
           contenedor.grid(
              row=0,
              column=columna,
              padx=10,
              pady=5
            )

           tk.Label(
               contenedor,
               text=texto,
               font=("Arial", 9, "bold")
           ).pack()

           tk.Label(
               contenedor,
               textvariable=self.estadisticas[clave],
               font=("Arial", 11)
           ).pack()

        for columna in range(len(datos_estadisticas)):
            frame_estadisticas.columnconfigure(
                columna,
                weight=1
            )
        

        tk.Label(
            self.root,
            text="Tokens enontrados",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", padx=20, pady=(5, 0))

        frame_tabla = tk.Frame(self.root)
        frame_tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.tabla_tokens = ttk.Treeview(
            frame_tabla,
            columns=("token", "lexema", "linea"),
            show="headings",
            height=8
        )

        self.tabla_tokens.heading("token", text="Token")
        self.tabla_tokens.heading("lexema", text="Lexema")
        self.tabla_tokens.heading("linea", text="Linea")

        self.tabla_tokens.column("token", width=200)
        self.tabla_tokens.column("lexema", width=300)
        self.tabla_tokens.column("linea", width=100, anchor="center")

        self.tabla_tokens.pack(
            side=tk.LEFT,
            fill="both",
            expand=True
        )

        scroll_tabla = ttk.Scrollbar(
            frame_tabla,
            orient="vertical",
            command=self.tabla_tokens.yview
        )

        scroll_tabla.pack(
            side=tk.RIGHT,
            fill="y"
        )

        self.tabla_tokens.configure(
            yscrollcommand=scroll_tabla.set
        )

        self.estado = tk.Label(
            self.root,
            text="Estado: Esperando archivo...",
            anchor="w"
        )

        self.estado.pack(fill="x", padx=20)

if __name__ == "__main__":

    root = tk.Tk()

    app = AnalizadorGUI(root)

    root.mainloop()