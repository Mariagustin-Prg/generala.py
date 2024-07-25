# Importamos la siguiente página del juego y tkinter
from player_page import P2
import tkinter as tk

# Inicializamos una ventana
ventana = tk.Tk()
# Le colocamos un título
ventana.title("Generala!")
# Configuramos el color del fondo
ventana.configure(bg= "dark olive green")
# Definimos el tamaño de la ventana y su lugar de aparición.
ventana.geometry("800x500+300+100")
# Configuramos la ventana para que no pueda cambiar de tamaño.
ventana.resizable(False, False)

# Generamos un espacio entre el borde de la ventana y el primer frame.
frame0 = tk.Frame(ventana, height=50, bg= "dark olive green")
frame0.pack()

# Creamos un frame que sea grande y pueda contener al título "GENERALA"
frame = tk.Frame(ventana, height= 100, width= 350)
# Le añadimos un borde y un color
frame.config(bd= 4, bg= "olive drab")
frame.pack()

# El título del juego lo incluimos dentro del frame creado.
titulo = tk.Label(frame, text="GENERALA", width=20)
# Configuramos la fuente, el color del texto y el color del fondo
titulo.config(font=("New Times Roman", 36, "bold"), fg="snow", bg= "dark olive green")
titulo.pack()

# Generamos un espacio entre el título y el primer botón.
frame2 = tk.Frame(ventana, height=50, bg= "dark olive green")
frame2.pack()

# Creamos el primer botón con una fuente, un ancho y un texto definido.
boton = tk.Button(ventana, text= "< Iniciar juego >", width=20, font=("Times New Roman", 18, "italic"))

# Definimos la función de la acción que hará el bptón al ser clickeado.
def on_click_button() -> None:
    # Cierra la ventana principal
    ventana.destroy()
    # Llama a la segunda ventana
    _p2_ = P2()

# Le añadimos la funcionalidad al botón.
boton.configure(command= on_click_button)
# Lo añadimos a la ventana.
boton.pack()

# El espacio entre los botones \/
frame3 = tk.Frame(ventana, height=30)
frame3.config(bg= "dark olive green")
frame3.pack()
# /\      /\      /\

# El botón para salir del juego:
boton_salir = tk.Button(ventana, text= "Cerrar")

# Creamos la función para cerrar la ventana principal.
def cerrar_juego() -> None:
    # Cierra la ventana
    ventana.destroy()

# Le añadimos la funcionalidad al botón de cierre
boton_salir.configure(command=cerrar_juego)
# Lo añadimos a la ventana
boton_salir.pack()

# Ejecutamos la ventana
ventana.mainloop()