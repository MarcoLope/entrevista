# Escribe tus funciones abajo de esta línea
def enumera(num):
    #for i in range(1,num+1)
    #    print(i)
    i=1
    while i <= num:
        print(i)
        i=i+1


def main():
    # Escribe tu código abajo de esta línea
    numero=int(input())
    enumera(numero)

if __name__ == '__main__':
    main()
