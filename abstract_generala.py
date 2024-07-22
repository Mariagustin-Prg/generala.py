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
    

    # Verifica si hay escalera
    def game_escalera(self) -> int:
        # Los dados en un diccionario.
        valores = self.mostrar_tirada()

        valores_unicos =[]
        valores_unicos = [v for v in valores.values() if v not in valores_unicos]

        if len(valores_unicos) == 5:
            if self.cantidad_lanzamientos == 1:
                return 25
            else:
                return 20
        else:
            return 0
        
    # Verifica si los dados hacen full house
    def game_full(self) -> int:
        valores = self.mostrar_tirada().values()
        full_house = False

        lista_full = [valores.count(c) for c in range(1,7)]

        if 3 in lista_full and 2 in lista_full:
            full_house = True
        else: 
            return 0
        
        if full_house and self.cantidad_lanzamientos == 1:
            return 35
        elif full_house and self.cantidad_lanzamientos > 1:
            return 30
        else:
            pass


    # Verifica si los dados hacen poker.
    def game_poker(self) -> int:
        valores = self.mostrar_tirada().values()
        poker = False

        cont_poker = [valores.count(x) for x in range(1,7)]

        if 4 in cont_poker:
            poker = True
        else:
            return 0
        
        if poker and self.cantidad_lanzamientos == 1:
            return 45
        elif poker and self.cantidad_lanzamientos > 1:
            return 40
        

    # Verifica si los dados hacen generala.
    def game_generala(self) -> int:
        pass

    # Verifica si hay generala doble.
    def game_generala_doble(self) -> int:
        pass