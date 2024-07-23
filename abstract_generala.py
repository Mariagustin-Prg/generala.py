# Importamos la clase Dado
from dados import Dado

#  Creamos la clase 'Generala'
class Generala:
    '''
    La clase Generala contiene las jugadas de los dados y los puntajes que puedes hacer con esos dados.
    '''
    # Al construir la clase se crearan 5 dados, con una variable de control que contendrá la cantidad de lanzamientos de los dados.
    def __init__(self) -> any:
        '''
        Crea cinco dados y una variable de control de lanzamientos.
        '''
        self.dado_01 = Dado()
        self.dado_02 = Dado()
        self.dado_03 = Dado()
        self.dado_04 = Dado()
        self.dado_05 = Dado()
        self.cantidad_lanzamientos = 0
        self.generala_1 = False


    #  Al llamar esta función, se sumará el lanzamiento y se generará una tirada aleatoria de los dados.
    def tirada(self) -> any:
        '''
        Genera un nueva tirada con los dados que no han sido bloqueados.

        Acumula un lanzamiento.
        '''
        self.dado_01.nueva_tirada()
        self.dado_02.nueva_tirada()
        self.dado_03.nueva_tirada()
        self.dado_04.nueva_tirada()
        self.dado_05.nueva_tirada()
        self.cantidad_lanzamientos += 1


    # Con esta función podemos obtener los valores de los dados en forma de diccionario.
    def mostrar_tirada(self) -> dict:
        '''
        Devuelve en forma de diccionario los valores de los cinco dados.
        '''
        return {
            "1er Dado": self.dado_01.valor,
            "2do Dado": self.dado_02.valor,
            "3er Dado": self.dado_03.valor,
            "4to Dado": self.dado_04.valor,
            "5to Dado": self.dado_05.valor
        }
    

    def game_1(self) -> int:
        '''
        Calcula el puntaje para la jugada de 1's.
        
        Retorna un entero.
        '''
        # Obtenemos un dict_values con los valores de los dados
        valores = self.mostrar_tirada().values()
        # Calculamos la suma de los dados que son iguales a 1.
        return sum(1 for x in valores if x == 1)


    def game_2(self) -> int:
        '''
        Calcula el puntaje para la jugada de 2's.
        
        Retorna un entero.
        '''
        # Obtenemos los valores de los dados.
        valores = self.mostrar_tirada().values()
        # Calculamos la suma de los dados iguales a 2.
        return sum(2 for x in valores if x == 2)


    def game_3(self) -> int:
        '''
        Calcula el puntaje para la jugada de 3's.
        
        Retorna un entero.
        '''
        # Obtenemos los valores de los dados.
        valores = self.mostrar_tirada().values()
        # Calculamos la suma de los dados iguales a 3.
        return sum(3 for x in valores if x == 3)


    def game_4(self) -> int:
        '''
        Calcula el puntaje para la jugada de 4's.
        
        Retorna un entero.
        '''
        # Obtenemos los valores de los dados.
        valores = self.mostrar_tirada().values()
        # Calculamos la suma de los dados iguales a 4.
        return sum(4 for x in valores if x == 4)


    def game_5(self) -> int:
        '''
        Calcula el puntaje para la jugada de 5's.
        
        Retorna un entero.
        '''
        # Una lista con los valores de los dados.
        valores = self.mostrar_tirada().values()
        # Calcula la suma de los dados iguales a 5.
        return sum(5 for x in valores if x == 5)

    def game_6(self) -> int:
        '''
        Calcula el puntaje para la jugada de 6's.
        
        Retorna un entero.
        '''
        # Obtiene una lista con los valores de los dados.
        valores = self.mostrar_tirada().values()
        # Calcula la suma de los dados iguales a 6.
        return sum(6 for x in valores if x == 6)

    def game_escalera(self) -> int:
        '''
        Verifica si existe escalera y retorna el puntaje de esta jugada.
        '''
        # Obtiene una lista con los valores de los dados.
        valores = list(self.mostrar_tirada().values())
        # Si la lista contiene 5 elementos distintos y la diferencia entre el valor máximo y el mínimo es 4:
        if len(set(valores)) == 5 and (max(valores) - min(valores) == 4):
            # Retorna 25 solo si hay un lanzamiento realizado, en otro caso, retorna 20.
            return 25 if self.cantidad_lanzamientos == 1 else 20
        # En caso de no haber escalera, retorna 0.
        return 0

    def game_full(self) -> int:
        '''
        Verifica la jugada es full y retorna el puntaje de esta.
        '''
        # Obtenemos los valores de los dados.
        valores = list(self.mostrar_tirada().values())
        # Hacemos un conteo de los valores de los dados, de entre 1 y 6, se agreaga a una lista.
        counts = [valores.count(i) for i in range(1, 7)]
        # Si existe un valor que fue contado tres veces y otro que haya sido contado 2, tenemos full house:
        if 3 in counts and 2 in counts:
            # Por tanto, retorna 35 solo si hay realizado un único lanzamiento, en otro caso, retorna 30.
            return 35 if self.cantidad_lanzamientos == 1 else 30
        # Si no hay full house, retorna 0.
        return 0

    def game_poker(self) -> int:
        '''
        Verifica si hay Poker y retorna el puntaje de esa jugada.
        '''
        # obtenemos los valores de los dados.
        valores = list(self.mostrar_tirada().values())
        # Contamos las veces que está cada dado en la lista
        counts = [valores.count(i) for i in range(1, 7)]
        # Si existe un elemento que aparece 4 veces, tenemos poker:
        if 4 in counts:
            # Si hay un único lanzamiento realizado, retorna 45, si no retorna 40.
            return 45 if self.cantidad_lanzamientos == 1 else 40
        # Si no hay poker, retorna 0.
        else:
            return 0

    def game_generala(self) -> int:
        '''
        Verifica si hay generala y retorna el puntaje de la jugada.
        '''
        # Una lista con los valores de los dados
        valores = list(self.mostrar_tirada().values())
        # Contamos cuantas veces están los valores en la lista
        counts = [valores.count(i) for i in range(1, 7)]
        # Si un elemento está 5 veces en la lista:
        if 5 in counts:
            # Definimos que la primer generala es válida.
            self.generala_1 = True
            # Retorna 50
            return 50
        else:
            return 0

    def game_generala_doble(self) -> int:
        '''
        Verifica si hay generala, si hubo anteriormente una y retorna el puntaje.
        '''
        # Si no hubo una generala anteriormente
        if not self.generala_1:
            # Retorna 0
            return 0
        valores = list(self.mostrar_tirada().values())
        counts = [valores.count(i) for i in range(1, 7)]
        if 5 in counts:
            return 100
        return 0

    def calcular_games(self) -> dict:
        '''
        Calcula todos los puntajes y los devuelve en forma de diccionario.
        '''
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