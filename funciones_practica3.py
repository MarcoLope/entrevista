
'''
Alcance de variables. 
'''
x = 500  # Variable Global

def fun1():
    print("Esta es la función 1")
    print(x)


def fun2():
    print("Esta es la función 2")
    x = 34  # ¿ De qué tipo es x ? 
    print("El valor de X es: ")
    print(x)


def fun3():
    print(f"El valor de X es:")
    print(x)  # Error por qué ?? 
    x = 54


def fun4():    
    global x # Manipular la variable Global
    print(x)
    x = 54  # ¿Se cambió el valor?

'''
Practica:
Verifica el llamado de cada una de las funciones. 
'''
def main():
    #fun1()
    #fun2()
    #fun3()
    fun4()
    fun1()
if __name__ == '__main__':
    main()
