import random

class Dados:
    def __init__(self):
        self.bloqueo = False
        self.valor = None

    def nueva_tirada(self):
        if not self.bloqueo:
            self.valor = random.randint(1, 6)
        else:
            pass
    
    def mantener_dado(self):
        self.bloqueo = True

    def no_mantener_dado(self):
        self.bloqueo = False


class Jugador:
    def __init__(self, nombre):
        self.game_1 = 0
        self.game_2 = 0
        self.game_3 = 0
        self.game_4 = 0
        self.game_5 = 0
        self.game_6 = 0
        self.escalera = 0
        self.full = 0
        self.poker = 0
        self.generala = 0
        self.generala_doble = 0
        self.total = 0

        self.nombre =nombre

    def calcular_resultados_finales(self):
        self.total = self.game_1 + self.game_2 + self.game_3 + self.game_4 + self.game_5 + self.game_6 + self.escalera + self.full + self.poker + self.generala + self.generala_doble

class Generala:
    def __init__(self):
        self.dado_01 = Dados()
        self.dado_02 = Dados()
        self.dado_03 = Dados()
        self.dado_04 = Dados()
        self.dado_05 = Dados()
        self.cantidad_lanzamientos = 0

    def tirada(self):
        self.dado_01.nueva_tirada()
        self.dado_02.nueva_tirada()
        self.dado_03.nueva_tirada()
        self.dado_04.nueva_tirada()
        self.dado_05.nueva_tirada()
        self.cantidad_lanzamientos = 1

    def mostrar_tirada(self):
        print(f" Dado 1: {self.dado_01.valor}\n", 
              f"Dado 2: {self.dado_02.valor}\n", 
              f"Dado 3: {self.dado_03.valor}\n",
              f"Dado 4: {self.dado_04.valor}\n", 
              f"Dado 5: {self.dado_05.valor}\n")
        
    def elegir_mantener_dados(self):
        self.mostrar_tirada()
        while True:
            lista_de_mantencion = input("Por favor, separando por comas, eliga los dados que desee mantener en la tirada.\n Solamente escribiendo los índices de los dados seleccionado. \n")

            try:
                lista_a_mantener = eval('[' + lista_de_mantencion +']')
                
                for index in lista_a_mantener:
                    exec(f"self.dado_0{index}.mantener_dado()")

                lista_que_no_mantiene = [n for n in range(1, 6) if n not in lista_a_mantener]
                
                for index in lista_que_no_mantiene:
                    exec(f"self.dado_0{index}.no_mantener_dado()")

                break

            except NameError:
                print(f"Algunos de los índices no está numerado correctamente: '{lista_de_mantencion}'")
                continue
    
    def jugadas(self):
        self.j_game_1 = 0
        self.j_game_2 = 0
        self.j_game_3 = 0
        self.j_game_4 = 0
        self.j_game_5 = 0
        self.j_game_6 = 0
        self.j_escalera = 0
        self.j_full = 0
        self.j_poker = 0
        self.j_generala = 0
        self.j_generala_doble = 0
        
        lista_de_jugada = (self.dado_01.valor,
                           self.dado_02.valor,
                           self.dado_03.valor,
                           self.dado_04.valor,
                           self.dado_05.valor)
        
        self.j_game_1 = sum([n for n in lista_de_jugada if n == 1])
        self.j_game_2 = sum([n for n in lista_de_jugada if n == 2])
        self.j_game_3 = sum([n for n in lista_de_jugada if n == 3])
        self.j_game_4 = sum([n for n in lista_de_jugada if n == 4])
        self.j_game_5 = sum([n for n in lista_de_jugada if n == 5])
        self.j_game_6 = sum([n for n in lista_de_jugada if n == 6])

        posibles_escaleras = ([1, 2, 3, 4, 5],
                              [2, 3, 4, 5, 6],
                              [1, 3, 4, 5, 6])
        
        if lista_de_jugada in posibles_escaleras:
            if self.cantidad_lanzamientos == 1:
                self.j_escalera = 25
            else:
                self.j_escalera = 20

        
        # Verifica y resulta si la lista tiene Full
        for n in range(1, 7):
            if lista_de_jugada.count(n) == 3:
                for n2 in [p for p in range(1, 7) if p != n]:

                    if lista_de_jugada.count(n2) == 2 and self.cantidad_lanzamientos == 1:
                        self.j_full = 35
                        break

                    elif lista_de_jugada.count(n2) == 2 and self.cantidad_lanzamientos != 1:
                        self.j_full = 30
                        break

                    else:
                        pass
            else:
                pass

        for n in range(1, 7):
            if lista_de_jugada.count(n) >= 4 and self.cantidad_lanzamientos == 1:
                self.j_poker = 45
                break

            elif lista_de_jugada.count(n) >= 4 and self.cantidad_lanzamientos != 1:
                self.j_poker = 40
                break

            else:
                continue

        for n in range(1, 7):
            if lista_de_jugada.count(n) == 5 and self.j_generala == 50:
                self.j_generala_doble = 100

            elif lista_de_jugada.count(n) == 5 and self.cantidad_lanzamientos != 1:
                self.j_generala = 50

            elif lista_de_jugada.count(n) == 5 and self.cantidad_lanzamientos == 1:
                print("¡Generala servida! Ha ganado el juego!")

            elif lista_de_jugada.count(n) == 5:
                print("Generala!!!!!!!")
    

    # Esta función imprime los resultados de las jugadas
    def mostrar_jugadas(self):
        print(f"1: {self.j_game_1}")
        print(f"2: {self.j_game_2}")
        print(f"3: {self.j_game_3}")
        print(f"4: {self.j_game_4}")
        print(f"5: {self.j_game_5}")
        print(f"6: {self.j_game_6}")
        print(f"Escalera: {self.j_escalera}")
        print(f"Full House: {self.j_full}")
        print(f"Poker: {self.j_poker}")
        print(f"Generala: {self.j_generala}")
        print(f"Generala Doble: {self.j_generala_doble}\n")

    def mostrar_conteo(self):
        lista_de_jugada = (self.dado_01.valor,
                        self.dado_02.valor,
                        self.dado_03.valor,
                        self.dado_04.valor,
                        self.dado_05.valor)
        
        for x in range(1, 7):
            print(f'{x}:', lista_de_jugada.count(x))