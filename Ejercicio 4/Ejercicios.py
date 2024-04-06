#Ejercicio 1
import matplotlib as plt
from matplotlib import pyplot as plt
a=[1,2,3]
plt.plot(a)

#Ejercicio 2
import matplotlib as plt
from matplotlib import pyplot as plt
a=[1,2,3]
b=[3,4,5]
plt.plot(a,b)

#Ejercicio 3
import matplotlib as plt
from matplotlib import pyplot as plt
a=[1,2,3]
b=[3,4,5]
plt.plot(a,b)
plt.axis([0,10,0,15])

#Ejercicio 4
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g')
plt.axis([0, 6, 0, 20])

#Ejercicio 5
import matplotlib as plt
from matplotlib import pyplot as plt

with open("Numero_exam.txt") as fichero: #Abrimos archivo  de texto
    for linea in fichero:
        #print(linea)
        van=int(linea)
        van_1=van%3
        print(van_1)
plt.plot([0,15], [5,100], 'g')



