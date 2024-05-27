from Logica import *
from types import MethodType
import matplotlib.pyplot as plt
import random



# Creación de función escribir para la decodificación         
def escribir_estudiante(self, literal,):
    if '-' in literal:
        atomo = literal[1:]
        neg = ' no'
    else:
        atomo = literal
        neg = ''
    prof_o_est, i, h, m = self.unravel(atomo)
    if prof_o_est == 1:
        return f'La materia {materias[m]}{neg} se ve en el horario {horarios[h]} del profesor {profesores[i]}.'
    else:
        return f'La materia {materias[m]}{neg} se ve en el horario {horarios[h]} del estudiante {estudiantes[i]}.'

class Horario:
    def __init__(self, Es = ['Daniel', 'Manuel'], Pr = ['Norma', 'Edgar'], M = ['Programación', 'Álgebra'], Ho = ['09:00 - 11:00', '11:00 - 13:00']):
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
        r4 = self.regla4()
        r5 = self.regla5()
        self.reglas = [r1, r2, r3, r4, r5]
    
    # TODO ESTUDIANTE DEBE TENER UN PROFESOR PARA LA MATERIA QUE DEMANDE   
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
                            form1 = '(' + self.H.ravel([0, e, k, m]) + 'Y' + self.H.ravel([1, p, k, m]) + ')'
                            lista_p.append(form1)
                        lista_h.append(Otoria(lista_p))
                    form2 = '(' + self.H.ravel([0, e, h, m]) + '>' + Otoria(lista_h) + ')'
                    lista_m.append(form2)
                lista_e.append(Ytoria(lista_m))
            lista.append(Ytoria(lista_e))
        return Ytoria(lista)
    
    # SOLO UNA MATERIA DE ESTUDIANTE Y PROFESOR EN EL MISMO HORARIO
    def regla2(self):
        lista = []
        for p in range(len(self.profesores)):
            lista_p =[]
            for e in range(len(self.estudiantes)):
                lista_e = []
                for h in range(len(self.horarios)):
                    lista_h = []
                    for m in range(len(self.materias)):
                        otras_materias = [k for k in range(len(self.materias)) if k != m]
                        lista_m = []
                        for k in otras_materias:
                            lista_m.append('(-' + self.H.ravel([0, e, h, k]) + 'Y-' + self.H.ravel([1, p, h, k]) + ')')
                        form2 = '((' + self.H.ravel([0, e, h, m]) + 'Y' + self.H.ravel([1, p, h, m]) + ')' + '>' + Ytoria(lista_m) + ')'
                        lista_h.append(form2)
                    lista_e.append(Ytoria(lista_h))
                lista_p.append(Ytoria(lista_e))
            lista.append(Ytoria(lista_p))
        return(Ytoria(lista))
    
    # SI UN ESTUDIANTE Y UN PROFESOR TIENE CLASE A DETERMINADO HORARIO, OTRO PROFESOR NO PUEDE TENER LA MISMA CLASE EN EL MISMO HORARIO                 
    def regla3(self):
        lista = []
        for e in range(len(self.estudiantes)):
            lista_e = []
            for p in range(len(self.profesores)):
                lista_p = []
                for h in range(len(self.horarios)):
                    lista_h = []
                    for m in range(len(self.materias)):
                        otros_profesores = [k for k in range(len(self.profesores)) if k != p]
                        lista_m = []
                        for k in otros_profesores:
                            lista_m.append('-' + self.H.ravel([1, k, h, m]))
                        form = '((' + self.H.ravel([1, p, h, m]) + 'Y' + self.H.ravel([0, e, h, m]) + ')>' + Ytoria(lista_m) + ')'
                        lista_h.append(form)
                    lista_p.append(Ytoria(lista_h))
                lista_e.append(Ytoria(lista_p))
            lista.append(Ytoria(lista_e))
        return(Ytoria(lista))
                    
    # SI EL ESTUDIANTE YA VIO UN MATERIA, NO PUEDE VER LA MISMA MATERIA EL MISMO DIA
    def regla4(self):
        lista = []
        for e in range(len(self.estudiantes)):
            lista_e = []
            for h in range(len(self.horarios)):
                lista_h = []
                for m in range(len(self.materias)):
                    otros_horarios = [k for k in range(len(self.horarios)) if k != h]
                    lista_m = []
                    for k in otros_horarios:
                        lista_m.append('-' + self.H.ravel([0, e, k, m]))
                    form2 = '(' + self.H.ravel([0, e, h, m]) + '>' + Ytoria(lista_m) + ')'
                    lista_h.append(form2)
                lista_e.append(Ytoria(lista_h))
            lista.append(Ytoria(lista_e))
        return(Ytoria(lista))
    
    # Si estudiante demandad, entonces profesor oferta
    def regla5(self):
        lista = []
        for e in range(len(self.estudiantes)):
            lista_e = []
            for p in range(len(self.profesores)):
                lista_p = []
                for h in range(len(self.horarios)):
                    lista_h = []
                    for m in range(len(self.materias)):
                        lista_m =[]
                        form = '(' + self.H.ravel([0, e, h, m]) + '>' + self.H.ravel([1, p, h, m]) +')'
                        lista_m.append(form)
                    lista_h.append(Ytoria(lista_m))
                lista_p.append(Ytoria(lista_h))
            lista_e.append(Ytoria(lista_p))
        return(Ytoria(lista_e))              
    
    def visualizar_est(self, I):
        datos = [[f'Rol', 'Persona', 'Horario', 'Materia']]
        colores = {}  # Diccionario para almacenar los colores asignados a cada estudiante/profesor
        filas = []  # Lista para almacenar las filas de datos

        for l in I:
            if I[l]:
                a, b, c, d = self.H.unravel(l)
                if d < 4:
                    if a == 1:
                        rol = 'Profesor'
                        nombre = self.profesores[b]
                    else:
                        rol = 'Estudiante'
                        nombre = self.estudiantes[b]
                    
                    # Asignar un color aleatorio si el estudiante/profesor aún no tiene uno asignado
                    if nombre not in colores:
                        colores[nombre] = (random.random(), random.random(), random.random())
                    
                    # Agregar la fila a la lista de filas
                    filas.append([rol, nombre, self.horarios[c], self.materias[d], c])

        # Agrupar las filas por persona
        filas_agrupadas = {}
        for fila in filas:
            persona = fila[1]
            if persona not in filas_agrupadas:
                filas_agrupadas[persona] = []
            filas_agrupadas[persona].append(fila)
        
        # Ordenar cada grupo por horario en orden descendente
        for persona in filas_agrupadas:
            filas_agrupadas[persona].sort(key=lambda x: x[4], reverse=False)
        
        # Combinar las filas ordenadas en una sola lista
        filas_ordenadas = []
        for persona in filas_agrupadas:
            filas_ordenadas.extend(filas_agrupadas[persona])
        
        # Agregar las filas ordenadas a los datos
        for fila in filas_ordenadas:
            datos.append(fila[:-1])  # Excluir el índice del horario (c) al agregar a datos

        # Calcular la altura de la figura en función del número de filas en la tabla
        altura_figura = max(len(datos), 6) * 0.15  # Ajusta el 0.15 según tus necesidades
        
        # Inicialización de la figura con la altura calculada
        fig, ax = plt.subplots(figsize=(8, altura_figura))
        ax.axis('off')
        
        tabla = plt.table(cellText=datos, loc='center', cellLoc='center')
        tabla.auto_set_font_size(False)
        tabla.set_fontsize(12)
        tabla.scale(1.2, 1.8)
        
        # Aplicar los colores asignados a cada fila correspondiente
        for i, fila in enumerate(datos[1:], start=1):
            rol, nombre, horario, materia = fila
            if nombre in colores:
                for j, item in enumerate(fila):
                    tabla[(i, j)].set_facecolor(colores[nombre])

