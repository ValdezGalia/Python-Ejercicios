def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    print("Indique una hora en formato militar (1-24): ")
    hora = int(input())
    
    if ( hora < 1 ) and ( hora > 25 ):
        print(f"ERROR, la hora suministrada es: {hora}")
        print("La misma ")
    
    
main()