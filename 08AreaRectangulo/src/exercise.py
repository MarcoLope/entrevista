#Escribe aqui tus funciones
#  03Tienda de Sillas
        
# Área de un rectángulo
def area_triangulo(base, altura):
    if base>0 or altura>0:
        Area=round(base*altura,3)
    else: 
        print('Para valores no definido')
    return(Area) 

def main():

    # 08ÁreaRectangulo
    #print(f'{"*"*50}\nTarea 03_Funciones: 08ÁreaRectangulo\n{"*"*50}')
    base= float(input('Dame la base: '))
    altura= float(input('Dame la altura: '))
    A=area_triangulo(base, altura)
    print(f'El área del rectángulo es: {A}')

if __name__ == '__main__':
    main()
