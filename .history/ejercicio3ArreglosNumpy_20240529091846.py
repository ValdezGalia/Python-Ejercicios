import random as rd
import numpy as np

arre = np.array([0]*5)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    print("Numero ordenado: ")
    for i in range(len(arre)):
        arre[i] = rd.randint(0, 5)
        
        print(arre[i], end=" ")
        print()
        
        for j in range(len(arre)):
            if arre[i] > arre[j]:
                arre[j] = arre[i]
                
            
        
    
    
    
    
    
    
    
    
main()