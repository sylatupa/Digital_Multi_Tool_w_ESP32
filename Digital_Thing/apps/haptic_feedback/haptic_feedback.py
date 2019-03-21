try:
    import machine
except:
    pass

global threshold, sr, x_val, l, sampleRate
def trigger_threshold(message=444):
    threshold = message
def sample_rate(message=2/60):
    sampleRate = message
def x(message):
    x_val = message
def trigger(message=None):
    try:
        p12 = machine.Pin(4)
        pwm12 = machine.PWM(p12)
        pwm12.duty(0)  # max 1023 , 0 off
        pwm12.freq(400)
        import time
        for i in range(444,1023):
            pwm12.duty('a'+ i)  # max 1023 , 0 off                                                                     
            time.sleep(.01)
            pwm12.duty(200)  # max 1023 , 0 off                                                                     
            print(i)

        pwm12.duty(0)
    except:
        print("____________Haptic feedback triggerd------",__name__)
def hall(message=None):
    print("hall from haptics")
    try:
        p12 = machine.Pin(4)
        pwm12 = machine.PWM(p12)
        pwm12.duty(0)  # max 1023 , 0 off
        pwm12.freq(400)
        import time
        for i in range(444,1023):
            pwm12.duty('a'+ i)  # max 1023 , 0 off                                                                     
            time.sleep(.01)
            pwm12.duty(200)  # max 1023 , 0 off                                                                     
            print(i)

        pwm12.duty(0)
    except:
        print("____________Haptic feedback triggerd------",__name__)


def up():
    for i in range(500,1023):
        pwm12.freq(200)
        time.sleep(.3)
        pwm12.freq(200)

        pwm12.duty(500)  # max 1023 , 0 off           

