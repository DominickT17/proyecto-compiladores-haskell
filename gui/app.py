import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

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

            self.estado.config(
                text=f"Estado: Archivo seleccionado"
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