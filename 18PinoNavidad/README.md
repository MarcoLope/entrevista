# Pino de navidad
Ciclos - Dibuja un pino de navidad en la pantalla

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():    
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

El programa debe pedir un número entero **N** al usuario, que representa la altura
del pino.
A continuación el programa debe imprimir **N** lineas, cada una con un número
creciente de asteriscos, de manera que se dibuje un pino.

**Nota 1**: Cuida el número de espacios y asteriscos a imprimir,
especialmente los espacios a la izquierda de los asteriscos.
No debe haber espacios a la derecha del último asterisco de cada linea.

**Nota 2**: Para poder pasar las pruebas sin problemas, la mas sencillo es
construir el contenido de cada linea en un string, usando concatenación.
Una vez que tengas los espacios y asteriscos correctos en el string, puedes
imprimirlo.

## Entrada

Un número entero

## Salida

Varias lineas que contienen sólo espacios y asteriscos

Ejemplos:

```
Enter tree height: 0
```

```
Enter tree height: 3
  *
 * *
* * *
```

```
Enter tree height: 10
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *
 * * * * * * * * *
* * * * * * * * * *
```


**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.