# Conjetura Ulam
Ciclos - Generar una secuencia de números según la Conjetura Ulam

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

El programa debe pedir un número entero positivo mayor a 0 al usuario.
A partir de ese número, se va a generar una secuencia nueva, según la
Conjetura Ulam (también llamada Collatz o "hailstone sequence").
La secuencia comienza con el número dado por el usuario, y termina con el
número 1. Para llegar a ello, se toma el número inicial y se modifica según
las siguientes reglas:

- Si el número es par, se divide entre 2 (división entera)
- Si el número es impar, se multiplica por 3 y se le suma 1

El proceso sigue con el nuevo número, hasta que se obtenga el 1.

**Sugerencia**: Utiliza el operador de division entera para los números pares.

**Sugerencia**: Utiliza concatenación de strings (+) para construir un string
más grande que contenga toda la secuencia y poder imprimir sólo ese string.
Cuida que haya sólo un espacio entre cada número, y que no haya un espacio al
final

Si el número ingresado no es mayor a 0, el programa debe imprimir:
`Invalid input`

## Entrada

Un número entero positivo mayor a 0

## Salida

Un string con la secuencia correcta según las reglas.

Ejemplo de ejecución del programa:
```
>>> 6
6   --------------  es par, se divide por 2
3   -------------   es impar, se multiplica por 3 y se suma 1
10 --------------  es par, se divide por 2
5 ---------------	es impar, se multiplica por 3 y se suma 1
16 -------------   es par se divide entre 2
8   -------------   es par se divide entre 2
4   -------------   es par se divide entre 2
2   -------------   es par se divide entre 2
1
```
(La explicación de la operación a realizar es sólo para la comprensión del
problema, el programa sólo desplegará los números de la conjetura,
en un sólo renglón y separados por un espacio)

La salida del programa debe de ser exactamente de la siguiente forma:

```
Enter a number: 8
8 4 2 1
```

```
Enter a number: 3
3 10 5 16 8 4 2 1
```

```
Enter a number: 0
Invalid input
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.
