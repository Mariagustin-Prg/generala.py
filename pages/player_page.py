import tkinter as tk
from p3 import P3
from tkinter import messagebox

class P2:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.configure(bg="dark olive green")
        self.ventana.geometry("600x400+300+250")
        self.ventana.resizable(False, False)
        self.ventana.title("Gestión de jugadores")

        self.frame0 = tk.Frame(self.ventana, height= 10, bg= 'dark olive green')
        self.frame0.pack()

        self.frame = tk.Frame(self.ventana, height= 100, width= 200, bg= "dark olive green")
        self.frame.pack()

        self.texto = tk.Label(self.frame, text= "Jugadores.", font=("Arial", 36, "bold"), bg= "dark olive green")
        self.texto.pack()


        self.frame2 = tk.Frame(self.ventana, height=40, bg= 'dark olive green')
        self.frame2.pack()


        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack()

        self.boton_jugador = tk.Button(self.ventana, text= "Ingresar jugador")
        self.boton_jugador.pack()

        self.frame3 = tk.Frame(self.ventana, height= 50, bg= 'dark olive green')
        self.frame3.pack()

        self.frame_jugadores = tk.LabelFrame(self.ventana, bg= "dark olive green", bd= 5, height=100, width= 380)
        self.frame_jugadores.config(text="Jugadores")
        self.frame_jugadores.pack()


        self.listaJugadores = []

        def add_player_on_click():
            VarNombre = self.entrada.get()

            if VarNombre not in self.listaJugadores:
                self.listaJugadores.append(VarNombre)
                playerA = tk.Label(self.frame_jugadores, text= VarNombre)
                playerA.pack()

            else:
                messagebox.showinfo("Información", "El nombre que intenta ingresar, ya fue utilizado.")

        def on_key_press(event):
            if event.char == "\r":
                add_player_on_click()

        self.ventana.bind("<KeyPress>", on_key_press)


        self.boton_jugador.config(command=add_player_on_click)

        self.boton_siguiente = tk.Button(self.ventana, text= "Comenzar juego")
        self.boton_siguiente.pack(side='right')

        def next_page_on_click():
            self.ventana.destroy()

            self.__p3__ = P3()
        
        self.boton_siguiente.config(command= next_page_on_click)

        self.ventana.mainloop()

if __name__ == "__main__":
    app = P2()