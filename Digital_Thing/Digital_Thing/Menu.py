import sys
import random
class Menu(object):
    """
    On each call get the last keyboard press, and process that character through the state machine.
    """
    def __init__(self,dt=None, pubsub=None, mqtt_client=None, udp_client=None):
        self.udp_client = udp_client
        self.mqtt_client = mqtt_client
        self.pubsub = pubsub

        self.indexApp       = 0
        self.indexPub       = 0
        self.indexSub       = 0
        self.dt             = dt
        self.currentAppName  = self.dt.this_thing.get("apps")[0]
        self.currentPubName = ''
        self.currentSubName = ''
        self.maxAppIndex = len(self.dt.this_thing.get("apps"))-1
        self.maxPubIndex    = 0
        self.maxSubIndex    = 0
        self.state          = "apps"
        self.app_st_menu    = ["Select","MQTT","DeSelect"]
        self.app_st_num     = 0
        if len(self.dt.this_thing.get("apps")) == 1:

            self.pubsub.init_new_app_pbr(self.currentAppName,self.dt.app_config)
    def menu_event(self, dirctn):
        self.dirctn = dirctn
        '''
        for app_pbr_key,app_pbr_val in self.pubsub.app_pbrs.items():
            for event_key, event_val in app_pbr_val.events.items():
                try:
                    app_pbr_val.dispatch(event_key,random.random())    
                except Exception as e: print(e)
        '''
        if self.state == 'pass':
            pass
        elif self.state == 'apps':
            '''apps state'''
            if self.dirctn == 'left':
                self.indexApp = levelUp(self.indexApp, self.maxAppIndex)
                self.currentAppName  = self.dt.this_thing.get("apps")[self.indexApp]
            elif self.dirctn == 'right':
                self.indexApp = levelDown(self.indexApp, self.maxAppIndex)
                self.currentAppName  = self.dt.this_thing.get("apps")[self.indexApp]
            elif self.dirctn  == 'up':
                self.state = 'app'
            elif self.dirctn == 'down':
                #self.state = 'HW'
                print("Lowest")
        elif self.state == 'app':
            if self.dirctn == 'up':
                if self.app_st_menu[self.app_st_num] == "DeSelect":
                    self.state = 'remove'
                elif self.app_st_menu[self.app_st_num] == "Select":
                    self.state = 'exec'
                    print("____EXECUTE!____")
                elif self.app_st_menu[self.app_st_num] == "MQTT":
                    pass
            elif self.dirctn == 'down':
                self.state = 'apps'
                print("apps")
            elif self.dirctn == 'left':
                self.app_st_num = levelUp(self.app_st_num, 2)
            elif self.dirctn == 'right':
                self.app_st_num = levelUp(self.app_st_num, 2)

        elif self.state == 'exec':
            print("EXECUTE!")
            self.state = 'apps'
            self.pubsub.init_new_app_pbr(self.currentAppName,self.dt.app_config)
            #self.mqtt_client.subscribes(self.currentAppName +"/#", 0)
 
        elif self.state == 'remove':
            print("remove!")
            self.state = 'app'
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            self.pubsub.remove_app_pbr(self.currentAppName,self.dt.app_config)
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



        elif self.dirctn == 'quit':
            sys.exit()
if __name__ == '__main__':
    import Digital_Object as dt
    sys.path.append(pth) #needed to import modules in same path

    menu = Menu(dt)
    while True:
        menu.menu_event()
        print("looping in for mqtt")
        time.sleep(.4)




def levelUp(level,maxLevel):
    if level < maxLevel:
        return level + 1
    else: return 0
def levelDown(level, maxLevel):
    if level > 0:
        return level - 1
    else: return maxLevel

