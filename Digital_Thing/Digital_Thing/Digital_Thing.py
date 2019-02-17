import json

import os
#print(os.listdir('..'))

print("Digital Config Start")
class Digital_Config:
    global filenames, filepath
    filepath = "../"
    filenames = [
            "hardware_config.json" , 
            "thing_config.json"  ,
            "behavior_config.json",  
            "feature_config.json"  
            ]
    def __init__(self):
        self.data = []

    def openConfigFile(this):
        for f in filenames:
            print("File:" + f)
            with open(filepath+f) as json_file:  
                data = json.load(json_file)

if __name__ == "__main__":
    d = Digital_Config()
    d.openConfigFile()
