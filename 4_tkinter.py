import tkinter as tk

app = tk.Tk()

app.title("Prueba nro 1 de tkinter")

label = tk.Label(app, text="Hola, ¿qué tal?")
label.pack(pady=10)

label1 = tk.Label(app, text="Not click me again, my friend...")


label2 = tk.Label(app, text="Ok, my friend. You're in serious problems...")

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Click me", command= lambda: label1.pack())
button.pack()

def on_button_click():
    user_input = entry.get()
    label_user = tk.Label(app, text=f"Bienvenido, {user_input}...")
    label_user.pack(pady=5)

button.config(command=on_button_click)

dont_button = tk.Button(app, text="Don't click me!", command=lambda: print(""))
dont_button.pack()

from tkinter import messagebox

def show_message():
    tk.messagebox.showinfo("Información", "No luck for you.")

dont_button.config(command=show_message)

app.mainloop()