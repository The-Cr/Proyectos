''''
Animamos a los usuarios a introducir cinco palabras.
Después comprobamos cuáles son palabras palíndromas o no.

¿Qué es un palíndromo? Es una palabra que podemos leer de la misma manera desde la izquierda a la derecha y viceversa.

Ejemplo:

madam es palíndromo.
También lo es malayalam.
En el caso de  geeks no lo es.
'''

palabras = []

print('Ingresa 5 palabras ')

for i in range(1,5):
    print(i,':')
    palabras.append(input(''))


def palindromos(lista):
    for palabra in lista:
        inv_palabras = ''.join(reversed(palabra))
        if inv_palabras == palabra:
            print(palabra,' es un palindromo')
        else:
            print(palabra,' no es in palindromo')

palindromos(palabras)

