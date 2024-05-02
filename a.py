from Logica import *
from types import MethodType


# Forma descriptor estudiantes P(e, h, m)
# Forma descriptor profesores Q(p, h, m)

# Información necesiaria para crear los distintos descriptores
Ne = 3
Np = 3
Nh = 3
Nm = 3

# Ejemplos estudiantes
estudiantes = ['Moñas', 'Manuel', 'Sara']
# Ejemplos profesores
profesores = ['Norma', 'Edgar', 'Edwin']
# Ejemplos intervalos de horarios
horarios = ['09:00 - 11:00', '11:00 - 13:00', '13:00 - 15:00 ']
# Ejemplso posibles materias
materias = ['Programación', 'Algebra', 'Calculo']

# Creació de función escribir para la decodificación         
def escribir_estudiante(self, literal):
    if '-' in literal:
        atomo = literal[1:]
        neg = ' no'
    else:
        atomo = literal
        neg = ''
    e, h, m = self.unravel(atomo)
    return f'La materia {materias[m]}{neg} se ve  en el horario {horarios[h]} del estudiante {estudiantes[e]}. Es el atomo {atomo}'

def escribir_docente(self, literal):
    if '-' in literal:
        atomo = literal[1:]
        neg = ' no'
    else:
        atomo = literal
        neg = ''
    p, h, m = self.unravel(atomo)
    return f'La materia {materias[m]}{neg} es dada en el horario {horarios[h]} del profesor {profesores[p]}. Es el atomo {atomo}'

# Creación del descriptor P para los estudiantes
P = Descriptor([Ne, Nh, Nm])
print(' ------- DESCRIPTOR P -------')
print("Cantidad de atomos en el descriptor p:", P.rango[1] - P.rango[0])

# Ver todos los atomos de P con su codificaicón
for e in range(Ne):
    for h in range(Nh):
        for m in range(Nm):
            atomo = P.ravel([e, h, m])
            print(f'La materia {materias[m]} se ve  en el horario {horarios[h]} del estudiante {estudiantes[e]}. Es el atomo {atomo}')
    print("")
    
# Ver posible decodificación para determinado atomo Q
P.escribir_estudiante = MethodType(escribir_estudiante, P)

atomo_e = P.ravel([0, 0, 0])
print(f'El caracter que codifica es {atomo_e}')
print('\n Su decodificación es:')
print(P.escribir_estudiante(atomo_e))
print(P.escribir_estudiante('-' + atomo_e))

# Creación del descriptor Q para los profesores
Q = Descriptor([Np, Nh, Nm])
print(' ------- DESCRIPTOR Q -------')
print('Cantidad de atomos en el descriptor Q: ', Q.rango[1] - Q.rango[0])

# Vert todos los atomos de Q para los profesores
for p in range(Np):
    for h in range(Nh):
        for m in range(Nm):
            atomo = Q.ravel([p, h, m])
            print(f'La materia {materias[m]} es dada en el horario {horarios[h]} del profesor {profesores[p]}. Es el atomo {atomo}')
    print ("")

# Ver posible decodificación apra derterminado atomo P
Q.escribir_docente = MethodType(escribir_docente, P)

atomo_p = Q.ravel([0, 0, 0])
print(f'El caracter que codifica es {atomo_p}')
print('\n Su decodificación es:')
print(Q.escribir_docente(atomo_p))
print(Q.escribir_docente('-' + atomo_p))