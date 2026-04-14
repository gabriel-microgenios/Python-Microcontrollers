#Microgenios Tecnologia e Educação
# www.microgeniosacademy.com.br
#Formação: Aprenda Arduino, Programação, Eletrônica e Microcontroladores com a LabGenios Nano
#Instrutor: Gabriel Rosa Paz
#Data: 14/04/2026
#Interfaces Gráficas utilizando Python, Tkinter e Comunicação serial com Firmata

#Importação de Bibliotecas necessárias
import tkinter as tk

#--------------------------------------------------------------
from pyfirmata import Arduino, util

# =========================================================
# CONFIGURAÇÃO DA PORTA SERIAL
# Altere para a porta correta do Arduino
# Exemplo no Windows: "COM3"
# Exemplo no Linux: "/dev/ttyUSB0" ou "/dev/ttyACM0"
# =========================================================
PORTA_ARDUINO = "COM3"

# =========================================================
# CONEXÃO COM A PLACA VIA FIRMATA
# =========================================================
placa = Arduino(PORTA_ARDUINO)
#--------------------------------------------------------------

# =========================================================
# CONFIGURAÇÃO DOS PINOS DIGITAIS DE SAÍDA
# Agora usaremos D13 (Ligado ao LED Azul)
# =========================================================
pino_d13 = placa.get_pin('d:13:o')

# Garante que tudo comece desligado
pino_d13.write(0)



#--------------------------------------------------------------------
#Funções que serão chamadas quando os botões forem pressionados
def ligar_led():
    canvas.itemconfig(led, fill="blue4")
    label_estado.config(text="Estado: LIGADO")
    pino_d13.write(1)

def desligar_led():
    canvas.itemconfig(led, fill="gray")
    label_estado.config(text="Estado: DESLIGADO")
    pino_d13.write(0)
#--------------------------------------------------------------------
    
#--------------------------------------------------------------------  
# =========================================================
# FUNÇÃO PARA FECHAR A APLICAÇÃO COM SEGURANÇA
# =========================================================
def fechar_aplicacao():
    # Desliga os pinos físicos
    pino_d13.write(0)

    # Encerra a comunicação com a placa
    placa.exit()

    # Fecha a janela
    janela.destroy()
#--------------------------------------------------------------------
    
#--------------------------------------------------------------------
#Criação da janela do aplicativo
janela = tk.Tk()
janela.title("Exemplo 3 - LED com botões de imagem")
janela.geometry("320x400")
#--------------------------------------------------------------------

#--------------------------------------------------------------------
#Label/Rótulo Superior (Topo)
#Label de título
tk.Label(janela, text="Controle de LED", font=("Arial", 14)).pack(pady=10)
#--------------------------------------------------------------------

#-------------------------------------------------------------------- 
#Canvas para desenhar o LED
canvas = tk.Canvas(janela, width=140, height=140)
canvas.pack(pady=10)

#Círculo de 100x100 representando o LED
led = canvas.create_oval(20, 20, 120, 120, fill="gray")
#--------------------------------------------------------------------

#--------------------------------------------------------------------
#Label/Rótulo Inferior
#Label de estado
label_estado = tk.Label(janela, text="Estado: DESLIGADO", font=("Arial", 12))
label_estado.pack(pady=10)
#--------------------------------------------------------------------

#--------------------------------------------------------------------
#Imagens dos botões (50x50)
# Coloque esses arquivos PNG na mesma pasta do script
img_liga = tk.PhotoImage(file="IconeLampadaAcesa50x50.png")
img_desliga = tk.PhotoImage(file="IconeLampadaApagada50x50.png")
#--------------------------------------------------------------------

#--------------------------------------------------------------------
#Frame para os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

# Botão ligar
botao_ligar = tk.Button(frame_botoes, image=img_liga, command=ligar_led)
botao_ligar.grid(row=0, column=0, padx=10)

# Botão desligar
botao_desligar = tk.Button(frame_botoes, image=img_desliga, command=desligar_led)
botao_desligar.grid(row=0, column=1, padx=10)
#--------------------------------------------------------------------

# =========================================================
# TRATAMENTO DO FECHAMENTO DA JANELA
# =========================================================
janela.protocol("WM_DELETE_WINDOW", fechar_aplicacao)

janela.mainloop()

