#Leer 2 numeros y hacer las operaciones fundamentales de la matematica
numero1 = int(input("Introdusca el primer numero: "))
numero2 = int(input("Introdusca el segundo numero: "))
suma = numero1 + numero2
print("Suma :",suma)
resta = numero1 - numero2
print("Resta:",resta)
multiplicacion = numero1*numero2
print("Multiplicacion :",multiplicacion)
if (numero2 != 0):
    division = numero1 / numero2
    print("Division: ",round(division,2))
else:
    print("No se puede dividir entre cero.")