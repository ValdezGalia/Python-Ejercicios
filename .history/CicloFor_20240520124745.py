def main():
    print("Ingrese un texto que termine en punto y final ( . ): ")
    cadena = input()
    cadena2 = ""
    
    for recorrido in range(0, len(cadena), 1):
        if cadena[recorrido] != " " and cadena[recorrido] != ".":
            if cadena[recorrido] == "a" or cadena[recorrido] == "A":
                cadena2 += ""
            elif cadena[recorrido] == "e" or cadena[recorrido] == "E":
                cadena2 += ""
            elif cadena[recorrido] == "i" or cadena[recorrido] == "I":
                cadena2 += ""
            elif cadena[recorrido] == "o" or cadena[recorrido] == "O":
                cadena2 += ""
            elif cadena[recorrido] == "u" or cadena[recorrido] == "U":
                cadena2 += ""
            else:
                cadena2 += cadena[recorrido]
                
        else:
            cadena2 += ""
    
    
main()