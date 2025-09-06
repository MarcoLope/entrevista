'''
    Práctica 1 
    Solicitar una edad (int) al usuario. 

    Utilizando:
    if 
    elif
    else

    Crear un programa para evaluar lo siguiente:
    < 0
    <= 6
    <= 11
    <= 16
    <= 100
'''
edad = int(input('Ingresa y tu edad: '))
if edad >= 18:
        identifiacion= input('TIENES ID (S/N): ')
        if identifiacion == 'S':
            print('Tramite de licencia concedido')
        elif identifiacion == 'N':
            print('NO CUMPLES CON LOS REQ')
        else:
            print('Respuesta erronea')
else:
        print('NO CUMPLES REQ')