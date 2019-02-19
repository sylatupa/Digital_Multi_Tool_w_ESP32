import json

import os
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
'''

IOT for All?
I dunno, its a digital thing.

'''
class Digital_Config:
    global cf_hw,cf_thng,cf_b,cf_f,cf_ths_thng, c_hw, c_thng, c_b, c_f, c_ths_thng
    filepath = "./" #if running main from 
    things_that_are_happening = []
    
    #Editing these configs changes slower, and maybe never
    cf_f =  "feature_config.json"                                   # feature_config.json is the the config file that interfaces the hardware to the functions
    cf_b =  "behavior_config.json"                                  # universal variables that guide the systems rate
    cf_hw = "hardware_config.json"                                  # hardware_config.json is the config file that lists ALL current hardware that can be selected
    
    #Change these configs depending on the hardware you have and what pins they are mapped to
    cf_thng = "thing_config.json"                                   # thing_config.json is the config that lists information specific to the network, mqtt, osc
    cf_ths_thng = "this_thing.json"                                 # this_thing.json is the config file that lists all the hardware on the board

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
        self.c_ths_thng = c_ths_thng = json.load(data)
        data = open(filepath+cf_hw)  
        self.c_hw = json.load(data)
        data = open(filepath+cf_b)  
        self.c_b = json.load(data)
        data = open(filepath+cf_f)  
        self.c_f = json.load(data)
        
        self.subscription_list =[]

        for thng in self.c_ths_thng["hardware_topics"]:             # get this_thing.json and look at its available hardware topics
            print("setting up: ",thng)
            for hardware in self.c_hw:
                if hardware["id"] == thng:                          # this hardware is listed in this_thing
                    for feature in hardware["feature_topics"]:     # for all the available features of the hardware that is available
                        print("adding: ", feature, " to the menu")
                        for f in self.c_f:                          # look through the feature set and find its match
                            if str(f['id'])==str(feature) :        # now do all the things that this feature can do
                                for pubs in f['publishes']:
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

def setPin(number,direction):
    if direction == "In":
        pin = machine.Pin(number, machine.Pin.IN, machine.Pin.PULL_UP)
    if direction == "Out":
        pin = machine.Pin(number, machine.Pin.OUT)



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

'''
