# Digital_Multi_Tool_w_ESP32 -- an internet of things, Micro-Python framework, and laser cut enclosure project..thing.

https://docs.google.com/document/d/1GEC8qHzyvEeZ4Jlq5biDOddLfApk-4TvIT527VtdID8/edit?usp=sharing

* The purpose of the Digital Multi tool is the following:
-- To use the ESP32, as it is a small, low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth, and can be powered using a battery. 
-- To design an an enclosure for ESP32 that can speed up the design, development, implement, and iterate lifecycle. The lazer cut patterns can be downloaded and slighly adapted for future uses cases. This bridges the gap between prototyping on a breadboard to prototyping for more embedded applications.
-- To build a framework that handles the common features of the ESP32 system on a chip; with the reuse of the framework, time can be spend developing the individual programs/apps/python scripts. The framework includes the ability to navigate to different programs, run or disable them. When programs are enabled the data is shared on the board using a publisher / subscriber design patter, and the data is also shared over MQTT to a broker on the network. Other features found in the framework are WIFI connection, OLED menu display, touch sensor menu navigation (only up,down,left,right).


https://en.wikipedia.org/wiki/ESP32


https://picamera.readthedocs.io/en/release-1.13/

# the spiPi has two features, right now
By doing object detection with opencv, the camera sends the coordinates of these objects to a MQTT broker. Now that the feature data is out of the pi, there are a variety of functions and interesting interactions that we can do with it.
( Please see the Digital Culture Server, here https://github.com/sylatupa/Digital_Culture_Server ; and also look here for more examples of this data being consumed: Pure Data Synthesizer: https://github.com/sylatupa/Digital-Culture-Sound-Client & IOT Device https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32  

So, this camera allows for artistic sampling of video data, a transmission of that data using a contemporary protocol MQTT.

## Reasoning and Motivations
IOT and the arts:
There is so much support for raspberry pis and they are small enough to run off a battery (and they are inexpensive). This project tries to solve a few things:
* Turning video data into a readily available data source
* Be able to provide a direct solution to gathering video that is easy as buying something off the shelf, but provides many more benefits. For a variety of uses, such as:
-- Security of the home and business
-- Art and entertainment using video data that is collected live and in place (in situ)
-- Citizen science, for the collection of time lapse video.

Stand alone server benefits:
Stand alone wifi-router: This project uses an additional wifi-router that is plugged into my homes wifi router, so it is interntet connected. But, the benefit of having this additional router layer is that I can take it with me to bring the network into locations that wouldn't have accessible wifi. Getting a battery operated wifi could make this potentially able to be run anywhere.



## Getting Started


### Prerequisites

Networking:

Running headless:

### Installing

(spiPi_requirements.txt) https://gist.github.com/sylatupa/e74248aba2906976b52d9d6011b660de


## Running the tests

## Deployment
```
with venv being the virtual environment folder, type:
source venv/bin/activate

which opens the virtual environment: 
(venv)pi@spipi:~/spiPi $

then type:
python specrideo.py

Now open a browser and go the the ip address for the raspberry pi, and go to port 8000.

``` 
## Built With

* Python 3.4m
* virtualenv 
* opencv --this was the most difficult to install. But, please see the pip installation requirements. And, the list of installation steps are available in this project.

## Contributing

#(comment) Please read [CONTRIBUTING.md](https://gist.github.com/sylatupa/4d0b51c97d2bd8cf210a60c0e7a7d175) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

## Authors

* **S P Y-M** - *Wrote and collected supporting code.
* Contributors:

## License

## Acknowledgments

## An Arizona State University Herberger, Institute for the Design and the Arts, Digital Culture Masters Final Project, 2019.


Software:

IOT Network that provides a routing of data between the IOT devices
UDP connection when no MQTT broker available
OFFLINE -- a standard Publisher Subscriber software paradigm so that the modules on the device can share the data 
Modules and software applications have a configuration file, leading to ‘code reuse’ for certain modules, like:
Neopixels of varying length, quantity of strips and the pins that they’re on.
Swapping/Adding analog sensors, or digital sensors
TouchPads of varying quantity.

Enclosure:
Laser cut acrylic
Multiple Sizes so that each box can have a varying number of hardware modules
Dupont connectors--a lot less soldering



Hardware / Hardware Modules:
Accelerometer
Neopixels of varying sizes
Amplified Microphone
Haptic feedback
OLED display

Reporting:
GITHUB Project
Issues
Project Board
Website--that re-layouts the issues.
