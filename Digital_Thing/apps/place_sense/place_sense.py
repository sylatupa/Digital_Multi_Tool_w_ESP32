'''
This place sense script 
collects a set of environmental data, using commonly avaialbe sensors.
Also, there is a function that aggregates and synthesizes the collected sensor values and makes a judgement of the quality of the place.

This is an assesment tool to determine the quality of a place, through computer sensing.

http://docs.micropython.org/en/latest/esp8266/tutorial/dht.html

'''

import sys
from machine import Pin, ADC 
import dht
print("place_sense was imported")
#G4 is an acceptible pin time
#xp.width(ADC.WIDTH_10BIT)

dhtP = dht.DHT11(Pin(32))
noiseP = ADC(Pin(35))
noiseP.atten(ADC.ATTN_11DB)
lightP = ADC(Pin(34))
motionP = Pin(25,mode=Pin.IN, pull=Pin.PULL_UP)

def light():
    return lightP.read()

def temp():
    tem = 0
    try:
        #dhtP.measure()
        tem = (dhtP.temperature() * (9/5)) + 32
    except Exception as e:
        print(e)
    return tem
def humidity():
    hum = 0
    try:
        dhtP.measure()
        hum = dhtP.humidity()
    except Exception as e:
        print(e)
    return hum
   
def motion():
    return motionP()

def noise():
    return noiseP.read()

def place_sense():
    return 9000


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
    if xvl > xmax:
        xmax = xvl
    elif xvl < xmin:
        xmin = xvl
    return ((xvl - xmin) / (xmax - xmin))


def yNorm(yvl):
    global ymax,ymin
    if yvl > ymax:
        ymax = yvl
    elif yvl < ymin:
        ymin = yvl
    return ((yvl - ymin) / (ymax - ymin))
def zNorm(zvl):
    global zmax,zmin
    if zvl > zmax:
        zmax = zvl
    elif zvl < zmin:
        zmin = zvl
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
