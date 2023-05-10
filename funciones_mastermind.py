import os
import string

def generar_respuesta(jugador1):
    """

    Pide 4 letras para el juego.

    Esta función pide al jugador 1 una combinación de 4 letras (de A a I) y verifica que no haya letras repetidas.
    
    """
    while True:
        solucion = input(f"{jugador1},  ingresa una combinación de 4 letras (de A a I): ").upper()
        if len(solucion) != 4:
            print("La combinación debe ser de 4 letras.")
            continue
        for letra in solucion:
            if letra not in string.ascii_uppercase[:9]:#Comprueba que las letras introducidas en la solución por el jugador 1 estén entre A e I, con la librería string.    
                print("Solo letras de A a I.")
                break
        else:
            if len(set(solucion)) != len(solucion):#
                print("No puede haber letras repetidas.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')#Borra la pantalla después de que el jugador 1 introduzca las letras que adivinará el jugador 1
                return solucion

def verificar_adivinanza(respuesta, adivinanza):
    """

    Verifica las respuestas.

    Verifica que la respuesta que dé el jugador 2 es correcta con la del jugador 1.
    
    """
    resultado = []
    for i in range(4):#Este for verifica las respuestas y sustituye por un "+" si la letra esta pero no en esa solución y un "-" si la letra no está.
        if adivinanza[i] == respuesta[i]:
            resultado.append(adivinanza[i])
        elif adivinanza[i] in respuesta:
            resultado.append("+")
        else:
            resultado.append("-")
    return ''.join(resultado)
