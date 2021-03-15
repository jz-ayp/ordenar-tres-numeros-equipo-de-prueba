#Entrada
num1= int(input("Introduzca el un número: "))
num2= int(input("Introduzca un segundo número: "))
num3= int(input("Introduzca un tercer número: "))
#operación

#primero
if (num1>=num2 and num1>=num3):
 primero = num1
elif(num2>=num1 and num2>=num3):
 primero = num2
elif(num3>=num1 and num3>=num2):
 primero = num3

#segundo
if (num1>=num2 and num1<=num3):
 segundo = num1
elif(num2>=num1 and num2<=num3):
 segundo = num2
elif(num3>=num1 and num3<=num2):
 segundo = num3

#último
if (num1<=num2 and num1<=num3):
 ultimo = num1
elif(num2<=num1 and num2<=num3):
 ultimo = num2
elif(num3<=num1 and num3<=num2):
 ultimo = num3
 
#salida
print(primero, segundo, ultimo)
