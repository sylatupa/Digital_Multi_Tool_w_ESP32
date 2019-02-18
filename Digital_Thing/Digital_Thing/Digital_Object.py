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

class Digital_Config:
    global cf_hw,cf_thng,cf_b,cf_f,cf_ths_thng, c_hw, c_thng, c_b, c_f, c_ths_thng
    filepath = "./" #if running main from 
    cf_hw = "hardware_config.json"
    cf_thng = "thing_config.json" 
    cf_b =  "behavior_config.json"
    cf_f =  "feature_config.json"  
    cf_ths_thng = "this_thing.json"
    
    things_that_are_happening = []
    
    def __init__(self):
        data = open(filepath+cf_ths_thng)  
        self.c_ths_thng = c_ths_thng = json.load(data)
        data = open(filepath+cf_hw)  
        self.c_hw = json.load(data)
        data = open(filepath+cf_b)  
        self.c_b = json.load(data)
        data = open(filepath+cf_f)  
        self.c_f = json.load(data)
    

        for thng in self.c_ths_thng["hardware_topics"]:
            print(thng)
            for hardware in self.c_hw:
                if hardware["id"] == thng: # this hardware is listed in this_thing
                    for features in hardware["feature_topics"]:
                        print(features)
                        for f in self.c_f:
                            if str(f['id'])==str(features) :
                                print(f)
if __name__ == "__main__":
    global filepath
    filepath = "../" #if running main from 
    d = Digital_Config()
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
