#Tkinter_LED_D13.py
#
#Interface gráfica simples com Tkinter para acender/apagar o LED no D13
#do Arduino usando Firmata.

from tkinter import *
from pyfirmata import Arduino, OUTPUT

#Porta do Arduino (altere se necessário):
PORTA = 'COM3'

#Conectando ao Arduino:
board = Arduino(PORTA)

#Pino do LED:
led = board.digital[13]
led.mode = OUTPUT

#Estado inicial do LED:
estado_led = False

# Função executada quando o botão é clicado
def alternar_led():
    global estado_led
    estado_led = not estado_led  # inverte o estado
    led.write(1 if estado_led else 0)
    #botao.config(text="APAGAR LED" if estado_led else "LIGAR LED")
    
    # Atualiza o texto e a cor do botão
    if estado_led:
        botao.config(text="APAGAR LED", bg="yellow")
    else:
        botao.config(text="LIGAR LED", bg="lightgreen")

#Interface Tkinter:
janela = Tk()
janela.title("Controle do LED D13")

#Botão que chama a função alternar_led():
botao = Button(janela, text="LIGAR LED", bg="lightgreen", width=20, height=2, command=alternar_led)
botao.pack(padx=20, pady=20)

# Inicia a interface gráfica
janela.mainloop()

# Ao sair da interface, desligar LED e desconectar Arduino
led.write(0)
board.exit()
