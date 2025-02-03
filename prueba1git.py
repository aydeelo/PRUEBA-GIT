nombreCliente = input("ingrese su nombre:  ")
print("hola, un gusto saludarte "  + nombreCliente)
print("haga su compra")
producto1 = int(input("ingrese el precio del primer producto: "))
producto2 = int(input("ingrese el precio del segundo producto: "))
producto3 = int(input("ingrese el precio del tercer producto: "))
print("sumando el total de su compra")
totalCompra = producto1 + producto2 + producto3


print("la suma de su compra es: ", totalCompra)

valorBillete = int(input("ingrese el valor del billete"))

resta = valorBillete - totalCompra
print("este es su cambio" , resta)
