import os
prendas = [ 'Camisa', 'Zapatos', 'Sueteres', 'Gorras' ]
precioPrendas = [ 10, 40, 25, 15 ]
seleccionPrenda = 0
subtotal = 0
total = 0
iva = 0

def main():
    print("================ Bienvenidos a los ciegos ================")
    print(f"Productos:\n1) {prendas[0]}\n2) {prendas[1]}\n3) {prendas[-2]}\n4) {prendas[-1]}\n")
    seleccionPrenda = int(input("Ingrese la prenda que desea: "))
    
    match seleccionPrenda:
        case 1:
            print(f"Tipo Prenda: {prendas[ 0 ]}\nCosto: {precioPrendas[0]}$")
            seleccion = int(input("Desea culminar su compra\n1) Si\n2) No\n\nIngrese una opción: "))
            
            if seleccion == 2:
                os.system('cls')
                main()
            elif seleccion != 1 | seleccion != 2:
                print("La opcion ingresada, no es valida vuelva pronto!")
                return
            else:
                os.system('cls')
                subtotal = precioPrendas[ seleccionPrenda - 1 ]
                iva = subtotal * 16 /100
                total = (subtotal + iva)
                print(f"Tipo prenda: { prendas[ seleccionPrenda - 1 ] }\nPrecio: {subtotal}$\n--------------------\nSubtotal: {subtotal}$\nIVA: {iva}$\n--------------------\nTotal: \t{total}$")
                
        case 2:
            print(f"Tipo Prenda: {prendas[ 1 ]}\nCosto: {precioPrendas[1]}$")
            seleccion = int(input("Desea culminar su compra\n1) Si\n2) No\n\nIngrese una opción: "))
            
            if seleccion == 2:
                os.system('cls')
                main()
            elif seleccion != 1 | seleccion != 2:
                print("La opcion ingresada, no es valida vuelva pronto!")
                return
            else:
                os.system('cls')
                subtotal = precioPrendas[ seleccionPrenda - 1 ]
                iva = subtotal * 16 /100
                total = (subtotal + iva)
                print(f"Tipo prenda: { prendas[ seleccionPrenda - 1 ] }\nPrecio: {subtotal}$\n--------------------\nSubtotal: {subtotal}$\nIVA: {iva}$\n--------------------\nTotal: \t{total}$")
        
        case 3:
            print(f"Tipo Prenda: {prendas[ -2 ]}\nCosto: {precioPrendas[-2]}$")
            seleccion = int(input("Desea culminar su compra\n1) Si\n2) No\n\nIngrese una opción: "))
            
            if seleccion == 2:
                os.system('cls')
                main()
            elif seleccion != 1 | seleccion != 2:
                print("La opcion ingresada, no es valida vuelva pronto!")
                return
            else:
                os.system('cls')
                subtotal = precioPrendas[ -2 ]
                iva = subtotal * 16 /100
                total = (subtotal + iva)
                print(f"Tipo prenda: { prendas[ -2 ] }\nPrecio: {subtotal}$\n--------------------\nSubtotal: {subtotal}$\nIVA: {iva}$\n--------------------\nTotal: \t{total}$")
        
        case 4:
            print(f"Tipo Prenda: {prendas[ -1 ]}\nCosto: {precioPrendas[ -1 ]}$")
            seleccion = int(input("Desea culminar su compra\n1) Si\n2) No\n\nIngrese una opción: "))
            
            if seleccion == 2:
                os.system('cls')
                main()
            elif seleccion != 1 | seleccion != 2:
                print("La opcion ingresada, no es valida vuelva pronto!")
                return
            else:
                os.system('cls')
                subtotal = precioPrendas[-1]
                iva = subtotal * 16 /100
                total = (subtotal + iva)
                print(f"Tipo prenda: { prendas[ seleccionPrenda - 1 ] }\nPrecio: {subtotal}$\n--------------------\nSubtotal: {subtotal}$\nIVA: {iva}$\n--------------------\nTotal: \t{total}$")
                       
        case _:
            print("La opción ingresada, no es valida!")

main()