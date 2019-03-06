# getting system ready, on ubuntu: sudo apt-get install gcc git wget make libncurses-dev flex bison gperf python python-pip python-setuptools python-serial python-cryptography python-future python-pyparsing
# Else, go here: https://docs.espressif.com/projects/esp-idf/en/latest/get-started/linux-setup.html
# Change your arduino sketch library to Digital_Multi_Tool_w_ESP32/Libraries
# went to arduino website and downloaded 1.8.8 and install.sh'ed.
# sudo chmod 777 /dev/ttyUSB0
import sys
import os
print(os.listdir("."))
#sys.path.append("./Digital_Thing")
try:
    sys.dont_write_bytecode = True #hoping to avoid .pyc files
except:
    print('probably on ubuntu machine')
    pass
#print(sys.modules)
import Digital_Thing.Digital_Object as dt
import Digital_Thing.Digital_Object_Functions as functions
import Digital_Thing.menu as menu
import network.mqtt_client.ubuntu_client
import network.pub_sub_local as pub_sub_local
import time
import hardware.touchpins as tp
#print(sys.modules)
try:
    import touchpins
    import network.simple_mqtt as mqtt
except:
    print("esp32")
try:
    import machine  
    led = machine.Pin(16, machine.Pin.OUT)
    for i in range(10):
        print("led")
        led(1)
        time.sleep(0.5)
        led(0)
        time.sleep(0.5)
except:
    print("led fail")
try:
    import hardware.neopixel as px
    px.main(20,25)
except:
    print("neopixel failure")
    pass
subscribed_routes = []
menu.maxMenuHardwareCurser = len(dt.this_thing["hardware"])
menu.maxMenuApplicationCurser = 0
publisher_list = []
def runThing():
    while True:
        menu.checkKeyboard()
        if menu.hardware and menu.up:
            print("checkinghardware")
            menu.hardware = False
            menu.up = False
        if menu.application and menu.up:
            menu.application = False
            print("checkingapps")
            pub             = pub_sub_local.Publisher()
            events_published    = dt.getPublishersForApp(hardware_name )
            subscribers         = dt.getSubscribersForApp(hardware_name)
            pub.add_events(events_published)
            publisher_list.append(pub)
            #app_name = dt.getApplication(hardware_name, menu.menuApplicationCurser)
            __import__(application_name)
            for sub in subscribers:
                for pubs in publisher_list():
                    for event in pubs.events:
                        if event == sub.get("id"):
                            pub.register(sub, getattr(new_app, sub)() )     
            menu.up = False

        if menu.down:
            menu.down = False 
            #del sys.modules[game]

        if menu.left:
            hardware_name = dt.this_thing["hardware"][menu.menuHardwareCurser]
            application_name = dt.app_config[hardware_name].get("applications")[menu.menuApplicationCurser]
            print(hardware_name  " + application_name)
            menu.left = False
        if menu.right:
            hardware_name = dt.this_thing["hardware"][menu.menuHardwareCurser]
            application_name = dt.app_config[hardware_name].get("applications")[menu.menuApplicationCurser]
            print(hardware_name +" " + application_name)
            menu.right = False
        #pub.dispatch("up","stuff2")
        time.sleep(.5)
        '''
        do.subscription_list
        do.publishing_list
        do.hardware_name_list
        '''
        #IF KEYBOARD CHANGE
            #Modifys the running list of pubs
                #remove the current pub topics
                #add the new pub topics
                 #pub.register(module
                #for each su

            #Updates the pubs subs local
            #Updates the MQTT
            #Updates the OSC Path

        #RUN MODULES
        #things_that_are_happening.append(thisApplication)


if __name__=="__main__":
    import subprocess as sp
    #sp.call('cls',shell=True)
    tmp = sp.call('clear',shell=True)
    

runThing()

