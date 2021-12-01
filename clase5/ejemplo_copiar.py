import os
import shutil

# # Copiar ficheros situados en el mismo directorio
# shutil.copy(src="quijote-ext03.txt", dst="quijote-ext01.txt")

# # Copiar ficheros preservando los metadatos
# shutil.copy2(src="quijote-ext03.txt", dst="quijote-ext02.txt")

# #Copiar al igual que el comando cp -R en GNU/Linux
# shutil.copytree(src="clase3/", dst="clase3copia/")

# # Ignorar ficheros .jpg al copiar
# shutil.copytree(src="clase3/", dst="clase3copiasinpatent/", ignore= shutil.ignore_patterns('*funcion*'))

# # Mover (o cambiar de nombre al fichero) al igual que el comando mv en GNU/Linux
# shutil.move(src="clase5/quijote-ext01.txt", dst="clase3copia/quijote-ext01.txt")

# # Mover o renombrar un fichero usando la biblioteca os
# os.rename("clase3copia/quijote-ext01.txt", "clase3copia/quijote-ext01b.txt")

# Borrar un fichero
os.remove("clase3copia/quijote-ext01b.txt")
