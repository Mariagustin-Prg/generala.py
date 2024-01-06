import os

os.system("pip install prettytable")

from prettytable import PrettyTable

os.system('cls')

datos = [
    ["Juan", 25, "Ciudad A"],
    ["María", 30, "Ciudad B"],
    ["Carlos", 22, "Ciudad C"]
]

encabezados = ["Nombre", "Edad", "Ciudad"]

tabla = PrettyTable(encabezados)
tabla.add_rows(datos)

print(tabla)
