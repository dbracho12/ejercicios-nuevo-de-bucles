# Ejercicio 4
'''Escribir un programa que pida al usuario un número entero positivo y
 muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''
#un_numero = int(input('Ingrese el numero entero: '))
#entero = []
#for numero   in range(un_numero + 1):
#    if numero  <= un_numero :
#        entero.append(numero)

#reverso = sorted(entero, reverse=True)

'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido.'''

#n_altura = int(input('numero entero: '))


#for i in range(n_altura + 1):
#    str(i)
#    altura = i* '*'
#    print(altura)

#Ejercicio 7
'''Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10'''
#n = int(input('Ingrese el numero de la table de multiplicar: '))

#for i in range(11):
#    multiplicar = n * i
#    print(multiplicar)

#Ejercicio 8
'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
 rectángulo como el de más abajo.'''
#n_altura = int(input('numero entero: '))


#for i in range(n_altura + 1):
#    if i % 3 == 0:
#        print(i)

# Ejercicio 9
'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

contracena = 'contraseña'
#contracena_separada = list(contracena)
#print(contracena_separada)

for i in range(len(contracena)):
    introducion_contrasena = input('Introducir contraseña: ')
    if contracena == introducion_contrasena:
        print('Contraseña correcta: ',contracena)
        break
    else:
        print('Contraseña Incorrecta')
        introducion_contrasena = input('Introducir contraseña: ')
