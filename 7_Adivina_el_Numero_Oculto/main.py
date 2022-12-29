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
def Validador(user_num,num_oculto):
    if user_num == num_oculto:
        return True
    else:
        return False

def validarRango(user_num):
    if  1 <= user_num and user_num <= 50:
        return True
    else:
        return False
    
Resp = 's'
cont = 0
while Resp != 'n':
    user_num = int(input('Ingresa un nuemro entre 1 - 50\n'))
    if validarRango(user_num):
        if Validador(user_num,numero_oculto):
            cont += 1
            print('Felicidades has acertado')
            print('intentos realizados ', cont)
            exit()
        else:
            print('Fallaste\n')
            Resp = input('Desea Continuar s/n\n')
            cont += 1
    else:
        print('valor fuera de rango')
        
