from dados import Jugador, Generala
import time

jugador_1 = Jugador(nombre = input("Jugador N°1: "))

juego = Generala()

while True:
    print(f"Haciendo {juego.cantidad_lanzamientos}°")

    juego.tirada()

    time.sleep(5)

    juego.mostrar_tirada()

    time.sleep(5)

    juego.jugadas()

    juego.mostrar_jugadas()
    while True:
        respuesta = input("¿Quiere anotar su puntaje? Y para Sí | N para No\n Respuesta: ")

        if respuesta == 'N':
            break
        elif respuesta == 'Y':
            break
        else:
            continue
    
    if respuesta == 'Y':
        break
    
    juego.dado_01.valor = 6
    juego.dado_02.valor = 6
    juego.dado_03.valor = 6
    juego.dado_04.valor = 6
    juego.dado_05.valor = 6

    juego.elegir_mantener_dados()

juego.mostrar_conteo()