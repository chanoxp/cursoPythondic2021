# Ejemplo break
# Verifica si un número es primo
for n in range(1, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equivale a', x, '*', n//x)
            break
    else:
        #El bucle sigue sin encontrar un factor
        print(n, 'es un número primo')


# Ejemplo continue
for num in range(1, 10):
    if num % 2 == 0:
        print("Encontrado un número par", num)
        continue
        # Con break sale de la iteración al encontrar el primer número par
        
    print("Encontrado un número impar", num)    