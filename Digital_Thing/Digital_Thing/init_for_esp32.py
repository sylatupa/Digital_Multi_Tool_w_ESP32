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
broker_ip =  "192.168.1.55"
#broker_ip = "192.168.0.135"
port = 1883

#import touchpins
import machine 
try:
    import Network.wifi_adptr as wifi
    wifi.connect("spyprjct-219","789sumrX")
except:
    print("no wifi")

#import utime
#from machine import Timer
#import hardware.neopixel as px
#px.main(20,25)
import sys
import Network.mqtt_client.esp32_client as mqtt_client 
import touchpin_getch as getch


import gui as gui_client
#global getch, gui_client, mqtt_client
getch = getch._Getch()  #TODO:esp32 convert

mqtt_client = mqtt_client.mqtt_client(broker_ip, port)
print(mqtt_client)
mqtt_client.connect_client()
#mqtt_client.client.loop_start()
#m.client.loop_forever()
#mqtt_client.test_publish()
#subscribe.callback(m.on_msg, "up", hostname=m.broker_address,port=m.port)

mqtt_client.client.subscribe("menu", qos=0)
mqtt_client.client.on_message = mqtt_client.on_msg
     

'''
t1 = Timer(0, 10)
t2 = Timer(1, 3)
t1.callback(lambda t: print(t, "tick1"))
t2.callback(lambda t: print(t, "tick2"))
utime.sleep(3)
led = machine.Pin(16, machine.Pin.OUT)
for i in range(10):
    print("led")
    led(1)
    time.sleep(0.5)
    led(0)
    time.sleep(0.5)

tim = pyb.Timer(4)              # create a timer object using timer 4
tim.init(freq=2)                # trigger at 2Hz
tim.callback(lambda t:pyb.LED(1).toggle())

def tick(timer):                # we will receive the timer object when being called
    print(timer.counter())      # show current timer's counter value
tim = pyb.Timer(4, freq=1)      # create a timer object using timer 4 - trigger at 1Hz
tim.callback(tick)              # set the callback to our tick function

tim = pyb.Timer(4, freq=100)    # freq in Hz
tim = pyb.Timer(4, prescaler=0, period=99)
tim.counter()                   # get counter (can also set)
tim.prescaler(2)                # set prescaler (can also get)
tim.period(199)                 # set period (can also get)
tim.callback(lambda t: ...)     # set callback for update interrupt (t=tim instance)
tim.callback(None)              # clear callback
'''
