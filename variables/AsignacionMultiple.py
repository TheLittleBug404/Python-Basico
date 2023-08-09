#En python podemos usar la asignacion multiple de variables como se vera a continuacion
nombre = "Ricardo"
apellido = "Jauregui"
edad = 32
#la asignacion multiple sera separado con una coma
nombre , apellido, edad = "Ricardo","Jauregui",32
#tambien podemos imprimir las variables 
print(nombre,apellido,edad)
#tambien podemos asignar a varias variables el mismo valor
var1 = var2 = var3 = "Todas estas variables son iguales"
print(var1,var2,var3)
#crearemos una lista
nombres = ["Pepito","Juana","JoseJOSE","Dora La exploradora","Marcelino Pan y vino"]
print(nombres)
#siqueremos asisgnar los nombres de la lista a variables diferentes lo hacemos como la asignacion multiple
nom1, nom2, nom3,nom4, nom5 = nombres
#la anterior linea es lo mismo que hacer
# nom1, nom2, nom3,nom4, nom5 = "Pepito","Juana","JoseJOSE","Dora La exploradora","Marcelino Pan y vino"
print(nom1,nom2,nom3,nom4,nom5)