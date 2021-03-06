'''
module initiates all the peripherial functions and data to run on a desktop:
  ...

Attributes
----------
name : str      the name of the animal
Methods
-------
says(sound=None)    Prints the animals name and what sound it makes
says_str = "A {name} says {sound}"

'''
def init(device_name, broker_ip,wifi_ssid,password):
    import apps.neopixels.neopixels as np
    #np.cycle(20,23)

    #broker_ip =  "192.168.1.55"
    #broker_ip = "192.168.1.115"
    port = 1883

    #import touchpins
    import machine 
    '''
    try:
        #import Network.wifi_adptr as wifi
        #wifi.connect(wifi_ssid,password)
        #wifi.connect("spyprjct-219","")
    except:
        np.fadeInOutWifi(20,23)
        print("no wifi")
    '''
    '''
    led = machine.Pin(16, machine.Pin.OUT)
    for i in range(10):
        print("led")
        led(1)
        time.sleep(0.5)
        led(0)
        time.sleep(0.5)
    '''
    import sys
    mqtt_client = ''
    try:
        import Network.mqtt_client.esp32_client as mqtt_client 
        mqtt_client = mqtt_client.mqtt_client(broker_ip, port)
        mqtt_client.connect_client()
        mqtt_client.client.subscribe("menu", qos=0)
        mqtt_client.client.subscribe(device_name+"/sleep", qos=0)
        mqtt_client.client.subscribe(device_name+"/screen", qos=0)
        mqtt_client.client.subscribe(device_name+"/publish", qos=0)
        mqtt_client.client.on_message = mqtt_client.on_msg
    except:
        np.fadeInOutMQTT(20,23)
        print("no mqtt client")
    import touchpin_getch as getch
    np.clear()
    getch = getch._Getch()  #TODO:esp32 convert
    #np.cycle(20,23)

    return getch,mqtt_client
    #from machine import Timer
    def setTimerForAppPbr(app_pbr_val):
        for app_pbr_key,app_pbr_val in app_pbr.items():
            for app_event,callback in app_pbr_val.app_events.items():
                m = callback()
                #app_event 

                t1 = Timer(0, 1)
                t1.callback(lambda t: print(t, "tick1"))
                app_pbr_val.dispatch(app_event, m) # (event,message sent)
                '''
                t2 = Timer(1, 3)
                t2.callback(lambda t: print(t, "tick2"))
                utime.sleep(3)
                tim = pyb.Timer(4)              # create a timer object using timer 4
                tim.init(freq=2)                # trigger at 2Hz
                tim.callback(lambda t:pyb.LED(1).toggle())

                def tick(timer):                # we will receive the timer object when being called
                    print(timer.counter())      # show current timer's counter value
                tim = pyb.Timer(4, freq=1)      # create a timer object using timer 4 - trigger at 1Hz
                tim.callback(tick)              # set the callback to our tick function

                tim = pyb.Timer(4, freq=100)    # freq in Hz
                tim = pyb.Timer(4, prescaler=0, period=99)
                '''
