numeros_analziar = 0
sumador_par= 0
sumador_impar = 0
 
 
numeros_analziar = int(input("Ingrese cuantos numeros desea analizar: "))
 
for i in range (numeros_analziar):
     numero = int(input("Ingrese un numero entero: "))
     
     if numero > 0:
         if numero % 2 == 0:
            sumador_par += numero
         else:
            sumador_impar += numero
    
     
 
 
 
 
print("La suma de los numeros PARES es: " + str(sumador_par))
print("La suma de los numeros IMPARES es: " + str(sumador_impar))