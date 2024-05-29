import random as rd
import numpy as np

arre = np.array([0]*5)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    for i in range(len(arre)):
        arre[i] = rd.randint(0, 5)
        
        print(arre[i], end=" ")
        
        for j in range(len(arre)):
            if arre[i] < arre[j]:
                aux = arre[i]
                arre[i] = 
                arre[j] = aux
            
        
    print()
    
    for i in range(len(arre)):
        print(arre[i], end=" ")
    
    
    
    
    
    
    
main()