import numpy as np # Crear una matriz (array bidimensional) 
def main():
    print("UCAB Elaborado por: Orlando Valdez")
    # n = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    n = np.array([[0]*3, [0]*3, [0]*3])
    print("Los numeros de la matriz son: ")
    for i in range(len(n)):
        print("")
        for j in range(len(n)):
            print(n[i][j], end=" ")
main()