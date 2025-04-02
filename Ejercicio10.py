sumador_negativos = 0
sumador_positivos = 0
contador_positivos = 0
contador_ceros = 0

for i in range(8):

    numero = int(input("Ingrese un numero entre -10 y 10: "))
    while not(-10 <= numero <= 10): 
        print("El numero esta fuera de rango")
        numero = int(input("Ingrese un numero entre -10 y 10: "))

    if numero < 0:
        sumador_negativos += numero
    elif numero > 0:
        sumador_positivos += numero
        contador_positivos += 1
    else:
        contador_ceros += 1


print("La sumatoria de numeros negativos es: " + str(sumador_negativos))
print("La cantidad de 0 ingresados es de: " + str(contador_ceros))
print("El promedio de los nuemros positivos es: " + str(int(sumador_positivos / contador_positivos)))