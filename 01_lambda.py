'''
Generación de listas utilizando range
Verificar: list(range(10,15))
'''

# def main():
#     lista=list(range(10,15))
#     print(lista)
#     print(type(lista))
# if __name__ == '__main__':
#     main()

'''
Creación de una lista utilizando la siguiente sintaxis
[n**2 for n in nums]  #Se elevará al cuadrado cada número n que se encuentra en la lista nums
'''
# def main():
#     nums=list(range(5))
#     lista=[n**2 for n in nums]
#     print(lista)
# if __name__ == '__main__':
#     main()

'''
map: Aplica una función a cada elemento de una lista
Ejemplo:

def times2(n):
    return n ** 2

seq = [1,2,3,4,5]
list(map(times2, seq))
'''
# def times2(n):
#     return n ** 2

# seq = [1,2,3,4,5]
# list(map(times2, seq))


# def main():
#     seq=list(range(1,6))
#     lista=list(map(times2, seq))
#     print(lista)
# if __name__ == '__main__':
#     main()
'''
Función lambda

def nombre_func(num): return num * 2 
Es equivalente a:   lambda num:num*2
Ejemplo: 
t = lambda num:num*2
print(t(3))
'''

def main():
    t = lambda num:num**2
    print(t(5))
    t2= lambda n1, n2:n1**n2
    print(t2(2,5))

if __name__ == '__main__':
    main()

'''
Utilice map y lambda para generar los cuadrados de una secuencia de numeros desde el 10 hasta el 15
list(map(lambda num:num*2, seq))
'''

def main():
    t = lambda num:num**2
    print(t(5))
    t2= lambda n1, n2:n1**n2
    print(t2(2,5))

if __name__ == '__main__':
    main()

''' 
Filter
list(filter(lambda n:n%2==0, seq))
'''
