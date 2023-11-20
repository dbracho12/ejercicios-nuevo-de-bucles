# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con bucle for y listas

# Comenzar con una lista de invitados
# Objetivo --> buscar si una persona fue 
# invitada a la fiesta
invitados = ["Manuel", "Ana", "Juan", "Laura"]

persona = input("Ingrese nombre persona a buscar en la lista:\n")

# Profe:
# Utilizar un bucle for sobre la lista de invitados
# y busque a la persona en la lista
# 1 - Utilice "capitalize" sobre el nombre
#     de la persona ingresada por consola
# 2 - Si la persona se encuentra en la lista,
#     notificar por consola el hallazgo 



# NOTA:
# Más adelante veremos que con el operador
# "in" puede logrese lo mismo sin un bucle
for invitado in invitados:
    if  persona.capitalize() == invitado:
        print(f'{invitado} esta en la lista de invitado.')
    else:
        print('A esta persona hay que hecharla a patadas.')
