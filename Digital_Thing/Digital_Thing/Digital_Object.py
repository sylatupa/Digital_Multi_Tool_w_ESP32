import json

_filepath = "./" #if running main from 
cf_a=  "app_config.json"                                   # feature_config.json is the the config file that interfaces the hardware to the functions
#cf_b =  "behavior_config.json"                                  # universal variables that guide the systems rate
cf_thng = "thing_config.json"                                   # thing_config.json is the config that lists information specific to the network, mqtt, osc
cf_ths_thng = "this_thing.json"                                 # this_thing.json is the config file that lists all the hardware on the board
#open all the confi files and load them into objects
data = open(_filepath+cf_ths_thng)  
this_thing = json.load(data)
#data = open(_filepath+cf_b)  
#c_b = json.load(data)
data = open(_filepath+ cf_a)  
app_config = json.load(data)

hardwares = []
subscription_list =[]
publishing_list=[]
hardware_name_list=[]
publishers = set()
'''
pub                  = pub_sub_local.Publisher()
events_published    = dt.getPublishersForApp(hardware_name )
subscribers         = dt.getSubscribersForApp(hardware_name)
pub.add_events(events_published)
publisher_list.append(pub)
__import__(application_name)
for sub in subscribers:
    for pubs in publisher_list():
        for event in pubs.events:
            if event == sub.get("id"):
                pub.register(sub, getattr(new_app, sub)() )     
'''

def pruneAppConfig():
    for hardware in this_thing.get("hardware"):
        thisThing_has_thisHardware = False
        for hw in app_config:
            if hardware == hw:
                thisThing_has_thisHardware = True
        if thisThing_has_thisHardware == False:
            try:
                del app_config[hardware]
            except:
                print("no hardware named " + hardware + " in config file")

def getPublishersForApp(appname):
    app = app_config.get(appname)
    publist = set()
    for pubs in app.get("publishes"):
        publist.add(pubs.get("id"))
    return publist

def getSubscribersForApp(appname):
    app = app_config.get(appname)
    sublist = set()
    for subs in app.get("subscribes"):
        sublist.add(subs.get("id"))
    return sublist

#def getApplication(ele_num):
#    return hardware.get("applications")[ele_num]

pruneAppConfig()  #removes all the config files that arent on this thing, modify the hardware list in this_thing.json

def setPin(number,direction):
    if direction == "In":
        pin = machine.Pin(number, machine.Pin.IN, machine.Pin.PULL_UP)
    if direction == "Out":
        pin = machine.Pin(number, machine.Pin.OUT)
