# Números de Fibonacci
Ciclos - Calcular un número especifico en la secuencia de Fibonacci

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():    
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

La secuencia de Fibonacci es una serie de números que inicia de la
siguiente forma:

```
0 1 1 2 3 5 8 13 21 34 55 ...
```

La característica que tiene es que cada número de la serie se calcula como
la suma de los dos números anteriores. De manera que el siguiente número sería
`34 + 55 = 89`.

Para efectos de este programa, asignaremos un número de posición (o índice) a
cada número de la secuencia, comenzando con el 0. Esto se puede visualizar
de la siguiente forma:

```
Serie:  0 1 1 2 3 5 8 13 21 34 55 ...
Indice: 0 1 2 3 4 5 6 7  8  9  10 ...
```

Escribe un programa que pida al usuario el índice, como un número entero
positivo. El programa debe calcular el número de Fibonacci correspondiente a
dicho ínidice. Por ejemplo, si el usuario da el número `9`, el programa debe
imprimir el número `34`.

**Nota**: Sólo necesitas recordar los dos números anteriores.
Debes empezar con los números `0` y `1`.
Debes utilizar un ciclo **while** para resolver este problema.

## Entrada

Un número entero positivo mayor o igual a 0

## Salida

Un número de la secuencia de Fibonacci.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Enter a number: 0
0
```

```
Enter a number: 3
2
```

```
Enter a number: 20
6765
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.