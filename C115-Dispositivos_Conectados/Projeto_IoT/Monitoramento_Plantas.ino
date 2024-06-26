#include <WiFi101.h>
#include <SPI.h>
#include <DHT.h>
#include <PubSubClient.h>

// Configurações da rede WiFi
const char* ssid = "******";
const char* password = "*********";

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
