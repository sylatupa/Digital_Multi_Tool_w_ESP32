
import os
'''makes a subscriber, this appName must have the functions it wil register with'''    
'''for the event name, add the firsts class object (the function to call) '''
app_pbrs = dict()

def init_new_app_pbr(app_pbr_name,app_config):
    app_pbr = App_Pbr(app_pbr_name,app_config)
    # TODO set the events for the app_pbr
    #for app_pbr_key, app_pbr_val in app_config[app_pbr_name].get("events"):
    app_pbrs[app_pbr_name] = app_pbr
    set_app_pbr_events(app_pbr_name,app_config)
    refresh_app_pbrs_subscribers(app_config,app_pbrs)



'''
Refreshes all the running apps with all the running app subscribers.
So, now that the apps have thier registered subscribers when the application dispatches thier function, they can run too!
'''
def refresh_app_pbrs_subscribers(app_config,app_pbrs):
    for app_name, app_val in app_pbrs.items():  #app_config.items():                                #iterate on the the APP_CONFIG
        for sub in app_config.get(app_name).get("subscribes") or []:                             #and for each of the subscribers
            for app_pbr, app_pbr_val in app_pbrs.items():                       #and for each of the APPLICATIONS
                for event in app_pbr_val.events:                                #and for all the APPLICATIONS EVENTS
                    #print("is there a match {} subscribes {} event {} "                            .format(sub.get("id")==event,sub,event))
                    if event == sub.get("id"):                                  #SEE IF THE APP EVENT IS THE SAME AS THE SUBSCRIBER
                        print("bringing in event {} for app {}".format(event,app_name))
                        #import the module by the config file name
                        module = __import__(("apps."+app_name), fromlist=[app_name]) 
                        #print("getting module", app_name)
                        try:
                            module = __import__(("apps."+app_name), fromlist=[app_name])
                            module = getattr(module,app_name)
                            #print("getting module", module)
                            #print(dir(module))
                            #module = getattr(module,sub.get("id"))
                            #print(dir(module))
                            #print("registering", sub.get("id"), module)
                            app_pbr_val.register(sub.get("id"),module, getattr(module, sub["id"])) #registering the subs
                        except Exception as e: print(e)

'''
Iterates through the app config and sets all the application publisher events
'''
def set_app_pbr_events( app_pbr_name,app_config):
    #try:
    if True:
        app_pbr = app_pbrs.get(app_pbr_name)
        print("events for: {}, {}".format(app_pbr_name, app_pbr))
        print(app_config.get(app_pbr_name))
        if app_config.get(app_pbr_name):
            for event in app_config.get(app_pbr_name).get("events") or []:
                print("adding events  {}".format(event))
                app_pbr.add_event(event.get("id"))
    #except:

    #    pass
#Application Publisher class
class App_Pbr:
    def __init__(self,name,app_config):
        self.name = name
        self.events = dict()
        self.app_events = dict()
        self.config = app_config(gt  fo app_pbr in app_config:
            

        # maps event names to subscribers
    def __str__(self): return self.name
    def __cmp__(self, other):
        return cmp(self.name, other.name)
        # Necessary when __cmp__ or __eq__ is defined
        # in order to make this class usable as a
        # dictionary key:
        # str -> dict
    def __hash__(self):
        return hash(self.name)
    def add_events(self,evnts):
        self.events = {event : dict() for event in evnts }
    def add_event(self,evnt):
        self.events[evnt] = dict() 
    def get_subscribers(self, evnt):
        return self.events[evnt]
    def register(self, event, who, callback=None):
        print("___registering: {}, to callback {}".format(event , getattr(who,event)))
        #prnt_funcs(who)
        #if callback == None:
        #    callback = getattr(who, event)
        self.get_subscribers(event)[who] = callback
        #print(self.events)
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
    def dispatch(self, event, message):
        for key, val in self.events.items():
            #newValue = event()
            #print(newValue)  #TODO
            for subscriber, callback in self.get_subscribers(key).items():
                print('getting event : {} from event dictionary, sending messge {} to subscriber {} with callback {}:'.format(event,message,subscriber.__name__,callback.__name__))
                callback(message)            


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
