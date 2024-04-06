#Ejercicio 1
a=int(input("Introduce un número mayor que 10"))
if a>10:
    print("Correcto")

#Ejercicio 2
a=int(input(print("Introduce un número mayor que 10=")))
if a>10:
    print("El número")
    print(a)
    print("es mayor que 10")


#Ejercicio 4
a=int(input("Introduce un número mayor que 10"))
if a>10:
    print("El número introducido es mayor que 10")
else:
    print("El número introducido no es mayor que 10")


#Ejercicio 5
a=int(input("Introduce un número mayor que 10"))
if a>10:
    print("El número introducido")
    print("es mayor que 10")
else:
    print("El número introducido")
    print("no es mayor que 10")
print("Gracias por tu colaboración")



#Ejercicio 6
a=int(input("Introduce un número mayor que 10 = "))
if a>10:
    print("Correcto")
elif a==10:
    print("Incorrecto, el número es igual a 10")
else:
    print("Incorrecto, el número es menor que 10")


#While
#Ejercicio 1
a=int(input("introduce un número positivo: "))
while(a<0):
    a=int(input("Ha escrito un número negativo. Introduzca un número positivo: "))
    print("Gracias por su colaboración")



    #Ejercicio 2
a=int(input("introduce un número menor de 10: "))
while(a>0):
    print(a)
    a-=1
print("Gracias por su colaboración")



#Ejercicio 3
a=int(input("introduce un número menor de 10: "))
while(a>0):
    if(a==3):
        break
    print(a)
    a-=1

    #Ejercicio 4
a=int(input("introduce un número menor de 10: "))
while(a>0):
    if(a==3):
        a-=1
        continue
    print(a)
    a-=1


#For
#Ejercicio 1
for x in "banana":
    print(x)

    #Ejercicio 2
students = ["Anne", "Mike", "John"]
for x in students:
    print(x)

    #Ejercicio 3
for i in range(10):
    print(i)

    #Ejercicio 4
for x in range (0,3):
    print(x)


#Ejercicio 5
for x in range (5,11):
    print(x)


#Ejercicio 6
for x in range(2, 30, 3):
    print(x)




while 1:
    a=input("Numero")
    if a=="*":
        break
    a=int(a)
    if a>1:
        for i in range(2,a):
            if(a%i) == 0:
                print(f"{a} isn't prime")
                break
        else:
            print(f"{a} is prime")
            
    else:
        print(f"{a} isn't prime")   
        


a=input("Contraseña = ")

while a:
    
    if a =="pizza":
        print("Congrats")
        break
    else:
        
        print("vuelve a intentarlo")
        a=input("Contraseña = ")

