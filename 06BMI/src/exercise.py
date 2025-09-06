def IMC(peso,altura):
    if peso>0 and altura >0:
        indice=peso/((altura)**2)
        if indice < 20:
            print('PESO BAJO')
        elif indice < 25:
            print('NORMAL')
        elif indice < 30:
            print('SOBREPESO')
        elif indice < 40:
            print('OBESIDAD')
        else:
            print(f'OBESIDAD MORBIDA')
    else:
         print('Revisa tus datos, alguno de ellos es erróneo.')

def main():
    #escribe tu código abajo de esta línea
    # 06BMI
    #print(f'{"*"*50}\nTarea 02_Decisiones: 06BMI\n{"*"*50}')
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    IMC(peso,altura)


if __name__ == '__main__':
    main()