import paho.mqtt.client as mqtt
import random
import time

# ThingSpeak MQTT Configuration
broker = "mqtt3.thingspeak.com"
port = 1883
channel_id = "2894243"
client_id = "DBMxBRwuOBQpBQ8dCC4wLAE"
username = "DBMxBRwuOBQpBQ8dCC4wLAE"
password = "Ui+3gD7Os6I+mytzWEAKnhPT"
topic = f"channels/{channel_id}/publish"

# MQTT Client Setup
client = mqtt.Client(client_id=client_id)
client.username_pw_set(username=username, password=password)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to ThingSpeak MQTT broker.")
    else:
        print(f"Connection failed with code {rc}.")

def on_disconnect(client, userdata, rc):
    print(f"Disconnected with result code {rc}.")
    if rc != 0:
        print("Unexpected disconnection. Attempting to reconnect...")
        try:
            client.reconnect()
        except Exception as e:
            print(f"Reconnect failed: {e}")

client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.connect(broker, port)
client.loop_start()

def generate_sensor_data():
    temperature = round(random.uniform(-50, 50), 2)  # Temperature between -50°C and 50°C
    humidity = round(random.uniform(0, 100), 2)      # Humidity between 0% and 100%
    co2 = round(random.uniform(300, 2000), 2)        # CO₂ levels between 300 ppm and 2000 ppm
    return temperature, humidity, co2

try:
    while True:
        if client.is_connected():
            temp, hum, co2 = generate_sensor_data()
            payload = f"field1={temp}&field2={hum}&field3={co2}"
            result = client.publish(topic, payload)
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"Published: {payload}")
            else:
                print(f"Failed to publish: {payload} (Error: {result.rc})")
        else:
            print("Client not connected. Waiting to reconnect...")
        time.sleep(15)

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    print("Stopped publishing.")
