import random as rd
import numpy as np

premioAlmacenado = np.array([0]*9)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    for i in range(0, len(premioAlmacenado)):
        premio = rd.randint(1000, 2000)
        premioAlmacenado[i] = premio
    
    print("Los numeros almacenados en el arreglo son: ")
    
    for i in range(0, len(premioAlmacenado)):
        print(premioAlmacenado[i], end=" ")
    print()
    
    #Buscar el mayor numero indicando su posición
    
    mayor = premioAlmacenado[0]
    posicion = 0
    
    for i in range(0, len(premioAlmacenado)):
        if menor > premioAlmacenado[i]:
            menor = premioAlmacenado[i]
            posicion = i
    
    print(f"\nElemento mayor: {mayor}\nPosicion: {posicion}")
    
    
main()