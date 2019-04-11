global x,y,x,trigger,sr,threshold
import random as r
import machine
import sys
#import utime
print("spirt modulee was imported")
nn = 2


def x():
    xv = 0
    xvp = 0
    #try:
    #for n in range(0,nn):
    #    xv = xp.read()
    #    #xv += xv - xvp
    #xv = xv/ nn
    #xvp = xv
    xv = xp.read()
    #xv = xSmooth(xv)
    #xv = xNorm(xv) 
    
    '''
    except Exception as e:
        print(e)
        xv = 'none' #r.random()
    '''
    return xv


def y():
    yv = 0
    yvp = 0
    try:
        #for n in range(0,nn):
        #    yv = yp.read()
        #    #yv += yv - yvp
        #yv = yv/ (nn)
        #yvp = yv
        yv = yp.read()
        #yv = ySmooth(yv)
        #yv = xNorm(yv)
 
    except Exception as e:
        print(e)
        yv = 'none' #r.random()
    return yv 

def z(): 
    zv = 0
    zvp = 0
    try:
        #for n in range(0,nn):
        #    #zv += zv - zvp
        #zv = zv / (nn)
        #zvp = zv
        zv = zp.read()
        #zv = zSmooth(zv)
        #zv = xNorm(zv)
    except:
        zv = 'none' # r.random()
    return zv
def trigger():
    return True 

def sample_rate(message):
    print('$$$new sample rate', message)
    sr = message
def trigger_threshold(message):
    threshold = message
    print ('$$$spirit level threshold change to: ',threshold)


#except Exception as e:
#    print(e)
#    print("spirit_level failed because not on esp32")
xhist = []
yhist = []
zhist = []
smth_val = 20 



xmax =  100
xmin = 0
ymax = 400
ymin = 0
zmax = 400
zmin = 0
def xNorm(xvl):
    global xmax,xmin
    #if xvl > xmax:
    #    xmax = xvl
    #elif xvl < xmin:
    #    xmin = xvl
    return ((xvl - xmin) / (xmax - xmin))


def yNorm(yvl):
    global ymax,ymin
    #if yvl > ymax:
    #    ymax = yvl
    #elif yvl < ymin:
    #    ymin = yvl
    return ((yvl - ymin) / (ymax - ymin))
def zNorm(zvl):
    global zmax,zmin
    #if zvl > zmax:
    #    zmax = zvl
    #elif zvl < zmin:
    #    zmin = zvl
    return ((zvl - zmin) / (zmax - zmin))




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


if True:
    from machine import Pin, ADC 
    pin = machine.Pin(16, Pin.OUT)
    pin.value(1)
    xp = ADC(Pin(34))
    xp.width(ADC.WIDTH_10BIT)
    xp.atten(ADC.ATTN_11DB)
    yp = ADC(Pin(32))
    yp.width(ADC.WIDTH_10BIT)
    yp.atten(ADC.ATTN_11DB)
    zp = ADC(Pin(35))
    zp.width(ADC.WIDTH_10BIT)
    zp.atten(ADC.ATTN_11DB)



#except Exception as e:
#    print(e)
#    print("spirit_level failed because not on esp32")

xhistory = []
yhistory = []
zhistory = []

def xChange(xval):
    xChange = xhistory[0] - xval
    xhistory[0] = xval;
    if xChange > 2:
        return "left";
    elif xChange < -2:
        return "right";
def yChange(yval):
    yChange = yhistory[0] - yval
    yhistory[0] = yval;
    if yChange > 2:
        return "forward";
    elif yChange < -2:
        return "backward";

def zChange(zval):
    zChange = zhistory[0] - zval
    zhistory[0] = zval;
    if zChange > 2:
        return "up";
    elif zChange < -2:
        return "down";
