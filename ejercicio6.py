print("------------------------------------------------------")
print("ejercicio6: distancia entre dos puntos A y B, en 2D")
print("------------------------------------------------------")

#entradas
print("ingrese coordenadas del punto A")
AX=float(input("AX: "))
AY=float(input("AY: "))

print("ingrese coordenadas del punto B")
BX=float(input("BX: "))
BY=float(input("BY: "))

#proceso
D=((AX-BX)**2+(BX-BY)**2)**0.5

#salida
print("el resultado es: ",D)

