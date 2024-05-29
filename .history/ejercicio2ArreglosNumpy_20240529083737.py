import random as rd
import numpy as np

premioAlmacenado = np.array([0]*9)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    for i in range(0, len(premioAlmacenado)):
        premio = rd.randint(1, 10)
        premioAlmacenado[i] = premio
    
    print("Los numeros almacenados en el arreglo son: ")
    
    for i in range(0, len(premioAlmacenado)):
        print(premioAlmacenado[i], end=" ")
    print()
    
    #Buscar el mayor numero indicando su posición
    
    menor = premioAlmacenado[0]
    posicion = 0
    sumaPremio = 0
    
    for i in range(0, len(premioAlmacenado)):
        if menor > premioAlmacenado[i]:
            menor = premioAlmacenado[i]
            posicion = i
        
        if premioAlmacenado[i] > 4 and premioAlmacenado[i] < 10:
            sumaPremio += premioAlmacenado[i]
    
    print(f"\nPremio menor: {menor}\nPosicion del premio menor: {posicion}\nPremio Sumado en (1800-1900): {sumaPremio}")
    
    
main()