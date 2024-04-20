import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage


def construir_horario_docente(docente, list):
    # Creación de tabla sin datos ni restriciones de horario
    datos = [[f'Horario Docente {docente}', 'Materia'],
            ['09:00 - 11:00', '-'],
            ['11:00 - 13:00', '-'],
            ['13:00 - 15:00', '-']]

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Ocultar ejes
    ax.axis('off')

    # Crear la tabla
    tabla = plt.table(cellText=datos,
                    loc='center',
                    cellLoc='center')

    # Configurar estilo de la tabla
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)
    tabla.scale(1.2, 1.8)  # Ajustar tamaño de celda

    # Colorear los horarios no disponibles
    c = 1
    for i in list:
        if i == False:
            for j in range(len(datos[0])):
                tabla.get_celld()[(c, j)].set_facecolor('red') 
        c += 1
            
    # for j in range(len(datos[0])):
    #     tabla.get_celld()[(3, j)].set_facecolor('red') 
    
    # Agregar texto fuera de la tabla
    plt.text(0.5, 1.1, f'Horario para el docente {docente}',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             transform = ax.transAxes,
             weight = 'bold')

    # Guardar la figura como archivo PNG en la carpeta del proyecto
    fig.savefig('horario_docente_' + str(docente) + '.png')

construir_horario_docente('Andres', [True, False, True])