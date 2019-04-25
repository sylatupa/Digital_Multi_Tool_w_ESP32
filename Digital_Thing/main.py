import sys
import os
import time
sys.path.append("./Digital_Thing") #needed to import modules in same path
pth = os.getcwd()
sys.path.append(pth) #needed to import modules in same path
platform = ""
import gui as gui_client

#from Digital_Thing.init_for_desktop import *
#getch, mqtt_client = init(device_name, broker_ip)
import Digital_Thing.Menu as menuC
import Digital_Thing.pub_sub_local as pubsub
import Digital_Thing.Digital_Object as dt
device_name= dt.this_thing.get("device_name")
print(device_name)
broker_ip =  dt.this_thing.get("broker_ip")  #"192.168.1.55"
print(broker_ip)
port = dt.this_thing.get("broker_port")  #1883
try:
    from Digital_Thing.init_for_desktop import *
    getch, mqtt_client = init(device_name, broker_ip)
    platform = "desktop"
    print("loaded desktop")
except Exception as e:
    from Digital_Thing.init_for_esp32 import *
    getch,mqtt_client = init(device_name, broker_ip,"spyprjct-219","789sumrX")
    platform = "esp32"

#if True:
def Run():
    global menu,device_name
    import apps.neopixels.neopixels as np

    #np.cycle(20,23)
    menu = menuC.Menu(dt=dt, pubsub=pubsub, mqtt_client=mqtt_client, udp_client="")
    menu_event = menu.menu_event #getting the function for performance
    print(  "*****************************Welcome to the menu****************************************\n***********************************************")
    print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT   |   a: QUIT")
    menuDict =     {"k":"up","j":"down","h":"left","l":"right","a":"quit"}
    #cntrl_key = getch()
    data = dict()
    #mqtt_client.client.subscribe("spirit_level/#", qos=0)
    ky = ""
    #gui_client.prnt(menu, pubsub)
    while True:

        #np.cycle(20,23)
        #ky = mqtt_client.client.on_message()
        #print(mqtt_client.timeSleep, ' ' , mqtt_client.publishOn ,' ',mqtt_client.screenOn)
        if platform == "esp32":
            try:
                ky = mqtt_client.client.check_msg()
            except:
                pass
            # TODO if this breaks then fix the connection
        for app_pbr_key,app_pbr_val in pubsub.app_pbrs.items():
            for app_event,callback in app_pbr_val.app_events.items():
                m = callback()
                app_pbr_val.dispatch(app_event, m) # (event,message sent)
                if True:
                    try:
                        mqtt_client.client.publish(device_name+"/"+app_pbr_key+"/"+app_event,str(m)) 
                    except:
                        pass
                if False:
                    #update gui client with location and data  
                    gui_client.prnt_data(app_event,m)
            #gui_client.prnt(menu, pubsub)

        
        #np.cycle(20,23)
        #drctn = (menuDict.get(getch()) or mqtt_client.get_key_value() or ky)
        drctn = (mqtt_client.get_key_value() or ky)
        
        #np.cycle(20,23)
        print(drctn)
        menu.menu_event(drctn)
        #time.sleep(.01275)
        #time.sleep(.215)
        time.sleep(mqtt_client.timeSleep)
        if type(drctn)!=type(None):
            gui_client.prnt(menu, pubsub)
            pass


Run()
