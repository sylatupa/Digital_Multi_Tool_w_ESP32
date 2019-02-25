def evoke(message):
    print("evokiinng" + message)

def configure():
    from time import sleep
    from machine import Pin, TouchPad
    for pin in touchpin_dict:
        pin_num = pin["pin"]
        touchpin_dict[pin]["touch"] = TouchPad(Pin(pin_num))
        touchpin_dict[pin]["threshold"] = []
        for x in range(12): # Scan TouchPad 12 times for calibration
            touchpin_dict[pin]["threshold"].append(touchpin_dict[pin]["touch"].read())
            sleep(.1)

            touchpin_dict[pin]["threshold"] = sum(touchpin_dict[pin]["threshold"])//len(touchpin_dict[pin]["threshold"]) # Store average threshold value
            
            print('Threshold0: {0}'.format(threshold0))
            touchpin_dict[pin]["threshold"].config(1000)
    
def readpins(touchpin_dict):
    for pin in touchpin_dict:
        capacitance = touchpin_dict[pin]["touch"].read()
        cap_ratio = capacitance / touchpin_dict[pin]["threshold"] 
        print(cap_ratio)
        # Check if a Touchpad is pressed
        if .40 < cap_ratio < .93:
            #print('Touch0: {0}, Diff: {1}, Ratio: {2}%.'.format(capacitance0, threshold0 - capacitance0, cap_ratio0 * 100))
            touchpin_dict[pin]["active"] = True
            sleep(.25)  # Debounce press
        else:
            touchpin_dict[pin]["active"] = False 

        print(touchpin_dict[pin], ' ', pin, ' ', touchpin_dict[pin]['active'])



def test(touchpin_dict):

    t = touchpads(touchpin_dict)

def test_touch_pads():
    """TouchPad Config Test."""
    from time import sleep
    from machine import Pin, TouchPad

    touch0 = TouchPad(Pin(0))
    threshold0 = []

    # Scan TouchPad 12 times for calibration
    for x in range(12):
        threshold0.append(touch0.read())
        sleep(.1)

    # Store average threshold value
    threshold0 = sum(threshold0) // len(threshold0)
    print('Threshold0: {0}'.format(threshold0))

    sensitivity = 0
    touch0.config(sensitivity)
    print('sensitivity {0}'.format(sensitivity))

    try:
        while True:
            capacitance0 = touch0.read()
            cap_ratio0 = capacitance0 / threshold0
            # Check if a Touchpad is pressed
            if .40 < cap_ratio0 < .95:
                print('Touch0: {0}, Diff: {1}, Ratio: {2}%.'.format(
                      capacitance0, threshold0 - capacitance0, cap_ratio0 * 100))
                sleep(.25)  # Debounce press
                sensitivity += 100
                touch0.config(sensitivity)
                print('sensitivity increased to {0}'.format(sensitivity))

    except KeyboardInterrupt:
        print('\nCtrl-C pressed.  Exiting...')



    touch0 = TouchPad(Pin(2))
    threshold0 = []

    # Scan TouchPad 12 times for calibration
    for x in range(12):
        threshold0.append(touch0.read())
        sleep(.1)

    # Store average threshold value
    threshold0 = sum(threshold0) // len(threshold0)
    print('Threshold0: {0}'.format(threshold0))

    sensitivity = 0
    touch0.config(sensitivity)
    print('sensitivity {0}'.format(sensitivity))

    try:
        while True:
            capacitance0 = touch0.read()
            print("capacitance:", capacitance0)
            cap_ratio0 = capacitance0 / threshold0
            # Check if a Touchpad is pressed
            if .40 < cap_ratio0 < .95:
                print('Touch0: {0}, Diff: {1}, Ratio: {2}%.'.format(
                      capacitance0, threshold0 - capacitance0, cap_ratio0 * 100))
                sleep(.25)  # Debounce press
                sensitivity += 100
                touch0.config(sensitivity)
                print('sensitivity increased to {0}'.format(sensitivity))
    except:
        pass
