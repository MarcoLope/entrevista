import os
import pdb
from matplotlib import pyplot as plt
def regresa_path():
    path = os.path.dirname(__file__)    
    return path

def regresa_datos(archivo):
    ruta = regresa_path() + '/'  
    file = ruta + archivo
    matriz = []
    with open(file, 'r') as f:
        while True:
            linea = f.readline()
            if not linea:
                break
            renglon = linea.split(',')
            matriz.append(renglon)
    return matriz

def limpia_datos(datos):
    #Se elimina el enter de la primera linea
    datos[0][-1] = datos[0][-1].split('\n')[0]
    for i in range(1, len(datos)):
        #Se convierte a numero la población
        datos[i][1] = int(datos[i][1])
        #Se quitan las comillas dobles del estado        
        datos[i][2] = datos[i][2][1:-1]
        #Se elimina el enter del ultimo dato
        datos[i][-1] = datos[i][-1].split('\n')[0]
        #Se convierten a numeros a partir de la columna 3
        for j in range(3, len(datos[i])):
            datos[i][j] = int(datos[i][j])
    return datos

def regresa_meses(fechas):
    meses = []
    for fecha in fechas:
        mes = fecha[3:]
        if mes not in meses:
            meses.append(mes)
    return meses

def regresa_acumulado_mes(datos, meses):
    fechas = datos[0][3:] #titulos de Población y el estado
    acumulados = []
    for renglon in datos[1:]:
        dato_mes = [renglon[2]] #Estado
        dato_mes.append(renglon[1]) #Población
        for mes in meses: #El primer mes es 02-2020
            suma = 0 #Cada vez que se inicia un mes, se inicializa la suma
            for pos, fecha in enumerate(fechas):
                mes_interno = fecha[3:]
                if mes_interno == mes:
                    cantidad = renglon[pos+3]
                    suma += cantidad
            dato_mes.append(suma) #El acumulado se guarda una vez que termino todo el renglon
        acumulados.append(dato_mes) #Por cada vez que termina de analizar un mes, se agrega
    return acumulados

def serie_estado(datos_acumulados, estado):
    for renglon in datos_acumulados:
        if renglon[0] == estado:
            return renglon[2:]
    return None

def grafica_serie(x, y):
    fig, ax = plt.subplots(figsize=(12,7))
    ax.plot(x,y)
    plt.xticks(x, rotation=90)
    plt.subplots_adjust(bottom=0.25)
    plt.grid(True)
    plt.title('Datos por mes')
    ax.set_xlabel('Meses')
    ax.set_ylabel('Casos positivos')
    plt.show()

def muestra_tabla(datos, titulos):
    fig, ax = plt.subplots(figsize=(24,7))
    table = ax.table(cellText=datos, colLabels=titulos, loc='center')
    table.auto_set_font_size(True)
    table.set_fontsize(9)
    table.auto_set_column_width(list(range(len(titulos))))
    ax.axis('off')
    plt.show()

def muestra_tabla_(lista,titulos,estado):
    datos=[titulos,lista]
    fig, ax = plt.subplots(figsize=(24,7))
    table = ax.table(cellText=datos, loc='upper center')
    table.auto_set_font_size(True)
    table.auto_set_column_width(list(range(len(titulos))))
    ax.axis('off')
    ax.set_title(f'Tabla de casos acumulados por mes/año correspondiente al estado de {estado}', 
                fontweight ="bold") 
    plt.show()
          


def regresa_datos_formato(datos):
    for i in range(len(datos)):
        #datos[i][0] = f'{datos[i][0]:,}' #Se coloca el formato de miles ','
        for j in range(1, len(datos[i])):
            datos[i][j] = f'{datos[i][j]:,}'
    return datos 
    

def regresa_datos_formato_m(datos,estado):
    for renglon in datos:
        if renglon[0] == estado:
            return renglon[0:]
    return None

def porcentaje(acum):
    tabla = []
    for i in range(len(acum)):
        fila = []
        valores = acum[i][2:]
        edo = acum[i][0]
        pob = acum[i][1]
        suma = sum(valores)
        porc = round(100*suma/pob,2)
        fila = [edo] + [f'{pob:,}'] + [f'{suma:,}'] + [porc]
        tabla.append(fila)
    return tabla


def muestra_tabla_p(datos, titulos):
    fig, ax = plt.subplots(figsize=(5,6))
    table = ax.table(cellText=datos, colLabels=titulos, loc='center', cellLoc='center',
        colColours=["lightsteelblue"] * 10)
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.auto_set_column_width(list(range(len(titulos))))
    ax.axis('off')
    plt.show()   

def maximo(estado,fechas, M):
    for renglon in M:
        # maximos = []
        if renglon[2] == estado:
            casos = renglon[3:]
            max_ = renglon.index(max(casos))
            print(f'El número máximo de casos en el estado de {estado} fue de {casos[max_-3]} el día {fechas[max_-3]}')


def main():
    file = '../datos/datos.csv'
    M = regresa_datos(file)
    # print(M[1])
    # pdb.set_trace()
    M = limpia_datos(M)
    
    print('*'*50)
    fechas = M[0][3:]
    meses = regresa_meses(fechas)
    print(meses)
    print('*'*50)
    acum = regresa_acumulado_mes(M, meses)
    print('*'*50)
    serie_puebla = serie_estado(acum, 'AGUASCALIENTES')
    print(serie_puebla)
    titulos = ['Estado', 'Población'] + meses  
    acum = regresa_datos_formato(acum) #['YUCATAN', '2,259,098', '0', '75                
    acumm = regresa_datos_formato_m(acum,'YUCATAN')
    muestra_tabla_(acumm, titulos,'YUCATAN')     
if __name__ == '__main__':
    main()