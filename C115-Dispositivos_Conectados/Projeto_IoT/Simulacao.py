import random
import time
import paho.mqtt.client as mqtt

# Configurações do MQTT
broker = "broker.emqx.io"
port = 1883
topic = "sensor/monitoring"

# Função para obter dados simulados do sensor
def get_sensor_data():
    humidity = random.uniform(0, 100)  # Umidade entre 0% e 100%
    temperature = random.uniform(-10, 50)  # Temperatura entre -10°C e 50°C
    return humidity, temperature

# Callback ao conectar ao broker MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT")
    else:
        print("Falha na conexão, código de retorno:", rc)

# Função para simular o monitoramento do sensor e publicar os dados via MQTT
def simulate_sensor_monitoring(duration):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker, port, 60)
    client.loop_start()

    start_time = time.time()
    while (time.time() - start_time) < duration:
        humidity, temperature = get_sensor_data()
        payload = f"Umidade: {humidity:.2f}%, Temperatura: {temperature:.2f}°C"
        client.publish(topic, payload)
        print(f"Publicado: {payload}")
        time.sleep(1)
    
    client.loop_stop()
    client.disconnect()

# Simular o monitoramento por 10 segundos
simulate_sensor_monitoring(10)