# Importamos la clase Dado
from dados import Dado

#  Creamos la clase 'Generala'
class Generala:

    # Al construir la clase se crearan 5 dados, con una variable de control que contendrá la cantidad de lanzamientos de los dados.
    def __init__(self) -> any:
        self.dado_01 = Dado()
        self.dado_02 = Dado()
        self.dado_03 = Dado()
        self.dado_04 = Dado()
        self.dado_05 = Dado()
        self.cantidad_lanzamientos = 0


    #  Al llamar esta función, se sumará el lanzamiento y se generará una tirada aleatoria de los dados.
    def tirada(self) -> any:
        self.dado_01.nueva_tirada()
        self.dado_02.nueva_tirada()
        self.dado_03.nueva_tirada()
        self.dado_04.nueva_tirada()
        self.dado_05.nueva_tirada()
        self.cantidad_lanzamientos += 1


    # Con esta función podemos obtener los valores de los dados en forma de diccionario.
    def mostrar_tirada(self) -> dict:
        return {
            "1er Dado": self.dado_01.valor,
            "2do Dado": self.dado_02.valor,
            "3er Dado": self.dado_03.valor,
            "4to Dado": self.dado_04.valor,
            "5to Dado": self.dado_05.valor
        }
    

    # Con esta función obtenemos el valor de la jugada para 1.
    def game_1(self) -> int:
        valores = self.mostrar_tirada().values()
        return sum(1 for x in valores if x == 1)

    def game_2(self) -> int:
        valores = self.mostrar_tirada().values()
        return sum(2 for x in valores if x == 2)

    def game_3(self) -> int:
        valores = self.mostrar_tirada().values()
        return sum(3 for x in valores if x == 3)

    def game_4(self) -> int:
        valores = self.mostrar_tirada().values()
        return sum(4 for x in valores if x == 4)

    def game_5(self) -> int:
        valores = self.mostrar_tirada().values()
        return sum(5 for x in valores if x == 5)

    def game_6(self) -> int:
        valores = self.mostrar_tirada().values()
        return sum(6 for x in valores if x == 6)

    def game_escalera(self) -> int:
        valores = list(self.mostrar_tirada().values())
        if len(set(valores)) == 5 and (max(valores) - min(valores) == 4):
            return 25 if self.cantidad_lanzamientos == 1 else 20
        return 0

    def game_full(self) -> int:
        valores = list(self.mostrar_tirada().values())
        counts = [valores.count(i) for i in range(1, 7)]
        if 3 in counts and 2 in counts:
            return 35 if self.cantidad_lanzamientos == 1 else 30
        return 0

    def game_poker(self) -> int:
        valores = list(self.mostrar_tirada().values())
        counts = [valores.count(i) for i in range(1, 7)]
        if 4 in counts:
            return 45 if self.cantidad_lanzamientos == 1 else 40
        else:
            return 0

    def game_generala(self) -> int:
        valores = list(self.mostrar_tirada().values())
        counts = [valores.count(i) for i in range(1, 7)]
        if 5 in counts:
            self.generala_1 = True
            return 50
        else:
            self.generala_1 = False
            return 0

    def game_generala_doble(self) -> int:
        if not self.generala_1:
            return 0
        valores = list(self.mostrar_tirada().values())
        counts = [valores.count(i) for i in range(1, 7)]
        if 5 in counts:
            return 100
        return 0

    def calcular_games(self) -> dict:
        return {
            "1": self.game_1(),
            "2": self.game_2(),
            "3": self.game_3(),
            "4": self.game_4(),
            "5": self.game_5(),
            "6": self.game_6(),
            "Escalera": self.game_escalera(),
            "Full House": self.game_full(),
            "Poker": self.game_poker(),
            "Generala": self.game_generala(),
            "Generala Doble": self.game_generala_doble()
        }