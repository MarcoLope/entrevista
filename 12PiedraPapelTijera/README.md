# Minijuego Piedra, Papel o Tijera
**Decisiones - Simule el juego de piedra, papel o tijera**

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

Escriba un programa que simule el juego <a href="https://es.wikipedia.org/wiki/Piedra,_papel_o_tijera">Piedra, papel, tijera</a> para dos jugadores (Ana y Juan).

Las reglas del juego son las siguientes:
- Simultáneamente, los dos jugadores muestran una mano en tres posibles posiciones:
- Piedra: se muestra el puño cerrado y se representa con un caracter `a`.
- Papel: se muestra la palma de la mano y se representa con un caracter `p`.
- Tijera: se muestra la palma de la mano con los dedos separados en dos grupos y se representa con un caracter `t`.
- El jugador que ha sacado Piedra gana al jugador que ha sacado Tijera.
- El jugador que ha sacado Tijera gana al jugador que ha sacado Papel.
- El jugador que ha sacado Papel gana al jugador que ha sacado Piedra.
- Caso de empate cuando dos jugadores elijan el mismo elemento.

**Entradas**
- Dos caracteres (a, p o t), cada uno en un renglón y representan la tirada de Ana y Juan, en ese orden.

**Salida**
- Mensaje de quien es el ganador en el siguiente formato: `"Gana Ana"` o `"Gana Juan"` o `"Empate"`. 
- En el caso de que ingresen algún string de más de un caracter se debe desplegar el siguiente mensaje `"Las tiradas deben ser un caracter"`, si son de un sólo caracter pero alguna de ellas no corresponde a un caracter válido, el mensaje a desplegar es `"Tirada incorrecta"`.

Estos son algunos ejemplos de ejecución del programa. La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Tirada de Ana: a
Tirada de Juan: p
Gana Juan

Tirada de Ana: t
Tirada de Juan: p
Gana Ana

Tirada de Ana: a
Tirada de Juan: a
Empate

Tirada de Ana: piedra
Tirada de Juan: a
Las tiradas deben ser un caracter

Tirada de Ana: p
Tirada de Juan: r
Tirada incorrecta
```
**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.