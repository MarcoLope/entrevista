# Lista de Precios

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

## Descripción del programa  

Escribe un programa que lea la clave del artículo que va a comprar (nota que es letra mayúscula) o X si ya no quiere comprar más artículos. El programa debe mostrar en la pantalla el precio correspondiente a cada artículo pedido, el programa debe repetirse mientras el usuario no teclee la clave X, cuando el usuario teclee la clave X el programa debe mostrar en la pantalla el total de la compra del cliente.

Clave | Precio
------|-------
  A   |  120
  B   |  250
  C   |  360

**Entrada**  
Una secuencia de letras que representan la clave del artículo que se va a comprar. Debe terminar con X que significa que ya se terminó de comprar.

**Salida**  
Para cada letra que se ingrese, se debe mostrar el precio del artículo correspondiente.
Después de que se teclee la letra X se debe mostrar el total de los artículos elegidos.

**Ejemplo de la ejecución del programa:**  
```
>>>B              
250               
>>>A                 
120               
>>>X                 
370 
```
**Nota:** El código `if __name__ == '__main__':` es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.