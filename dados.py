# Importamos random para poder generar la tirada
import random

# Iniciamos la clase Dados
class Dado:
    '''
    El objeto tendrá seis valores posibibles y podrá mantener ese valor, o volver a ser lanzado
    '''
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
    def cambiar_bloqueo(self) -> any:
        '''
        Al llamar a esta función, el dado cambia de su estado de estar bloqueado
        a estar desbloqueado y viceversa.
        '''
        if self.bloqueo is True: 
            self.bloqueo = False
        
        else:
            self.bloqueo = True

