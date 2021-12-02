import math

numero1 = int(input("Dime el primer numero : "))
numero2 = int(input("Dime el segundo numero : "))
numero3 = int(input("Dime el tercer numero : "))
numero4 = int(input("Dime el cuarto numero : "))
numero5 = int(input("Dime el quinto numero : "))

lista =(numero1,numero2,numero3,numero4,numero5)
extremos = (numero1,numero5)
maxmin = (max(lista),min(lista))

print (lista)
print (extremos)
print (maxmin)