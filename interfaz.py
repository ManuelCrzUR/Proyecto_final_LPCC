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

        # Agregar texto fuera de la tabla
        plt.text(0.5, 1.1, f'Horario para monitorias {nombre}',
                 horizontalalignment='center',
                 verticalalignment='center',
                 transform=ax.transAxes,
                 weight='bold')

        # Mostrar la figura
        fig.savefig("horario" + str(nombre) + ".png")
  
from codificadores1 import *
# lista de profesores:
profesores = ['Norma', 'Edgar', 'Edwin']
# lista de horarios:
horarios = ['09:00 - 11:00', '11:00 - 13:00', '13:00 - 15:00 ']
    
def horario_profesor(lista_profesores, lista_horarios):
    for p in lista_profesores:  
        visualizar_horario(p, lista_horarios)

horario_profesor(profesores, horarios)