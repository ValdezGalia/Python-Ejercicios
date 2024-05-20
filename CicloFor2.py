def main():
    print("Ingrese un texto que termine en punto y final( . ): ")
    cadena = input()
    cadena2 = cadena
    cadenaInvertida = ""
    
    for recorrido in range(len(cadena) - 1, -1, -1):
        if ( cadena2[recorrido] != " ") or (cadena2[recorrido] != "."): 
            cadenaInvertida += cadena2[recorrido]
            
    print("Cadena Vieja: ", cadena2)
    print("Cadena Nueva: ", cadenaInvertida)


main()