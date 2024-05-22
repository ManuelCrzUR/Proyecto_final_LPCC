from Logica import *
from types import MethodType
import matplotlib.pyplot as plt

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
        return f'La materia {self.materias[m]}{neg} se ve en el horario {self.horarios[h]} del profesor {self.estudiantes[i]}.'
    else:
        return f'La materia {self.materias[m]}{neg} se ve en el horario {self.horarios[h]} del estudiante {self.profesores[i]}.'

class Horario:
    def __init__(self, Es = ['Daniel', 'Manuel', 'Sara'], Pr = ['Norma', 'Edgar', 'Edwin'], M = ['Programación', 'Álgebra', 'Cálculo'], Ho = ['09:00 - 11:00', '11:00 - 13:00', '13:00 - 15:00']):
        self.estudiantes = Es
        self.profesores = Pr
        self.materias = M
        self.horarios = Ho
        self.PoE = 2
        self.PyE = max(len(self.profesores), len(self.estudiantes))
        self.H = Descriptor([self.PoE, self.PyE, len(Ho), len(M)])
        self.H.escribir = MethodType(escribir_estudiante, self.H)
        r1 = self.regla1()
        r2 = self.regla2()
        r3 = self.regla3()
        self.reglas = [r1, r2, r3]
        
    def regla1(self):
        lista = []
        for e in range(self.PyE):
            lista_e = []
            for m in range(len(self.materias)):
                lista_m = []
                for h in range(len(self.horarios)):
                    lista_h = []
                    for p in range(len(self.profesores)):
                        otros_horarios = [k for k in range(len(self.horarios)) if k != h]
                        lista_p = []
                        for k in otros_horarios:
                            form1 = '(' + self.H.ravel([1, e, h, m]) + 'Y' + self.H.ravel([0, e, h, m]) + ')'
                            lista_p.append(form1)
                        lista_h.append(Otoria(lista_p))
                    form2 = '(' + self.H.ravel([0, e, h, m]) + '>' + Otoria(lista_h) + ')'
                    lista_m.append(form2)
                lista_e.append(Ytoria(lista_m))
            lista.append(Ytoria(lista_e))
        return Ytoria(lista)
            
    def regla2(self):
        lista =[]
        for p in range(len(self.profesores)):
            lista_p = []
            for e in range(len(self.estudiantes)):
                lista_e =[]
                for h in range(len(self.horarios)):
                    lista_h = []
                    for m in range(len(self.materias)):
                        otras_materias = [(k) for k in range(len(self.materias)) if k != m]
                        lista_m = []
                        for k in otras_materias:
                            form1 = '-(' + self.H.ravel([0, e, h, m]) + 'Y' + self.H.ravel([1, e, h, m]) + ')' 
                            lista_m.append(form1)
                        form = '(' + '(' + self.H.ravel([0, e, h, m]) + 'Y' + self.H.ravel([1, e, h, m]) +')' + '>' + Ytoria(lista_m) + ')'
                        lista_h.append(form)
                    lista_e.append(Ytoria(lista_h))
                lista_p.append(Ytoria(lista_e))
            lista.append(Ytoria(lista_p))
        return Ytoria(lista)
                        
    def regla3(self):
        lista = []
        for p in range(len(self.profesores)):
            lista_p = []
            for e in range(len(self.estudiantes)):
                lista_e = []
                for h in range(len(self.horarios)):
                    lista_h = []
                    for m in range(len(self.materias)):
                        otros_profesores = [(k) for k in range(len(self.profesores)) if k != p]
                        lista_m = []
                        for k in otros_profesores:
                            form2 = '-(' + self.H.ravel([0, e, h, m]) + 'Y' + self.H.ravel([1, e, h, m]) + ')'
                            lista_m.append(form2)
                        form1 = '((' + self.H.ravel([0, e, h, m]) + 'Y' + self.H.ravel([1, e, h, m]) + ')' + '>' + Ytoria(lista_m) + ')'
                        lista_h.append(form1)
                    lista_e.append(Ytoria(lista_h))
                lista_p.append(Ytoria(lista_e))
            lista.append(Ytoria(lista_p))
        return Ytoria(lista)
    
def visualizar_est(self, I):
    datos = [[f'Rol', 'Individio', 'Horario', 'Materia']]
    for l in I:
        if I[l]:
            a, b, c, d = self.H.unravel(l)
            if a == 1:
                datos.append(['Profesor', self.profesores[b], self.horarios[c], d])
    
    # Calcular la altura de la figura en función del número de filas en la tabla
    altura_figura = max(len(datos), 6) * 0.15  # Ajusta el 0.15 según tus necesidades
    
    # Inicialización de la figura con la altura calculada
    fig, ax = plt.subplots(figsize=(8, altura_figura))
    ax.axis('off')
    
    tabla = plt.table(cellText=datos, loc='center', cellLoc='center')
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)
    tabla.scale(1.2, 1.8)

    plt.text(0.5, 1.1, f'Horario monitorías', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, weight='bold')

    plt.show()
