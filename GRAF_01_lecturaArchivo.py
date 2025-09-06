'''
Leyendo un archivo
Probando el método readlines
with open('datos.csv', 'r') as f:
        lines = f.readlines()
¿Qué  hace?

¿Es necesario cerrar el archivo?

Ruta:
os.path.dirname(__file__)

¿Cómo lo guardo en una matriz?

otra forma..   readline()
with open('datos.csv', 'r') as f:
        linea = True        
        while linea:
            linea = f.readline()
'''
import os
def regresa_path():
    path = os.path.dirname(__file__)
    print(path)
    return path

def lee_archivo():
    # file = './../../files/numero.txt' ----> este es de windows
    ruta = regresa_path()
    file = ruta + '/../../files/datos.csv'
    with open(file, 'r') as f:
        lineas = f.readlines()
    return lineas

def lee_archivo_2():
    ruta = regresa_path()
    file = ruta + '/../../files/datos.csv'
    matriz = []
    with open(file, 'r') as f:
        while True:
            linea = f.readline()
            if not linea:
                break
            renglon = linea.split(',')
            matriz.append(renglon)
    return matriz

def main():
    regresa_path()
    res = lee_archivo_2()
    #print(res)
    print(res[2])

if __name__ == '__main__':
    main()