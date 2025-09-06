import utils as ut

#Variables globales
file = '../datos/datos.csv'

def muestra_opciones_menu():
    opc0 = '0.- Cambia archivo de datos'
    opc1 = '1.- Estadísticas nacionales'
    opc2 = '2.- Estadísticas por estado'
    opc3 = '3.- Porcentaje de casos respecto a la población total'
    opc4 = '4.- Salir'
    largo = 70
    print("*"*largo)
    print(f"** {opc0}{'**':>40}")
    print(f"** {opc1}{'**':>40}")
    print(f"** {opc2}{'**':>40}")
    print(f"** {opc3}{'**':>14}")
    print(f"** {opc4}{'**':>58}")
    print("*"*largo)

def pide_numero_valido():
    while True:
        op = int(input('Opción ==> '))
        if op >= 0 and op <= 4:
            return op
        print('Opción inválida')

def menu_opciones():
    op = 0
    while op != 4:
        muestra_opciones_menu()
        op = pide_numero_valido()
        if op == 0:
            cambia_archivo()
        elif op == 1:
            estadisticas_nacional()
            # print('Realiza cálculo para Nacional')
        elif op == 2:
            # print('Realiza cálculo para Estado')
            estadisticas_por_estado()
        elif op == 3:
            # print('Tabla de porcentaje Nacional')
            porcentaje()

            

def estadisticas_nacional():    
    M = ut.regresa_datos(file)    
    M = ut.limpia_datos(M)    
    fechas = M[0][3:]
    meses = ut.regresa_meses(fechas)    
    acum = ut.regresa_acumulado_mes(M, meses)    
    serie = ut.serie_estado(acum, "Nacional")    
    ut.grafica_serie(meses, serie)
    titulos = ['Estado', 'Población'] + meses  
    acum = ut.regresa_datos_formato(acum)
    ut.muestra_tabla(acum, titulos)

def estadisticas_por_estado():
    estado = input("Estado ==> ")
    M = ut.regresa_datos(file)    
    M = ut.limpia_datos(M)
    fechas = M[0][3:] 
    columnaedo = [fila[2] for fila in M]
    if estado in columnaedo:
        meses = ut.regresa_meses(fechas)    
        acum = ut.regresa_acumulado_mes(M, meses) 
        titulos = ['Estado', 'Población'] + meses  
        acumm = ut.regresa_datos_formato_m(acum, estado)
        ut.muestra_tabla_(acumm, titulos,estado)
        MAX= ut.maximo(estado,fechas,M)       
        serie = ut.serie_estado(acum, estado)
            #if serie and MAX:  
        ut.grafica_serie(meses, serie)
    else:
        print('Estado inválido...')
    
    
    



def porcentaje():
    M = ut.regresa_datos(file)
    M = ut.limpia_datos(M)
    fechas = M[0][3:]
    meses = ut.regresa_meses(fechas)
    acum = ut.regresa_acumulado_mes(M, meses)
    titulos =  ['Estado', 'Población Total', 'Total de casos', '% Casos vs Población'] 
    tabla = ut.porcentaje(acum)
    ut.muestra_tabla_p(tabla,titulos)


def cambia_archivo():
    global file
    file = input('Ruta y nombre del archivo: ')
    print('Ruta cambiada...')

def main():
    menu_opciones()

if __name__ == '__main__':
    main()

