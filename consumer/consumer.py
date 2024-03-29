import paho.mqtt.client as mqtt
from pymongo import MongoClient
import datetime
import json

mongo_client = MongoClient('18.228.159.69', 27017)
mongo_db = mongo_client['projeto_in242']
mongo_collection = mongo_db['in242']


def on_message(mqtt_client, obj, msg):
    print('recebendo mensagem...')
    msg_formatada = json.loads(msg.payload)
    msg_formatada['data_coleta'] = datetime.datetime.now()
    mongo_collection.insert_one(msg_formatada)
    print('mensagem inserida')


print('configurando...')
mqtt_client = mqtt.Client()
mqtt_client.connect('18.228.159.69', 1883, 60)
mqtt_client.on_message = on_message
mqtt_client.subscribe("projeto_in242/#", 0)
mqtt_client.loop_forever()
