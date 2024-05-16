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

# Creación de función escribir para la decodificación         
def escribir_estudiante(self, literal):
    if '-' in literal:
        atomo = literal[1:]
        neg = ' no'
    else:
        atomo = literal
        neg = ''
    prof_o_est, i, h, m = self.unravel(atomo)
    if prof_o_est == 1:
        return f'La materia {materias[m]}{neg} se ve en el horario {horarios[h]} del profesor {estudiantes[i]}.'
    else:
            return f'La materia {materia[m]}{neg} se ve en el horario {horarios[h]} del estudiante {profesores[i]}.'

def escribir_docente(self, literal):
    if '-' in literal:
        atomo = literal[1:]
        neg = ' no'
    else:
        atomo = literal
        neg = ''
    p, h, m = self.unravel(atomo)
    return f'La materia {materias[m]}{neg} es dada en el horario {horarios[h]} del profesor {profesores[p]}.'

# Creación del descriptor P para los estudiantes
P = Descriptor([Ne, Nh, Nm])
# print(' ------- DESCRIPTOR P -------')
# print("Cantidad de atomos en el descriptor p:", P.rango[1] - P.rango[0])

# # Ver todos los atomos de P con su codificaicón
# for e in range(Ne):
#     for h in range(Nh):
#         for m in range(Nm):
#             atomo = P.ravel([e, h, m])
#             print(f'La materia {materias[m]} se ve  en el horario {horarios[h]} del estudiante {estudiantes[e]}. Es el atomo {atomo}')
#     print("")
    
# # Ver posible decodificación para determinado atomo Q
# P.escribir_estudiante = MethodType(escribir_estudiante, P)

# atomo_e = P.ravel([0, 0, 0])
# print(f'El caracter que codifica es {atomo_e}')
# print('\n Su decodificación es:')
# print(P.escribir_estudiante(atomo_e))
# print(P.escribir_estudiante('-' + atomo_e))

# Creación del descriptor Q para los profesores
Q = Descriptor([Np, Nh, Nm])
# print(' ------- DESCRIPTOR Q -------')
# print('Cantidad de atomos en el descriptor Q: ', Q.rango[1] - Q.rango[0])

# # Vert todos los atomos de Q para los profesores
# for p in range(Np):
#     for h in range(Nh):
#         for m in range(Nm):
#             atomo = Q.ravel([p, h, m])
#             print(f'La materia {materias[m]} es dada en el horario {horarios[h]} del profesor {profesores[p]}. Es el atomo {atomo}')
#     print ("")

# # Ver posible decodificación apra derterminado atomo P
# Q.escribir_docente = MethodType(escribir_docente, P)

# atomo_p = Q.ravel([0, 0, 0])
# print(f'El caracter que codifica es {atomo_p}')
# print('\n Su decodificación es:')
# print(Q.escribir_docente(atomo_p))
# print(Q.escribir_docente('-' + atomo_p))



# Codificación para las reglas:

# r1 = todo estudiante debe tener un tutor para la materia que demande.
# E = range(3)
# M = range(3)
# H = range(3)
# P = range(3)

# e1 = 0
# h1 = 0
# asignacion_e = (e1, h1)
# print(asignacion_e)

formula1 = ''

class Horario:
    def __init__(self, Es = 3, Pr = 3, M = 3, H = 3):
        self.estudiantes = Es
        self.profesores = Pr
        self.materias = M
        self.horarios = Ho
        self.PyE = 2
        self.PyE = max(len(self.profesores), len(self.estudiantes))
        self.H = Descriptor([self.PoE, self.PyE, len(Ho), len(M)])
        self.H.escribir = MethodType(escribir_estudiante, self. H)
        r1 = self.regla1()
        r2 = self.regla2()
        r3 = self.regla3()
        self.reglas = [r1, r2, r3]
        
    def regla1(self):
        lista = []
        for e in range(self.estudiantes):
            lista_e = []
            for m in range(self.materias):
                lista_m = []
                for h in range(self.horarios):
                    lista_h = []
                    for p in range(self.profesores):
                        otros_horarios = [k for k in range(self.horarios) if k != h]
                        lista_p = []
                        for k in otros_horarios:
                            form1 = '(' + self.P.ravel([e, k, m]) + 'Y' + self.Q.ravel([p, k, m]) + ')'
                            lista_p.append(form1)
                        lista_h.append(Otoria(lista_p))
                    form2 = '(' + self.P.ravel([e, h, m]) + '>' + Otoria(lista_h) + ')'
                    lista_m.append(form2)
                lista_e.append(Ytoria(lista_m))
            lista.append(Ytoria(lista_e))
        return Ytoria(lista)
                 
            
    def regla2(self):
        lista =[]
        for p in range(self.profesores):
            lista_p = []
            for e in range(self.estudiantes):
                lista_e =[]
                for h in range(self.horarios):
                    lista_h = []
                    for m in range(self.materias):
                        otras_materias = [(k) for k in range(self.materias) if k != m]
                        lista_m = []
                        for k in otras_materias:
                            form1 = '-(' + self.P.ravel([e, h, k]) + 'Y' + self.Q.ravel([p, h, k]) + ')' 
                            lista_m.append(form1)
                        form = '(' + '(' + self.P.ravel([e, h, m]) + 'Y' + self.Q.ravel([p, h, m]) +')' + '>' + Ytoria(lista_m) + ')'
                        lista_h.append(form)
                    lista_e.append(Ytoria(lista_h))
                lista_p.append(Ytoria(lista_e))
            lista.append(Ytoria(lista_p))
        return Ytoria(lista)
                        
    
    def regla3(self):
        lista = []
        for p in range(self.profesores):
            lista_p = []
            for e in range(self.estudiantes):
                lista_e = []
                for h in range(self.horarios):
                    lista_h = []
                    for m in range(self.materias):
                        otros_profesores = [(k) for k in range(self.profesores) if k != p]
                        lista_m = []
                        for k in otros_profesores:
                            form2 = '-(' + self.P.ravel([e, h, m]) + 'Y' + self.Q.ravel([k, h, m]) + ')'
                            lista_m.append(form2)
                        form1 = '((' + self.P.ravel([e, h, m]) + 'Y' + self.Q.ravel([p, h,m]) + ')' + '>' + Ytoria(lista_m) + ')'
                        lista_h.append(form1)
                    lista_e.append(Ytoria(lista_h))
                lista_p.append(Ytoria(lista_e))
            lista.append(Ytoria(lista_p))
        return Ytoria(lista)
    
h = Horario()
print('regla 1:\n')
print(inorder_to_tree(h.reglas[0]), '\n')

print('regla 2:\n')
print(inorder_to_tree(h.reglas[1]), '\n')

print('regla 3:\n')
print(inorder_to_tree(h.reglas[2]), '\n')

