try:
    import machine, neopixel
except:
    pass
import time

global threshold, sr, x_val, l, sampleRate
def trigger(message=None):
    try:
        print("_______________NeoPixels triggerd------",__name__)

    except:
        print("NeoPixels triggerd------",__name__)


def sample_rate(message=2/60):
    sampleRate = message

def x(message):
    x_val = message

def length(message):
    l = message

def clear(count,pin):
    n = count
    np = neopixel.NeoPixel(machine.Pin(pin), count)
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

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
    pass    
#count, pin    
ps = [[20,26]]
#ps = [[5,25],[20,26],[4,27],[20,33]]
l = 4
def lightOn():
    while True:
        for strip in ps:
            key = strip[0]
            val = strip[1]
            clear(key,val)
            cycle(key,val)
            fadeInOut(key,val)
            bounce(key,val)
