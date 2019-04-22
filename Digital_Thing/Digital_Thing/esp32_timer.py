from machine import Timer
def setTimerForAppPbr(app_pbr_val):
    for app_pbr_key,app_pbr_val in app_pbr.items():
        for app_event,callback in app_pbr_val.app_events.items():
            m = callback()
            #app_event 
            t1 = Timer(0, 1)
            t1.callback(lambda t: print(t, "tick1"))
            app_pbr_val.dispatch(app_event, m) # (event,message sent)


def NewTimerTest(app_pbr_val):
    t2 = Timer(1, 3)
    t2.callback(lambda t: print(t, "tick2"))
    utime.sleep(3)
    tim = pyb.Timer(4)              # create a timer object using timer 4
    tim.init(freq=2)                # trigger at 2Hz
    tim.callback(lambda t:pyb.LED(1).toggle())

def tick(timer):                # we will receive the timer object when being called
    print(timer.counter())      # show current timer's counter value

if __name__=="__main__":
    tim = pyb.Timer(4, freq=1)      # create a timer object using timer 4 - trigger at 1Hz
    tim.callback(tick)              # set the callback to our tick function

