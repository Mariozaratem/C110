import random

respuesta = "y"

while respuesta == "y":
    # Simular el lanzamiento de un dado (generar un número aleatorio entre 1 y 6)
    numero_dado = random.randint(1, 6)
    
    # Imprimir la representación gráfica del dado
    print("Tirando el dado...")
    print("----------")
    print("|       |")
    print(f"|   {numero_dado}   |")
    print("|       |")
    print("----------")
    
    # Preguntar al usuario si quiere tirar el dado nuevamente
    respuesta = input("¿Quieres tirar el dado de nuevo? (y/n): ").lower()
    
    # Validar la respuesta del usuario
    while respuesta != "y" and respuesta != "n":
        respuesta = input("Respuesta no válida. Ingresa 'y' para tirar de nuevo o 'n' para salir: ").lower()

print("Gracias por jugar. ¡Hasta luego!")