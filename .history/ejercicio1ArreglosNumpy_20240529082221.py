import random as rd
import numpy as np

n = np.array([0]*9)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    for i in range(0, len(n)):
        # print("Indique un valor entero: ")
        # num = int(input())
        num = rd.randint(1, 20)
        n[i] = num
    
    print("Los numeros almacenados en el arreglo son: ")
    
    for i in range(0, len(n)):
        print(n[i], end=" ")
    print()
    
    #Buscar el mayor numero indicando su posición
    
    mayor = n[0]
    pos
    
    
main()