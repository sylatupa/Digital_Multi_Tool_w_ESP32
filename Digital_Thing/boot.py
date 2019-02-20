# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import Digital_Thing.Digital_Object as do
do.Digital_Config(False)

import machine

led = machine.Pin(16, machine.Pin.OUT)
for i in range(10):
    print("led")
    led(1)
    time.sleep(0.5)
    led.(0)
    time.sleep(0.5)
