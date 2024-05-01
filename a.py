from Logica import *

def escribir_horario(self, literal):
    if '-' in literal:
        atomo = literal[1:]
        neg = ' no'
    else:
        atomo = literal
        neg = ''
    x, y = self.unravel(atomo)
    return f'El profesor {neg} tiene clase {x}, {y}'

class Horario:
    
    def __init__(self, horarios_p, materias_p, horarios_e, materias_e) -> None:
        self.P = Descriptor([3, 3, 3])
        self.Q = Descriptor([3, 3, 3])