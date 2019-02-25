# getting system ready, on ubuntu: sudo apt-get install gcc git wget make libncurses-dev flex bison gperf python python-pip python-setuptools python-serial python-cryptography python-future python-pyparsing
# Else, go here: https://docs.espressif.com/projects/esp-idf/en/latest/get-started/linux-setup.html
# Change your arduino sketch library to Digital_Multi_Tool_w_ESP32/Libraries
# went to arduino website and downloaded 1.8.8 and install.sh'ed.
# sudo chmod 777 /dev/ttyUSB0
import sys
import os
sys.path.append("./Digital_Thing")
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

print("starting")
published_routes = []
subscribed_routes = []
menu.maxMenuHardwareCurser = len(dt.this_thing["hardware"])
menu.maxMenuApplicationCurser = 0
# Using the list of Digital Objects
# and the Digital Object Helper Functions
# with the menu to browse
def runThing():
    while True:
        print(menu.menuHardwareCurser , " " , menu.menuApplicationCurser)
        #pub.register(str(route["id"]),this_subscriber)
        menu.checkKeyboard()
        if menu.up: 
            
            _import__(do.getApplication(menu.menuApplicationCurser))
            events = ['up']
            ipub  = pub_sub_local.Publisher()
            pub.add_events(events)
            pub.register("up",tp)

        if menu.down:
            #'del sys.modules[game]'

        if menu.left:

        if menu.right:


        pub.dispatch("up","stuff2")
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

runThing()
