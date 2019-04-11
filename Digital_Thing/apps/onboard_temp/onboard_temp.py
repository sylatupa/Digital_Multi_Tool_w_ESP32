try:
    import esp32
except:
    pass

rate = 10
thresh_above = 100
thresh_below = 100

def sample_rate(msg):
    rate = msg

def threshold_above(msg):
    thresh_above = msg

def threshold_below(msg):
    thresh_below = msg

def temp():
    #esp32.temperature()
    return esp32.raw_temperature()
