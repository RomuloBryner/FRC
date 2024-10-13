palabra = input("Ingresa una palabra: ").lower()
vocales = "aeiou"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print("La palabra tiene", contador, "vocales.")