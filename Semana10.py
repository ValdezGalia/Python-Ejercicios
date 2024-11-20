import random as rd
from colorama import *
from enum import Enum as en
import re
init(autoreset=True)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    c1 = "1000 Roky M, 2000 Fifi M, 1000 Lulu H, 1000 Roco M, 3000 Luna H"
    
    lista = c1.split(", ")
    costo = 0
    for perro in lista:
        if(re.findall("M$", perro)):
            datos = perro.split(" ")
            #                        [INICIO, FINAL, PASO]
            costoc =  datos[0] #perro[0:5:1]
            nombre = datos[1]
            genero = datos[2]
            print("------------------")
            print("Nombre: ", nombre)
            print("Genero: ", genero)
            print("------------------")
            costo += int(costoc)
    
    print(Fore.LIGHTMAGENTA_EX + "El costo de todos los perros masculinos:", costo)
    print    
    # print(lista)

main()