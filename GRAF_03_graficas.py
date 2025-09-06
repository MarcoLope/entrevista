'''
1.- Crear un entorno virtual
    a.- Cargar el entorno
    b.- Instalar la librería matplotlib
2.- Importar la libraria pyplot de matplotlib
3.- Crear la función graficaLinea que recibe 2 arreglos (eje de las x y eje de las y's )
4.- Preparar el contenedor donde se va a graficar
    fig, ax = plt.subplots(figsize=(10,5))
5.- Graficar  ax.plot(x,y)
6.- Mostrar la gráfica
    plt.show()
'''

'''
Practica 2
1.- Cargar el entorno virtual
2.- Importar la libraria pyplot de matplotlib
3.- Preparar el contenedor donde se van a tener 2 gráficas
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
4.- Realizar las siguientes gráficas
    ax1.plot(x,y)    
    ax2.bar(x,y)
'''


''''
Practica 3 
Etiquetas y otras propiedades.
verifica los métodos de plt:
    xticks(x,rotation=90)
    margins(0.1)
    subplots_adjust(bottom=0.25)
    grid(True)
    title("Titulo de la gráfica")
Ahora verifica los métodos de "ax"
    set_xlabel("Eje x")
    set_ylabel("Eje y")    
'''

from matplotlib import pyplot as plt

def grafica_linea(x,y):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(x,y)
    plt.show()


def grafica_doble(x,y):
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,5))
    ax1.plot(x,y)
    ax2.bar(x,y)
    plt.show()

def grafica3(x,y):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(x,y)
    plt.xticks(x,rotation=90)
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.25)
    plt.grid(True)
    plt.grid('Grafica Edo y Valores')
    ax.set_xlabel('Estados')
    ax.set_ylabel('Calificaciones')
    plt.ylimit(-15,150)
    plt.show()

def main():
    # Escribe tu código abajo de esta línea
    estados = ['Puebla', 'Mexico', 'Veracruz', 'Hidalgo']
    valores = [5, 60, 99, 77]
    grafica_doble(estados,valores)



if __name__ == '__main__':
    main()