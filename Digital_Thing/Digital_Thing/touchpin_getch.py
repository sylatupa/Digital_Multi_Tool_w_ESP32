from machine import Pin, TouchPad
class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        self.touchpin_dict = dict()
        self.touchpin_dict["k"] = {"pin":0} #up 
        self.touchpin_dict["j"] = {"pin":4} #down
        self.touchpin_dict["h"] = {"pin":2} #right
        self.touchpin_dict["l"] = {"pin":15} #left
        print("TOUCH PINS!!")
        self.configure()
    def __call__(self):
        return self.readpins()

    def configure(self):
        for key,val in self.touchpin_dict.items():
            pin_num = val["pin"]
            self.touchpin_dict[key]["touch"] = TouchPad(Pin(pin_num))
            self.touchpin_dict[key]["threshold"] = []
            #for x in range(12): # Scan TouchPad 12 times for calibration
            #    self.touchpin_dict[key]["threshold"].append(self.touchpin_dict[key]["touch"].read())
            #    self.touchpin_dict[key]["threshold"] = sum(self.touchpin_dict[key]["threshold"])//len(self.touchpin_dict[key]["threshold"]) # Store average threshold value
            self.touchpin_dict[key]["touch"].config(100)
        
    def readpins(self):
        for pin,val in self.touchpin_dict.items():
            capacitance = self.touchpin_dict[pin]["touch"].read()
            #print(capacitance)
            #cap_ratio = capacitance / self.touchpin_dict[pin]["threshold"] 
            if capacitance < 111:
                #print(pin)
                return pin
                #sleep(.25)  # Debounce press
