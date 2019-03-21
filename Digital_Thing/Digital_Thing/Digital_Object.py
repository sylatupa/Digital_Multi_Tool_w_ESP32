import json
_filepath = "./" 
cf_a=  "app_config.json"    
#cf_b =  "behavior_config.json"
cf_thng = "thing_config.json"
cf_ths_thng = "this_thing.json"
data = open(_filepath+cf_ths_thng)  
this_thing = json.load(data)
#data = open(_filepath+cf_b)  
#c_b = json.load(data)
data = open(_filepath+ cf_a)  
app_config = json.load(data)

hardwares = []
subscription_list =[]
publishing_list=[]
publishers = set()
subscriptions = set()

def setPublishers():
    pubs = getPublishersForApp(appname)


def setPublishersForApp(appname):
    app = app_config.get(appname)
    for pubs in app.get("publishes"):
        publishers.add(pubs.get("id"))

def getSubscribersForApp(appname):
    app = app_config.get(appname)
    for subs in app.get("subscribes"):
        subscriptions.add(subs.get("id"))

#def getApplication(ele_num):
#    return hardware.get("applications")[ele_num]
def pruneAppConfig():
    for ap in this_thing.get("apps"):
        remove_this = True
        for app in app_config.copy():
            if str(ap) == str(app):
                remove_this = False
                break
        if remove_this:
            try:
                del app_config[app]
                break
            except:
                print("no hardware named " + ap + " in config file")

pruneAppConfig()  #removes all the config files that arent on this thing, modify the hardware list in this_thing.json

def setPin(number,direction):
    if direction == "In":
        pin = machine.Pin(number, machine.Pin.IN, machine.Pin.PULL_UP)
    if direction == "Out":
        pin = machine.Pin(number, machine.Pin.OUT)
