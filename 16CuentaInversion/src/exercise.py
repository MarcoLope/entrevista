# Escribe tus funciones abajo de esta línea
from math import sqrt
from math import ceil

# def valida(A1, A2):
#     if A1>0 and A2>0:
#         Porcentual=A2/100
#         Mensual=Porcentual/12
#         return Mensual
#     else:
#         print('Error en los datos')   

    
def INTERES_ACUMULADO(A1, A2):
    if A1>0 and A2>0:
        Porcentual=A2/100
        Mensual=Porcentual/12
        for i in range(1,13):
                i=round(A1*pow(1+Mensual,i),2)
        print(i)
    else:
        #TOTAL=A1*pow(1+Mensual,12)
        print('Error en los datos')   
        

def main():
    #escribe tu código abajo de esta línea
    #print(f'{"*"*50}\nTarea 04_Ciclos: 16CuentaInversion\n{"*"*50}')
    A1= float(input('Escribe la cantidad de dinero inicial : '))
    A2= float(input('Escribe el porcentaje de interes anual : '))
    INT=INTERES_ACUMULADO(A1,A2)
    

            
if __name__ == '__main__':
    main()
