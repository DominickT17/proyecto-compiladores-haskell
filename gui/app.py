import tkinter as tk
from tkinter import ttk


class AnalizadorGUI:

    def __init__(self, root):

        self.root = root

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
            width=18
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            botones,
            text="Analizar código",
            width=18
        ).pack(side=tk.LEFT)

        ttk.Separator(self.root, orient="horizontal").pack(fill="x", pady=15)

        estado = tk.Label(
            self.root,
            text="Estado: Esperando archivo...",
            anchor="w"
        )

        estado.pack(fill="x", padx=20)

if __name__ == "__main__":

    root = tk.Tk()

    app = AnalizadorGUI(root)

    root.mainloop()