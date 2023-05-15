from funciones_mastermind import verificar_adivinanza, generar_respuesta

print("El juego ha comenzado. ¡Adivina la combinación!")
jugador1 = input("Nombre del jugador 1: ")
jugador2 = input("Nombre del jugador 2: ")
respuesta = generar_respuesta(jugador1)
intentos = 0
while True:
    adivinanza = input(f"{jugador2} Adivina: ").upper()
    if adivinanza == "ZZZZ":#Termina el juego y da la respuesta si el jugador 2 introduce ZZZZ al intentar adivininar la respuesta.
        print("Has perdido. La respuesta era", respuesta,".")
        break
    resultado = verificar_adivinanza(respuesta, adivinanza)
    print("Resultado:", resultado)
    if resultado == respuesta:#Si el jugador 2 acierta nos dice que ha ganado y los intentos que ha necesitado.
        print(jugador2, "has ganado en ", intentos+1," intentos!")
        print("hola")
        break
    intentos += 1
