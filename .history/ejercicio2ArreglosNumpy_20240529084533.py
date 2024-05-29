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
    
    menor = premioAlmacenado[0]
    posicion = 0
    sumaPremio = 0
    
    for x in range(0, len(premioAlmacenado)):
        if menor > premioAlmacenado[x]:
            menor = premioAlmacenado[x]
            posicion = x
        
        if premioAlmacenado[x] >= 1800 and premioAlmacenado[i] <= 1900:
            sumaPremio += premioAlmacenado[i]
    
    print(f"\nPremio menor: {menor}\nPosicion del premio menor: {posicion}\nPremio Sumado en (1800-1900): {sumaPremio}")
    
    
main()