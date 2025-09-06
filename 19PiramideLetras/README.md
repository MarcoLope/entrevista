# Pirámide de letras
Ciclos - Dibuja una pirámide con las letras del alfabeto

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():    
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

El programa debe pedir un número entero **N** al usuario, que representa
la altura de la pirámide. El número debe ser entre 1 y 26
A continuación el programa debe imprimir **N** lineas, cada una con un número
creciente de letras mayusculas. Iniciando siempre con la __A__ y avanzando
hasta donde permita el ancho de cada nivel.

**Nota 1**: Utiliza ciclos **for** para simplificar el código

**Nota 2**: Cuida el número de espacios y letras a imprimir,
especialmente los espacios a la izquierda de las letras.
No debe haber espacios a la derecha de la última letra de cada linea.

**Nota 3**: Para poder pasar las pruebas sin problemas, la mas sencillo es
construir el contenido de cada linea en un string, usando concatenación.
Una vez que tengas los espacios y letras correctos en el string, puedes
imprimirlo.

## Entrada

Un número entero entre 1 y 26

## Salida

Si el número está fuera de rango, sólo imprimir el mensaje: `Out of range`.

De otra forma, imprimir varias lineas que contienen sólo espacios
y letras mayusculas, y que forman patrones como los mostrados a continuación.

Ejemplos:

```
Enter pyramid height: 0
Out of range
```

```
Enter pyramid height: 27
Out of range
```

```
Enter pyramid height: 3
    A
  A B A
A B C B A
```

```
Enter pyramid height: 5
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
```

```
Enter pyramid height: 20
                                      A
                                    A B A
                                  A B C B A
                                A B C D C B A
                              A B C D E D C B A
                            A B C D E F E D C B A
                          A B C D E F G F E D C B A
                        A B C D E F G H G F E D C B A
                      A B C D E F G H I H G F E D C B A
                    A B C D E F G H I J I H G F E D C B A
                  A B C D E F G H I J K J I H G F E D C B A
                A B C D E F G H I J K L K J I H G F E D C B A
              A B C D E F G H I J K L M L K J I H G F E D C B A
            A B C D E F G H I J K L M N M L K J I H G F E D C B A
          A B C D E F G H I J K L M N O N M L K J I H G F E D C B A
        A B C D E F G H I J K L M N O P O N M L K J I H G F E D C B A
      A B C D E F G H I J K L M N O P Q P O N M L K J I H G F E D C B A
    A B C D E F G H I J K L M N O P Q R Q P O N M L K J I H G F E D C B A
  A B C D E F G H I J K L M N O P Q R S R Q P O N M L K J I H G F E D C B A
A B C D E F G H I J K L M N O P Q R S T S R Q P O N M L K J I H G F E D C B A
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.
