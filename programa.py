from os import system
import time
import sys
system('cls')

i=0
def escribir_letra_por_letra(texto, retardo=0.1):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(retardo)
    print()  # Salto de línea al final

while i<69:
    escribir_letra_por_letra("Nigga", 0.18)
    i=+1   
