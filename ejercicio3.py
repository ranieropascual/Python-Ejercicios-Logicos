print("-----------------------------")
print("ejercicio3 puntaje final")
print("-----------------------------")

#entradas
print("ingrese el numero de respuestas correctas")
RC=int(input())
print("ingrese el numero de respuestas incorrectas")
RI=int(input())
print("ingrese el numero de respuestas en blanco")
RB=int(input())

#proceso
PCR=RC*3
PRI=RI*-1
PRB=RB*0

PF=PCR+PRI+PRB

#salida
print("el puntaje total es: ",PF)


