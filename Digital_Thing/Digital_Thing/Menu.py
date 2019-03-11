

import sys
class State(object):
    def __init__(self):
        print('Processing current state:', str(self))
    def on_event(self, event):
        pass
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self.__class__.__name__

class SimpleDevice(object):
    def __init__(self):
        self.state = hardware()
        #self.state = LockedState()
    def on_event(self, event):
        self.state = self.state.on_event(event)

'''
superclass for Menu, takes Digital_Thing object to get some fo the menu parameters
'''
class Menu(object):
    """
    On each call get the last keyboard press, and process that character through the state machine.
    """
    def __init__(self,dt):
        self.device = SimpleDevice()
        self.getch = _Getch()
        print(  "***************************************Welcome to the menu****************************************\n***************************************************************************************************")
        print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT   |   a: QUIT")
        self.menuDict = {"k":"up","j":"down","h":"left","l":"right","a":"quit"}
        self.indexHW = 0
        self.indexApp = 0
        self.dt = dt
        self.currentHWName = self.dt.this_thing.get("hardware")[0]
        self.currentAppName = self.dt.app_config.get(self.currentHWName).get('applications')[0]
        print(self.currentHWName, "  " ,self.device.state)
        self.maxHWIndex = len(self.dt.app_config.get(self.currentHWName))
        self.maxAppIndex =  len(self.dt.app_config.get(self.currentHWName).get('applications'))
        
    def menu_event(self):
        self.a = self.getch()
        self.dirctn = self.menuDict.get(self.a)
        self.device.on_event(self.dirctn)
        if self.dirctn == 'None':
            print('check')
            pass
        elif self.dirctn == 'quit':
            sys.exit()
        elif self.dirctn == 'left':
            if str(self.device.state) == 'hardware':
                self.indexHW = levelUp(self.indexHW, self.maxHWIndex)
                self.indexApp = 0
                self.currentHWName = self.dt.this_thing.get("hardware")[self.indexHW]
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]

            elif str(self.device.state) == 'applications':
                self.indexApp = levelUp(self.indexApp, self.maxAppIndex)
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
            self.prnt()
        elif self.dirctn == 'right':
            if str(self.device.state) == 'hardware':
                self.indexHW = levelDown(self.indexHW, self.maxHWIndex)
                self.currentHWName = self.dt.this_thing.get("hardware")[self.indexHW]
                self.indexApp = 0
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
            elif str(self.device.state) == 'applications':
                self.indexApp = levelUp(self.indexApp, self.maxAppIndex)
                self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
            self.prnt()
        elif self.dirctn == 'up':
            self.updateMaxIndex()
            self.currentAppName = self.dt.app_config.get(self.currentHWName).get("applications")[self.indexApp]
            self.prnt()
        elif self.dirctn == 'down':        
            self.updateMaxIndex()
            self.prnt()
    def updateMaxIndex(self):
        print("updating device state to",self.device.state)
        self.maxAppIndex = len(self.dt.app_config.get(self.currentHWName).get("applications"))
        self.maxHWIndex = len(self.dt.this_thing.get("hardware"))

    def prnt(self):
        print(self.device.state ," ", self.indexHW , " ", self.currentHWName, " " , " App Name", self.indexApp ," ", self.currentAppName ,":",self.dt.app_config.get(self.currentHWName).get("applications"))
class hardware(State):
    def __init__(self):
        super().__init__()
        print("in menu")
    def on_event(self, event):
        if event == 'up':
            print("up")
        elif event == 'down':
            print("down")
            return applications()

        elif event == 'left':
            print("left")
            #self.indexHW = levelUp(self.index, self.maxIndex)
            #self.currentHWName = self.dt.this_thing.get("hardware")[self.index]
            #print(self.maxIndex, " " ,self.index)
            #print(self.currentHWName, " " , self.device , " " ,self.currentHWName)
        elif event == 'right':
            print("right")
            #self.index = levelDown(self.index,self.maxIndex)
            #self.currentHWName = self.dt.this_thing.get("hardware")[self.index]
            #print(self.maxIndex, " " ,self.index, " HW: " ,self.currentHWName)

        return self
class applications(State):
    def __init__(self):
        super().__init__()
        print("in applications ")
    def on_event(self, event):
        if event == 'up':
            print("up")
            print("EXECUTE!")
        elif event == 'down':
            print("down")
            return hardware()
        elif event  == 'left':
            print("left")
            #self.index = levelUp(self.index, self.maxIndex)
            #self.currentAppName = self.dt.app_config.get(self.currentHWName]).get('applications')[self.index]
            #print(self.maxIndex, " " ,self.index)
            #print(self.currentAppName, "  " ,self.currentHWName)
        elif event == 'right':
            print("right")
            #self.index = levelDown(self.index,self.maxIndex)
            #self.currentAppName = self.dt.app_config.get(self.currentHWName]).get('applications')[self.index]
            #print(self.maxIndex, " " ,self.index, " HW: " ,self.currentHWName)
            #print(self.currentAppName, "  " ,self.currentHWName)
 
        return self

def levelUp(level,maxLevel):
    if level < maxLevel-1:
        return level + 1
    else: return 0
def levelDown(level, maxLevel):
    if level > 0:
        return level - 1
    else: return maxLevel

#from active state github repo, code recepies.
#this is a helper file that allows for keyboard interaction
#renaming from getch to keyboard
class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            print("importing getch unix")
            self.impl = _GetchUnix()
    def __call__(self): return self.impl()
class _GetchUnix:
    def __init__(self):
        import sys,select,termios,tty
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
    def __call__(self):
        import sys, tty, termios,select
        #fd = sys.stdin.fileno()
        #old_settings = termios.tcgetattr(fd)
        #try:
        if True:
            input = select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
            if input:
                value = sys.stdin.read(1)
                return value
        #except:
        #    pass
        #finally:
        #    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        #return ch
class _GetchWindows:
    def __init__(self):
        import msvcrt
    def __call__(self):
        #import msvcrt
        if msvcrt.kbhit(): # <--------
            key = msvcrt.getch()
            print("a to exit, current key: "+ key)
            if key == 'a':
                sys.exit()
            return key
class _GetchMacCarbon:
    """
    A function which returns the current ASCII key that is down;
    if no ASCII key is down, the null string is returned.  The
    page http://www.mactech.com/macintosh-c/chap02-1.html was
    very helpful in figuring out how to do this.
    """
    def __init__(self):
        import Carbon

    def __call__(self):
        import Carbon
        if Carbon.Evt.EventAvail(0x0008)[0]==0: # 0x0008 is the keyDownMask
            return ''
        else:
            (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            return chr(msg)

if __name__ == '__main__':
    menu = Menu()
    while True:
        menu.menu_event()
    
