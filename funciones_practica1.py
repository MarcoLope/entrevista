import random

'''
Práctica 

pip install pep8

1.- Crear la función fortuna(number)
2.- Dentro de ella colocar el siguiente código:

3.- Desde la función main generar un número aleatorio
    entre 1 y 4
    r = random.randint(1, 5)
4.- Llama a la función fortuna 
5.- Imprime el resultado en pantalla
'''
def fortuna(number):
    if number == 1:
        return 'Hoy tendrás un día maravilloso'
    elif number == 2:
        return "Hoy será el peor día tu vida"
    elif number == 3:
        return "Mejor no digas nada"
    elif number == 4:
        return "Apuesta todo!"
    else:
        return "Nada para nadie"

def main():
    numero= random.randint(1,5)
    f=fortuna(numero)
    print(f)
if __name__ == '__main__':
    main()
