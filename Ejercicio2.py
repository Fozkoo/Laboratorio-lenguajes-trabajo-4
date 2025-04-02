"""
Escribir un programa que solicite el ingreso de un número entero e informe si el
valor leído es o no mayor que el número 10.

"""
# Solicitar al usuario que ingrese un numero
num = int (input("Ingrese un numero: "))

#Verificar si el numero ingresado es mayor o menor que 10
if num > 10:
    print(f"El numero {num} ingresado es mayor que 10")
elif num == 10:
    print(f"El numero {num} ingresado es igual a 10")
else:
    print(f"El numero {num} ingresado es menor que 10")

