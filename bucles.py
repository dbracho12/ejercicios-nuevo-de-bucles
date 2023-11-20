# 1 Ejercicio
''' Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.'''

for i in range(10):
    if i <= 10:
        print('Mamaguevo')

# Ejercicio 2
'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
 los años que ha cumplido(desde 1 hasta su edad).'''

edad = int(input('Ingrese su esdad: '))
for ano in range(edad):
    print( ano + 1, 'Años' )
    

# Ejercicio 3
''' Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todoslos números impares desde 1 hasta ese número separados por comas.'''
un_numero = int(input('Ingrese numero pasitivo: '))
impar = []
for numero in range(un_numero):
    if numero % 2 == 1:
        impar.append(numero)

print(impar)

