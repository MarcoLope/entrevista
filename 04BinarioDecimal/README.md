# Convierte binario a decimal

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Diseña un programa que incluya la función binario_decimal que convierta números binarios (base 2)
en números decimales (base 10).
La función deberá recibir un string que contenga el número binario a convertir y
regresar un número entero equivalente en base 10.
Si el string recibido es de tamaño 0 o no está formada por sólo 1s y 0s se devuelve un -1.

Escribe después la función main que lea el string,
lo envíe a la función y luego muestre el valor de retorno de la función en la pantalla.

#### Entrada
Un string formado por 1s y 0s.

#### Salida
Un número entero que representa la conversión del binario al formato decimal.
Si el string recibido es de tamaño 0 o no está formada por sólo 1s y 0s se devuelve un -1.

#### NOTA IMPORTANTE:
Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente
con el formato y/o tipo de dato que se te pide como salida.

La salida del programa debe de ser exactamente de la siguiente forma:

```
1111111
127

Hola
 -1

0a
-1

1010
15

```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.