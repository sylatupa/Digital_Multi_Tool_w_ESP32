global x,y,x,trigger,sr,threshold
print("spirt modulee was imported")
def x():
    try:
        x = accel.x()
    except:
        x = 666
    return x

def x(m):
    x = m
    print("$$$new accel x: ",x)

def y():
    print("$$$new accel y ")
    try:
        y = accel.y()
    except:
        y = 666
    return y

def z():
    try:
        z = accel.z()
    except:
        z = 666
    return z
def trigger():
    return True 

def sample_rate(message):
    print('$$$new sample rate', message)
    sr = message
def trigger_threshold(message):
    threshold = message
    print ('$$$spirit level threshold change to: ',threshold)

try:
    accel = pyb.Accel()
    SENSITIVITY = 3
    y = accel.y()
except:
    print("spirit_level failed because not on esp32")