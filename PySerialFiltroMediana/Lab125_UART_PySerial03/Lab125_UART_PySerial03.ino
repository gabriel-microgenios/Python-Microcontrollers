/*
Microgenios Tecnologia e Educação.
www.microgenios.com.br / www.microgeniosacademy.com.br
Curso: Formação LabGenios Nano
Instrutor: Gabriel Rosa Paz
Data: 25/04/2026

Laboratórios para estudo de Comunicação ente Computador e Arduino (Microcontrolador)
utilizando Python, PySerial e criação/decodificação de protocolos básicos

Laboratório 125 - Recebimento de Dados Analógicos via Python do Arduino
*/

/*
Arduino envia leituras analógicas A6 e A7:
A6 → trimpot
A7 → LM35DZ

Covnersão das leituras:
Para o Trmpot (Tensão de 0V a 5V):
tensao = leitura * 5.0 / 1023.0;

Para o Sensor de Temperatura (10mV/°C):
temperatura = tensao_lm35 * 100.0;
*/

//Constantes:
#define entradaTrimpot A6
#define pinoLM35 A7
#define NUM_AMOSTRAS 11

//Variáveis Globais:
int leituras[NUM_AMOSTRAS];

//Código de filtro de Mediana
float lerTemperaturaMediana() 
{
  //Faz 11 leituras:
  for (int i = 0; i < NUM_AMOSTRAS; i++) 
  {
    leituras[i] = analogRead(pinoLM35);
    delay(5);
  }

  //Ordena as leituras em ordem crescente:
  for (int i = 0; i < NUM_AMOSTRAS - 1; i++) 
  {
    for (int j = i + 1; j < NUM_AMOSTRAS; j++) 
    {
      if (leituras[j] < leituras[i]) 
      {
        int temp = leituras[i];
        leituras[i] = leituras[j];
        leituras[j] = temp;
      }
    }
  }

  //Como são 11 amostras, a mediana é o elemento central:
  int adcMediana = leituras[NUM_AMOSTRAS / 2];

  /*
  //Converte ADC para tensão:
  float tensao = adcMediana * 5.0 / 1023.0;

  //LM35: 10 mV por °C:
  float temperatura = tensao * 100.0;

  return temperatura;
  */
  return adcMediana;
}

void setup() 
{
  //Config. Serial:
  Serial.begin(9600);
}

void loop() 
{
  
  //Leitura das entradas analógicas:
  int adcA6 = analogRead(entradaTrimpot);
  delay(10);
  //int adcA7 = analogRead(entradaLM35);
  //delay(10);

  //Conversão para tensão:
  float tensaoA6 = adcA6 * 5.0 / 1023.0;
  //float tensaoA7 = adcA7 * 5.0 / 1023.0;

  //Leitura, Filtro de Mediana:
  int adcA7 = lerTemperaturaMediana();

  //Converte ADC para tensão:
  float tensaoA7 = adcA7 * 5.0 / 1023.0;

  //LM35: 10 mV por °C:
  float temperatura = tensaoA7 * 100.0;

  //Montagem o protocolo de comunicação:
  Serial.print("ANALOG ");
  Serial.print(adcA6);
  Serial.print(" ");
  Serial.print(tensaoA6, 2);
  Serial.print(" ");
  Serial.print(adcA7);
  Serial.print(" ");
  Serial.println(temperatura, 1);

  delay(2000);
}
