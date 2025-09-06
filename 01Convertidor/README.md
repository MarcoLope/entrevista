# Convertidor a centímetros
**Decisiones - Convierte pies, pulgadas y yardas a centímetros**

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
# Escribe tus funciones abajo de esta línea

def main():
  # Escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```
La línea `#Escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Escribe un programa que convierta pies, pulgadas y yardas a centímetros, para lo cual debes definir tres funciones:
- La función **pies_cm(pies)** que recibe una cantidad en `pies`(entero positivo) y devuelva su equivalencia en centímetros.
- La función **pulgadas_cm(pulgadas)** que recibe una cantidad en `pulgadas`(entero positivo) y devuelva su equivalencia en centímetros.
- La función **yardas_cm(yardas)** que recibe una cantidad en `yardas`(entero positivo) y devuelva su equivalencia en centímetros.

**Entradas**
- La opción a ejecutar (`1. pies a cm, 2. pulgadas a cm, 3. yardas a cm`). 
- Un valor entero positivo que corresponde a la cantidad en la medida de acuerdo con la opción tecleada (sólo el número).

**Salida**
- La cantidad equivalente en centímetros (sólo el número). 
- En caso de que el número de opción sea diferente a 1, 2, o 3 se desplegará el mensaje: `Error`.
- En caso de que el valor a convertir sea 0 o menor se desplegará el mensaje: `Error`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
1. pies a cm, 2. pulgadas a cm, 3. yardas a cm
Introduce una opcion: 1
Introduce la cantidad: 1
30.48

1. pies a cm, 2. pulgadas a cm, 3. yardas a cm
Introduce una opcion: 2
Introduce la cantidad: 1
2.54

1. pies a cm, 2. pulgadas a cm, 3. yardas a cm
Introduce una opcion: -5
Introduce la cantidad: 1
Error
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.