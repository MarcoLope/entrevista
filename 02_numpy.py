
'''
Instalar librería numpy 
Array
1.- np.array(lista)
2.- np.array(matriz)
3.- Acceso a los datos haciendo uso de [1,1] por ejemplo
'''
import numpy as np 

def main():
    pass
if __name__=='__main__':
    main()
'''
np.zeros(3)
np.zeros((3,4))
'''

'''
np.ones(3)
np.ones((3,4))
'''

'''
Linspace
Regresa un array con números espaciados uniformemente en un intervalo especificado
np.linspace(1, 5, 10)
'''

'''
eye
Crea una matriz identidad
np.eye(4)
'''

'''
random.rand
Crea una arreglo (distribución uniforme) entre [0, 1)
np.random.rand(5)
np.random.rand(3,2)
'''


'''
random.randn
Devuelve una muestra de la distribución normal estándar, a diferencia de rand que es uniforme
'''

'''
randint
Devuelve un entero aleatorio incluyendo el límite inferior y excluyendo el límite superior
random.randint(0, 100)
random.randint(0, 100, 10)
'''

'''
reshape
x = np.random.randint(0, 100, 10)
x = x.reshape(5,2)
print(x)
print(x.shape)
'''

'''
Max y Min
x = np.random.randint(0,100,10)
print(x)
print(x.max())
print(x.min())
#Posiciones donde se encuentran respectivamente
print(x.argmax())
print(x.argmin())
print(x.dtype)
'''

'''
Notación de sub-array
x = np.random.randint(0,100,10)
print(x)
x1 = x[0:3]
print(x1)
x[0:3] = 100
print(x)
'''

'''
Numpy no copia un arreglo crea una vista!!!!
x = np.random.randint(0,100,10)
print(x)
x1 = x[:5]
print(x1)
x1[:] = 99
print(x1)
print(x)
'''

'''
Copia
x = np.random.randint(0,100,10)
x1 = x[:5].copy()
x1[:] = 99
print(x1)
print(x)
'''

'''
Selector 
x = np.arange(20)
x = x.reshape(5,4)
print(x)
print(x[1])
print(x[1,2])
print('*'*50)
print(x[1:4, 1:3])
'''

'''
Selector y condicionante
x = np.arange(20)
casos = x>5
print(casos)
print(x[casos])
print(x[x>5])
'''

'''
Numpy array Operaciones
x = np.arange(9)
print(x)
print(x+x)
print(x + 10)
print(x*2)
print(x*x)
y = x.reshape(3,3).copy()
print(y+y)
#0/0 Nan    1/0  Inf 
x = np.arange(9)
print(np.sqrt(x))
print(np.sin(x))
print(np.log(x))
'''


