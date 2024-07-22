from dados import Dado

class Generala:

    
    def __init__(self) -> any:
        self.dado_01 = Dado()
        self.dado_02 = Dado()
        self.dado_03 = Dado()
        self.dado_04 = Dado()
        self.dado_05 = Dado()
        self.cantidad_lanzamientos = 0



    def tirada(self) -> any:
        self.dado_01.nueva_tirada()
        self.dado_02.nueva_tirada()
        self.dado_03.nueva_tirada()
        self.dado_04.nueva_tirada()
        self.dado_05.nueva_tirada()
        self.cantidad_lanzamientos += 1



    def mostrar_tirada(self) -> dict:
        return {
            "1er Dado": self.dado_01.valor,
            "2do Dado": self.dado_02.valor,
            "3er Dado": self.dado_03.valor,
            "4to Dado": self.dado_04.valor,
            "5to Dado": self.dado_05.valor
        }
            
    def game_1(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 1:
                suma += 1

        return suma
    
    def game_2(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 2:
                suma += 2

        return suma
    
    def game_3(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 3:
                suma += 3

        return suma
    
    def game_4(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 4:
                suma += 4

        return suma
    
    def game_5(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 5:
                suma += 5

        return suma
    
    def game_6(self) -> int:
        valores = self.mostrar_tirada()

        suma = 0

        for x in valores.values():
            if x == 6:
                suma += 6

        return suma