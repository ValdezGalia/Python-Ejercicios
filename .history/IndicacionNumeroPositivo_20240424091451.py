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
            menor 