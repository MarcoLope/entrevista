import random

def llena_matriz(filas,columnas):
    M=[]
    # Se piden los datos de la fila 0
    for i in range(filas):
        fila=[]
        for j in  range(columnas):
            dato= int(input(f'C[{i},{j}]='))
            fila.append(dato)
        M.append(fila)
    return M

def llena_matriz_aleatorio(filas,columnas):
    M=[]
    # Se piden los datos de la fila 0
    for i in range(filas):
        fila=[]
        for j in  range(columnas):
            dato= random.randint(1, 6)
            fila.append(dato)
        M.append(fila)
    return M

def main():
    #A = llena_matriz(2,3)
    A = llena_matriz_aleatorio(2,3)
    print(A)

if __name__ == '__main__':
    main()
