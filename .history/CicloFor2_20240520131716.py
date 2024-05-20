#  Dado una cadena de caracteres C1 terminada en punto, la cual contiene palabras separadas
# por un solo espacio en blanco ,se desea generar a partir de esta otra cadena C2 la cual contenga
# las mismas palabras que C1 pero cada palabra Invertida.

def main():
    print("Ingrese un texto que termine en punto y final( . ): ")
    cadena = input()
    cadena2 = cadena
    
    print(f"Cadena Ingresada: {cadena}")
    for recorrido in range(len(cadena) - 1, -1, -1):
        if ( cadena2 != " ") or (cadena2 != "."): 
            print(f"Cadena Invertida: {cadena2[recorrido]}", end=" ")

main()