# Escribe tus funciones abajo de esta línea

def regresa_lista():
    lista=[]
    while True:
        num= input()
        if num == '*': 
            break
        lista.append(int(num))
    return lista

def cuenta_pares_impares(lista):
    num_pares = 0 
    num_impares = 0
        for elmento in lista:
            if elmento % 2 == 0:
                num_pares += 1
            else:
                num_impares +=1

    return num_impares, num_pares

def main():
    # Escribe tu código abajo de esta línea
    numeros = regresa_lista()
    print(numeros)
    pares, impares = cuenta_pares_impares(numeros)
    print(f'PARES={pares}')
    print(f'IMPARES={impares}')
if __name__ == '__main__':
    main()
