import filecmp

# Directorios a comparar
dir1 = "clase3copia"
dir2 = "clase3copiasinpatent"

# Ficheros comunes dentro de los directorios a comparar
comunes = ["Ejemplo_break.py","ejemplo_for.py","ejemplo_funcion_arg.py"]

# Comparar los metadatos de los ficheros comunes
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, comunes)

print("Verifica los metadatos:")
print("Coinciden:", match)
print("NO coinciden:", mismatch)
print("Errores:", errors, "\n")

# compara también los datos dentro de los ficheros
match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, comunes, shallow=False)
print("Deep comparison:")
print("Coinciden:", match)
print("NO coinciden:", mismatch)
print("Errores :", errors)

