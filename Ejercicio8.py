numeros_analziar = 0
sumador = 0


numeros_analziar = int(input("Ingrese cuantos numeros desea analizar: "))

for i in range (numeros_analziar):
    numero = int(input("Ingrese un numero entero"))
    
    sumador += numero
    
    




print("La suma de los numeros es: " + str(sumador))