from paquete import modulo1, modulo2


llamar_modulo1 = modulo1.Clase1('Clase1') # creamos una instancia
print (llamar_modulo1) # direccion objeto memoria
print(modulo1.Clase1.mostrar) # direccion de la clase
print(llamar_modulo1.mostrar())


llamar_modulo2 = modulo2.Clase2('Clase1') # creamos una instancia
print (llamar_modulo2) # direccion objeto memoria
print(modulo2.Clase2.mostrar) # direccion de la clase
print(llamar_modulo2.mostrar())