
#x = [1, "hola", 3.45, True, None]
#print(x[2])
#print(x[10])  
# 10 no es un indice válido 

# x = [[1, 2, 3, 4], [7, 5, 6], ["hola", "Mexico", "Mundo"], [4.56, 1]]
# print(x[2][1])
# print(x[3][1])
# print(x[0])
# largo= Len(X)
# Print(largo)


# Indices negatigvos empiezan de izquieda a derecha en el -1
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(x[-4])
# print(x[-10])

#MODIFICAR LOS VALORES DE LA LISTA 
#x[2]=50
#AGREGAR VALOR AL FINAL
#x.append(150)
#pritn(x)

# SUBLISTA desde el indice inical hasta el fina 
# sub = x[3:6]
# print(sub)
# sub2 = x[:3]
# print(sub2)
# sub3 = x[5:]
# print(sub3)

# sub4 = sub3 + sub2
# print(sub4)

# print(sub)
# sub5 = sub * 3
# print(sub5)
# print(len(sub5))

# del sub[1]
# print(sub)

# for elemento in x:
#     print(elemento)

# print("+"*50)

# for i in range(len(x)):
#     print(x[i])

# print(5 in x)
# print(45 in x)
# print(7 not in x)

# lista = ['hola', 34, 21]
# a, b, c = lista  # Asignación multiple
# print(a, b, c)

# for index, element in enumerate(lista):
#     print(index, element)

# print("+"*50)

# print(lista.index(34))
# # print(lista.index(7575))   #Error porque no existe en la lista.

# lista.append(45)
# lista.append(98)
# lista.append('Mexico')

# print(lista)
# print("+"*50)

# lista.insert(1, "xxxxxx")
# print(lista)
# lista.insert(0, 67.32)
# lista.insert(0, 67.32)
# print(lista)
# print(lista.index(67.32))

# print("+"*50)
# lista.remove('hola')
# lista.remove(67.32)
# print(lista)

# ctr  + k +  c
# ctr  + k +  u

# l = [3, 2, 6, 4, 7, 9, 10, 1, 0, 1, 3, 2]
# print(l)
# l.sort()
# print(l)

# a = ['Hola', '4', 'ave', '56.23', '0.2']
# a.sort()
# print(a)


# String
# cadena = "Hola Mundo"
# for c in cadena:
#     print(c, end=" ")
# print()

# l1 = list(cadena)
# print(l1)

# z = ""
# for c in l1:
#     z += c
# print(z)

#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    for elemento in x:
#        print(elemento, end=' ')
#print()

#lista= ['Hola',34,21]
#print(lista.index(34))
#print(lista.index(345))

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
