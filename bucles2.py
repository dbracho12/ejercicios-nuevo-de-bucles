'''# Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por 
pantalla si es un número primo o no.'''
#n = int(input('Ingrese un numero: '))
#for i  in range(2, n):
#    if n % i  != 0:
#        print(f'{n} es una numero primo')
        
#    else:
#        print(f'{n} es un numero compuesto')

'''Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una
 las letras de la palabra introducida empezando por la última.'''
palabra = input('Pedir una palabra: ')
separar_palabra = list(palabra)
print(separar_palabra)
palabra_invertida = ''.join(reversed(separar_palabra))
print('Palabra invertida: ')
for i in palabra_invertida:
   
   print(f'{i}')



    
        
