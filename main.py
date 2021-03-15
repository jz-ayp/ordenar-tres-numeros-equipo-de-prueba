#25/02/2021
#Multiplos de 10
#Este programa ordena los numeros de mayor a menor y determina si algun numero es multiplo de 10
#Equipo 1: Bruno Mauricio, Maite Manzanares, Juan Pablo Rubio

#Entradas
num1 = int(input("Escriba el primer numero"))
num2 = int(input("Escriba el segundo numero"))
num3 = int(input("Escriba el tercer numero"))

#Procesos

if (num1>=num2 and num1>=num3):
 primero = num1
elif(num2>=num1 and num2>=num3):
 primero = num2
elif(num3>=num1 and num3>=num2):
 primero = num3

if (num1>=num2 and num1<=num3):
 segundo = num1
elif(num2>=num1 and num2<=num3):
 segundo = num2
elif(num3>=num1 and num3<=num2):
 segundo = num3

if (num1<=num2 and num1<=num3):
 tercero = num1
elif(num2<=num1 and num2<=num3):
 tercero = num2
elif(num3<=num1 and num3<=num2):
 tercero = num3

#Salida
# ¿Qué tienen que ver los múltiplos de 10?
print(primero, segundo, tercero)
