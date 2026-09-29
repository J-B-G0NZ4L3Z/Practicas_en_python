# Numeros 

# Enteros- Integers
#Division entera//


"""
Los numeros enteros los podemos 
sumar(+), restar(-), multiplicar(*) 
y dividir(/).
"""
#Sumar
#Restar
#Multiplicar
#Dividir/
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1 + number_2)

#Potencias **n
print(3**2) #3^2
print(3**3) #3^3
print(10**6) #10^6
print(10%2) #Modulo (mod)
age = 17
print(age)
name = "Jesus Gonzalez"
print(name, age)
#Floats

"""
Python llama float a cualquier numero 
con punto decimal
"""
print()



# Imprimir la edad de alguien 
age = 34 #Variable del tipo int 
message = "Charly tiene" + str(age) + "años."
print(message)

#Type error 
"""
Typererror: Python no puede reconocer el tipo de informacion 
que se esta utilizando.

"""

message_f = f"Charly tiene {age} años."
print(message_f)

#Metodo build-in type()
print(type(age), type("hola"), type(0.54), type(True))