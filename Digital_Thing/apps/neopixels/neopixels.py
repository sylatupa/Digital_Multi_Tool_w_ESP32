try:
    import machine, neopixel
except:
    pass
import time

global threshold, sr, x_val, l, sampleRate
def trigger(message=None):
    try:
        pass
        #print(">>>",__name__," success")

    except:
        pass
        #print(">>>",__name__)


def sample_rate(message=2/60):
    sampleRate = message


np = neopixel.NeoPixel(machine.Pin(23), 20)
def clear():
    for i in range(20):
        np[i] = (0,0,0)
        np.write()




clear_wait = 15

count = 0
def x(message):
    global count, clear_wait
    if count > clear_wait: 
        clear()
        count = 0
    else:
        count +=1

    if message > .75 and message < .99:
        for i in range(5,10):
            np[i] = (int(message*200),0,0)
    if message > .0 and message < .25:
        for i in range(15,20):
            np[i] = ( int(message*200),0,0)
    np.write()

def y(message):
    #    message = yChange(message)

    if message > .25 and message < .50:
        for i in range(10,15):
            np[i] = ( 0,0,int(message*200))
    if message > .75 and message < 1:
        for i in range(0,5):
            np[i] = ( 0,0,int(message*200))
 
    #np[int((message/255)*20)] = (message, message, message)
    np.write()

def z(message):
    #message = zChange(message)
    if message == 'up':
        pass
        #print("z ", message)
    elif message == 'down':
        pass
        #print("z ", message)
    #np[int((message/255)*20)] = (message, message, message)
    #np.write()

xhistory = [0]
yhistory = [0]
zhistory = [0]

def xChange(xval):
    xChange = xhistory[0] - xval
    xhistory[0] = xval
    print("xd:", xChange)
    if xChange > .3:
        return "left";
    elif xChange < -.3:
        return "right";
def yChange(yval):
    yChange = yhistory[0] - yval
    yhistory[0] = yval;
    print("yd:", yChange)
    if yChange > .035:
        return "forward";
    elif yChange < -.035:
        return "backward";

def zChange(zval):
    zChange = zhistory[0] - zval
    zhistory[0] = zval;
    print("zd:", zChange)
    if zChange > .25:
        return "up";
    elif zChange < -.25:
        return "down";





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

def fadeInOutWifi(count,pin):
    n = count
    #np = neopixel.NeoPixel(machine.Pin(pin), count)
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (0, 0, val)
        np.write()

def fadeInOutMQTT(count,pin):
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

if __name__=="__main__":
    fadeInOut(10,26)
