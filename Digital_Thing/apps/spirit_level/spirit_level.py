global x,y,x,trigger,sr,threshold
import random as r
import machine
import sys
import time
nn = 20  #number of neopixels
import neopixel
import random
global threshold, sr, x_val, l, sampleRate
from machine import Pin, Timer

p12 = machine.Pin(19) #HAPTIC 
pwm12 = machine.PWM(p12)
pwm12.duty(0)  # max 1023 , 0 off

# set up pin PWM timer for output to buzzer or speaker
p = Pin(14)   #BUZZER
pw = machine.PWM(p)
pw.duty(0)

if True:
    from machine import Pin, ADC 
    pin = machine.Pin(16, Pin.OUT)
    pin.value(1)
    xp = ADC(Pin(32))
    xp.width(ADC.WIDTH_10BIT)
    xp.atten(ADC.ATTN_11DB)
    yp = ADC(Pin(35))
    yp.width(ADC.WIDTH_10BIT)
    yp.atten(ADC.ATTN_11DB)
    zp = ADC(Pin(34))
    zp.width(ADC.WIDTH_10BIT)
    zp.atten(ADC.ATTN_11DB)


def x():
    xv = 0
    xv = xp.read()
    xv = xNorm(xv)
    xv = xSmooth(xv)
    xchange = xChange(xv)
    #haptic(xv,xchange)
    #notes(xv,xchange)
    xNeo(xv,xchange)
    return xv

def y():
    yv = 0
    yv = yp.read()
    yv = yNorm(yv)
    yv = ySmooth(yv)
    yNeo(yv)
    return yv 

def z(): 
    zv = 0
    zv = zp.read()
    zv = zNorm(zv)
    zv = zSmooth(zv)
    return zv
xhist = []
yhist = []
zhist = []
smth_val = 10

xmax = 333
xmin = 0
ymax = 1
ymin = 331
zmax = 333
zmin = 331

xnormed = 1
ynormed = 1
znormed = 1 

norm_xmax = 1 
norm_xmin = 0
norm_ymax = 1
norm_ymin = 0
norm_zmax = 1
norm_zmin = 0

def xNorm(xvl):
    global xmax,xmin,norm_xmax,norm_xmin,xnormed
    if xvl > xmax:
        xmax = xvl
    elif xvl < xmin:
        print("NEW X MIN!")
        xmin = xvl
    xnormed = ((xvl - xmin) / (xmax - xmin))
    if xnormed > norm_xmax:
        norm_xmax = xnormed
    elif xnormed < norm_xmin:
        norm_xmin = xnormed
    return xnormed



def yNorm(yvl):
    global ymax,ymin,norm_ymax,norm_ymin,ynormed
    if yvl > ymax:
        ymax = yvl
    elif yvl < ymin:
        ymin = yvl
    ynormed = ((yvl - ymin) / (ymax - ymin))
    if ynormed > norm_ymax:
        norm_ymax = ynormed
    elif ynormed < norm_ymin:
        norm_ymin = ynormed
    return ynormed

def zNorm(zvl):
    global zmax,zmin,norm_zmax,norm_zmin,znormed
    if zvl > zmax:
        zmax = zvl
    elif zvl < zmin:
        zmin = zvl
    znormed = ((zvl - zmin) / (zmax - zmin))
    if znormed > norm_zmax:
        norm_zmax = znormed
    elif znormed < norm_zmin:
        norm_zmin = znormed
    return znormed

def xSmooth(x):
    if len(xhist)< smth_val:
        xhist.append(x)
    else:
        xhist.pop(0)
        xhist.append(x)
    return float(sum(xhist))/(len(xhist)+1)

def ySmooth(y):
    if len(yhist)< smth_val:
        yhist.append(y)
    else:
        yhist.pop(0)
        yhist.append(y)
    return float(sum(yhist))/(len(yhist)+1)

def zSmooth(z):
    if len(zhist)< smth_val:
        zhist.append(z)
    else:
        zhist.pop(0)
        zhist.append(z)
    return float(sum(zhist))/(len(zhist)+1)



#except Exception as e:
#    print(e)
#    print("spirit_level failed because not on esp32")

xhistory = []
yhistory = []
zhistory = []

def xChange(xval):
    xchange = xhistory[0] - xval
    xhistory[0] = xval
    return xchange
def yChange(yval):
    ychange = yhistory[0] - yval
    yhistory[0] = yval

def zChange(zval):
    zChange = zhistory[0] - zval
    zhistory[0] = zval

np = neopixel.NeoPixel(machine.Pin(23), 20)
def clear():
    for i in range(20):
        np[i] = (0,0,0)
        np.write()
    np.write()

clear_wait = 5

#Right is 0 to 3 and 17 to 20
#Front is 4 
#Left is 5 to 13
#15 an 15
count = 0


def xNeo(message,xchange):
    global count, clear_wait
    if count > clear_wait: 
        clear()
        count = 0
    else:
        count +=1
    rr = random.randint(0,1)
    gr = random.randint(0,1)
    br = random.randint(0,1)
    np[int(20*message)] = (int(message*255*rr), int(message*255*gr), int(message*255*br))
    np.write()



def yNeo(message):
    global count, clear_wait
    if count > clear_wait: 
        clear()
        count = 0
    else:
        count +=1


def xNeo1(message,xchange):
    global count, clear_wait
    if count > clear_wait: 
        clear()
        count = 0
    else:
        count +=1
    print(message, ' xmin:' , xmin, ' xmax:' , xmax)
    if message < norm_xmin *1.8:
        for i in range(5,13):
            np[i] = (int(message*200),int(message*200),int(message*200))
    if message > norm_xmax*.8:
        for i in range(0,3):
            np[i] = (int(message*200),int(message*200),int(message*200))
        for i in range(17,20):
            np[i] = (int(message*200),int(message*200),int(message*200))
    np.write()
def yNeo1(message):
    global count, clear_wait
    if count > clear_wait: 
        clear()
        count = 0
    else:
        count +=1

    if message < norm_ymin*1.8:
        for i in range(15,15):
            np[i] = (int(message*200),int(message*200),int(message*200))
    if message > norm_ymax*.8:
        for i in range(4,4):
            np[i] = (int(message*200),int(message*200),int(message*200))
    np.write()




xhistory = [0]
yhistory = [0]
zhistory = [0]


clear_wait = 10
clear_waitn = 0
def x_direction(count,pin,value):
    if clear_waitn > clear_wait:
        clear()
        clear_waitn = 0
    else:
        clear_waitn += 1
    for i in range(0,5):
        np[i % n] = (value * 255, value * 255, value * 255)
        np.write()
def y_direction(count,pin,value):
    if clear_waitn > clear_wait:
        clear()
        clear_waitn = 0
    else:
        clear_waitn += 1
    for i in range(0,5):
        np[i % n] = (value * 255, value * 255, value * 255)
        np.write()


def length(message):
    l = message

def cycle(count,pin):
    n = count
    #np = neopixel.NeoPixel(machine.Pin(pin), count)
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)
        np.write()

def bounce(count,pin):
    n = count
    #np = neopixel.NeoPixel(machine.Pin(pin), count)
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

def fadeInOut(count,pin):
    n = count
    #np = neopixel.NeoPixel(machine.Pin(pin), count)
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

temp_message = 0
def haptic(message,xchange):
    global temp_message 
    #pwm12.duty(int(500*message))  # max 1023 , 0 off                       
    if xchange > .05:
        pwm12.duty(int(message*900))  
        pwm12.freq(int(message*1023))  
        temp_message = message 
    else:
        pwm12.duty(0)
    '''
    else:
        if temp_message - .08 <= 0:
            print("zero haptic")
            pwm12.duty(0)  
        else:
            print("no temp")
            temp_message = temp_message - .08
            pwm12.duty(int(temp_message*900))  
            pwm12.freq(int(temp_message*1023))  
    '''
def notes(message,xchange):
    global temp_message
    if xchange > .02:
        pw.duty(int(message*900))  
        pw.freq(int(message*1023))  
        temp_message = message 
    else:
        pw.duty(0)
    '''
    else:
        if temp_message - .08 <= 0:
            pw.duty(0)  
        else:
            pw.duty(int(temp_message*900))  
            pw.freq(int(temp_message*1023))  
    '''
