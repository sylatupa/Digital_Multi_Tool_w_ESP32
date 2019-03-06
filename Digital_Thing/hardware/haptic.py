import machine
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

def up():
    for i in range(500,1023):
        pwm12.freq(200)
        time.sleep(.3)
        pwm12.freq(200)

        pwm12.duty(500)  # max 1023 , 0 off           

