def filtrar_palabras_con_a(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Filtrar las palabras que contienen la letra 'A'
    palabras_con_a = [palabra for palabra in palabras if 'A' in palabra.upper()]

    # Unir las palabras filtradas en una nueva cadena
    nueva_cadena = ' '.join(palabras_con_a)

    return nueva_cadena

# Ejemplo de uso
cadena_original = input("Ingrese un texto que termine en punto y final: ")
cadena_filtrada = filtrar_palabras_con_a(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena filtrada:", cadena_filtrada)