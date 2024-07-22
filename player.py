# Importamos la clase Dado
from dados import Dado

# Creamos la clase Jugador
class Jugador:
    
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
        self.nombre = name