import hardware.keyboard as getch #external library that grabs a character from keyobard
'''
menu from keyboard
'''
global menu_level,up,down,left,right
getch = getch._Getch()
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
def checkKeyboard():
    global menu_level , menuHardwareCurser,up,down,left,right,hardware,application
    a = getch()

    if hardware:
        if a == 'k':
            print('up')
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

    if application:
        if a == 'k':
            print('up')
            print('down')
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

    if a == 'a':
        sys.exit()
