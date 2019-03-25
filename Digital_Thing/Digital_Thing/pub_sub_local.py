import os
app_pbrs = dict()

def init_new_app_pbr(app_pbr_name,app_config):
    '''
  Parameters
  ----------
  app_pbr_name: str     application publisher name
  app_config:   array   application config array
    '''
    app_pbr = App_Pbr(app_pbr_name,app_config)
    # TODO set the events for the app_pbr
    app_pbrs[app_pbr_name] = app_pbr
    set_app_pbr_events(app_pbr_name,app_config)
    refresh_app_pbrs_subscribers(app_config,app_pbrs)


def refresh_app_pbrs_subscribers(app_config,app_pbrs):
    '''
    Refreshes all the running apps with all the running app subscribers.
    So, now that the apps have thier registered subscribers when the application dispatches thier function, they can run too!
    Parameters
    ----------
    app_config: dictionary of config data
    app_pbrs:   dictionary of app publisher objects
    '''
    for app_name, app_val in app_pbrs.items():  #app_config.items():                                #iterate on the the APP_CONFIG
        for sub in app_config.get(app_name).get("subscribes") or []:                             #and for each of the subscribers
            for app_pbr, app_pbr_val in app_pbrs.items():                       #and for each of the APPLICATIONS
                for event in app_pbr_val.events:                                #and for all the APPLICATIONS EVENTS
                    #print("is there a match {} subscribes {} event {} "                            .format(sub.get("id")==event,sub,event))
                    if event == sub.get("id"):                                  #SEE IF THE APP EVENT IS THE SAME AS THE SUBSCRIBER
                        #print("bringing in event {} for app {}".format(event,app_name))
                        #import the module by the config file name
                        module = __import__(("apps."+app_name+"."+app_name), [app_name]) 
                        #try:
                        #from "apps."+app_name import app_name
                        module = __import__(("apps."+app_name), [app_name])
                        #print(module)
                        #print(dir(module))
                        module = getattr(module,app_name)
                        #print(module)
                        #print(dir(module))
                        module = getattr(module,app_name)
                        #print("last",module)
                        #print(dir(module))
                        #module = getattr(module,app_name)
                        #print(module)
                        #print(dir(module))
                        #print("getting module", module)
                        #print(dir(module))
                        #module = getattr(module,sub.get("id"))
                        #print(dir(module))
                        #print("registering", sub.get("id"), module)
                        #print(sub.get("id"),module, getattr(module, sub["id"])) #registering the subs
                        app_pbr_val.register(sub.get("id"),app_name, getattr(module, sub["id"])) #registering the subs
                        #app_pbr_val.register(sub.get("id"),module, getattr(module, sub["id"])) #registering the subs
                        #except Exception as e: print(e)

'''
Iterates through the app config and sets all the application publisher events
'''
def set_app_pbr_events( app_pbr_name,app_config):
    #try:
    if True:
        app_pbr = app_pbrs.get(app_pbr_name)
        print("events for: {}, {}".format(app_pbr_name, app_config.get(app_pbr_name) ))
        if app_config.get(app_pbr_name):
            for event in app_config.get(app_pbr_name).get("events") or []:
                print("adding events  {}".format(event))
                app_pbr.add_event(event.get("id"))
    #except:

    #    pass

class App_Pbr:
    """
    Application Publisher Class is the object for each application in the config file.
    Each Application has:
        --name
        --events
        --app_events    -- 
        --config        -- any other information from the config file

    """
    def __init__(self,name,app_config):
        self.name = name
        self.events = dict()
        self.app_events = dict()
        self.app_config = app_config
        #self.module = __import__(("apps."+self.name), fromlist=[self.name])
        #self.module = __import__(("apps."+self.name), [self.name])
        self.module = __import__(("apps."+self.name+"."+self.name), [self.name]) 
        #print("module: " ,self.module , dir(self.module))
        self.module = getattr(self.module,self.name)
        self.module = getattr(self.module,self.name)
        print("module: " ,self.module , dir(self.module))
        for event in self.app_config.get(self.name).get("events") or []:
            #module = __import__(("apps."+self.name), fromlist=[self.name])
            try:
                self.app_events[event["id"]] = getattr(self.module,event["id"])
                print("app has events", self.app_events)
            except Exception as e: print(e)
        print(self.app_events)
           

    # returns this objects name when its string method is called.
    def __str__(self): return self.name
    def __cmp__(self, other):
        '''
        returns this objects comparable method
        Necessary when __cmp__ or __eq__ is defined
        in order to make this class usable as a
        # dictionary key:
        # str -> dict
        '''
        return cmp(self.name, other.name)
    def __hash__(self):
        return hash(self.name)

    def add_events(self,evnts):
        '''evnts is coming form the app_config file'''
        self.events = {event : dict() for event in evnts }

    def add_event(self,evnt):
        self.events[evnt] = dict() 
    
    def get_subscribers(self, evnt):
        return self.events[evnt]
    
    def register(self, event, who, callback=None):
        print("___registering: {} who:{}, to callback {}".format(event,who , callback))
        #prnt_funcs(who)
        #if callback == None:
        #    callback = getattr(who, event)
        self.get_subscribers(event)[who] = callback
        #print(self.events)
    
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
    
    def dispatch(self, event, message):
        print('dispatch1',event, message)
        for subscriber, callback in self.get_subscribers(event).items():
            #print('dispatch2',event, message, subscriber, callback)
            #print('{} {}({}) -> {}.{}:'.format(self.name, event,message,subscriber.__name__,callback.__name__))
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
