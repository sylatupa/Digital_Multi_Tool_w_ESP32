'''
module initiates all the peripherial functions and data to run on a desktop:
  ...

Attributes
----------
name : str      the name of the animal
Methods
-------
says(sound=None)    Prints the animals name and what sound it makes
says_str = "A {name} says {sound}"

'''
def init(device_name,broker_ip):
    #broker_ip =  "192.168.1.55"
    #broker_ip =  "localhost"
    #broker_ip = "127.0.0.1"
    #broker_ip = "192.168.0.135"
    port = 1883
    import sys
    sys.dont_write_bytecode = True #hoping to avoid .pyc files
    import subprocess as sp
    tmp = sp.call('clear',shell=True)
    import Network.mqtt_client.ubuntu_client as mqtt_client 
    import getch
    #import gui as gui_client
    #global getch, gui_client, mqtt_client
    getch = getch._Getch()  #TODO:esp32 convert

    mqtt_client = mqtt_client.mqtt_client(broker_ip, port)
    mqtt_client.connect_client()
    mqtt_client.client.loop_start()
    #m.client.loop_forever()
    #mqtt_client.test_publish()
    #subscribe.callback(m.on_msg, "up", hostname=m.broker_address,port=m.port)

    mqtt_client.client.subscribe("menu", qos=0)

    mqtt_client.client.subscribe(device_name+"/sleep", qos=0)
    mqtt_client.client.subscribe(device_name+"/screen", qos=0)
    mqtt_client.client.subscribe(device_name+"/publish", qos=0)
    mqtt_client.client.on_message = mqtt_client.on_msg
    return getch,mqtt_client

#init("name","192.168.0.135")
