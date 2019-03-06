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


#ddpub = Publisher(published_routes) 
#pub.register(str(route["id"]),this_subscriber)


def setPin(number,direction):
    if direction == "In":
        pin = machine.Pin(number, machine.Pin.IN, machine.Pin.PULL_UP)
    if direction == "Out":
        pin = machine.Pin(number, machine.Pin.OUT)

if __name__ == "__main__":
    print("you tried to run this as main")


def listAllImportedModules():
    import sys
    print(sys.modules.keys())
    print(list(imports()))
        
def imports():
    import types
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            try:
                yield val
            except:
                yield ''
