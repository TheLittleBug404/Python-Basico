#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra
producto = float(input("Introdusca el precio del producto: "))
descuento = producto*(0.15)
print("Descuento del 15'%' sera de: ", round(descuento,2))
total = producto - descuento
print("Total a pagar: ",round(total,2))