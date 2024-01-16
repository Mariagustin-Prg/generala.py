import tkinter as tk
from tkinter import messagebox

def continuar_con_proceso():
    respuesta = messagebox.askyesno("Confirmar", "¿Desea continuar con el proceso?")
    if respuesta:
        # Coloca aquí el código para continuar con el proceso
        print("Proceso en marcha...")
    else:
        print("Proceso detenido.")

# Configuración básica
app = tk.Tk()
app.title("Ejemplo con MessageBox")

# Botón para iniciar el proceso
button = tk.Button(app, text="Iniciar Proceso", command=continuar_con_proceso)
button.pack(pady=20)

# Bucle de eventos
app.mainloop()

