# Área = ( PI * Radio 2)

area = 0
pi = 3.1416
diametro = 0
radio = 0


def main():
    print("================ Bienvenidos al calculo de un circulo ================")
    diametro = float(input("Ingrese el diametro a calcular: "))
    
    if diametro != 0:
        radio = diametro / 2
        area = ( pi * radio**2 )
        
        print(f"El area de la circunferencia es igual a: {round(area, 2)}")
    else:
        print("El diametro no puede ser igual 0")
        
main()