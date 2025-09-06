# Escribe tus funciones abajo de esta línea
def suma(num):
    #for i in range(1,num+1)
    #    print(i)
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum


def main():
    # Escribe tu código abajo de esta línea
    numero=int(input())
    r=suma(numero)
    print(r)
if __name__ == '__main__':
    main()
