import random as rd
import numpy as np

premioAlmacenado = np.array([0]*9)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    for i in range(0, len(n)):
        premio = rd.randint(1000, 2000)
        n[i] = premio
    
    print("Los numeros almacenados en el arreglo son: ")
    
    for i in range(0, len(n)):
        print(n[i], end=" ")
    print()
    
    #Buscar el mayor numero indicando su posición
    
    mayor = n[0]
    posicion = 0
    
    for i in range(0, len(n)):
        if mayor < n[i]:
            mayor = n[i]
            posicion = i
    
    print(f"\nElemento mayor: {mayor}\nPosicion: {posicion}")
    
    
main()