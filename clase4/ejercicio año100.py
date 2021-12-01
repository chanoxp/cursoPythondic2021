import datetime
import math

def preguntar_nombre():
    nombre = input("Cuál es tu nombre? ")
    print("Hola", nombre)
    return

def preguntar_edad():
    
    def suma100(edad):
        diferencia = 100 - edad
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return int(year)+diferencia

    edad = int(input("Cuál es tu edad? "))
    print("tendras 100 años en el año", str(suma100(edad)))


#preguntar_nombre()
preguntar_edad()
