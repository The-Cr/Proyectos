"""
edimos al usuario que introduzca varias entradas con varias preguntas.

Puede ser cualquier cosa, como un nombre, un adjetivo, un pronombre o incluso una acción.
Una vez que se obtiene la entrada, se puede reorganizar para construir su propia historia.
"""

def Entrada():
    lista = ['','','']
    lista[0] = input('ingresa una pregunta')
    lista[1] = input('ingresa un adjetivo')
    lista[2] = input('ingresa una accion en tercera persona')
    return lista


datos = Entrada()

def salida():
    print('Mark le pregunta a lucia')
    print(datos[0])
    print('lucia se ')
    print(datos[2])
    print('luego lucia le dice')
    print(datos[1])

salida()