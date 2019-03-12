

def sub_cb(topic, msg):
    print((topic, msg))

if __name__=='__main__':
    #import subprocess as sp
    #tmp = sp.call('clear',shell=True)
    import sys
    import os
    print(os.listdir("."))
    sys.path.append("./Digital_Thing") #needed to import modules in same path
    try:
        sys.dont_write_bytecode = True #hoping to avoid .pyc files
        import network.mqtt_client.ubuntu_client
    except:
        print('probably on ubuntu machine')
        pass
    import Digital_Thing.Digital_Object as dt
    import Digital_Thing.Menu as mn 
    import Digital_Thing.pub_sub_local as pub_sub_local
    import time


    try:
        import touchpins
    except:
        print("esp32")
    try:
        #import hardware.touchpins as tp
        from machine import Timer
        import machine  
        led = machine.Pin(16, machine.Pin.OUT)
        for i in range(10):
            print("led")
            led(1)
            time.sleep(0.5)
            led(0)
            time.sleep(0.5)
        print("micro-python and imports")
    except:
        print("led fail")
    try:
        import hardware.neopixel as px
        px.main(20,25)
    except:
        pass

    dtm = mn.Menu(dt)
    menu_event = dtm.menu_event #getting the function for performance
    while True:
        menu_event() 




'''
        pub                  = pub_sub_local.Publisher()
        events_published    = dt.getPublishersForApp(hardware_name )
        subscribers         = dt.getSubscribersForApp(hardware_name)
        pub.add_events(events_published)
        publisher_list.append(pub)
            __import__(application_name)
            for sub in subscribers:
                for pubs in publisher_list():
                    for event in pubs.events:
                        if event == sub.get("id"):
                            pub.register(sub, getattr(new_app, sub)() )     
'''
'''
tim = pyb.Timer(4)              # create a timer object using timer 4
tim.init(freq=2)                # trigger at 2Hz
tim.callback(lambda t:pyb.LED(1).toggle())

def tick(timer):                # we will receive the timer object when being called
    print(timer.counter())      # show current timer's counter value
tim = pyb.Timer(4, freq=1)      # create a timer object using timer 4 - trigger at 1Hz
tim.callback(tick)              # set the callback to our tick function

tim = pyb.Timer(4, freq=100)    # freq in Hz
tim = pyb.Timer(4, prescaler=0, period=99)
tim.counter()                   # get counter (can also set)
tim.prescaler(2)                # set prescaler (can also get)
tim.period(199)                 # set period (can also get)
tim.callback(lambda t: ...)     # set callback for update interrupt (t=tim instance)
tim.callback(None)              # clear callback
'''
