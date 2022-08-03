from asyncore import read
from turtle import distance


print ('ingrese la velocidad y el tiempo de la unidad');
V = float(input('velocidad'));
T = float(input('tiempo'));

D = V*T;

print(D);
