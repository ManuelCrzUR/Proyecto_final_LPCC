from Logica import *
from types import MethodType
import matplotlib.pyplot as plt
import random
    
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

