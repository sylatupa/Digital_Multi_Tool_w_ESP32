from umqtt.simple import MQTTClient

class mqtt_client():
    global broker_address, client
    def __init__(self,broker_ip,port):
        self.port = port
        self.broker_address=broker_ip
        self.mqtt_topic=""
        self.key_value = 'key val'
        self.client = MQTTClient("umqtt_client", broker_ip)
        #self.client.disconnect()
        self.client.set_callback(self.on_msg)
        #c.connect()
        #c.subscribe(b"#")

    def subscribes(self,route,q=0):
        self.client.subscribe(route)

    def unsubscribes(self,route,q=0):
        self.client.unsubscribe(route)


    def connect_client(self):
        print("trying to connect to {}",self.broker_address)
        #self.client.connect(self.broker_address, self.port)
        self.client.connect()

    def on_msg(self,topic, message):
        print("{} {}".format(topic.decode("utf-7") ,message.decode("utf-7")))
        #print("message received " ,str(message.decode("utf-7")))
        self.key_value = str(message.decode("utf-7"))
        #val = obj['v']

    def get_key_value(self):
        v = self.key_value
        self.key_value = ''
        return v

    def publish_data(self,topic,message):
        self.client.connect(self.broker_address, self.port)
        self.client.publish(topic,message )

    def test_publish(self):
        self.client.publish("up","1.0")
        self.client.publish("down","1.0")
        self.client.publish("left","1.0")
        self.client.publish("test3","3.0")        
        self.client.publish("apples", 5.0)


def sub_cb(path,message):
    print(path)
    print(message)
    print("qqqqqqqqqqqqqqqqqqqqqqqqttttt")


if __name__== "__main__":
    import time
    #broker_ip =  "192.168.1.55"
    #broker_ip =  "localhost"
    #broker_ip = "127.0.0.1"
    broker_ip = "192.168.1.115"
    port = 1883
    m = mqtt_client(broker_ip, port)
    m.connect_client()
    m.test_publish()
    #subscribe.callback(m.on_msg, "up", hostname=m.broker_address,port=m.port)
    m.client.subscribe("menu", qos=0)
    m.client.on_message = m.on_msg
 
    while True:
        c.check_msg()
        print("looping in for mqtt")
        time.sleep(.4)
    #data = {"topic":"spyPi/direction/right", "m":22 }
    #publish_data(data)
    #data = {"topic":"spyPi/direction/up", "m":21}
    #publish_data(data)
    #data = {"topic":"spyPi/direction/down", "m":2 }
    #publish_data(data)
    ##test_publish()
