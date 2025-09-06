# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    
    (
        ["Hola. Buenos días."],
        ["Dame un párrafo: ","Número de oraciones terminadas por un punto: 2"],
        " -->a) Cuenta cuántos puntos hay. Utiliza un ciclo para practicar."
    ),
    (
        ["""Por una mirada, un mundo,
por una sonrisa, un cielo,
por un beso… ¡yo no sé
qué te diera por un beso!"""],
        ["Dame un párrafo: ","Número de oraciones terminadas por un punto: 0"],
        " -->b) Cuenta cuántos puntos hay. Utiliza un ciclo para practicar."
    ),
    (
        ["""Amor empieza por desasosiego,
solicitud, ardores y desvelos;
crece con riesgos, lances y recelos;
susténtase de llantos y de ruego.

Doctrínanle tibiezas y despego,
conserva el ser entre engañosos velos,
hasta que con agravios o con celos
apaga con sus lágrimas su fuego.

Su principio, su medio y fin es éste:
¿pues por qué, Alcino, sientes el desvío
de Celia, que otro tiempo bien te quiso?

¿Qué razón hay de que dolor te cueste?
Pues no te engañó amor, Alcino mío,
sino que llegó el término preciso."""],
        ["Dame un párrafo: ","Número de oraciones terminadas por un punto: 3"],
        " -->v) Cuenta cuántos puntos hay. Utiliza un ciclo para practicar."
    )
]
