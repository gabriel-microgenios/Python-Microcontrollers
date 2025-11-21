from pyfirmata import Arduino, util
from time import sleep

board = Arduino('COM3')   #Verifique a sua porta de comunicação em device manager

print("Conectado ao Arduino (Firmata)")

while True:
    board.digital[13].write(1)
    sleep(0.5)
    board.digital[13].write(0)
    sleep(0.5)
