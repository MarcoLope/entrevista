# Escribe tus funciones abajo de esta línea
def entero():
    n= int(input())
    return n
def de_float():
    n=float(input())
    return n
def promedio(N_elementos_Prom):
    suma=0
    for i in range(N_elementos_Prom):
        num= de_float()
        suma= suma+num
    promedio=suma/N_elementos_Prom
    return promedio

def main():
    # Escribe tu código abajo de esta línea
    n=entero()
    res=promedio(n)
    print(res)

if __name__ == '__main__':
    main()
