import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

def visualizar_horario(nombre, horarios):

        # Recolección de los datos que se van a usar en las tablas.
        datos = [[f'Horario {nombre}', 'Materia']]
        for horario in horarios:
            datos.append([horario, '-'])


        # Inicialización de tabla y estructura, que contiene la figura
        fig, ax = plt.subplots()
        ax.axis('off')
        tabla = plt.table(cellText=datos,
                          loc='center',
                          cellLoc='center')
        tabla.auto_set_font_size(False)
        tabla.set_fontsize(12)
        tabla.scale(1.2, 1.8)
        
        c = 1
        for i in disponibilidad:
            if not i:
                for j in range(len(datos[0])):
                    tabla.get_celld()[(c, j)].set_facecolor('red')
            c += 1


        # Agregar texto fuera de la tabla
        plt.text(0.5, 1.1, f'Horario para monitorias {nombre}',
                 horizontalalignment='center',
                 verticalalignment='center',
                 transform=ax.transAxes,
                 weight='bold')

        # Mostrar la figura
        fig.savefig("horario" + str(nombre) + ".png")
  
def colorear_ocupados():
        c = 1
        for i in disponibilidad:
            if not i:
                for j in range(len(datos[0])):
                    tabla.get_celld()[(c, j)].set_facecolor('red')
            c += 1

          
from codificadores import *

# lista de profesores:
profesores = ['Norma', 'Edgar', 'Edwin']
# lista de horarios:
horarios = ['09:00 - 11:00', '11:00 - 13:00', '13:00 - 15:00 ']
    
def horario_profesor(lista_profesores, lista_horarios, Nlista_horarios = []):
    for p in range(len(lista_profesores) - 1):
        for Np in range(len(Nlista_horarios) - 1):
            
            visualizar_horario(p, lista_horarios)

horario_profesor(profesores, horarios)

