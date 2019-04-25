# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
try:
    pass
except:
    print("Main Did not Run")
import network
import time
ssid = "spyprjct-219"
password = "789sumrX"
'''
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        for t in range(0, 120):
            if sta_if.isconnected() != True:
                print('Oh Yes! Get connected')
                time.sleep_ms(200)
                sta_if.active(True)
                sta_if.connect(ssid, pwd)
            else:
                break
'''
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()
'''
import machine
from network import WLAN
wlan = WLAN() # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(WLAN.STA)
    # configuration below MUST match your home router settings!!
    wlan.ifconfig(config=('192.168.178.107', '255.255.255.0', '192.168.178.1', '8.8.8.8'))

if not wlan.isconnected():
    wlan.connect('mywifi', auth=(WLAN.WPA2, 'mywifikey'), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting
print('network config:', sta_if.ifconfig())
'''

#import pyb
#pyb.main('main.py') # main script to run after this one
#pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
#pyb.usb_mode('CDC+HID') # act as a serial device and a mouse
'''
import machine
led = machine.Pin(, machine.Pin.OUT)

for i in range(10):
    print("led")
    led(1)
    time.sleep(0.5)
    led.(0)
    time.sleep(0.5)
'''
