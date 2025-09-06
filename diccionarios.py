
'''
Un diccionario es una estructura de datos "ordenada"
intercambiable y no permite duplicidad. 
Un diccionario se maneja mediante una llave y un valor. 
''' 

#Ejemplo de un diccionario
persona = {'nombre':'Francisco', 'appPaterno':'Vázquez', 
                'materias':['Python', 'Java', 'Matemáticas discretas']}

#Como acceder a un campo 
print(persona['nombre'])
print(persona['materias'][0])

'''
Modificar el nombre y appPaterno del diccionario persona
Modificar el diccionario persona, agregar la llave edad y colocar un entero
'''
persona["nombre"]="Javier"
persona['appPaterno']="Gomez"
persona['color']='azul'
persona['edad']=46

print(persona)


def regresa_auto(marca,sub_marca,modelo,color):
    auto={"marca":marca, "sub_marca": sub_marca, "modelo": modelo, "color": color}
    return auto

c1= regresa_auto("FORD","FOCUS",2021,"Rojo")
c2= regresa_auto("Maza","Mazda 3",2022,"Blanco")

lista_autos= [c1,c2]
lista_autos.append(regresa_auto("VW","Jetta",2019,"Verde"))
# print(lista_autos)
# print(lista_autos[1]["modelo"])

# d1= {
#         "id":"c1","contenido":c1
#     }

# d2= {
#         "id":"c2","contenido":c2
#     }

# tupla = (d1,d2)
# print(tupla)
# print(tupla[1]["contenido"]["sub_marca"])

#Recorrido de un diccionario mediante las llaves del mismo 
for key in persona: 
    print(f'key = {key} => valor= {persona[key]}')

for auto in lista_autos:
    for llave in auto: 
        print(f"{auto[llave]}", end=' ')
    print() # Enter 

#Recorrido por tuplas
print('*'*50)
for llave, valor in persona.items():
    print(f'llave = {llave} => valor= {valor}')

print('*'*50)
print(persona.items())
#Método dict
per2 = dict(nombre='Francisco', appPaterno='Vazquez')
print(per2)

#Método zip 
print('*'*50)
l1 = ['A','B','C','D','E']
l2 = [12, 45, 23, 56, 344]
l3 = [12, 45, 23, 56, 344]
d3 = dict(zip(l1, l2))
print(d3)

print('*'*50)
l4 = 'ABCDE'
d4 = dict(zip(l4,l2))
print(d4)

'''
Verificar los métodos:
keys()
values()
get('key')
pop('key') # regresa el valor y lo elimina 
'''
print('*'*50)
print(d4.keys())
print(d4.values())
print(d4.get('B'))
print(d4.pop('B'))
d4['B']=46
print(d4)

#for k in d4.keys():
#    print(k)