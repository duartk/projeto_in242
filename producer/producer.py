import random
import time
import datetime
import paho.mqtt.client as mqtt
import json
import tago

# conectar ao broker

print('Conectando ao mqtt broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('18.228.159.69', 1883, 60)

# conectar ao Tago
MY_DEVICE_TOKEN = '5a06f128-ae9b-4c25-b662-e3f655dc0312'
my_device_1 = tago.Device(MY_DEVICE_TOKEN)

while True:
    temperatura = random.uniform(15,30)
    data = str(datetime.datetime.now())    
    print(data, temperatura)
    msg = {
        'data': data,
        'temperatura': temperatura
        }
    # ====Publicando no Mosquito ===
    mqtt_client.publish('projeto_in242', json.dumps(msg), qos=0)
    time.sleep(0.5)
    # ====Publicando no Tago.io ===
    payload = {'variable': 'temperatura', 'time': data, 'value': temperatura}
    my_device_1.insert(payload)
    print('Publicado na Tago.io')
    time.sleep(1)
    
    
    
    
    
