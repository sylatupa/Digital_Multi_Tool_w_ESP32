from machine import Pin, TouchPad

class touchpins:

    anyactive = False
    touch1 = False
    touch2 = False
    touch3 = False
    touch4 = False
    def __init__(t1=12,t2=13,t3=14,t4=15):
        tp1 = TouchPad(Pin(t1))
        tp2 = TouchPad(Pin(t2))
        tp3 = TouchPad(Pin(t3))
        tp4 = TouchPad(Pin(t4))
        sens = 444
        tp1.config(sens)
        tp2.config(sens)
        tp3.config(sens)
        tp4.config(sens)
        
    def detect():
        if tp1.read():
            touch1 = True
            anyactive = True
        
        if tp2.read():
            touch2 = True
            anyactive = True
            
        if tp3.read():
            touch3 = True
            anyactive = True
        
        if t4.read():
            touch4 = True
            anyactive = True

'''
    touch0 = TouchPad(Pin(4))
    touch1 = TouchPad(Pin(0))
    touch2 = TouchPad(Pin(2))
    touch3 = TouchPad(Pin(15))
    touch4 = TouchPad(Pin(13))
    touch5 = TouchPad(Pin(12))
    touch6 = TouchPad(Pin(14))
    touch7 = TouchPad(Pin(27))
    touch8 = TouchPad(Pin(33))
    touch9 = TouchPad(Pin(32))
    touch0.config(600)  # I think 0 is default sensitivity and higher is less sensitive
    touch0.read()
'''
