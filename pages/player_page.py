import tkinter as tk

class p2:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.configure(bg="lightblue")

        frame = tk.Frame(self.ventana)
        texto = tk.Label(frame, text= "Jugadores.")

        texto.pack()
        frame.pack()

        self.ventana.mainloop()