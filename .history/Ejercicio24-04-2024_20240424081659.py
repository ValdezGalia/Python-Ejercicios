def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    print("Indique un numero entero positivo correspondiente a la produccion de canillas diarias: ")
    canillas = int(input())
    
    saco = ( canillas // 25 )
    resto1 = ( canillas % 25 )
    
    empaque = ( resto1 // 10 )
    resto2 = ( resto1 % 10 )
    
    bolsasPapel = ( resto2 // 5)
    resto3 = ( resto2 % 5 )
    
    bolsasPlasticas = ( resto3 // 3 )
    canillasSobrantes = ( resto3 % 3 )
    
    costoSaco = ( saco * 76 )
    costoEmpaque = ( empaque * 50 )
    costoBolsasPapel = ( bolsasPapel * 15 )
    costoBolsasPlasticas = ( bolsasPlasticas * 3 )
    
    total = ( costoSaco + costoEmpaque + costoBolsasPapel + costoBolsasPlasticas )
    
    print()
    print("-----------------------------------------------------")
    print(f"La produccion de canillas diarias es: {canillas}")
    print(f"La cantidad de sacos necesarios es: {saco}")
    print(f"La cantidad de empaque necesarios es: {empaque}")
    print(f"La cantidad de bolsas de papel necesarios es: {bolsasPapel}")
    print(f"La cantidad de bolsas plasticas necesarios es: {bolsasPlasticas}")
    print("-----------------------------------------------------")
    print(f"El costo de los sacos es: {costoSaco}")
    print(f"El costo de los empaques es: {costoEmpaque}")
    print(f"El costo de las bolsas de papel es: {costoBolsasPapel}")
    print(f"El costo de las bolsas plasticas es: {costoBolsasPlasticas}")
    print("-----------------------------------------------------")
    print(f"El costo total es: {total}")
    print("-----------------------------------------------------")
    print(f"Las canillas sobrantes son: {canillasSobrantes}")
    
    
main()