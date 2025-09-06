# Multiplicación rusa
Ciclos - Implementación del método de multiplicación rusa de dos números

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

El programa debe pedir dos números enteros positivos, incluyendo 0.
Con estos números, llamados **factor1** y **factor2**, se realizan
las siguientes operaciones:

- El **factor1** se multiplica repetidamente por 2
- El **factor2** se divide repetidamente entre 2 (división entera),
    hasta que llegue a ser igual a 1

Para obtener la multiplicación, se suman todos los valores obtenidos de
**factor1** correspondientes a los valores impares de **factor2**.

El proceso a seguir de manera más gráfica es:
```
factor1: 5
factor2: 12
factor1----factor2---se suma ?
5           12	       no
10          6	       no
20          3	       si
40          1	       si
La multiplicación rusa es = 20 + 40  = 60
```

**Sugerencia**: Utiliza concatenación de strings (+) para construir un string
más grande que contenga toda la secuencia y poder imprimir sólo ese string.
Cuida que haya sólo un espacio entre cada número, y que no haya un espacio al
final

## Entrada

Dos números enteros positivos mayores o iguales a 0

## Salida

Una serie de renglones, donde cada renglón es un paso en el proceso, y
contiene los dos factores separados por un espacio.
Al final se debe imprimir otro renglón con el número resultante de la
multiplicación.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Enter factor 1: 3
Enter factor 0: 0
0
```

```
Enter factor 1: 0
Enter factor 2: 4
0 4
0 2
0 1
0
```

```
Enter factor 1: 37
Enter factor 0: 12
37 12
74 6
148 3
296 1
444
```

```
Enter factor 1: 12
Enter factor 0: 37
12 37
24 18
48 9
96 4
192 2
384 1
444
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.