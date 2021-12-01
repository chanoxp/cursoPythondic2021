import io

quijoteEscribir = "../documentos/quijote_ext01.txt"

entrada = """Primera parte del ingenioso hidalgo don Quijote de la Mancha


"""

""" # Creamos un fichero y pegamos el texto de la variable entrada
with open(quijoteEscribir, 'x') as file:
    file.write(entrada) """

# En este caso vamos a agregar el texto de la variable “entrada_agregar” 
# al␣final del fichero:
# entrada_agregar = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme,"""

# Abrimos el fichero y adjuntamos el texto de la variable “entrada_agregar”
#with open(quijoteEscribir, 'a') as file:
#    file.write(entrada_agregar)"""


# Busca a partir del carácter 18 e imprime los 42 caracteres siguientes
with open(quijoteEscribir, 'r') as file:
    file.seek(18)
    contenido = file.read(42)
    print(contenido)

    