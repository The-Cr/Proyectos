''''
En este caso, nuestro objetivo es averiguar exactamente la cantidad de propina que 
hay que proporcionar después de un servicio. En este caso, 
hay que solicitar la factura total. 
Con esto, aplicaremos la propina para el 18%, 20% y 25%.

Ejemplo:

Mensaje inicial: ¿Cuál es la factura total de hoy, por favor?
Entrada: $55.87
Salida: La propina aplicando el 18% is $10.06, que contabiliza un total de $65.93
'''

factura = float(input('Cual es la factura total de hoy?\n'))

def fact(num):
    if num > 1 and num < 60:
        propina = round((num*18)/100,2)
        porc_prop = 18
        total = propina + num
    if num > 60 and num < 120:
        propina = round((num*20)/100,2)
        porc_prop = 20
        total = propina + num
    if num > 120:
        propina = round((num*25)/100,2)
        porc_prop = 25
        total = propina + num
    print('La propina aplicando el ',porc_prop,'% , es', propina ,", que contabiliza un total de $",round(total,2))

fact(factura)