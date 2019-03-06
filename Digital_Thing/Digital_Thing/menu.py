import sys
import os
#print(os.listdir())

#sys.path.append("hardware")
#import keyboard as getch 
'''
menu from keyboard
'''
global menu_level,up,down,left,right,getch
maxMenuCurser = 0
'''
menu_in_application = False
menuHardwareCurser = 0
menuApplicationCurser = 0
maxMenuHardwareCurser = 0
maxMenuApplicationCurser = 0
up = False
down = False
left = False
right = False
menu_level = "hardware"
print("Welcome to the menu,\n this is the available hardware:")
print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT")
print("a: EXIT")

global hardware,application
hardware = True
application = False

level = 0
'''



def init():
    global menu_level,up,down,left,right,getch
    getch = _Getch()
    maxMenuCurser = 0
    menu_in_application = False
    menuHardwareCurser = 0
    menuApplicationCurser = 0
    maxMenuHardwareCurser = 0
    maxMenuApplicationCurser = 0
    up = False
    down = False
    left = False
    right = False
    menu_level = "hardware"
    print("Welcome to the menu,\n this is the available hardware:")
    print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT")
    print("a: EXIT")

    global hardware,application
    hardware = True
    application = False

    level = 0

def levelUp(maxLevel):
    if level <= maxLevel:
        level = level + 1
        return level
    else:
        return level

def levelDown(maxLevel):
    if level <= maxLevel:
        level = level - 1
        return level
    else: return level

def checkKeyboard():
    a = getch()
def checkKeyboard():
    global menu_level , menuHardwareCurser,up,down,left,right,hardware,application
    a = getch()

'''
if hardware and a != None:
        if a == 'k':
            print('up, edit application')
            application = True
            hardware = False
            up = True
        if a == 'h':
            print('left')
            left = True
            if menuHardwareCurser > 0:
                menuHardwareCurser = menuHardwareCurser - 1
            else:
                menuHardwareCurser = maxMenuHardwareCurser - 1
        if a == 'l':
            print('right')
            right = True
            if menuHardwareCurser < maxMenuHardwareCurser - 1:
                menuHardwareCurser = menuHardwareCurser + 1
            else:
                menuHardwareCurser = 0
        if a == 'j':
            down = True
            print('down')
        a = None
    if application and a != None:
        if a == 'k':
            print('up')
            application = False
            hardware = True
        if a == 'h':
            print('left')
            if self.menuApplicationCurser > 0:
                self.menuApplicationCurser = self.menuApplicationCurser - 1
            else:
                print(self.maxMenuCurser)
                self.menuApplicationCurser = self.maxMenuCurser -1
        if a == 'l':
            print('right')
            if self.menuApplicationCurser < self.maxMenuCurser -1:
                self.menuApplicationCurser = self.menuApplicationCurser + 1
            else:
                self.menuApplicationCurser = 0
        if a == 'k':
            pass
        a = None
    if a == 'a':
        sys.exit()

'''

#from active state github repo, code recepies.
#this is a helper file that allows for keyboard interaction
#renaming from getch to keyboard
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
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
            #print("difSelect",str(select.select([sys.stdin], [], [], 0)[0]) , " " , select.select([sys.stdin], [], []), " ",select.select([sys.stdin],[],[])[1])
            input = select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
            #input = select.select([sys.stdin], [], [], 1)[0]
            #print("in:", input)
            if input:
                value = sys.stdin.read(1)
                #value = sys.stdin.readline().rstrip()
                return value
                #tty.setraw(sys.stdin.fileno())
                #if ch == 'a':
                #    sys.exit()
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

#getch = _Getch()


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
            #
            # The event contains the following info:
            # (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            #
            # The message (msg) contains the ASCII char which is
            # extracted with the 0x000000FF charCodeMask; this
            # number is converted to an ASCII character with chr() and
            # returned
            #
            (what,msg,when,where,mod)=Carbon.Evt.GetNextEvent(0x0008)[1]
            return chr(msg)

# StateMachine/stateMachine2/StateMachine.py
# A table-driven state machine

class StateMachine:
    def __init__(self, initialState, tranTable):
        self.state = initialState
        self.transitionTable = tranTable

    def nextState(self, input):
        print(map)
        print(state)
        #it=((list)map.get(state)).iterator()
        while(it.hasNext()):
            #Object[] tran = (Object[])it.next()
            tran = it.next()
            if(input == tran[0] or input.getClass() == tran[0]):
                if(tran[1] != null):
                    Condition c = (Condition)tran[1]
                    if(!c.condition(input))
                        continue # Failed test

                if(tran[2] != null)
                    ((Transition)tran[2]).transition(input)
                state = (State)tran[3]
                return


        throw RuntimeException(
          "Input not supported for current state")


# StateMachine/vendingmachine/VendingMachine.py
# Demonstrates use of StateMachine.py
import sys
#sys.path += ['../stateMachine2']
import StateMachine

class State:
    def __init__(self, name): self.name = name
    def __str__(self): return self.name

State.hardware = State("hardware")
State.application = State("application")
State.left = State("left")
State.right = State("right")
State.up = State("up")
State.down = State("down")

class HasChange:
    def __init__(self, name): self.name = name
    def __str__(self): return self.name

HasChange.yes = HasChange("Has change")
HasChange.no = HasChange("Cannot make change")

class ChangeAvailable(StateMachine):
    def __init__(self):
        StateMachine.__init__(State.makesChange, {
          # Current state, input
          (State.makesChange, HasChange.no) :
            # test, transition, next state:
            (null, null, State.noChange),
          (State.noChange, HasChange.yes) :
            (null, null, State.noChange)
        })

class Money:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(self): return self.name
    def getValue(self): return self.value

Money.quarter = Money("Quarter", 25)
Money.dollar = Money("Dollar", 100)

class Quit:
    def __str__(self): return "Quit"

Quit.quit = Quit()

class Digit:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(self): return self.name
    def getValue(self): return self.value

class FirstDigit(Digit): pass
FirstDigit.A = FirstDigit("A", 0)
FirstDigit.B = FirstDigit("B", 1)
FirstDigit.C = FirstDigit("C", 2)
FirstDigit.D = FirstDigit("D", 3)

class SecondDigit(Digit): pass
SecondDigit.one = SecondDigit("one", 0)
SecondDigit.two = SecondDigit("two", 1)
SecondDigit.three = SecondDigit("three", 2)
SecondDigit.four = SecondDigit("four", 3)

class ItemSlot:
    id = 0
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    def __str__(self): return `ItemSlot.id`
    def getPrice(self): return self.price
    def getQuantity(self): return self.quantity
    def decrQuantity(self): self.quantity -= 1

class VendingMachine(StateMachine):
    changeAvailable = ChangeAvailable()
    amount = 0
    FirstDigit first = null
    ItemSlot[][] items = ItemSlot[4][4]

    # Conditions:
    def notEnough(self, input):
        i1 = first.getValue()
        i2 = input.getValue()
        return items[i1][i2].getPrice() > amount

    def itemAvailable(self, input):
        i1 = first.getValue()
        i2 = input.getValue()
        return items[i1][i2].getQuantity() > 0

    def itemNotAvailable(self, input):
        return !itemAvailable.condition(input)
        #i1 = first.getValue()
        #i2 = input.getValue()
        #return items[i1][i2].getQuantity() == 0

    # Transitions:
    def clearSelection(self, input):
        i1 = first.getValue()
        i2 = input.getValue()
        ItemSlot is = items[i1][i2]
        print (
          "Clearing selection: item " + is +
          " costs " + is.getPrice() +
          " and has quantity " + is.getQuantity())
        first = null

    def dispense(self, input):
        i1 = first.getValue()
        i2 = input.getValue()
        ItemSlot is = items[i1][i2]
        print(("Dispensing item " +
          is + " costs " + is.getPrice() +
          " and has quantity " + is.getQuantity()))
        items[i1][i2].decrQuantity()
        print ("Quantity " +
          is.getQuantity())
        amount -= is.getPrice()
        print("Amount remaining " +
          amount)

    def showTotal(self, input):
        amount += ((Money)input).getValue()
        print("Total amount = " + amount)

    def returnChange(self, input):
        print("Returning " + amount)
        amount = 0

    def showDigit(self, input):
        first = (FirstDigit)input
        print("First Digit= "+ first)

    def __init__(self):
        StateMachine.__init__(self, State.quiescent)
        for(int i = 0 i < items.length i++)
            for(int j = 0 j < items[i].length j++)
                items[i][j] = ItemSlot((j+1)*25, 5)
        items[3][0] = ItemSlot(25, 0)
        buildTable(Object[][][]{
         ::State.quiescent, 
            # Input, test, transition, next state:
           :Money.class, null,
             showTotal, State.collecting,
         ::State.collecting, # Current state
            # Input, test, transition, next state:
           :Quit.quit, null, returnChange, State.quiescent,
           :Money.class, null, showTotal, State.collecting,
           :FirstDigit.class, null,
             showDigit, State.selecting,
         ::State.selecting, # Current state
            # Input, test, transition, next state:
           :Quit.quit, null,
             returnChange, State.quiescent,
           :SecondDigit.class, notEnough,
             clearSelection, State.collecting,
           :SecondDigit.class, itemNotAvailable,
             clearSelection, State.unavailable,
           :SecondDigit.class, itemAvailable,
             dispense, State.wantMore,
         ::State.unavailable, # Current state
            # Input, test, transition, next state:
           :Quit.quit, null,
             returnChange, State.quiescent,
           :FirstDigit.class, null,
             showDigit, State.selecting,
         ::State.wantMore, # Current state
            # Input, test, transition, next state:
           :Quit.quit, null,
             returnChange, State.quiescent,
           :FirstDigit.class, null,
             showDigit, State.selecting,
        )


if __name__ == '__main__':
    import time
    import sys
    init()
    while True:
        checkKeyboard()
        
        time.sleep(1)
