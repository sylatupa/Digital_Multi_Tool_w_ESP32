global xsize, ysize
xsize = 128*12
ysize = 64*12
def prnt(menuo,pubsubs):
    #for key,val in menuo.events.items(): print("{} = {}".format(key, type(val)))
    init(xsize,ysize) # initialize a 16x3 display#draw the three lines passed as a list
    fullPrint = []
    fullPrint.append(menuo.state + " " + str(menuo.prntDict.get(menuo.state))  )
    fullPrint.append( "App:"+ str(menuo.indexApp)+"/"+str(menuo.maxAppIndex) +" "+ menuo.currentAppName )

    for app_pbr in pubsubs.app_pbrs: 
        fullPrint.append(app_pbr+":")
        for event in pubsubs.app_pbrs.get(app_pbr).events:
            fullPrint.append("    " + str(event))
            for k,v in pubsubs.app_pbrs.get(app_pbr).events.items():
                #print('event : {}, sending messge {} to subscriber {} with callback {}'.format(event,gttsub.message,pub.subscriber.__name__,pub.callback.__name__))
                #print('event : {}, sending messge {} to subscriber {} with callback {}'.format(event,gttsub.message,pub.subscriber.__name__,pub.callback.__name__))
                #fullPrint.append('event : {}, sending messge {} to subscriber {} with callback {}'.format(event,gttsub.message,pub.subscriber.__name__,pub.callback.__name__))
                #fullPrint.append('subscriber {} with callbacks: '.format(k))
                callbacks = '    '
                for key in v.keys():
                    callbacks += str(key.__name__) + ', '        
                fullPrint.append('{}'.format(callbacks))
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
        #    str(str_array)
            
        #    ])
    draw(fullPrint)

#code attribution goes to PrashantMohta https://github.com/PrashantMohta/mlcd/blob/master/mlcd_example.py
try:
    import pygame
except:
    print('no pygame')
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
