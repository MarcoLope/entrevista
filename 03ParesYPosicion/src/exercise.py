# Escribe tus funciones abajo de esta línea

# pide usuario el numero de elementos y los va guardadno 
def recibe(num):
    Numeros=[]
    for i in range(num):
        Numeros.append(int(input()))
    return(Numeros)

# con el modulo 2 va imprimiendo aquellos pares 

def par(lista):
    for i in lista:
        if i % 2 ==0:
             print(f'pos {lista.index(i)}, valor {i}')
            # pos 3, valor 4

def main():
    #escribe tu código abajo de esta línea
    #print(f'{"*"*50}\nTarea 05_Listas: 03Pares y posición\n{"*"*50}')
    A1= int(input(''))
    lista=recibe(A1)
    par(lista)
            
if __name__ == '__main__':
    main()
