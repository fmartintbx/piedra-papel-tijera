import random

opciones = {"piedra":"tijera", "papel":"piedra", "tijera":"papel" }

while True:
    jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar el juego): ")
    
    if jugador == "salir":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
        
    if jugador not in opciones:
        print("Opción no válida. Por favor, elige piedra, papel o tijera.")
        continue

    computadora = random.choice(list(opciones.keys())) 

    print(f"Tu elección: {jugador}")
    print(f"La elección de la computadora: {computadora}")

    if jugador == computadora :
        print("Empate")
    elif opciones[jugador] == computadora :
        print("Gane")
    else:
        print("Gana la computadora")
    