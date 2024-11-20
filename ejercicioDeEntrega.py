import random as rd
from colorama import *
from enum import Enum as en
import re
init(autoreset=True)

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    c1 = "23621137 Jose Perez A 75378 jperez@gmail.com, 30514220 Sebastian Figueira A 99999 sfigueira@gmail.com, 13637584 Joao Figueira J 100000 jfigueira@yahoo.com, 3651890 Luis Guzman J 83102 pp@hotmail.com, 11512121 Paul Fritz J 83642 op@yahoo.com, 29821634 Paola Carvajal A 23140 paoc@gmail.com"
    
    lista = c1.split(", ")
    costo = 0
    for personas in lista:
        if(re.findall("@gmail.com", personas) and re.findall(r'\b(2[3-9]|30)\b')):
            datos = personas.split("")
            cedula = datos[0]
            print(cedula)
    
main()