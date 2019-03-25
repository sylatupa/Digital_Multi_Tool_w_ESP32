global xsize, ysize
try:
    import pygame
except:
    print('no pygame')


xsize = 128*12
ysize = 64*12
try:
    import machine
    import libs.ssd1306 as ssd1306 
    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    oled.fill(0) 
    oled.text('MicroPython on', 0, 0)
    oled.text('an ESP32 with an', 0, 10)
    oled.text('attached SSD1306', 0, 20)
    oled.text('OLED display', 0, 30)
    oled.show()
except Exception as e:
    print(e)

prntDict = {"apps":"<|----APPS----|>","app":"<> ^-EXEC v-BACK"}
vowels = ('a', 'e', 'i', 'o', 'u')
def rmVwl(strng):
    return ''.join([l for l in strng if l not in vowels])

def prnt(menuo,pubsubs):
    #for key,val in menuo.events.items(): print("{} = {}".format(key, type(val)))
    fullPrint = []
    fullPrint.append(str(prntDict.get(menuo.state))  )
    fullPrint.append( str(menuo.indexApp)+"/"+str(menuo.maxAppIndex) +" "+ rmVwl(menuo.currentAppName) )

    for app_pbr in pubsubs.app_pbrs: 
        fullPrint.append(app_pbr+":")
        for event in pubsubs.app_pbrs.get(app_pbr).events:
            for k,v in pubsubs.app_pbrs.get(app_pbr).events.items():
                callbacks = '    '
                for key in v.keys():
                    callbacks += str(key) + ', '        
                    #callbacks += str(key.__name__.split('.')[2]) + ', '        
            #fullPrint.append("-" + str((event)) + " " + (callbacks))
            fullPrint.append("-" + str(rmVwl(event)) + " " + rmVwl(callbacks))
        #fullPrint +=pubs
        str_array = ""
        '''
        length = xsize /20
        for x in pubs:
            
            str_array +="--"
            for c in x:
                if len(str_array)<length:
                    str_array+=c
                else:
                    str_array+=c
                    fullPrint.append(str_array)
                    str_array=''
            str_array +=" --"
        fullPrint += str_array
        '''
        #draw([(menuo.state + " " + str(menuo.prntDict.get(menuo.state))  ),
        #    ( "App:"+ str(menuo.indexApp)+"/"+str(menuo.maxAppIndex) +" "+ menuo.currentAppName ),
        #    str(str_array
            
        #    ])
    try:
        print(fullPrint)
    except:
        pass
    try:
        draw(fullPrint)
    except Exception as e:
        print(e)
        pass
    try:
        drawOled(fullPrint)
    except:
        pass

prnt_data_dict= dict()

def prnt_data(app_event,m):
    prnt_data_dict[app_event] = m
    for key,val in prnt_data_dict.items():
        oled.text(ket, 0, n*10)
        oled.show()

def drawOled(fullPrint):
    oled.fill(0) 
    for n in range(0,len(fullPrint)):
        oled.text(fullPrint[n], 0, n*10)
        oled.show()


#code attribution goes to PrashantMohta https://github.com/PrashantMohta/mlcd/blob/master/mlcd_example.py
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
    try:
        screen.fill((0,0,0))#erase screen contents
        while(i<len(args)):
            line= myfont.render(args[i], 2, (255,255,0))
            screen.blit(line, (0, 20*i))
            i+=1
        pygame.display.flip()
    except Exception as e:
        print(e)

try:
    init(xsize,ysize) # initialize a 16x3 display#draw the three lines passed as a list
except Exception as e:
    print(e)
    print("no pygame")


