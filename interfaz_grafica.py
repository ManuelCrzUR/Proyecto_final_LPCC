import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

def construir_horario_docente(docente, list_disponibilidad, list_materias):
    # Creación de tabla sin datos ni restriciones de horario
    datos = [[f'Horario Docente {docente}', 'Materia'],
            ['09:00 - 11:00', list_materias[0] if len(list_materias) > 0 and list_disponibilidad[0] else '-'],
            ['11:00 - 13:00', list_materias[1] if len(list_materias) > 1 and list_disponibilidad[1] else '-'],
            ['13:00 - 15:00', list_materias[2] if len(list_materias) > 2 and list_disponibilidad[2] else '-']]

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
    for i in list_disponibilidad:
        if i == False:
            for j in range(len(datos[0])):
                tabla.get_celld()[(c, j)].set_facecolor('red') 
        c += 1         
    # Agregar materias al horario

    
    # Agregar texto fuera de la tabla
    plt.text(0.5, 1.1, f'Horario para monitorias del docente {docente}',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             transform = ax.transAxes,
             weight = 'bold')

    # Guardar la figura como archivo PNG en la carpeta del proyecto
    fig.savefig('horario_docente_' + str(docente) + '.png')

# Para el caso de la proyección de las materias, se encuentra restrinjido la modificación en los casos que la disponibilidad sea false
# Dejar '' en espacios donde la disponibilidad sea falsta, como lo muestra el ejemplo

def construir_horario_estudiante(estudiante, list_disponibilidad, list_materias):
    # Creación de tabla sin datos ni restriciones de horario
    datos = [[f'Horario Docente {estudiante}', 'Materia'],
            ['09:00 - 11:00', list_materias[0] if  list_disponibilidad[0] else '-'],
            ['11:00 - 13:00', list_materias[1] if  list_disponibilidad[1] else '-'],
            ['13:00 - 15:00', list_materias[2] if  list_disponibilidad[2] else '-']]

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
    for i in list_disponibilidad:
        if i == False:
            for j in range(len(datos[0])):
                tabla.get_celld()[(c, j)].set_facecolor('red') 
        c += 1         
    # Agregar materias al horario

    
    # Agregar texto fuera de la tabla
    plt.text(0.5, 1.1, f'Horario para monitorias del estudiante {estudiante}',
             horizontalalignment = 'center',
             verticalalignment = 'center',
             transform = ax.transAxes,
             weight = 'bold')

    # Guardar la figura como archivo PNG en la carpeta del proyecto
    fig.savefig('horario_estudiante_' + str(estudiante) + '.png')

construir_horario_docente('Manuel_Cruz', [True, False, True], ['Matematicas', '', 'Programación' ])
construir_horario_estudiante('Mariana_Romero', [False, True, True], ['', 'Lógica 2', 'Programación'])