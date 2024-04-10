# Primer corte de notas 25%
# Segundo corte de notas 40%
# Tercer corte de notas 35%

calculoNotas1, calculoNotas2, calculoNotas3, faltante = 0, 0, 0, 0

def main():
    print("================== Bienvenidos al calculador de notas ==================\nNotas del 1 al 20")
    firstNote = int(input("Ingrese su primera nota (25%): "))
    secondNote = int(input("Ingrese su segunda nota (40%): "))
    thirdNote = int(input("Ingrese su tercera nota (35%): "))
    
    calculoNotas1 = (25 / 100) * firstNote
    calculoNotas2 = (40 / 100) * secondNote
    calculoNotas3 = (35 / 100) * thirdNote
    
    nf = calculoNotas1 + calculoNotas2 + calculoNotas3
    faltante =  round(nf - 10, 2)
    
    if round(nf) < 10:
        print(f"\nLo sentimos, no logro pasar la materia :( \nle falto: {faltante}pts\nPuntos totales: {nf}pts")
    else:
        print(f"\nFelicitaciones, logro pasar la materia :) \nPuntos totales: {round(nf)}pts")
main()