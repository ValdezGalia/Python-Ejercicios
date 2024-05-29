import random as rd
import numpy as np

arre = np.array([0]*20)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    print("Numero ordenado: ")
    for i in range(len(arre)):
        arre[i] = rd.randint(0, 20)
        
        print(arre[i], )
        for j in range(len(arre)):
            if arre[i] > arre[j]:
                aux = arre[i]
                arre[j] = aux
                
    
                print(arre[i], end=" ")
            
        
    
    
    
    
    
    
    
    
main()