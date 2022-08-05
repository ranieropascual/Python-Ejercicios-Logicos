print ('ingrese numero de respuestas correctas');
RC = int( input())
print ('ingrese numero de respuestas incorrectas');
RI = int( input())
print ('ingrese numero de respuestas en blanco');
RB = int( input())

# proceso
PCR = RC*3
PRI = RI*-1
PRB = RB*0

PF = PCR+PRI+PRB
print('elpuntaje total es:',PF)