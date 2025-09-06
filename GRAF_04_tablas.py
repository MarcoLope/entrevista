'''
1.- Crear la función muestra_tabla que recibe una matriz con los datos y 
una lista con los titulos de las columnas
2.- Preparar el contenedor donde se va a graficar
    fig, ax = plt.subplots(figsize=(10,5))    
5.- Graficar  la tabla
    ax.table(cellText=data, colLabels=column_labels, loc="center")
6-  Mostrar la tabla
    plt.show()
7.- verifica los métodos de ax:
    axis('tight')
    axis('off')
'''
import matplotlib.pyplot as plt

def muestra_tabla(datos, titulos):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.table(cellText=datos,colLabels=titulos, loc='center')
    ax.axis('tight')
    ax.axis('off')
    plt.show()

def main():
    columnas = ['Estado', 'Población', 'Calificación']
    matriz = [['Yucatán', 3550000, 9.2], ['CDMX', 8780932, 7.5], ['Puebla', 4650000, 8.3]]
    muestra_tabla(matriz,columnas)
if __name__=='__main__':
    main()
