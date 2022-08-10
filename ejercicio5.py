import math


print("------------------------------------------------------")
print("ejercicio5: numero de micro discos 3.5 necesarios")
print("------------------------------------------------------")

#entradas
print("ingrese GB: ")
GB=float(input())

#proceso
MG=GB*1024
MD=MG/1.44

#salida
print(MD)
#en caso de decimal aproximar al siguiente entero
#ya que la parte decimal debe ser almacenada en otro disco 3.5

print("el numero de discos necesarios es: ",math.ceil(MD))