
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

class MqttClass():


    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def publish(self, id_dispositivo, mensagem):
        client.publish("device/"+str(id_dispositivo)+"/code", payload=str(mensagem), qos=0, retain=False)


    def startServer(self, id_avaliador, id_dispositivo):
        client = mqtt.Client(client_id=str(id_avaliador), clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect( "192.168.1.200", 1883, 60)
        subscribe.callback(on_message, "device/"+str(id_dispositivo)+"/code", hostname="192.168.1.200", protocol=mqtt.MQTTv31)
