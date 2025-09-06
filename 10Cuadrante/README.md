# Cuadrante
**Decisiones - Número de cuadrante donde se encuentra un número (grados) entre 0 y 360**

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
  # Escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

La línea `#Escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

Escribe un programa que lea un número entero que se encuentre entre 0 y 360 que representa los grados del plano cartesiano y que muestre como resultado el número de cuadrante en donde se encuentra. 
En caso de que el grado caiga en un eje, tu programa debe mostrar la palabra `"eje"`.
En caso de que el grado sea menor a cero o mayor a 360,  tu programa debe mostrar la palabra `"excede"`.

**Entrada**
- Un número entero que representa una cantidad de grados.

**Salida**
- La palabra cuadrante (en minúsculas) seguida del número de cuadrante correspondiente (por ejemplo: `cuadrante 2`), o bien alguna de las palabras `eje` o `excede`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Introduce los grados: -10
excede

Introduce los grados: 90
eje

Introduce los grados: 45
cuadrante 1

Introduce los grados: 215
cuadrante 3
```
**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.