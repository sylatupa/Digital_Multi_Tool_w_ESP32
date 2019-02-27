import time
import machine, neopixel

global threshold, sr, x_val, l
def trigger_threshold(message):
    threshold = message

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
    fadeInOut(10,26)
