from dados import Jugador, Generala
import time, os


n_jugadores = 0
while True:
    os.system('cls')
    n_jugadores += 1
    exec(f"jugador_{n_jugadores} = Jugador(nombre = input(f'Ingrese el nombre del jugador n°{n_jugadores}:'))")

    time.sleep(1)

    exec(f'print(f"¿El nombre del jugador n°{n_jugadores} es: {globals()["jugador_" + str(n_jugadores)].nombre}?")')

    respuesta_jugadores = input("Sí(Y) o No(N): ")

    bool_de_respuesta = [True if respuesta_jugadores == 'Y' else False]

    if bool_de_respuesta[0] is False:
        n_jugadores -= 1
        continue
    else:
        pass

    mas_jugadores = input("¿Hay más jugadores para agregar? Sí(Y) o No(N). Respuesta:")

    bool_mas_jugadores = [True if mas_jugadores == 'Y' else False]

    if bool_mas_jugadores[0] is False:
        break
    else:
        # print(bool_mas_jugadores)
        time.sleep(1)
        continue

os.system('cls')
print("Lista de Jugadores:\n")
for x in range(1, n_jugadores + 1):
    exec(f'print(f"Jugador N°{x}: {globals()["jugador_" + str(x)].nombre}")')
