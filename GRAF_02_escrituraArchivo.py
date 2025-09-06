'''
Escribiendo un archivo
lines = ['linea 1', 'Línea 2', 'linea 3']
    with open('salida.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
'''
import os 


def regresa_path():
    path= os.path.dirname(__file__)    
    return path

def escribe_archivo():
    ruta= regresa_path()
    file= ruta + './../../files/salida.txt'
    lines = ['linea 1', 'Línea 2', 'linea 3']
    with open('salida.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    


def main():
    # Escribe tu código abajo de esta línea
    escribe_archivo()

if __name__ == '__main__':
    main()
