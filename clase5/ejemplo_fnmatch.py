import fnmatch
import os
# Busca todos los ficheros con el patrón especificado
patron = 'ejemplo*.py'
print('Patrón :', patron)
print('*****')
ficheros = os.listdir('./clase4')
for nombre in ficheros:
    print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre, patron)))