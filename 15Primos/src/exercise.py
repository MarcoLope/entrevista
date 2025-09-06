# Escribe tus funciones abajo de esta línea

def es_primo(num):
    if num <2:
        return False
    else:
        for n in range(2, num):
            if num % n == 0:
                #print("No es primo", n, "es divisor")
                return False
        #print("Es primo")
        return True

def main():
    #escribe tu código abajo de esta línea
    #print(f'{"*"*50}\nTarea 04_Ciclos: 15Primo\n{"*"*50}')
    A1= int(input('Escribe un numero entero : '))
    primo= es_primo(A1)
    print(primo)
            
if __name__ == '__main__':
    main()
