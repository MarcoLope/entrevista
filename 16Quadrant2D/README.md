# Cuadrante en el plano cartesiano
Decisiones - Determina en qué cuadrante del plano cartesiano se encuentra
un punto dado.

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    # Escribe tu código abajo de esta línea
    pass


if __name__ == '__main__':
    main()
```

El plano cartesiano se divide en 4 cuadrantes, que van en sentido contrario
a las manecillas del reloj. El cuadrante depende del signo de las coordenadas
del punto en X y Y.

![Cuadrantes](../../images/quadrants.png)

El programa va a preguntar por dos números, las coordenadas en X y en Y,
y luego imprimirá en qué cuadrante se encuentra el punto dado.
Las respuestas pueden incluir, además de los cuatro cuadrantes
(I, II, III y IV), el **Origin** o los puntos sobre los ejes: **X axis** o
**Y axis**.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter X coordinate of the point: 0
Enter Y coordinate of the point: 0
The point is in quadrant: Origin
```

```plaintext
Enter X coordinate of the point: 2
Enter Y coordinate of the point: 2
The point is in quadrant: I
```

```plaintext
Enter X coordinate of the point: -4.7
Enter Y coordinate of the point: 0
The point is in quadrant: Y axis
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.