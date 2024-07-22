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
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 1:
                suma += 1

        return suma
    
    # Con esta función obtenemos el valor de la jugada para los dados iguales a 2.
    def game_2(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 2:
                suma += 2

        return suma
    

    # Con esta función obtenemos el valor para la jugada con los dados iguales a 3.
    def game_3(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 3:
                suma += 3

        return suma
    

    # Dados iguales a 4
    def game_4(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 4:
                suma += 4

        return suma
    

    # Suma de los dados iguales a 5.
    def game_5(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 5:
                suma += 5

        return suma
    

    # Suma de los dados iguales a 6.
    def game_6(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 6:
                suma += 6

        return suma