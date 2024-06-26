# Projeto Arduino com Sensor DHT11 e MQTT

Este projeto demonstra como ler dados de um sensor DHT11 (umidade e temperatura) usando um Arduino e enviar esses dados para um broker MQTT para visualização no aplicativo MyMQTT.

## Componentes Necessários

- Arduino (UNO, Mega, etc.)
- Sensor DHT11
- WiFi Shield ou módulo WiFi compatível com Arduino (por exemplo, ESP8266)
- Resistor de 10kΩ (se necessário)
- Jumpers e Protoboard

## Bibliotecas Utilizadas

- `WiFi101`: Para conexão WiFi.
- `DHT`: Para leitura do sensor DHT11.
- `PubSubClient`: Para comunicação MQTT.

## Conexões do Sensor DHT11

### DHT11 com 4 Pinos:

1. **VCC (ou +5V)**: Alimentação do sensor.
2. **Data**: Pino de saída de dados.
3. **NC**: Não conectado (sem uso).
4. **GND (ou Ground)**: Terra.

### DHT11 com 3 Pinos (módulo):

1. **VCC**: Alimentação do sensor.
2. **Data**: Pino de saída de dados.
3. **GND**: Terra.

### Conexões para o Arduino:

#### Para o DHT11 com 4 Pinos:

- **VCC (ou +5V)** do DHT11 -> **5V** no Arduino
- **Data** do DHT11 -> **Pino Digital 2** no Arduino
- **NC** do DHT11 -> Não conectado
- **GND** do DHT11 -> **GND** no Arduino

#### Para o DHT11 com 3 Pinos (módulo):

- **VCC** do DHT11 -> **5V** no Arduino
- **Data** do DHT11 -> **Pino Digital 2** no Arduino
- **GND** do DHT11 -> **GND** no Arduino

### Diagrama de Conexão com Pull-Up Resistor:

- Resistor de 10kΩ entre **Data** e **VCC**.

## Configuração do MQTT Dash

1. **Baixe e instale** o aplicativo MyMQTT.
2. **Adicione um novo broker**:
   - **Host**: `broker.hivemq.com`
   - **Port**: `1883`
3. **Adicione widgets** para os tópicos:
   - `home/temperature/humidity`
   - `home/temperature/temperature`

## Código Arduino

```cpp
#include <WiFi101.h>
#include <SPI.h>
#include <DHT.h>
#include <PubSubClient.h>

// Configurações da rede WiFi
const char* ssid = "*******";
const char* password = "*******";

int status = WL_IDLE_STATUS; // Status da conexão

// Configurações do sensor DHT11
#define DHTPIN 2     // Pino digital onde o DHT11 está conectado
#define DHTTYPE DHT11   // Define o tipo de sensor DHT

DHT dht(DHTPIN, DHTTYPE);

// Configurações do MQTT
const char* mqtt_server = "broker.hivemq.com"; // Endereço do broker MQTT
const char* mqtt_topic_humidity = "home/temperature/humidity";
const char* mqtt_topic_temperature = "home/temperature/temperature";

WiFiClient wifiClient;
PubSubClient client(wifiClient);

void setup() {
  // Inicializa a comunicação serial
  Serial.begin(9600);

  // Inicializa o sensor DHT
  dht.begin();

  // Verifica se a placa WiFi está presente
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("WiFi shield não encontrada.");
    while (true);
  }

  // Conecta à rede WiFi
  connectToWiFi();

  // Configura o servidor MQTT
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Lê a umidade e a temperatura do sensor DHT11
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Verifica se a leitura falhou
  if (isnan(h) || isnan(t)) {
    Serial.println("Falha ao ler do sensor DHT11!");
    return;
  }

  // Imprime os valores lidos no Monitor Serial
  Serial.print("Umidade: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.println(" *C");

  // Envia os valores para o MQTT
  sendMQTTMessage(mqtt_topic_humidity, h);
  sendMQTTMessage(mqtt_topic_temperature, t);

  // Aguarda 2 segundos antes de fazer uma nova leitura
  delay(2000);
}

void connectToWiFi() {
  // Tenta conectar à rede WiFi
  while (status != WL_CONNECTED) {
    Serial.print("Tentando conectar à rede: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, password);

    // Aguarda 10 segundos antes de tentar novamente
    delay(10000);
  }

  // Conexão bem-sucedida
  Serial.println("Conectado à rede WiFi");
  printWifiStatus();
}

void reconnect() {
  // Loop até que a conexão MQTT seja estabelecida
  while (!client.connected()) {
    Serial.print("Tentando conectar ao broker MQTT...");
    if (client.connect("ArduinoClient")) {
      Serial.println("conectado");
    } else {
      Serial.print("falhou, rc=");
      Serial.print(client.state());
      Serial.println(" tentando novamente em 5 segundos");
      // Aguarda 5 segundos antes de tentar novamente
      delay(5000);
    }
  }
}

void sendMQTTMessage(const char* topic, float value) {
  char msg[50];
  dtostrf(value, 6, 2, msg);
  client.publish(topic, msg);
}

void printWifiStatus() {
  // Imprime o SSID da rede
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // Imprime o endereço IP do Arduino
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // Imprime a intensidade do sinal
  long rssi = WiFi.RSSI();
  Serial.print("Signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
```

## Autores

[Jonathan Stefan Covelo de Carvalho e Gabriel Augusto Teodoro Vilas Boas ]