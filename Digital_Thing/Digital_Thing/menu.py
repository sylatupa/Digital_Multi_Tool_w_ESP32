import hardware.keyboard as getch #external library that grabs a character from keyobard
'''
menu from keyboard
'''
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
global menu_level
menu_level = "hardware"
print("Welcome to the menu,\n this is the available hardware:")
print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT")
print("a: EXIT")

def checkKeyboard():
    up = False
    down = False
    left = False
    right = False
    global menu_level , menuHardwareCurser
    a = getch()
    print(menu_level)
    if menu_level == 'hardware':
        if a == 'k':
            print('up')
            menu_level = "application"
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

    elif menu_level == 'application':
        if a == 'k':
            print('up')
            menu_level = ""
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
            print('down')
    if a == 'a':
        sys.exit()
