class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        touchpin_dict = dict()
        touchpin_dict["up"] = {"pin":"0"}
        touchpin_dict["down"] = {"pin":"4"}
        touchpin_dict["left"] = {"pin":"13"}
        touchpin_dict["right"] = {"pin":"15"}

        self.impl = _GetchESP32()
        print("TOUCH PINS!!")
        try:
            self.impl.configure()
        except:
            pass
    def __call__(self): return self.impl()
class _GetchESP32:
    def __init__(self):
        try:
            from machine import Pin, TouchPad
        except:
            pass
    def __call__(self):
        return "nothing"
        #return self.readpins()

    def configure():
        for pin in touchpin_dict:
            pin_num = pin["pin"]
            touchpin_dict[pin]["touch"] = TouchPad(Pin(pin_num))
            touchpin_dict[pin]["threshold"] = []
            for x in range(12): # Scan TouchPad 12 times for calibration
                touchpin_dict[pin]["threshold"].append(touchpin_dict[pin]["touch"].read())
                touchpin_dict[pin]["threshold"] = sum(touchpin_dict[pin]["threshold"])//len(touchpin_dict[pin]["threshold"]) # Store average threshold value
                print('Threshold0: {0}'.format(threshold0))
                touchpin_dict[pin]["threshold"].config(1000)
        
    def readpins(touchpin_dict):
        for pin in touchpin_dict:
            capacitance = touchpin_dict[pin]["touch"].read()
            cap_ratio = capacitance / touchpin_dict[pin]["threshold"] 
            if .40 < cap_ratio < .93:
                return pin
                #sleep(.25)  # Debounce press
