altura = float(input("Ingrese altura (0 para finalizar): "))
acum = 0
cont = 0

if altura == 0:
    print("No se ingresaron alturas.")
else:
    while altura != 0:
        acum += altura
        cont += 1
        altura = float(input("Ingrese altura (0 para finalizar): "))

    promedio = acum / cont
    print("El promedio de las alturas ingresadas es:", promedio)