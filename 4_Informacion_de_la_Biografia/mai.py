''''
Pregunte a un usuario su información personal en una sola ronda de preguntas.
Luego hay que verificar que la información que se ha ingresado sea válida.
Finalmente, se imprime un resumen de toda la información que ha sido ingresada.

Por ejemplo: ¿Cuál es su nombre? Si el usuario ingresa *,
hay que indicar que la entrada es incorrecta y se pide que se ingrese correctamente un nombre válido.

Cuando se introduce todo correctamente, se muestra un resumen como el que aparece a continuación:

- Nombre: John Doe
- Fecha de nacimiento: Jan 1, 1954
- Dirección: 24 fifth Ave, NY
- Metas personales: To be the best programmer there ever was.
'''

nombre = input('Cual es tu nombre\n')
nacimiento = input('Cuan es la fecha de la nacimiento?\n')
derreccion = input('Cual es tu dirreccion?\n')
metas_P = input('Cuales son tus metas personales?\n')

def Validador(dato):
    
    if dato in (['*','?',' ','+','1']):
        return True
    else:
        return False

if Validador(nombre):
    print('Ingresa un nombre valido\n')
    nombre = input('Cual es tu nombre?\n')
else:
    print('Nombre: ', nombre,'\n')
print('Nombre: ', nombre,'\n')
print('Nacimiento : ', nacimiento,'\n')
print('Dirreccion: ', derreccion,'\n')
print('Metas Personales: ',metas_P,'\n')





Validador(nombre)