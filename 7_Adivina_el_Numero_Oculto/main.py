''''
Debemos de preguntar al usuario un número entre 1 y 50.

Si añaden un número fuera de ese rango, 
vamos a indicar con un error que anime a elegir un número dentro del rango adecuado..

Si no acertamos el número oculto,
preguntaremos al usuario si queremos seguir jugando, 
introduciendo un nuevo número o queremos dejar de jugar.

Finalmente, cuando el usuario acierta correctamente el número oculto, 
mostramos un mensaje de enhorabuena y 
mostramos el número de intentos que hemos utilizado para llegar a esta situación.
'''
from random import randint

numero_oculto = randint(0,50)

user_num = int(input('Ingresa un nuemro entre 1 - 50'))

def menu():
    resp = input('Deseas Continuar s/n\n')
    if resp == 's':
        user_num = int(input('Ingresa un nuemro entre 1 - 50\n'))
        validarRango(user_num)

def Validador(user_num,num_oculto):
    if user_num == num_oculto:
        print('Adivinaste Felicidades')
    else:
        print('Fallaste\n')
        menu()
        
def validarRango(user_num):
    if  1 <= user_num and user_num <= 50:
        Validador(user_num,numero_oculto)
    else:
        print('Valor fuera de rango\n')
        user_num = int(input('Ingresa un nuemro entre 1 - 50\n'))
        validarRango(user_num)
    
