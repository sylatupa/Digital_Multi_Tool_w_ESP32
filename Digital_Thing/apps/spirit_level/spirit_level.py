global x,y,x,trigger,sr,threshold
import random as r

import machine
import sys
import utime


#INTO GS a * 1.6 / 32.0


print("spirt modulee was imported")
def x():
    try:
        xv = xChange(xp.read())
        #xv = int((xp.read()/ 1024) * 255)
    except Exception as e:
        print(e)
        xv = 'none' #r.random()
    return xv


def y():
    try:
        yv = yChange(yp.read()) #int((yp.read()/ 1024) * 255)
    except:
        yv = 'none' #r.random()
    return yv

def z(): 
    try:
        zv = zChange(zp.read()) #int((zp.read()/ 1024) * 255)
    except:
        z = 'none' # r.random()
    return zv
def trigger():
    return True 

def sample_rate(message):
    print('$$$new sample rate', message)
    sr = message
def trigger_threshold(message):
    threshold = message
    print ('$$$spirit level threshold change to: ',threshold)

#adc = machine.ADC(adc_pin)
#try:
if True:
    from machine import Pin, ADC 
    xp = ADC(Pin(34))
    #xp.width(ADC.WIDTH_10BIT)
    #xp.atten(ADC.ATTN_11DB)
    yp = ADC(Pin(35))
    #yp.width(ADC.WIDTH_10BIT)
    #yp.atten(ADC.ATTN_11DB)
    zp = ADC(Pin(32))
    #zp.width(ADC.WIDTH_10BIT)
    #zp.atten(ADC.ATTN_11DB)



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
