acum = 0
cont1 = 0
cont2 = 0

sueldo = int(input("Ingrese el sueldo: "))

if sueldo == -1:
    print("No se ingresaron sueldos.")
else:
    while sueldo != -1:
        acum += sueldo
        if 500000 <= sueldo <= 900000:
            cont1 += 1
        elif sueldo > 900000 and sueldo <= 1500000:  
            cont2 += 1
        sueldo = int(input("Ingrese el sueldo: "))

    print("La empresa gasta $", acum, " en sueldos del personal")
    print("Los empleados que cobran entre $500,000 y $900,000 son: ", cont1)
    print("Los empleados que cobran más de $900,000 y hasta $1,500,000 son: ", cont2)
