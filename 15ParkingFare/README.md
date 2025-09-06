# Tarifa de estacionamiento
Decisiones - Determina la tarifa a pagar en un estacionamiento público.

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    # Escribe tu código abajo de esta línea
    pass


if __name__ == '__main__':
    main()
```

Un estacionamiento público cobra una tarifa que varía según el tiempo que un
auto haya permanecido dentro. La tarifa se determina según la siguiente imagen:
![Tarifa estacionamiento](../../images/IMG_20210320_204417498.jpg)

El programa va a preguntar por dos números, la cantidad de horas, y la cantidad
de minutos que duró un carro en el estacionamiento.
Calcula el precio que debe pagar un auto que haya permanecido ese tiempo.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter number of hours: 1
Enter number of minutes: 40
Total to pay: 5
```

```plaintext
Enter number of hours: 3
Enter number of minutes: 1
Total to pay: 22
```

```plaintext
Enter number of hours: 6
Enter number of minutes: 50
Total to pay: 65
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.