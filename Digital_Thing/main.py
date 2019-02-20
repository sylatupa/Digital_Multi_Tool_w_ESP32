# getting system ready, on ubuntu: sudo apt-get install gcc git wget make libncurses-dev flex bison gperf python python-pip python-setuptools python-serial python-cryptography python-future python-pyparsing
# Else, go here: https://docs.espressif.com/projects/esp-idf/en/latest/get-started/linux-setup.html
# Change your arduino sketch library to Digital_Multi_Tool_w_ESP32/Libraries
# went to arduino website and downloaded 1.8.8 and install.sh'ed.
# sudo chmod 777 /dev/ttyUSB0

import Digital_Thing.Digital_Object as do

hasMQTT = False
try:
    import network.simple_mqtt as mqtt
    hasMQTT = True
except:
    print("MQTT Failed")

if __name__ == "__main__":
    print("starting")
    dc = do.Digital_Config(hasMQTT)


#while True:
        # if new program 
        #   then reset pins
        #   reset subscribers


        
        #loop on each programs 

        #1) setLocalVariables

        #2) if online and frequency, then publish
        # set local variables


        #3)
