# CalculaGrado

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa en el cual definas la función calcula_grado(numero). Esta función debe recibir un número flotante entre 0 y 1, y debe regresar una nota alfabética de acuerdo a la siguiente tabla.
    Score               nota
    mayor a 0.9           A
    mayor a 0.8           B
    mayor a 0.7           C
    mayor a 0.6           D
    otro dentro del rango F

    Cualquier otro valor fuera del rango debe regresar "score incorrecto"

    ```
Entrada
Un número flotante entre 0 y 1.

Salida
La letra correspondiente al score asignado de acuerdo a la tabla de arriba.
Si la entrada no está dentro del rango de 0 a 1 (inclusive), la función debe regresar la leyenda "score incorrecto"
La función main( ) debe llamar a la función calcula_grado(valor) y debe desplegar el valor que retorna la función.

La salida del programa debe de ser exactamente de la siguiente forma:
```
Ingresa Un valor entre 0.0 y 1.0: 0.98
A                                                              
Ingresa Un valor entre 0.0 y 1.0: -5.1
score incorrecto
Ingresa Un valor entre 0.0 y 1.0: 0.8
C  
Ingresa Un valor entre 0.0 y 1.0: 0.65
D
Ingresa Un valor entre 0.0 y 1.0: 50
score incorrecto
```

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.