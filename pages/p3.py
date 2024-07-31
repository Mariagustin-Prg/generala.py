import tkinter as tk
import pandas as pd
from player import Jugador

class P3:
    def __init__(self) -> None:
        df = pd.DataFrame()

    def set_jugadores(self, lista_jugadores: list) -> None:
        self.jugadores = lista_jugadores

        for n_jugador in self.jugadores:
            
            jugador = Jugador()

            jugador.set_nombre(n_jugador)















if __name__ == '__main__':
    app = P3()