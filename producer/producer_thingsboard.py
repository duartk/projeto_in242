import random
import time
import datetime
import paho.mqtt.client as mqtt
import json

# conectar ao broker

print('Conectando ao mqtt broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('18.228.159.69', 1883, 60)

# conectar ao ThingsBoard

THINGSBOARD_HOST = "demo.thingsboard.io"
ACCESS_TOKEN = "p84flMwDcHzOFYWCuBne"

thingsboard_client = mqtt.Client()
thingsboard_client.username_pw_set(ACCESS_TOKEN)
thingsboard_client.connect(THINGSBOARD_HOST, 1883, 60)

while True:
    temperatura = random.uniform(15,30)
    data = str(datetime.datetime.now())
    print(data, temperatura)
    msg = {
        'data': data,
        'temperatura': temperatura
        }
    mqtt_client.publish('projeto_in242', json.dumps(msg), qos=0)
    time.sleep(0.5)
    thingsboard_client.publish('v1/devices/me/telemetry', json.dumps(msg), 1)
    time.sleep(1)
    
    
    
    
    
