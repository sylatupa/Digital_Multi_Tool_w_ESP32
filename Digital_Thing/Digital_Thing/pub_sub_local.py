
'''makes a subscriber, this appName must have the functions it wil register with'''    
def setSubRegisterFirstClassObject(hw,appName,app_config):
    import os
    #app = __import__(("hardware."+str(appName)), fromlist=[appName])
    app = __import__(("hardware"), fromlist=[appName])
    print(dir(pub))
    app = app.spirit_level
    print(dir(app))
    #__import__("hardware."+appName, globals={}, locals={}, fromlist=[], level=-1) 
    for subs in app_config.get(hw).get("subscribes"):
        print(subs)
        #method_to_call = getattr(app, subs.get("id"))
        #result = method_to_call("valuee")
        #setPubRegister(subs.get("id"),method_to_call)
        setPubRegister(subs.get("id"),app)


'''for the event name, add the firsts class object (the function to call) '''
def setPubRegister(subscriber, pubEventName ):
    pub.register(subscriber ,pubEventName)

'''for the event name, send the value to all registered subscribers '''
def runPubDispatch(pubEventName,value):
    pub.dispatch(pubEventName,value)
    #pub.dispatch("lunch", "It's lunchtime!") 

'''1) add all the events for the publisher'''
def setPubEvents(hw,app_config):
    if app_config.get(hw).get("publishes"):
        for route in app_config.get(hw).get("publishes"):
            published_routes.append(route["id"])
            pub.add_event(route["id"])
    if app_config.get(hw).get("subscribes"): 
        #a subscriber exsists with-out a corresponding publisher it fails, so adding all the subscriber routes too.
        for route in app_config.get(hw).get("subscribes"):
            published_routes.append(route["id"])
            pub.add_event(route["id"])

class Subscriber:
    def __init__(self, name):
        self.name = name
    def evoke(self, message):
        print('{} got message "{}"'.format(self.name, message))
    def lunch(self, message):
        print('{} got message "{}"'.format(self.name, message))
    def dinner(self, message):
        print('{} got message "{}"'.format(self.name, message))


    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))

    def __str__(self): return self.name
    def __cmp__(self, other):
        return cmp(self.name, other.name)
    # Necessary when __cmp__ or __eq__ is defined
    # in order to make this class usable as a
    # dictionary key:
    def __hash__(self):
        return hash(self.name)

class Publisher:
    def __init__(self):
        self.events = []
        # maps event names to subscribers
    def __str__(self): return self.action
    def __cmp__(self, other):
        return cmp(self.action, other.action)
        # Necessary when __cmp__ or __eq__ is defined
        # in order to make this class usable as a
        # dictionary key:
        # str -> dict
    def __hash__(self):
        return hash(self.action)
    def add_events(self,events):
        self.events = {event : dict() for event in events }
    def add_event(self,event):
        self.events[event] = dict() 
    def get_subscribers(self, event):
        return self.events[event]
    def register(self, event, who, callback=None):
        print("registr:",event,who,callback)
        #method_to_call = getattr(app, subs.get("id"))
        #result = method_to_call("valuee")
        #setPubRegister(subs.get("id"),method_to_call)
        print(who, ' ' , event)
        if callback == None:
            callback = getattr(who, event)
        self.get_subscribers(event)[who] = callback
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
    def dispatch(self, event, message):
        print( event, message)
        print(self.events)
        print(self.get_subscribers(event))
        for subscriber, callback in self.get_subscribers(event).items():
            print(subscriber)
            callback(message)            

{'dinner': {<pub_sub_local.Subscriber object at 0x7fbad13aa860>: <bound method Subscriber.dinner of <pub_sub_local.Subscriber object at 0x7fbad13aa860>>, <pub_sub_local.Subscriber object at 0x7fbad13aa898>: <bound method Subscriber.dinner of <pub_sub_local.Subscriber object at 0x7fbad13aa898>>},
'lunch': {<pub_sub_local.Subscriber object at 0x7fbad13aa828>: <bound method Subscriber.lunch of <pub_sub_local.Subscriber object at 0x7fbad13aa828>>, <pub_sub_local.Subscriber object at 0x7fbad13aa898>: <bound method Subscriber.lunch of <pub_sub_local.Subscriber object at 0x7fbad13aa898>>},
'breakfast': {},
'x': {},
'y': {},
'z': {},
'trigger': {},
'sample_rate': {<module 'hardware.spirit_level' from '/home/spy/Digital_Multi_Tool_w_ESP32/Digital_Thing/hardware/spirit_level.py'>: <function sample_rate at 0x7fbabd10c6a8>}, 
'trigger_threshold': {<module 'hardware.spirit_level' from '/home/spy/Digital_Multi_Tool_w_ESP32/Digital_Thing/hardware/spirit_level.py'>: <function trigger_threshold at 0x7fbabd10c730>}}


subscribed_routes = []
published_routes= []
pub = Publisher() 
pub.add_events({'lunch','dinner'})
pub.add_event('breakfast')
bob = Subscriber('Bob') 
alice = Subscriber('Alice') 
john = Subscriber('John') 
pub.register("lunch", bob) 
pub.register("dinner", alice) 
pub.register("lunch", john) 
pub.register("dinner", john) 



if __name__ == "__main__":
    pass

    #ddpub = Publisher(published_routes) 
    #pub.register(str(route["id"]),this_subscriber)

    pub = Publisher() 
    pub.add_events({'lunch','dinner'})
    pub.add_event('breakfast')
    bob = Subscriber('Bob') 
    alice = Subscriber('Alice') 
    john = Subscriber('John') 
    pub.register("lunch", bob) 
    pub.register("dinner", alice) 
    pub.register("lunch", john) 
    pub.register("dinner", john) 
     
    pub.dispatch("lunch", "It's lunchtime!") 
    pub.dispatch("dinner", "Dinner is served") 
