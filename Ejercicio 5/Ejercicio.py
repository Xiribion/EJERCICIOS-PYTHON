#Ejercicio 1
import matplotlib as plt
from matplotlib import pyplot as plt
y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75]
with open ("Numero_exam.txt") as fichero:
    i=0
    for linea in fichero:
        a=int(linea)
        if (a%3==0):
            y[i]=a
        else:
            y[i]=0
        i=i+1
plt.plot(x,y,"green")
plt.axis([0,100,0,20])
plt.ylabel("age")
plt.xlabel("%height")