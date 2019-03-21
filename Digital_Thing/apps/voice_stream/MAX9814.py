'''
https://www.hackster.io/julianfschroeter/esp32-voice-streamer-52bd7e
https://www.thomaschristlieb.de/morsecode-entschluesseln-mit-micropython/#more-920
https://docs.pycom.io/firmwareapi/pycom/machine/adc.html
'''
'''
def run(client):
    while True:
       val = read_mic()
        print(val)
        client.write(val,sizeof(val))
        time.sleep(0.1)
'''
def con():
    import network
    import usocket as socket
    import ssl
    import sys
    import machine
    import time
    import array
    p = machine.Pin(35)
    adc = machine.ADC(p)
    adc.atten(adc.ATTN_11DB) #11DB attnuation may allow for voltages over 1.1 upt 3.3v
    ssid     = "spyprjct-219"
    password = "789sumrX"
    host     = "192.168.1.115"
    transmitNow = False 
    max_value_in = 3825 #maybe higer like 4095
    max_value_out= 255
    factor = max_value_in / max_value_out
    adjust = -44
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid,password)
    time.sleep(1.5)
    print("connected: " ,station.isconnected())
    #print(station.ifconfig())
    #print("hello")
    #print(dir(socket))
    ai = socket.getaddrinfo(host,4444)
    socket = socket.socket()
    #print(dir(socket))
    print("connecting socket")
    socket.connect(ai[0][-1])
    print("connecting socket")
    #s = ssl.wrap_socket(socket)
    print("connecting socket")
    #import pyb
    from machine import Timer

    #tim = pyb.Timer(
    buffsize = 800
    loop = range(buffsize) #optimized
    rd = adc.read
    buf = array.array('H',loop)  #an unsignted integer array
    while True:
        for i in loop:
            buf[i] = min(max(int(rd()/factor) + adjust, 0), 255)
        socket.write(buf,len(buf))
    '''
    while True
        val = read_mic()
        print(val)
        #socket.write(val,sizeof(val))
        socket.write(val,len(buf))
        time.sleep(0.1)
    s.close()
    '''
print("out")
if __name__=="__main__":
    print("main")



'''
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
'''
