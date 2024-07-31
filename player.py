# Importamos la clase Dado
from dados import Dado

# Creamos la clase Jugador
class Jugador:
    '''
    Esta clase contendrá los puntajes de los jugadores, junto con su nombre.

    Para introducir el nombre se debe llamar a la función 'set_nombre'.
    '''
    # Al crear la clase, se crearan las variables que contendran los valores de los juegos
    def __init__(self) -> any:
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

        self.nombre = ""


    #  Con esta función se configura el nombre
    def set_nombre(self, name: str) -> any:
        '''
        Se introduce el nombre del jugador.
        '''
        self.nombre = name


    def get_nombre(self) -> str:
        '''
        Retorna el nombre del jugador.
        '''
        return self.nombre
    
    def get_puntajes(self) -> dict:
        return {"1":self.game_1,
                "2": self.game_2,
                "3": self.game_3,
                "4": self.game_4,
                "5": self.game_5,
                "6": self.game_6,
                "Escalera": self.escalera,
                "Full": self.full,
                "Poker": self.poker,
                "Generala": self.generala,
                "Generala": self.generala_doble}