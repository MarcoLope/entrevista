# Pass Fail Grade
Decisiones - Calificacion aprobatoria o reprobatoria

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    # Escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

El programa va a preguntar por una calificación numerica, entre 0 y 100.
Añade el código necesario para que el programa imprima **Pass** si la
calificación es mayor o igual a 70, o que imprima **Fail** si la
calificación es menor a 70.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Enter grade: 90
Pass
```

Únicamente necesitas modificar la función **check_grade** y asegurarte de
que regrese la palabra correcta.

**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.