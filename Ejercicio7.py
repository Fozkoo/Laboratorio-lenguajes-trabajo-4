numero = int(input("Ingrese un numero entero"))

print("El numero ingresado es " + str(numero))

if numero % 2 == 0:
    print("El numero es par")
    
    for i in range(numero, numero * 2):
        if i % 2 == 0:
            print(i)

else:
    print("El numero es impar")
    for i in range(numero, numero * 2):
        if i % 2 != 0:
            print(i)