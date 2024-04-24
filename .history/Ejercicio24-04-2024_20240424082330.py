def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    print("Indique un numero entero positivo correspondiente a la produccion de canillas diarias: ")
    canillas = int(input())
    
    saco = ( canillas // 25 )
    empaque = (( canillas % 25 ) // 10 )
    bolsasPapel = ( (( canillas % 25 ) % 10 ) // 5)
    
    bolsasPlasticas = (((( canillas % 25 ) % 10 ) % 5 ) // 3 )
    canillasSobrantes = (((( canillas % 25 ) % 10 ) % 5 ) % 3 )
    
    costoSaco = ( saco * 76 )
    costoEmpaque = ( empaque * 50 )
    costoBolsasPapel = ( bolsasPapel * 15 )
    costoBolsasPlasticas = ( bolsasPlasticas * 3 )
    
    total = ( costoSaco + costoEmpaque + costoBolsasPapel + costoBolsasPlasticas )
    
    print()
    print("-----------------------------------------------------")
    print(f"La produccion de canillas diarias es: \t\t{canillas}")
    print(f"La cantidad de sacos necesarios es: \t\t{saco}")
    print(f"La cantidad de empaque necesarios es: \t\t{empaque}")
    print(f"La cantidad de bolsas de papel necesarios es: {bolsasPapel}")
    print(f"La cantidad de bolsas plasticas necesarios es: \t{bolsasPlasticas}")
    print("-----------------------------------------------------")
    print(f"El costo de los sacos es: \t{costoSaco}")
    print(f"El costo de los empaques es: \t{costoEmpaque}")
    print(f"El costo de las bolsas de papel es: \t{costoBolsasPapel}")
    print(f"El costo de las bolsas plasticas es: \t{costoBolsasPlasticas}")
    print("-----------------------------------------------------")
    print(f"El costo total es: \t{total}")
    print("-----------------------------------------------------")
    print(f"Las canillas sobrantes son: \t{canillasSobrantes}")
    
    
main()