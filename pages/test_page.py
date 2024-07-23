import tkinter as tk

ventana = tk.Tk()
ventana.configure(bg="lightgray")

class Ventana:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.configure(bg="lightblue")
        self.ventana.mainloop()

def on_click_button1():
    ventana.destroy()  # Destruir la ventana principal
    click = Ventana()  # Crear una nueva ventana

boton1 = tk.Button(ventana, text="Abrir Ventana", command=on_click_button1)
boton1.pack()

ventana.mainloop()
