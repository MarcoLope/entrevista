# Escribe tus funciones abajo de esta línea

def Par_Impar(A1, A2): 
    PAR=0
    IMPAR=0
    for NUMERO in range(A1,A2+1):
        if NUMERO%2==0 and A1!=A2:
            PAR +=1
        else:
            IMPAR +=1
    return PAR

def Pares(A1, A2,PAR):
    if PAR==0 and A2==A1:
        print('No hay pares')
    else:
        if A1<A2:
            for NUMERO in range(A1,A2+1):
                if NUMERO%2==0:
                    print(f'{NUMERO}')
        else:
            for NUMERO in range(A2,A1+1):
                if NUMERO%2==0:
                    print(f'{NUMERO}')
        

def main():
    #escribe tu código abajo de esta línea
    # 14ParesRangoFunc
    #print(f'{"*"*50}\nTarea 04_Ciclos: 14ParesRangoFunc\n{"*"*50}')
    A1= int(input('Valor 1: '))
    A2= int(input('Valor 2: '))
    X= Par_Impar(A1, A2)
    Pares(A1,A2,X)

            
if __name__ == '__main__':
    main()
