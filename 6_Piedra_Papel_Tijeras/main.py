'''
Es un popular juego para dos jugadores. 
Cualquier jugador puede 
ejecutar una jugada con sus manos con estas opciones que tenemos disponible  a continuación:

piedra (puño cerrado)
papel (mano plana)
tijeras (un puño con el dedo índice y el dedo medio extendidos, formando una V)

'''

from random import randint

def menu():
    res = input('Dease Continuar s/n')
    if res == 's':
        opciones_user = input('''tijera','papel','piedra\n''')
        Juego(opciones_user)
    else:
        exit()

def Juego(user):
    opciones = ['tijera','papel','piedra']
    bot = opciones[randint(0,2)]
    print('USUARIO: ',user,'\n')
    print('BOT: ',bot,'\n')
    if user == bot:
        print('Empate')
        menu()
    elif user == 'tijera' and bot == 'papel':
        print('Ganaste')
        menu()
    elif user == 'piedra' and bot == 'tijera':
        print('Ganaste')
        menu()
    elif user == 'papel' and bot == 'piedra':
        print('Ganaste')
        menu()

    elif bot == 'tijera' and user == 'papel':
        print('Perdiste')
        menu()
    elif bot == 'piedra' and user == 'tijera':
        print('Perdiste')
        menu()
    elif bot == 'papel' and user == 'piedra':
        print('Perdiste')
        menu()
    
opciones_user = input('''tijera','papel','piedra\n''')
Juego(opciones_user)
  

