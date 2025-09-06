# Factorial de un número
Ciclos - Factorial de un número

Escribe un programa que calcule el factorial de un número N, donde N es solicitado al usuario.  
El factorial de un número es:  

Si N=0 o N=1, el factorial es 1  
Si N es cualquier número positivo se calcula como  
 N! = 1 * 2 * 3 * ... * N.  

Por ejemplo factorial de 4 es 1 * 2 * 3 * 4 = 24

Si el usuario ingresa un valor negativo se debe mostrar el siguiente mensaje:  
"Factorial no definido para negativos"


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

La salida del programa debe de ser solamente el resultado, sin leyendas ni mensajes, debe ser de la siguiente forma:

```
Escribe un numero entero no negativo para calcular su factorial: 4
24
```

```
Escribe un numero entero no negativo para calcular su factorial: -2
Factorial no definido para negativos
```

```
Escribe un numero entero no negativo para calcular su factorial: 3
6
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.