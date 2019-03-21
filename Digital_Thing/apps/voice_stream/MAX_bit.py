'''
https://www.hackster.io/julianfschroeter/esp32-voice-streamer-52bd7e
https://www.thomaschristlieb.de/morsecode-entschluesseln-mit-micropython/#more-920
https://docs.pycom.io/firmwareapi/pycom/machine/adc.html
'''
import network
import usocket as socket
import ssl
import sys
import machine
import time
import array
from machine import Timer

adc = getADC()
bufferPointer = 0
max_value_in = 3825 #maybe higer like 4095
max_value_out= 255
factor = max_value_in / max_value_out
adjust = -44
buffsize = 800
loop = range(buffsize) #optimized
buf = array.array('H',loop)  #an unsignted integer array
adc = getMachineADC()
sendIt = False
pin = 35
def setPin(number):
    pin = number

def getMachineADC():
    import machine
    p = machine.Pin(pin)
    adc = machine.ADC(p)
    adc.atten(adc.ATTN_0DB) #11DB attnuation may allow for voltages over 1.1 upt 3.3v #adc.atten(adc.ATTN_6DB) #adc.width(adc.WIDTH_9BIT)
    adc.width(adc.WIDTH_12BIT)
    return adc.read

def getADCRead():
    val = adc()
    val
    bp = bp + 1
    buf[bp] = min(max(int(rd()/factor) + adjust, 0), 255)
    print(buf[bp])
    if buffsize == bp:
        bp == 0
        sendIt = True

def startTimer():
    timer = Timer(0, mode=Timer.PERIODIC, width=32)
    timer_a = timer.channel(Timer.A,freq=80)
    timer_a.irq(hanler=onTime(),trigger=Timer.TIMEOUT)
    #timer = timerBegin(0, 80, true); // 80 Prescaler
    #timerAttachInterrupt(timer, &onTimer, true); // binds the handling function to our timer 
    #timerAlarmWrite(timer, 125, true);
    #timerAlarmEnable(timer);

def run():
    while True:
        getADCRead()
        print("cool")
        time.sleep(2)
        print("woah")
        time.sleep(2)
        if sendIt:
            socket.write(buf,len(buf))


if __name__=="__main__":
    print("main")
    import sys
    sys.path.append("../network")
    sys.path.append("../")
    import network.wifi_adptr as wfi
    import network.socket_adptr as sckt
    wifi.do_connect("spyprjct-219","789sumrX")
    sckt.get_socket("192.168.1.115","4444")           #socket of computer to send to, and port number
    setPin(35)
    startTimer()
    run()



    sckt.close_socket(sckt)
