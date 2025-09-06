#Escribe aqui tus funciones

def costo(Tipo_Silla,Num_Sillas):
    if Tipo_Silla in ('B'):
        Total= float(round(Num_Sillas*700,1))
    elif Tipo_Silla in ('E') :
        Total= float(round(Num_Sillas*900,1))
    elif Tipo_Silla in ('L') :
        Total= float(round(Num_Sillas*1500,1))
    return(Total)


# Calcula Costo de las Sillas 
def sillas(Tipo_Silla,Tipo_Cliente,Num_Sillas,Total):
    if Tipo_Cliente in ('F') and Tipo_Silla in ('B','E','L'):
        Total_Desc = Total*0.2        
    elif Tipo_Silla in ('B','E','L') and Total >=10000 and Total <20000:
        Total_Desc = Total*0.1
    elif Tipo_Silla in ('B','E','L') and Total >=20000 :
        Total_Desc = Total*0.15
    else :
        Total_Desc = Total*0.0
    Total_pagar=Total-Total_Desc
    return(Total, Total_Desc, Total_pagar)
        


def main():
    #escribe tu código abajo de esta línea
    # 03TiendadeSillas
    #print(f'{"*"*50}\nTarea 03_Funciones: 03TiendadeSillas\n{"*"*50}')
    Tipo_Silla = input('Tipo silla: ')
    Tipo_Cliente = input('Tipo cliente: ')
    Num_Sillas= int(input('Cantidad de sillas: ')) 
    Total=costo(Tipo_Silla,Num_Sillas)    
    Total, Total_Desc, Total_pagar= sillas(Tipo_Silla,Tipo_Cliente,Num_Sillas,Total)
    print(f"Total sin dcto.  ${Total:>7}")
    print(f"Descuento        ${Total_Desc:>7}")
    print(f"Total a pagar    ${Total_pagar:>7}")
if __name__ == '__main__':
    main()