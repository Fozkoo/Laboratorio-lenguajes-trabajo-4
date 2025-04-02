""""
Escribir un programa que solicite el ingreso de un número entero y, si el
número leído es par, imprima la leyenda 'El número es PAR'. En caso
contrario, deberá
mostrar el texto 'El número es IMPAR'.

"""


esValido = True
while esValido:
    try:
        valor_one = int(input("Ingrese un numero(entero): "))
        esValido = False
    except ValueError:
        print("Error: Debes ingresar un número entero")
        
if ((valor_one % 2) == 0):
    print("El numero: ", valor_one, "es PAR")
else:
    print("El numero: ", valor_one, "es IMPAR")
