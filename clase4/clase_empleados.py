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


