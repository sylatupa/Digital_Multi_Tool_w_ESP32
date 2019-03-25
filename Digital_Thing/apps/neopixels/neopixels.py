try:
    import machine, neopixel
except:
    pass
import time

global threshold, sr, x_val, l, sampleRate
def trigger(message=None):
    try:
        print(">>>",__name__," success")

    except:
        print(">>>",__name__)


def sample_rate(message=2/60):
    sampleRate = message
np = neopixel.NeoPixel(machine.Pin(23), 20)
def clear():
    for i in range(20):
        np[i] = (0,0,0)
        np.write()

def x(message):
    clear()
    if message == 'left':
        print("neo, ", message)

    elif message == 'right':

        print("neo, ", message)

    #np[int((message/255)*20)] = (message, message, message)
    np.write()

def y(message):
    np[int((message/255)*20)] = (message, message, message)
    np.write()
    print("neo, ", message)

def z(message):
    np[int((message/255)*20)] = (message, message, message)
    np.write()
    print("neo, ", message)
    
def length(message):
    l = message

def cycle(count,pin):
    n = count
    np = neopixel.NeoPixel(machine.Pin(pin), count)
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)
        np.write()

def bounce(count,pin):
    n = count
    np = neopixel.NeoPixel(machine.Pin(pin), count)
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
    np = neopixel.NeoPixel(machine.Pin(pin), count)
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
