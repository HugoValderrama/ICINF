preguntas = int(input("Ingrese preguntas realizadas: "))
print("")
respuestas = int(input("Ingrese respuestas correctas: "))

porcentaje = (respuestas / preguntas) * 100

if respuestas < preguntas:

    if porcentaje >= 95:
        nivel = "Nivel máximo"
    elif porcentaje >= 70:
        nivel = "Nivel medio"
    elif porcentaje >= 40:
        nivel = "Nivel regular"
    else:
        nivel = "Fuera de nivel"

    print("")
    print("Su porcentaje de respuestas correctas es del ", porcentaje,"%")
    print(nivel)

else:

    print("")
    print("La cantidad de respuestas correctas es mayor al de preguntas.")
    print("Por favor, reinicie el programa")