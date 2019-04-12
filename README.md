# Digital_Multi_Tool_w_ESP32 -- an internet of things, Micro-Python framework, and laser cut enclosure project..thing.

https://docs.google.com/document/d/1GEC8qHzyvEeZ4Jlq5biDOddLfApk-4TvIT527VtdID8/edit?usp=sharing

Following similar product design patterns, this project will design and develop an electronic widget and the code and patterns will be shared in an appropriate social media platform such as GitHub or ThingiVerse. People can download these instructions, code, and laser cut templates to build all, some, or customize the Multitool for their purposes. Its a Digital Tool for people living in an Analog World.

In anticipation that this object will change overtime, additional layers of acrylic can be added or removed to make the necessary room for any expansions made for the ESP2866.

This jewel is wifi enabled and so getting it onto the network to send OSC communication to pure data will be one demonstration. Also, controlling it with OSC, perhaps putting them in a 5x5 grid and controlling them by index.

This device only works locally, with a raspberry pi that has an MQTT broker and a Node-Red Server. 

The ESP32 has the ability to send data using many communication protocols, such as TCP, UDP, MQTT, Serial.
But, this device only sends MQTT data, any additional inter-networktivity is handled using Node-Red flows.

* The purpose of the Digital Multi tool is the following:
** To use the ESP32, as it is a small, low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth, and can be powered using a battery. 
** To design an an enclosure for ESP32 that can speed up the design, development, implement, and iterate lifecycle. The lazer cut patterns can be downloaded and slighly adapted for future uses cases. This bridges the gap between prototyping on a breadboard to prototyping for more embedded applications.
** To build a framework that handles the common features of the ESP32 system on a chip; with the reuse of the framework, time can be spend developing the individual programs/apps/python scripts. The framework includes the ability to navigate to different programs, run or disable them. When programs are enabled the data is shared on the board using a publisher / subscriber design patter, and the data is also shared over MQTT to a broker on the network. Other features found in the framework are WIFI connection, OLED menu display, touch sensor menu navigation (only up,down,left,right).

https://en.wikipedia.org/wiki/ESP32

# Physical Description:
* Laser cut acrylic
* Stained wood panels. 
* Sandwiched on top of each other.
* A visible, through the acrylic, void inside for boards and sensor modules.

# Materials used in MultiTool
* ESP8266 TTGO  G620
* Accelerometer MMA7361 
** https://www.aliexpress.com/item/MMA7361-Angle-Sensor-Inclination-Accelerometer-Acceleration-Module-For-Arduino/32597885640.html
* Lithium Battery

https://www.dx.com/p/mma7361-accelerometer-module-tilt-slant-angle-sensor-2017571?tc=USD&ta=US&gclid=EAIaIQobChMI_ryRraW_3wIVQyCtBh0HgghsEAQYAiABEgKiq_D_BwE#.XCRk_7dlB-E
http://arduinolearning.com/code/arduino-mma7361-accelerometer-example.php
https://www.hackster.io/julianfschroeter/esp32-voice-streamer-52bd7e


# Why use the ESP32?
## Reasonings and Motivations
Build something that is more constrained with inputs/outputs and cpu power, than tools that I typically use such as Raspberry Pis
Go through the process of packaging a design in way that can be picked up an internet audience
An experimental approach to the media environment
“Instead of fulfilling pre-figured roles or enacing pre-determined schema, media create conditions for social relations to emerge dynamically (or rhizomatically) in the space.” (Garrett Johnson. Catalogue of Logics of Subjectivity.)


# Enclosure Design and Construction
## Reasonings and Motivations

# The Framework 
## Reasonings and Motivations

# The Digital_Multi_Tool use cases are listed below:
## Classic Living System Monitor-- to observe Climate and Place Data
* Sensors include: Temp, Humidity, Noise (Sound Amplitude), Motion, Light

# Sound and Video Controller
# Something Fun with Media Creation (Sound and/or Video)
##*Bells and Whistles
MUSIC with Accelerometer:
--Drone that changes pitch up and down
--Arpegiator 

--


Human Interface Device (Hid) - something like a computer mouse
Input for musical instrument

With this application I'm demonstrating a device that has an application that works both online and offline, 'stand-alone'.
LEDs around the edge
 
Listening with out using your ears , Haptics skin music , Lauren Hayes. Communicating with other improvisors. Notification tool 
# Utility
## Demonstrate some simple use cases that are 'Tool' like:
* Light / Torch
* Bike Light
* Bike Blinker
* Spirit Level to Hang a Picture
* clock 
* Timer
* Level
* HID
* mouse 3D touch 
* pedometer 
* flashlite
* Microphone to bue tooth , microphone to SD card
* weather station

# Opportunities when using an ESP32
Creates its own wifi hotspot for advanced configuration and re-connecting to wifi.
Limited inputs and outputs:
Touch sensitive 
Haptic Feedback
Lithium Ion battery with on board battery charging, or it can run off usb.
Bluetooth and Wifi

## Getting Started

### Prerequisites

Networking:

Running headless:

### Installing

(spiPi_requirements.txt) https://gist.github.com/sylatupa/e74248aba2906976b52d9d6011b660de


## Running the tests

## Deployment


## Contributing

#(comment) Please read [CONTRIBUTING.md](https://gist.github.com/sylatupa/4d0b51c97d2bd8cf210a60c0e7a7d175) for details on our code of conduct, and the process for submitting pull requests to us.

## License

Product design and presentation like 
* https://nsynthsuper.withgoogle.com/
* https://github.com/googlecreativelab/open-nsynth-super 
* https://www.instructables.com/id/MeArm-Build-a-Small-Hackable-Robot-Arm/
* https://perso.aquilenet.fr/~sven337/english/2016/07/14/DIY-wifi-baby-monitor.html


## An Arizona State University Herberger, Institute for the Design and the Arts, Digital Culture Masters Final Project, 2019.
