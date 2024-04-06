#Ejercicio1
def mensaje():
    print("El número es correcto")
    
a=True
while (a):
        numero=int(input("Introduce un número del 1 al 10: "))
        if(numero<5):
            mensaje()
            a=False
        elif(numero<10):
            mensaje()
            a=False


#Ejercicio2
def mensaje(argumento):
    print(argumento)
    
a=True
while (a):
    numero=int(input("Introduce un número del 1 al 10"))
    if(numero<5):
        mensaje("Correcto. El número es menor de 5")
        a=False
    elif(numero<=10):
        mensaje("Correcto. El número está entre 5 y 10")
        a=False
    else:
        print("Incorrecto. Vuelve a intentarlo")


#Ejercicio3
def add(a,b):
    print("La suma es: " , a+b)
def mult(a,b):
    print("La multiplicación es: " , a*b)
a=True
while (a):
    numero1=int(input("Introduce un número del 1 al 10: "))
    numero2=int(input("Introduce un número del 1 al 10: "))
    if(numero1<10 and numero2<10):
        add(numero1, numero2)
        mult(numero1, numero2)
        a=False
    else:
        print("Incorrecto. Vuelve a intentarlo")



#Ejercicio4
def lista(comida):
    for x in comida:
        print(x)
frutas = ["manzana", "pera", "cereza"]
lista(frutas)

#Ejercicio5
def prod5(x):
    return 5 * x
print(prod5(3))
print(prod5(5))
print(prod5(9))



#Ejercicio de practica 1

def add(a,b):
    print("El area es: " , (b*a)/2)
a=True
while (a):
    numero1=int(input("Introduce un número del 1 al 10: "))
    numero2=int(input("Introduce un número del 1 al 10: "))
    if(numero1<10 and numero2<10):
        add(numero1, numero2)
        a=False
    else:
        print("Incorrecto. Vuelve a intentarlo")


#Ejercicio de practica 2
def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

numbers = [1, 2, 3, 4, 5]
even_numbers, odd_numbers = separate_even_odd(numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#Ejercicio6
def is_multiple(a, b):
    if b % a == 0 or a % b == 0:
        return True
    else:
        return False
    
print(is_multiple(4, 2)) # True
print(is_multiple(7, 3)) # False

#Ejercicio7
def login():
    print("Verdadero, correcto")

while(a<5):
    numero=int(input("Introduce contraseña: "))
    if(numero == 12345678):
        login()
        a=a+1
    else:
        print("Falso, intentalo de nuevo")
        a=a+1