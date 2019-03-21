broker_ip =  "192.168.1.55"

#broker_ip =  "localhost"
broker_ip = "127.0.0.1"
#broker_ip = "192.168.0.135"
port = 1883
    
if __name__ == '__main__':
    import sys
    import os
    sys.path.append("./Digital_Thing") #needed to import modules in same path
    pth = os.getcwd()
    sys.path.append(pth) #needed to import modules in same path
    import time
    from Digital_Thing.init_for_desktop import *
    import Digital_Thing.Digital_Object as dt
    import Digital_Thing.Menu as menu 
    import Digital_Thing.pub_sub_local as pubsub
    menu = menu.Menu(dt=dt, pubsub=pubsub, mqtt_client=mqtt_client, udp_client="")
    menu_event = menu.menu_event #getting the function for performance
    print(  "************Welcome to the menu****************************************\n******************************************")
    print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT   |   a: QUIT")
    menuDict =     {"k":"up","j":"down","h":"left","l":"right","a":"quit"}
    cntrl_key = getch()
    while True:
        
        menu.menu_event(menuDict.get(getch()) or mqtt_client.get_key_value())

        #menu.menu_event(getch())
        gui_client.prnt(menu, pubsub)
        time.sleep(.075)
        '''
        if type(self.dirctn)!=type(None):
            self.gui_client.prnt()
        '''

   
