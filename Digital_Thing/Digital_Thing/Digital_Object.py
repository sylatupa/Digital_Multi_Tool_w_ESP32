import json
import os
import sys
import Digital_Thing.getch as getch
import time
sys.path.append("./hardware")
try:
    import touchpins
except:
    print("touchpins not imported")
'''
IOT for All?
I dunno, its a digital thing.
'''

getch = getch._Getch()
class Digital_Config:
    global cf_hw,cf_thng,cf_b,cf_a,cf_ths_thng , c_thng, c_b, c_f, c_ths_thng,filepath
    filepath = "./" #if running main from 
    things_that_are_happening = []
    #Editing these configs changes slower, and maybe never
    cf_a=  "app_config.json"                                   # feature_config.json is the the config file that interfaces the hardware to the functions
    cf_b =  "behavior_config.json"                                  # universal variables that guide the systems rate
    cf_hw = "hardware_config.json"                                  # hardware_config.json is the config file that lists ALL current hardware that can be selected
    #Change these configs depending on the hardware you have and what pins they are mapped to
    cf_thng = "thing_config.json"                                   # thing_config.json is the config that lists information specific to the network, mqtt, osc
    cf_ths_thng = "this_thing.json"                                 # this_thing.json is the config file that lists all the hardware on the board

    maxMenuCurser = 0
    menu_in_application = False
    def __init__(self, hasMQTT):
        #open all the confi files and load them into objects
        '''
        a = Digital_Config()
        a.c_hw                  #all the config_hardware data dictionary
        a.c_ths_thng            #all the config_this_thing data dictionary
        '''
        print("setting up")
        print("MQTT active:" , hasMQTT)
        data = open(filepath+cf_ths_thng)  
        self.this_thing = json.load(data)
        data = open(filepath+cf_hw)  
        self.c_hw = json.load(data)
        data = open(filepath+cf_b)  
        self.c_b = json.load(data)
        data = open(filepath+ cf_a)  
        self.app_config = json.load(data)
        print("size", len(self.this_thing))
        
        self.maxMenuCurser = len(self.this_thing["hardware_topics"])
        self.menuCurser = 0
        self.subscription_list =[]
        self.publishing_list=[]
        self.hardware_name_list=[]
        step = "hardware"
        print("Welcome to the menu,\n this is the available hardware:")
        print(self.this_thing.get("hardware_topics"))
        
        while True:
            a = getch()
            time.sleep(.5)
            if step == 'hardware':
                if a == 'j':
                    print('up')
                    loadModuleRoutes(self.app_config.get(self.self.this_thing["hardware_topics"][self.menuCurser]))

                    thing_that_are_happening.append(import__(hardware["id"]+".py"))
                    step = "application"
                if a == 'h':
                    print('left')
                    if self.menuCurser > 0:
                        self.menuCurser = self.menuCurser - 1
                    else:
                        print(self.maxMenuCurser)
                        self.menuCurser = self.maxMenuCurser -1
                    print(self.this_thing["hardware_topics"][self.menuCurser])
                if a == 'l':
                    print('right')
                    if self.menuCurser < self.maxMenuCurser -1:
                        self.menuCurser = self.menuCurser + 1
                    else:
                        self.menuCurser = 0
                    print(self.this_thing["hardware_topics"][self.menuCurser])


                if a == 'k':
                    print('down')
                    del sys.modules[hardware["id"]+".py"]
            elif step == 'application':
                if a == 'j':
                    print('up')
                    loadModuleRoutes(self.this_thing["hardware_topics"][self.menuCurser])
                    thing_that_are_happening.append(import__(hardware["id"]+".py"))
                    step = "application"
                if a == 'h':
                    print('left')
                    if self.menuCurser > 0:
                        self.menuCurser = self.menuCurser - 1
                    else:
                        print(self.maxMenuCurser)
                        self.menuCurser = self.maxMenuCurser -1
                    print(self.this_thing["hardware_topics"][self.menuCurser])
                if a == 'l':
                    print('right')
                    if self.menuCurser < self.maxMenuCurser -1:
                        self.menuCurser = self.menuCurser + 1
                    else:
                        self.menuCurser = 0
                    print(self.this_thing["hardware_topics"][self.menuCurser])


                if a == 'k':
                    print('down')
                 

def loadModuleRoutes(app_name ):
    print(app_name)
    for route in app_config.get(app_name).get("publishes"):
        print(route)
    '''
        if "pin" in pubs.keys():
                            print(pubs['pin'])
                            #setPin(pubs["pin"],"Out"),
                        
                    for subs in f['subscribes']:
                        print(subs)
                        if "pin" in pubs.keys():
                            print(subs['pin'])
                            #setPin(subs["pin"],"In"),
                         #setsubscription on MQTT
                            print(f)

    publishing_list.append("newlist")
    '''
def runThing():
    while True:
        m = menu(files)
        selected = 0
        while True:
            try:
                selected = next(m)
            except StopIteration:
                break
        screen.box(0)
        game = files[selected]
        del screen
        del m
        del files
        try:
            __import__(game)
        except pew.GameOver:
            pass
    del sys.modules[game]

class GameOver(Exception):
    pass

def setPin(number,direction):
    if direction == "In":
        pin = machine.Pin(number, machine.Pin.IN, machine.Pin.PULL_UP)
    if direction == "Out":
        pin = machine.Pin(number, machine.Pin.OUT)

#print(os.listdir('..'))
class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
class Publisher:
    def __init__(self, events):
        # maps event names to subscribers
        # str -> dict
        self.events = { event : dict()
                          for event in events }
    def get_subscribers(self, event):
        return self.events[event]
    def register(self, event, who, callback=None):
        if callback == None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)            


if __name__ == "__main__":
    global filepath
    filepath = "../" #if running main from 
    d = Digital_Config(hasMQTT=False)
'''
    pub = Publisher(['lunch', 'dinner']) 
    bob = Subscriber('Bob') 
    alice = Subscriber('Alice') 
    john = Subscriber('John') 
     
    pub.register("lunch", bob) 
    pub.register("dinner", alice) 
    pub.register("lunch", john) 
    pub.register("dinner", john) 
     
    pub.dispatch("lunch", "It's lunchtime!") 
    pub.dispatch("dinner", "Dinner is served") 

import sys
        print(sys.modules.keys())
        print(list(imports()))
        
import types
def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            try:
                yield val
                
            except:
                yield ''
'''

