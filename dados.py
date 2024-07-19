# Importamos random para poder generar la tirada
import random

# Iniciamos la clase Dados
class Dado:
    def __init__(self) -> any:
        # Al iniciar tendrá dos variables asignadas:

        # Si el Dado se encuaentra bloqueado, es decir: no cambiará su valor.
        self.bloqueo = False
        # Y el valor del dado en si mismo
        self.valor = None


    def nueva_tirada(self) -> any:
        '''
        Al llamar a esta función, el valor del dado se verá afectado.

        No retornará ningún dato.
        '''
        # Verifica que el dado no esté bloqueado.
        if not self.bloqueo:
            # Le da un nuevo valor al dado.
            self.valor = random.randint(1, 6)
    
    # Declaramos la función para bloquear el dado.
    def mantener_dado(self) -> any:
        self.bloqueo = True

    # Declaramos la función para desbloquear el dado.
    def no_mantener_dado(self) -> any:
        self.bloqueo = False
