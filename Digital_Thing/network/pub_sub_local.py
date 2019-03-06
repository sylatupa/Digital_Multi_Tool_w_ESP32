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
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
class Publisher:
    def __init__(self):
        self.events = []
        # maps event names to subscribers
        # str -> dict
    def add_events(self,events):
        self.events = { event : dict() for event in events }
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
