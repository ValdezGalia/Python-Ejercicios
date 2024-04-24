def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    print("Indique la palabra o frase a repetir: ")
    palabra = input()
    print("Indique el numero de veces que desea imprimir: ")
    nv = int(input())
    
    count = 1
    while count < nv:
        print(palabra)
        count = count + 1
        
main()