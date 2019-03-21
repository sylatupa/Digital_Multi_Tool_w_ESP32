import sys
import getch
import pub_sub_local as pubsub
class Menu(object):
    """
    On each call get the last keyboard press, and process that character through the state machine.
    """
    def __init__(self,dt):
        self.getch = getch._Getch()  #TODO:esp32 convert
        print(  "************Welcome to the menu****************************************\n******************************************")
        print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT   |   a: QUIT")
        self.menuDict =     {"k":"up","j":"down","h":"left","l":"right","a":"quit"}
        self.indexHW        = 0
        self.indexApp       = 0
        self.indexPub       = 0
        self.indexSub       = 0
        self.dt             = dt
        self.currentHWName  = self.dt.this_thing.get("hardware")[0]
        self.currentAppName = self.dt.app_config.get(self.currentHWName).get('applications')[0]
        self.currentPubName = ''
        self.currentSubName = ''
        self.maxHWIndex     = len(self.dt.app_config.get(self.currentHWName))
        self.maxAppIndex    = len(self.dt.app_config.get(self.currentHWName).get('applications'))
        self.maxPubIndex    = 0
        self.maxSubIndex    = 0
        self.state          = "HW"
    def menu_event(self):
        self.a = self.getch()
        # self.a = "  #TODO:esp32 convert
        # self.dirctn = "" #TODO: esp32 convert 
        self.dirctn = self.menuDict.get(self.a)
        self.prnt()
        if self.state == 'application_on':
            pubsub.pub.dispatch(current,122)
            if self.dirctn == 'down':
                self.state = 'HW'
            elif self.dirctn == 'right':
                self.indexSub = levelDown(self.indexSub, self.maxSubIndex)
                self.currentSubName = "sub"
                self.currentPubName = "sub"
            elif self.dirctn == 'up':
                print(self.pubsub.pub.events)
                

        elif self.state == 'HW':
            '''HARDWARE STATE'''
            if self.dirctn == 'left':
                self.indexApp = 0
                self.indexHW = levelUp(self.indexHW, self.maxHWIndex)
                self.currentHWName = self.dt.this_thing.get("hardware")[self.indexHW]
                self.updateMaxIndex()
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
            elif self.dirctn == 'right':
                self.indexApp = 0
                self.indexHW = levelDown(self.indexHW, self.maxHWIndex)
                self.currentHWName = self.dt.this_thing.get("hardware")[self.indexHW]
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
            elif self.dirctn == 'up':
                self.state = "apps"
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
                self.updateMaxIndex()
            elif self.dirctn == 'down':
                print("lowest")
        elif self.state == 'apps':
            '''apps state'''
            if self.dirctn == 'left':
                self.indexApp = levelUp(self.indexApp, self.maxAppIndex)
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
            elif self.dirctn == 'right':
                self.indexApp = levelDown(self.indexApp, self.maxAppIndex)
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
            elif self.dirctn  == 'up':
                self.state = 'app'
            elif self.dirctn == 'down':
                self.state = 'HW'
                print("HW")
        elif self.state == 'app':
            if self.dirctn == 'up':
                self.state = 'exec'
                print("PRESS UP TO EXECUTE!")
            elif self.dirctn == 'down':
                self.state = 'apps'
                print("apps")
        elif self.state == 'exec':
            print("EXECUTE!")
            self.state = 'application_on'
            pubsub.setPubEvents(self.currentHWName,self.dt.app_config)
            pubsub.setSubRegisterFirstClassObject(self.currentHWName,self.currentAppName,self.dt.app_config)
            self.prnt()
        elif self.dirctn == 'quit':
            sys.exit()

        if type(self.dirctn)!=type(None):
            self.prnt()

    def updateMaxIndex(self):
        #print("updating device state to",self.device.state)
        self.maxAppIndex = len(self.dt.app_config.get(self.currentHWName).get("applications")) - 1
        self.maxHWIndex = len(self.dt.this_thing.get("hardware")) - 1

    def prnt(self):
        init(128*3,64*3) # initialize a 16x3 display#draw the three lines passed as a list
        #draw(["Hello","world", "Mock LCD !!!"])

        #draw([self.state])
        draw([self.state, ("HW:"+ str(self.indexHW)+"/"+str(self.maxHWIndex) +" "+ self.currentHWName),( "App:"+ str(self.indexApp)+"/"+str(self.maxAppIndex) +" "+ self.currentAppName )])
        #draw([self.state ," ", self.indexHW , " ", self.currentHWName, " " , " App Name", self.indexApp ," ", self.currentAppName ])


def levelUp(level,maxLevel):
    if level < maxLevel:
        return level + 1
    else: return 0
def levelDown(level, maxLevel):
    if level > 0:
        return level - 1
    else: return maxLevel

'''
class State(object):
    def __init__(self):
        print('Processing current state:', str(self))
    def on_event(self, event):
        pass
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self.__class__.__name__

class application_on(State):
    def __init__(self):
        #super().__init__()
        #pubsub.published_routes.append(
        print("in applications ")
    def on_event(self, event):
        if event == 'up':
            #pubsub.published_routes
            print("up")
            print("EXECUTE!")
        elif event == 'down':
            print("down")
            return applications()
        elif event  == 'left':
            print("left")
        elif event == 'right':
            print("right")
        return self

class applications(State):
    def __init__(self):
        #super().__init__()
        print("in applications ")
    def on_event(self, event):
        if event == 'up':
            print("up")
            print("EXECUTE!")
            return application_on()
        elif event == 'down':
            print("down")
            return hardware()
        elif event  == 'left':
            print("left")
        elif event == 'right':
            print("right")
        return self
class hardware(State):
    def __init__(self):
        #super().__init__()
        print("in menu")
    def on_event(self, event):
        if event == 'up':
            print("up")
        elif event == 'down':
            print("down")
            return applications()
        elif event == 'left':
            print("left")
        elif event == 'right':
            print("right")
        return self
class SimpleDevice(object):
    def __init__(self):
        pass
        #self.state = hardware()
        #self.state = LockedState()
    def on_event(self, event):
        self.state = self.state.on_event(event)
'''
#code attribution goes to PrashantMohta https://github.com/PrashantMohta/mlcd/blob/master/mlcd_example.py
import pygame
def init(chars,lines):
    global screen
    global myfont
    pygame.init()
    #size = [12*chars,20*lines]
    size = [chars,lines]
    screen= pygame.display.set_mode(size)
    pygame.display.set_caption("Mock LCD")
    myfont = pygame.font.SysFont("monospace", 20)


def draw(args):
    i=0;
    global screen
    global myfont
    screen.fill((0,0,0))#erase screen contents
    while(i<len(args)):
        line= myfont.render(args[i], 2, (255,255,0))
        screen.blit(line, (0, 20*i))
        i+=1
    pygame.display.flip()

if __name__ == '__main__':
    import Digital_Object as dt
    import sys
    import os
    pth = os.getcwd()
    sys.path.append(pth) #needed to import modules in same path
 
 
    menu = Menu(dt)
    while True:
        menu.menu_event()



