# Ejemplo clase
# Creando la clase
class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
    

# Herencia: extendiendo la clase
class Aptirudes(Empleado):
    # El método __init__() para crear una clase hija
    def __init__(self, nombre, puesto, lenguajes, so, idioma):
        super().__init__(nombre, puesto)
        self.lenguajes = lenguajes
        self.so = so
        self.idioma = idioma



    # Agregar un nuevo método a la clase
    def cargar(self):
        self.nivel_carga = 100
        print('El coche está cargado.')
    
    # Sobrescribir un método del padre
    def gasolina_completo(self):
        print('El coche no tiene depósito de gasolina!')

# Creando las instancias de la clase Coche
objeto_coche = Coche('SEAT','Ateca', '1.0')


# Acceder a los atributos de ese objeto
print(objeto_coche.marca)
print(objeto_coche.modelo)
print(objeto_coche.tipo)
# Llamando a los métodos de la clase

print()
objeto_coche.gasolina_completo()
objeto_coche.conducir()        


# Usar el método padre e hijo
coche_electrico = CocheElectrico('Tesla', 'Modelo 3', 'Berlina')

print(coche_electrico.modelo)
coche_electrico.cargar()
coche_electrico.conducir()
coche_electrico.gasolina_completo()


# Mostrar la o las clases de la cual se está heredando
print(CocheElectrico.__mro__)