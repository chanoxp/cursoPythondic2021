import re

# encontrar coincidencias

texto = "Hoy es un dia magnifico y maravilloso"

exp_reg = re.search("^Hoy.*oso$",texto)
print("exp_reg = ",exp_reg)

exp_reg2 = re.findall("ma", texto)
exp_reg2b = re.search("ma",texto)
print("exp_reg2 = ",exp_reg2)
print("exp_reg2b = ",exp_reg2b)

exp_reg3 = re.sub("\s","    ",texto)
print("exp_reg3 = ",exp_reg3)

