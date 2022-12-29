''''
Vamos a pedir al usuario que ingrese el significado completo de una organización o concepto y 
con ello como resultado obtendremos el acrónimo. 
Por ejemplo:

Entrada -> As Soon As Possible. Salida -> ASAP.
Entrada -> World Health Organization. Salida -> WHO.
Entrada -> Absent Without Leave. Salida -> AWL.
'''

comparador = 'qwertyuiopñlkjhgfdsazxcvbnm '
frase = 'cristian vallejos ruiz gabriel'

def acronimo(frase,comparador):
    frase = frase.title()
    frase_list = list(frase)
    list_comp = list(comparador)
    for i in range(0,len(list_comp)):
        print(list_comp[i], i)
        
        if list_comp[i] in frase_list:
            for j in range(0,frase_list.count(list_comp[i])):
                frase_list.remove(list_comp[i])
                print(frase_list)
    resp = ''.join(frase_list)
    return resp

print(acronimo(frase,comparador))
