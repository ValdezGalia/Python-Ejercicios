def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    print("Indique primer numero entero positivo: ")
    numero1 = int(input())
    
    print("Indique el segundo numero entero positivo, distinto al anterior: ")
    numero2 = int(input())
    
    print("Indique el tercer numero entero positivo, distinto a los anteriores: ")
    numero3 = int(input())
    
    if ( numero1 > numero2 ) and ( numero1 > numero3 ):
        mayor = numero1
        
        if ( numero2 < numero3 ):
            menor = numero2
        else:
            menor = numero3
            
    elif ( numero2 > numero1 ) and ( numero2 > numero3 ):
        mayor = numero2
        if( numero1 < numero3 ):
            menor = numero1
        else:
            menor = numero3
    else:
        mayor = numero3
        
        if(numero1 < numero2):
            menor = numero1
        else:
            menor = numero2
            
print 