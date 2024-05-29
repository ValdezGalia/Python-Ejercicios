import ram
import numpy as np

n = np.array([0]*9)

def main():
    for i in range(0, len(n)):
        print("Indique un valor entero: ")
        num = int(input())
        
        n[i] = num
    
    print("Los numeros almacenados en el arreglo son: ")
    
    for i in range(0, len(n)):
        print(n[i], end=" ")
main()