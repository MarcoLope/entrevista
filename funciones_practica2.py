
def saludo_simple():
    """Función sin arugmentos de entrada
    """
    print("Hola a secas")
    print("Adios.")

def saluda(mensaje):
    """Función con un argumento y sin valor de retorno
    Args:
        mensaje (_str_): String con el mensaje a mostrar
    """
    print("Hola " + mensaje)

def saluda_default(mensaje = 'Alicia'):
    """Función con un argumento opcional y sin valor de retorno
    Args:
        mensaje (str, optional): String con el mensaje a mostrar. 
        Defaults to 'Alicia'.
    """
    print("Hola " + mensaje)

def suma(num1, num2):
    """Función que suma 2 números y regresa el resultado
    Args:
        num1 (_int_): Valor del primer entero
        num2 (_int_): Valor del segundo entero
    Returns:
        int: Valor de la suma
    """
    resultado = num1 + num2
    return resultado

'''
Practica:
Verifica el llamado de cada una de las funciones. 
'''
def main():
    #saludo_simple()
    #saluda('PACO PACO')
    #saluda_default('PATO')
    #saluda_default()
    res= suma(1,2)
    print(res)
    res= suma("Hola", "PATO")
    print(res)
if __name__ == '__main__':
    main()
