"""
    Modificar el programa anterior para que ahora solicite el ingreso
    de dos números enteros, y que luego informe si el primero es o no
    mayor que el segundo, usando el formato 'X es mayor que Y' 
    (o ‘X no es mayor que Y’). Si ambos números fueran iguales, deberá
    informar 'X es igual a Y'. Por ejemplo, si se ingresan 23 y 42, se
    mostraría '42 es mayor que 23'.

"""


esValido = True

while esValido:
    try:
        valor_one = int(input("Ingrese el primer valor numérico: "))
        esValido = False
    except ValueError:
        print("Error: Debes ingresar un número entero")

esValido = True
while esValido:
    try:
        valor_two = int(input("Ingrese el segundo valor numérico: "))
        esValido = False
    except ValueError:
        print("Error: Debes ingresar un número entero. Inténtalo de nuevo.")


if (valor_one > valor_two):
    print("El numero ", valor_one, "es mayor que ", valor_two)
elif valor_two > valor_one:
    print("El numero ", valor_one, "no es mayor que ", valor_two)
else:
    print("El numero ", valor_one, "es igual a ", valor_two)
