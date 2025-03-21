FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 1
META_COLUMNA = COLUMNAS - 1

def imprimir_laberinto(fila_jugador, columna_jugador):
    """Imprime el laberinto con la posición del jugador y la meta."""
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if i == fila_jugador and j == columna_jugador:
                print("X ", end="")  # Jugador
            elif i == META_FILA and j == META_COLUMNA:
                print("O ", end="")  # Meta
            else:
                print(". ", end="")  # Espacio vacío
        print()

def mover_jugador(fila_jugador, columna_jugador):
    """Solicita al jugador un movimiento y actualiza la posición del jugador."""
    movimiento = input("\nIngrese movimiento (w: arriba, s: abajo, a: izq, d: der): ")

    if movimiento == 'w' and fila_jugador > 0:
        fila_jugador -= 1
    elif movimiento == 's' and fila_jugador < FILAS - 1:
        fila_jugador += 1
    elif movimiento == 'a' and columna_jugador > 0:
        columna_jugador -= 1
    elif movimiento == 'd' and columna_jugador < COLUMNAS - 1:
        columna_jugador += 1
    else:
        print("Movimiento no válido.")
    
    return fila_jugador, columna_jugador

def juego():
    """Función principal que ejecuta el juego de laberinto."""
    fila_jugador, columna_jugador = 0, 0

    while True:
        imprimir_laberinto(fila_jugador, columna_jugador)

        if fila_jugador == META_FILA and columna_jugador == META_COLUMNA:
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break

        fila_jugador, columna_jugador = mover_jugador(fila_jugador, columna_jugador)

if __name__ == "__main__":
    juego()
