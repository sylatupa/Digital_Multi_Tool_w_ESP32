global x,y,x,trigger,sr,threshold

def x():
    try:
        x = accel.x()
    except:
        x = 666
    return x

def y():
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
    sr = message
def trigger_threshold(message):
    threshold = message

try:
    accel = pyb.Accel()
    SENSITIVITY = 3
    y = accel.y()
except:
    print("spirit_level failed")
