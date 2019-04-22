# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
try:
    import main
    #main.Run()
except:
    print("Main Did not Run")

#import pyb
#pyb.main('main.py') # main script to run after this one
#pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
#pyb.usb_mode('CDC+HID') # act as a serial device and a mouse
#led = machine.Pin(16, machine.Pin.OUT)
#for i in range(10):
#    print("led")
#    led(1)
#    time.sleep(0.5)
#    led.(0)
#    time.sleep(0.5)
