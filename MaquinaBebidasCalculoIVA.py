import os
bebidas = [ 'Coca-Cola', 'Pepsi', '7up', 'Colita', 'Malta']
costoBebida = [ 5, 4, 3, 4, 6 ] # Valor referencial en dolares $
subtotal = 0
iva = 0
total = 0
cambio = 0
faltante = 0
ingresoDinero = 0

def CulminacionCompra (dineroIngresado, total):
    ciclo = True
    
    while ciclo:
        if dineroIngresado < total:
            faltante = dineroIngresado - total
            os.system('cls')
            print(f"\nAun no alcanza para comprar el producto le falta: {round(faltante, 2)}$")
            try:
                dineroIngresado += int(input("Ingrese más dinero: "))
            except ValueError:
                print("\nNo puede ingresar números decimales y No puede introducir caracteres!")

        elif dineroIngresado >= total:
            os.system('cls')
            cambio = dineroIngresado - total
            print(f"\nSu compra se ha realizado, exitosamente!\nSu Cambio es de: {round(cambio, 2)}$ \n\nGracias por su compra! Vuelva pronto :)")
            ciclo = False

def IngresoDineroUsuario( total,  finalisarCompra ):
    ciclo = True   
    
    if finalisarCompra != 1:
        print("Usted ha rechazado la compra!\n Vuelva pronto")
        return
    
    try:
        ingresoDinero = int(input("Ingrese dinero: "))
        
        while ciclo:
            if ingresoDinero < total:
                faltante = ingresoDinero - total
                print(f"\nAun no alcanza para comprar el producto le falta: {round(faltante, 2)}$")
                ingresoDinero += int(input("Ingrese más dinero: "))
            elif ingresoDinero >= total:
                os.system('cls')
                cambio = ingresoDinero - total
                print(f"\nSu compra se ha realizado, exitosamente!\nSu Cambio es de: {round(cambio, 2)}$ \n\nGracias por su compra! Vuelva pronto :)")
                ciclo = False
    except ValueError:
        print("\nNo puede ingresar números decimales y No puede introducir caracteres!")
        CulminacionCompra(ingresoDinero, total)       

def main():
    print("====================== Maquina espendedora ======================")
    print("Bebidas: \n1) Coca-Cola\n2) Pepsi\n3) 7up\n4) Colita\n5) Malta")
    eleccion = int(input("Ingrese el número de la bebida que desea: "))
    
    match eleccion:
        case 1:
            subtotal = costoBebida[ eleccion - 1 ]
            iva = subtotal * 16/100
            total = subtotal + iva
            os.system('cls')
            print(f"\nBebida seleccionada es: { bebidas[ eleccion - 1 ] }\nCosto de bebida: { subtotal }$\n-------------------")
            cambioBebida = int(input("Desea cambiar de bebida: \n1) Si\n2) No\n\nEscoga una opción: "))
            
            match cambioBebida:
                case 1:
                    os.system('cls')
                    main()
                case 2: 
                    os.system('cls')
                    print(f"\nSubtotal: \t{subtotal}$\nIVA 16%: \t{iva}$\n-------------------\nTotal: \t\t{total}$")
                    finalisarCompra = int(input("\nDesea finalizar su compra?\n1) Si\n2) No\n\nElija una opción: "))
                    
                    if finalisarCompra != 2:
                        IngresoDineroUsuario(total, finalisarCompra)
                        
                case _:
                    os.system('cls')
                    print("Opción elegida, no existe :(\n\n")
                    main()
        case 2:
            subtotal = costoBebida[1]
            iva = subtotal * 16/100
            total = subtotal + iva
            os.system('cls')
            print(f"\nBebida seleccionada es: { bebidas[1] }\nCosto de bebida: { subtotal }$\n-------------------")
            cambioBebida = int(input("Desea cambiar de bebida: \n1) Si\n2) No\n\nEscoga una opción: "))
            
            match cambioBebida:
                case 1:
                    os.system('cls')
                    main()
                case 2: 
                    os.system('cls')
                    print(f"\nSubtotal: \t{subtotal}$\nIVA 16%: \t{iva}$\n-------------------\nTotal: \t\t{total}$")
                    finalisarCompra = int(input("\nDesea finalizar su compra?\n1) Si\n2) No\n\nElija una opción: "))
                    
                    if finalisarCompra != 2:
                        IngresoDineroUsuario(total, finalisarCompra)
                        
                case _:
                    os.system('cls')
                    print("Opción elegida, no existe :(\n\n")
                    main() 
        case 3:
            subtotal = costoBebida[2]
            iva = subtotal * 16/100
            total = subtotal + iva
            os.system('cls')
            print(f"\nBebida seleccionada es: { bebidas[2] }\nCosto de bebida: { subtotal }$\n-------------------")
            cambioBebida = int(input("Desea cambiar de bebida: \n1) Si\n2) No\n\nEscoga una opción: "))
            
            match cambioBebida:
                case 1:
                    os.system('cls')
                    main()
                case 2: 
                    os.system('cls')
                    print(f"\nSubtotal: \t{subtotal}$\nIVA 16%: \t{iva}$\n-------------------\nTotal: \t\t{total}$")
                    finalisarCompra = int(input("\nDesea finalizar su compra?\n1) Si\n2) No\n\nElija una opción: "))
                    
                    if finalisarCompra != 2:
                        IngresoDineroUsuario(total, finalisarCompra)
                        
                case _:
                    os.system('cls')
                    print("Opción elegida, no existe :(\n\n")
                    main()                
        case 4:
            subtotal = costoBebida[-2]
            iva = subtotal * 16/100
            total = subtotal + iva
            os.system('cls')
            print(f"\nBebida seleccionada es: { bebidas[-2] }\nCosto de bebida: { subtotal }$\n-------------------")
            cambioBebida = int(input("Desea cambiar de bebida: \n1) Si\n2) No\n\nEscoga una opción: "))
            
            match cambioBebida:
                case 1:
                    os.system('cls')
                    main()
                case 2: 
                    os.system('cls')
                    print(f"\nSubtotal: \t{subtotal}$\nIVA 16%: \t{iva}$\n-------------------\nTotal: \t\t{total}$")
                    finalisarCompra = int(input("\nDesea finalizar su compra?\n1) Si\n2) No\n\nElija una opción: "))
                    
                    if finalisarCompra != 2:
                        IngresoDineroUsuario(total, finalisarCompra)
                        
                case _:
                    os.system('cls')
                    print("Opción elegida, no existe :(\n\n")
                    main()                    
        case 5:
            subtotal = costoBebida[-1]
            iva = subtotal * 16/100
            total = subtotal + iva
            os.system('cls')
            print(f"\nBebida seleccionada es: { bebidas[-1] }\nCosto de bebida: { subtotal }$\n-------------------")
            cambioBebida = int(input("Desea cambiar de bebida: \n1) Si\n2) No\n\nEscoga una opción: "))
            
            match cambioBebida:
                case 1:
                    os.system('cls')
                    main()
                case 2: 
                    os.system('cls')
                    print(f"\nSubtotal: \t{subtotal}$\nIVA 16%: \t{iva}$\n---------------------------\nTotal: \t\t{total}$")
                    finalisarCompra = int(input("\nDesea finalizar su compra?\n1) Si\n2) No\n\nElija una opción: "))
                    
                    if finalisarCompra != 2:
                        IngresoDineroUsuario(total, finalisarCompra)
                    else:
                        main()
                        
                    os.system('cls')
                    print("Su compra se ha cancelado, exitosamente! :)\n")
                        
                case _:
                    os.system('cls')
                    print("Opción elegida, no existe :(\n\n")
                    main()
        
        case _: 
            print("La Bebida seleccionada, no existe!")
            
main()