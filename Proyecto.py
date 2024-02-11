
texto = input("Ingrese el texto que desea analiasr: ")
letras = []

texto = texto.lower()

letras.append(input("Infrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("ingrese la seegunda letra: ").lower())

print("\n")
print("Cantidad de letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("Cantidad de palabras")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("Letras de inicio y de fin")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la ultima es '{letra_fin}'")

print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Texto al invertido es el siguiente: '{texto_invertido}'")

print("\n")
print("Buscando la palabra Python")
buscar_python = 'python' in texto
dic = {True: "Si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")

