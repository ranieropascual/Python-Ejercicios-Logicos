print("---------------------------------------")
print("ejercicio4: puntaje total de partidos")
print("---------------------------------------")

#entrada
print("ingrese el total de partidos ganados")
PG=int(input())
print("ingrese el total de partidos perdidos")
PP=int(input())
print("ingrese el total de partidos empatados")
PE=int(input())

#proceso
PPG=PG*1
PPP=PP*-1
PPE=PE*0

PF=PPG+PPP+PPE

#salida
print ("---------------------------------------")
print("puntaje final: ",PF)   


