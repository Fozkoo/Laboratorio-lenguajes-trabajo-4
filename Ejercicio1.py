"""
Escribir un programa que solicite el ingreso de dos números enteros y que
imprima el resultado de la suma, resta, multiplicación, cociente y resto de la
división.

"""
#Se utiliza el while para permitir al usuario repetir la operacion hasta que decida salir
while True:
    #Solicitar al usuario que ingrese 2 numeros
    num1 = int (input("Ingrese un numero: "))
    num2 = int (input("Ingrese otro numero: "))

    #Se realizan las operaciones basicas
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    # Se muestran los resultados en pantalla
    print(f"La suma de los dos numeros es:  {suma}")
    print(f"La resta de los dos numeros es:  {resta}")
    print(f"La multiplicacion de los dos numeros es:  {multiplicacion}")

    #Se verifica que el divisor no sea 0 antes de realizar la division
    if num2 != 0:
        division = num1 / num2
        resto = num1 % num2
        print(f"La division de los dos numeros es:  {division}")
        print(f"El resto de la division es:  {resto}")
    else:
        print("No se puede realizar la division y calcular el resto ya que no se puede dividir por cero")

    continuar = input("¿Desea ingresar otros numeros? (s/n): ").lower() #La funcion lower() convierte una cadena de texto en minuscula
        
    if continuar != "s":
        print("¡Fin!")
        break