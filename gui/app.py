import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os

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


    def limpiar_tabla(self):
        for elemento in self.tabla_tokens.get_children():
            self.tabla_tokens.delete(elemento)

    def analizar_codigo(self):
        if not self.archivo_actual:
            self.estado.config(
                text="Estado: Debe seleccionar un archivo antes de analizar"
            )
            return

        ruta_json = os.path.join(
            os.path.dirname(__file__),
            "mock_tokens.json"
        )

        try:
            with open(ruta_json, "r", encoding="utf-8") as archivo_json:
                tokens = json.load(archivo_json)

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
            with open(self.archivo_actual, "r", encoding="utf-8") as archivo_fuente:
                contenido = archivo_fuente.read()

            cantidad_lineas = len(contenido.splitlines())
            cantidad_caracteres = len(contenido)
            cantidad_enteros = 0
            cantidad_flotantes = 0
            cantidad_identificadores = 0
            cantidad_booleanos = 0
            cantidad_operadores = 0

            for token in tokens: 
                tipo = token["token"]

                if tipo == "ENTERO":
                    cantidad_enteros += 1

                elif tipo == "FLOTANTE":
                    cantidad_flotantes += 1
                elif tipo in ("ID", "IDENTIFICADOR", "CONSTRUCTOR"):
                    cantidad_identificadores += 1
                elif tipo == "BOOLEANO":
                    cantidad_booleanos += 1
                elif tipo.startswith("OP_"):
                    cantidad_operadores += 1

            self.estadisticas["lineas"].set(str(cantidad_lineas))
            self.estadisticas["caracteres"].set(str(cantidad_caracteres))
            self.estadisticas["enteros"].set(str(cantidad_enteros))
            self.estadisticas["flotantes"].set(str(cantidad_flotantes))
            self.estadisticas["identificadores"].set(str(cantidad_identificadores))
            self.estadisticas["booleanos"].set(str(cantidad_booleanos))
            self.estadisticas["operadores"].set(str(cantidad_operadores))

            self.estado.config(
                            text="Estado: Analisis simulado completado"
                        )

        except Exception as error:
            self.estado.config(
                text=f"Estado: Error al calcular estadisticas: {error}"
            )
            return

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