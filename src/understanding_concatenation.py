# Concatenacion 
first_name = "benji"
last_name = "gonzalez"
full_name = first_name +  " " + last_name
print(full_name.title())

print("hola".upper(), first_name + " "+ last_name)

"""
white space se refiere a cualquier caracter que nos imprime,
es decir, un espacio, tabuladores (\t) y finales de linea (\n).

Los whitespaces se utilizan comunmente para organizar las salidas
de tal manera que sea mas amigable de leer o ver para los usuarios.


"""

print("python")
print("\t python")
print("\t\t python")

print("Lenguajes:\npython\n\n\tJavascrpits")
programming_languages = "Lenguajes:\npython\nC\n\tJavascrpits"

print(programming_languages)

# f-strings

famous_person = "jesus gonzalez"
message = f"{famous_person} una vez dijo: Python es amor"
print(message)

practice = "jesus", "benjamin", "gonzalez", "vallejo"

result = " ".join(practice)
print(result.title())

result_script = "-".join(practice)
print(result_script.upper())