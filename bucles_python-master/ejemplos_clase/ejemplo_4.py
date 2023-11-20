# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con bucle for, listas y
# operador incremento (+=)

# Comenzar con una lista de edades
# Objetivo --> calcular el promedio de todas las edades
# utilizando un bucle y el operador incremento (+=)
edades = [35, 38, 55, 33]
suma_edades = 0
promedio = 0
cantidad_numero = len(edades)
# Profe:
# Utilizar un bucle for sobre la lista de edades
# acumule en la variable "suma_edades" (+=)
# la suma de todas las edades
for edad in edades:
    suma_edades += edad
    promedio = suma_edades / cantidad_numero

print(promedio)



# Utilizar la función len para determinar
# cuantos elementos hay en la lista edades


# Calcular el promedio de las edades:


# Imprimir en pantalla el promedio de edades

