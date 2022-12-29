'''
Preguntamos al usuario en que está pensando. 
Cuando se introduce la respuesta, realizará el conteo de palabras en la sentencia e imprimimos en la salida el resultado.

Ejemplo:

Pregunta: ¿En qué estás pensando?
Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!
'''


import string

def entrada(pensamiento):
    delim = [',',' ','?','¡','¿','!','.']
    lista = pensamiento.split()
    print('Bien expresaste tu pensamiento en ',len(lista), ' palabras')


pensamiento = input('En que estas pensando?')


entrada(pensamiento)
