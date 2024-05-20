import os

tasaBCV = 36.26
tasaParalelo = 38.09
dolarBCV, dolarParalelo, dineroIngresado = 0, 0, 0

def main():
    print("========================== Bienvenidos a tasa de cambio ==========================")
    print(f"\nTasas por cada dolar:\n$ BCV: {tasaBCV}Bs\n$ Paralelo: {tasaParalelo}Bs\n-----------------------\n")
    dineroIngresado = int(input("Ingrese cantidad en dolares : $"))
    
    if dineroIngresado <= 0:
        print("No se puede realizar la operacion,\nporque el numero ingresado no es mayor a 0")
        return
    
    dolarBCV = dineroIngresado * tasaBCV
    dolarParalelo = dineroIngresado * tasaParalelo
    
    print(f"\nBCV: {round(dolarBCV, 2)}Bs\nParalelo: {round(dolarParalelo, 2)}Bs")
    
main()