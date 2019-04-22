broker_ip =  "192.168.1.55"
#broker_ip = "127.0.0.1"
port = 1883
import sys
import os
sys.path.append("./Digital_Thing") #needed to import modules in same path
pth = os.getcwd()
sys.path.append(pth) #needed to import modules in same path
print(sys.path)
import time
platform = ""
import gui as gui_client

#device_name="desktop"
#from Digital_Thing.init_for_desktop import *
#getch, mqtt_client = init(device_name, broker_ip)
 
try:
    device_name="desktop"
    from Digital_Thing.init_for_desktop import *
    getch, mqtt_client = init(device_name, broker_ip)
    platform = "desktop"
    print("loaded desktop")
except Exception as e:
    print("ERROR:", e)
    from Digital_Thing.init_for_esp32 import *
    getch,mqtt_client = init(device_name, broker_ip,"spyprjct-219","789sumrX")
    platform = "esp32"
import Digital_Thing.Digital_Object as dt
import Digital_Thing.Menu as menuC
import Digital_Thing.pub_sub_local as pubsub


def Run():
    global menu
    menu = menuC.Menu(dt=dt, pubsub=pubsub, mqtt_client=mqtt_client, udp_client="")
    menu_event = menu.menu_event #getting the function for performance
    print(  "*****************************Welcome to the menu****************************************\n***********************************************")
    print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT   |   a: QUIT")
    menuDict =     {"k":"up","j":"down","h":"left","l":"right","a":"quit"}
    cntrl_key = getch()
    data = dict()
    #mqtt_client.client.subscribe("spirit_level/#", qos=0)
    ky = ""
    gui_client.prnt(menu, pubsub)
    while True:

        #ky = mqtt_client.client.on_message()
        print(mqtt_client.timeSleep, ' ' , mqtt_client.publishOn ,' ',mqtt_client.screenOn)
        if platform == "esp32":
            ky = mqtt_client.client.check_msg()
            # TODO if this breaks then fix the connection
        for app_pbr_key,app_pbr_val in pubsub.app_pbrs.items():
            for app_event,callback in app_pbr_val.app_events.items():
                m = callback()
                mqtt_client.client.publish(app_pbr_key+"/"+app_event,str(m)) 
                app_pbr_val.dispatch(app_event, m) # (event,message sent)
                
                #update gui client with location and data  
                gui_client.prnt_data(app_event,m)
        gui_client.prnt(menu, pubsub)


        drctn = (menuDict.get(getch()) or mqtt_client.get_key_value() or ky)

        menu.menu_event(drctn)
        #time.sleep(.01275)
        #time.sleep(.215)
        time.sleep(mqtt_client.timeSleep)
        if type(drctn)!=type(None):
            gui_client.prnt(menu, pubsub)
            pass
if __name__ == '__main__':
    Run()
