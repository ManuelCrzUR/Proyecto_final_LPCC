import matplotlib.pyplot as plt

class Horarios:
    def __init__(self, materias=['', '', ''], disponibilidad=[False, False, False]) -> None:
        self.materias = materias
        self.disponibilidad = disponibilidad

    def visualizar_horario(self, rol, nombre, diccionario_monitorias):
        # Convertir el diccionario a listas de materias y disponibilidad
        materias, disponibilidad = self.dicc_a_lista(diccionario_monitorias)

        # Recolección de los datos que se van a usar en las tablas.
        datos = [[f'Horario {rol} {nombre}', 'Materia'],
                 ['09:00 - 11:00', materias[0] if disponibilidad[0] else '-'],
                 ['11:00 - 13:00', materias[1] if disponibilidad[1] else '-'],
                 ['13:00 - 15:00', materias[2] if disponibilidad[2] else '-']]

        # Inicialización de tabla y estructura, que contiene la figura
        fig, ax = plt.subplots()
        ax.axis('off')
        tabla = plt.table(cellText=datos,
                          loc='center',
                          cellLoc='center')
        tabla.auto_set_font_size(False)
        tabla.set_fontsize(12)
        tabla.scale(1.2, 1.8)

        # Colorear horarios no disponibles
        c = 1
        for i in disponibilidad:
            if not i:
                for j in range(len(datos[0])):
                    tabla.get_celld()[(c, j)].set_facecolor('red')
            c += 1

        # Agregar texto fuera de la tabla
        plt.text(0.5, 1.1, f'Horario para monitorias del {rol} {nombre}',
                 horizontalalignment='center',
                 verticalalignment='center',
                 transform=ax.transAxes,
                 weight='bold')

        # Mostrar la figura
        plt.show()

    def dicc_a_lista(self, diccionario_monitorias):
        materias = []
        disponibilidad = []

        for materia, disponible in diccionario_monitorias.items():
            materias.append(materia)
            disponibilidad.append(disponible)

        return materias, disponibilidad
    
    def visualizacion_corregida(horarios, materias, profesores, estudiantes):
        
        for h in horarios:
            for m in materias:
                for p in profesores:
                    for e in estudiantes:
                        if 
                    


# Ejemplo de uso
diccionario_monitorias = {'Matemáticas': True, 'Física': False, 'Química': True}
horario = Horarios()
horario.visualizar_horario('Monitor', 'Juan', diccionario_monitorias)