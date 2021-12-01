import datetime

class FestivalMusical:
    def __init__(self,nombre , pais, estilo_musical):
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

    def festival_metodo(self):
        print('El Mejor festival es.')

    @classmethod
    def valor_ticket(cls, valor):
        cls.valor_ticket = valor

    @staticmethod
    def dia_evento(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return print ('Es en fin de semana')
        return print ('Es un dia laboral')


# se crea el objeto o instancia
festival1 = FestivalMusical('Creamfields','UK','Dance')
festival2 = FestivalMusical('Versiales','España','Regional')

# se crea el valor del ticket
FestivalMusical.valor_ticket(100)

# se accede al objeto
print(festival1.nombre)
print(festival1.pais)
print(festival1)

# se accede al objeto
festival1.festival_metodo()


# se accede a los atributos del objeto
print (festival1.nombre.upper())

festival1.nombre = ('Primavera sound')
print (festival1.nombre)

#elimina el objeto
#del festival1
print(festival1.valor_ticket)
print(FestivalMusical.valor_ticket)
print(festival2.valor_ticket)

dia1 = datetime.date(2021,11,30)

FestivalMusical.dia_evento(dia1)
