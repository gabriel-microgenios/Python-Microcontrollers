#Microgenios Tecnologia e Educação
# www.microgeniosacademy.com.br
#Formação: Aprenda Arduino, Programação, Eletrônica e Microcontroladores com a LabGenios Nano
#Instrutor: Gabriel Rosa Paz
#Data: 21/03/2026
#Interfaces Gráficas utilizando Python e Tkinter

#Importação de Bibliotecas necessárias
import tkinter as tk

#--------------------------------------------------------------------
#Funções que serão chamadas quando os botões forem pressionados
def ligar_led():
    canvas.itemconfig(led, fill="red")
    label_estado.config(text="Estado: LIGADO")

def desligar_led():
    canvas.itemconfig(led, fill="gray")
    label_estado.config(text="Estado: DESLIGADO")
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

janela.mainloop()
