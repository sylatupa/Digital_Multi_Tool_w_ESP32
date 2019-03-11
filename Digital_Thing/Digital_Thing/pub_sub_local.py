published_routes = []
subscribed_routes = []
def setPublisher(app_name,app_config ):
    if app_config.get(app_name).get("publishes"):
        for route in app_config.get(app_name).get("publishes"):
            published_routes.append(route["id"])
    '''
    maybe want to add the subscribers to the set
    if app_config.get(app_name).get("subscribes"):
        for route in app_config.get(app_name).get("subscribes"):
            published_routes.append(route["id"])
    '''
    return published_routes

def getListOfPublishers(app_name,app_config):
    published_routes = []
    this_subscriber = Subscriber(app_name)
    if app_config.get(app_name).get("publishes"):
        for route in app_config.get(app_name).get("publishes"):
            published_routes.append(route["id"])
    if app_config.get(app_name).get("subscribes"):
        for route in app_config.get(app_name).get("subscribes"):
            published_routes.append(route["id"])
    return published_routes

def getListOfSubscribers(app_name,app_config):
    if app_config.get(app_name).get("subscribes"):
        for route in app_config.get(app_name).get("subscribes"):
            subscribed_routes.append(str(route["id"]))
    return subscribed_routes

def setSubscriber(app_name,app_config ):
    this_subscriber = Subscriber(app_name)
    if app_config.get(app_name).get("publishes"):
        for route in app_config.get(app_name).get("publishes"):
            published_routes.append(route["id"])

    if app_config.get(app_name).get("subscribes"):
        for route in app_config.get(app_name).get("subscribes"):
            published_routes.append(route["id"])

    #pub = Publisher(published_routes) # Publisher(['lunch', 'dinner']) 

    if app_config.get(app_name).get("subscribes"):
        for route in app_config.get(app_name).get("subscribes"):
            subscribed_routes.append(str(route["id"]))
            pub.register(str(route["id"]),this_subscriber)

def getPublishers_iter():
    yield ''
    pass

def getSubscribers_iter():
    yield ''
    pass

class Subscriber:
    def __init__(self, name):
        self.name = name
    def evoke(self, message):
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
        if callback == None:
            callback = getattr(who, 'evoke')
        self.get_subscribers(event)[who] = callback
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)            
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
