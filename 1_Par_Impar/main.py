"""
Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000

Cuando el usuario proporciona el número, comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.

Ejemplo:

Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro?
"""

def ParImpar(num):
    res = num % 2
    if (res == 0):
        print('\n¡Es un número par! ¿Puedes añadir otro?\n')
        Validar()
    elif(res != 0):
        print('\n¡Es un número impar! ¿Puedes añadir otro?\n')
        Validar()


def Validar():
    num1 = int(input('\nEn que numeros estas pensando?\n'))
    if (num1 >= 1 and num1 <= 1000):
        ParImpar(num1)
    else:
        print('\nIngrese Un numeo dentro del rango 1 - 1000\n')
        Validar()

Validar()
