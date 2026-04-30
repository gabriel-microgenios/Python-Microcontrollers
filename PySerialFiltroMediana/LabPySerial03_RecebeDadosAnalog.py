#Microgenios Tecnologia e Educação
# www.microgeniosacademy.com.br
#Formação: Aprenda Arduino, Programação, Eletrônica e Microcontroladores com a LabGenios Nano
#Instrutor: Gabriel Rosa Paz
#Data: 25/04/2026
#Comunicação Computador - Arduino(Microcontrolador) com Python e Pyserial
#Comunicação com a placa utilizando UART e criando protocolos básicos

import serial
import time

PORTA = "COM3"
BAUDRATE = 9600

arduino = serial.Serial(PORTA, BAUDRATE, timeout=1)
time.sleep(2)

while True:
    linha = arduino.readline().decode().strip()
    #Decoficação:
    if linha.startswith("ANALOG"):
        partes = linha.split()
        
        #Trimpot:
        adc_a6 = int(partes[1])
        tensao_a6 = float(partes[2])
        
        #Sensor LM35Dz:
        adc_a7 = int(partes[3])
        temperatura = float(partes[4])

        print(f"A6 Trimpot: ADC={adc_a6} | Tensão={tensao_a6:.2f} V")
        print(f"A7 LM35:    ADC={adc_a7} | Temperatura={temperatura:.1f} °C")
        print("-" * 40)