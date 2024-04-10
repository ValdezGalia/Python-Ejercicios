import os
# Velocidad = Distancia en Kilómetros recorrida / Tiempo en Horas

velocidad, distanciaKm, tiempoHs = 0, 0, 0
hectometros, tiempoMinutos = 0, 0

def main():
    os.system('cls')
    print("\n=============== Calculo de velocidad de vehiculo ===============")
    print("Cada kilometro son 10 hectometros\n")
    hectometros = float(input("Hectometros recorridos: "))
    tiempoMinutos = int(input("Minutos que tardo en el recorrido: "))
    
    if hectometros <= 0 & tiempoMinutos <= 0:
        print("No se puede calcular la velocidad del vehiculo.\nha ingresado valores iguales o menores a 0")
        return
    
    distanciaKm = hectometros / 10
    tiempoHs = tiempoMinutos / 60
    
    velocidad = distanciaKm / tiempoHs
    
    print(f"\n-----------------------\nVelocidad: {velocidad}Km/h\nKilometros recorridos: {distanciaKm}km\nTiempo en recorrido: {round(tiempoHs, 2)}hs")
    
main()