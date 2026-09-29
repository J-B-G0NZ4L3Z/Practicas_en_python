"""
Las listas nos permiten almacenar informacion en un 
lugar, la cantidad que se desee: ya sean pocos 
elementos o millones de elemntos.

Una lista es una coleccion de items (elemntos) que
tienen un orden particular. Se pueden creae listas que 
incluyan strings, enteros, floats, los nombres de 
las personas de tu familia, etcetera, podemos almacenar 
(los tipos de datos permitidos en python) 


"""

bicycles = ['trek', 'cannondal', 'redline', 'specialized', 'giant']

#¿Como podemos acceder a los elemntos de una lista?

print(bicycles[0], bicycles[1], bicycles[2])
print(bicycles[0].upper())

print(bicycles[-1])#con el -1 se pone el ultimo elemento de la lista 

message = f"My first bicycle was a {bicycles}"