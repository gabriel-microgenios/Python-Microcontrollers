from pyfirmata import Board, util
from time import sleep

# Layout customizado p/ Nano (8 analógicos)
layout_nano = {
    'digital': tuple(range(14)),      # D0..D13
    'analog':  tuple(range(8)),       # A0..A7 → canais 0..7
    'pwm':     (3, 5, 6, 9, 10, 11),
    'use_ports': True,
    'disabled': (0, 1)                # não usar RX/TX como GPIO
}

board = Board('COM3', layout=layout_nano)

it = util.Iterator(board)
it.start()

# Habilita relatório de A6 e A7
board.analog[6].enable_reporting()   # A6
board.analog[7].enable_reporting()   # A7

print("Lendo A6 e A7... (Ctrl+C para parar)")

while True:
    v6 = board.analog[6].read()  # entre 0.0 e 1.0 ou None
    v7 = board.analog[7].read()

    if v6 is not None and v7 is not None:
        print(f"A6 = {v6:.3f}   A7 = {v7:.3f}")
    else:
        print("Aguardando primeira leitura...")

    sleep(0.2)
