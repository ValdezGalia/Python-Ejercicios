def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    print("Indique una hora en formato militar (1-24): ")
    hora = int(input())
    
    if ( hora < 1 ) and ( hora > 25 ):
        print(f"ERROR, la hora suministrada es: {hora}")
        print("La misma debe estar en el rango del formato militar (1-24)")
    elif ( hora >= 6 ) and ( hora <= 17):
        turno = "Turno del dia"
    else:
        turno = "Turno de la noche"
    
    print(f"La hora en formato militar (1 - 24) ")
    
main()