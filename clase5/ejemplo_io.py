import io
quijote = "../documentos/quijote_pg2000.txt"

""" fichero = open(quijote, 'r')
for linea in fichero:
    print(linea)
fichero.close()  """

""" # Lee los primeros 200 caracteres de un fichero
with open(quijote, 'r') as fichero:
    contenido = fichero.read(200)
    print(contenido) """

""" # Lee la primera línea de un fichero
with open(quijote, 'r') as file:
    contenido = file.readline()
    print(contenido) """

# Lee los párrafos de un fichero.
# Strip() evita una línea en blanco entre ellos.
with open(quijote, 'r') as file:
    contenidos = file.readlines(2000)
    for c in contenidos:
        print(c.strip())

        