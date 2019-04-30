# Digital_Thing -- an IOT Digital Client and Multi Tool
## A Micro-Python framework, for embedded and internet of things projects. This code was developed for the ESP32.

![wood_enclosure][wood_enclosure]

## Table of Contents
1. [Introduction](#introduction)
2. [Milestones from the project](#milestones)
3. [Parallel projects that work with the Digital_Thing](#parallel_projects)
4. [Enclosure Design and Construction](#enclosure)
5. [The Software](#software) 
6. [Use Cases](#use_cases)
7. [Place_Sense: Classic Living System Monitor](#place_sense)
8. [Sound and Video Controller](#controller)
9. [The Edge Server: Raspberry Pi, Node-Red, MQTT, Wifi, and some custom Scripts](#the_server)
10. [Getting Started](#getting_started)
11. [Deployment](#deployment)


## Introduction
*Welcome,* this repository has the code and supporting material for you to develop micro-python programs for the ESP32. This_Thing works inside the [Edges](https://en.wikipedia.org/wiki/Edge_computing) of the WiFi network when paired with a Raspberry pi, a [mosquitto MQTT server](https://mosquitto.org/), and [Node-Red](https://nodered.org/). This enlocuse and construction requires little to no soldering as the connection of the Sensor modules mimics the initial stages of prototyping--using a breadboard. [The enclosure and wiring](https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/tree/master/Enclosure) solve 2 issues--1) An enclosure with features that can adapt per project and 2) the connections can be made and changed in a way that is commonly available and used. With these two observations about contemporary prototyping techniques: 1) [DuPont connections](https://www.google.com/search?q=dupont+connections&client=ubuntu&hs=R4r&channel=fs&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjJvfnT4_XhAhXSvJ4KHbh-D8EQ_AUIECgD&biw=1533&bih=748) are used and 2) [Sensor modules](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20190429090218&SearchText=dht) and other peripherials can typically be found with a number of male pins for voltage, ground, and data. 

```
Its an Internet of Things device, software and enclosure
designed to adapt to the the many new IOT concepts and technologies
and speed up the time it take to get prototypes 
from off of the work bench and into the world. 
```

## Milestones from the project:
- [x] Using and authenticating to Network protocols: WiFi and MQTT
- [x] A publisher and subscriber paradigm that allows multiple programs to run on the board, where some programs publish data and others subscribe to the data in a seamless way (such as an accelerometer creates xyz data and neopixels use that data for some light affect), found here [pub_sub_local.py](https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Digital_Thing/Digital_Thing/pub_sub_local.py)
- [x] A state-machine, written with a series of if-else statements, that allow for navigation to and the activation of programs--and code for an OLED display to show data and the menu during navigation. found here [Menu.py](https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Digital_Thing/Digital_Thing/Menu.py) and diagramed here [State Machine and Process Diagram](https://raw.githubusercontent.com/sylatupa/Digital_Multi_Tool_w_ESP32/master/Images/process_and_state_diagram.png) or the [Lucid Chart version ](https://www.lucidchart.com/invitations/accept/83a8f492-7b02-4a9a-af31-d71b3470497e). And the GUI with OLED found here, in the [gui.py](./Digital_Thing/gui.py)
- [x] Touch interaction with the Menu, with the touch points of contact being the 4 corner bolts for the enclosure, found here in the [toucpin_getch.py](./Digital_Thing/touchpin_getch.py) 
- [x] A configuration file that helps manage the name of the board, wifi ssid and password, IP address of the MQTT server, and a list of apps to be used found here in the [this_thing.json](./Digital_Thing/this_thing.json).
- [x] A configuration file that lists what the program will be publishing or subscribing to , found here in the [app_config.json](./Digital_Thing/app_config.json)
- [ ] Ability to deactivate currently running programs
- [ ] Multiple wifi configurations
- [ ] Using the configuration file with pin numbers, which would allow for abstraction of basic analog sensing programs and thus allow for code reuse for each new analog sensing program.
- [ ] More explicit and interactive mapping of data publisher to data subscribers.
- [ ] Publish data over UDP directly (rather than using a intermediate MQTT broker and Node-Red for inter-networktivity.
- [x] Be able to run on a laptop for more rapid development, but then also seamlesly deploy to ESP32, the two initialization file can be found here in the [init_for_esp32.py](./Digital_Thing/Digital_Thing/init_for_esp32.py) and [init_for_desktop.py](./Digital_Thing/Digital_Thing/init_for_desktop.py)
- [x] Design a laser cut enclosure that will speed up and bridge the gap of breadboard protoptyping to the deployment of a contained object that can be embedded in a place or interacted with-out cumbersome wires. All information found for that is found here in the [Enclosure Folder](./Enclosure).
- [x] A collection of python programs that demonstrate how they exsist in this embedded micro-python ecosystem, in the [folder /apps](./Digital_Thing/Digital_Thing/apps) You will see example programs that work with digital and analog sensor pins on the ESP32, neopixels, onboard temperature and hall sensor, DHT11 (TempHumid), MAX9814 Amplified Microphone, OLED screen, MQTT, connecting to WiFi, and accelerometer.

```
Its a Digital Tool for people living in an Analog World.
```
:robot:

## parallel_projects
## Parallel projects that work with the Digital_Thing:

The Digital_Thing is built in the context of a Digital Culture, Arts Media and Engineering, Master of Arts program and some of the following project examples are with interactive art and media. 

* [Digital_Culture_Server](https://github.com/sylatupa/Digital_Culture_Server)
        ** A collection of Node-Red Flows and Python Scripts. This runs on a Raspberry Pi and is connected to WiFi.
        ** The Digital_Thing takes sensor data and sends it over an MQTT Network. Node Red recieves this data and sends it the ETC Video Synthesizer and the Digital_Culture_Sound_Client, over OSC.  

* [Digital_Culture_Sound_Client](https://github.com/sylatupa/Digital-Culture-Sound-Client)
        ** A sound synthesizer written in Pure Data. This runs on a Raspberry Pi and is connected to Wifi and controlled by Node-Red and This_Thing.
* [Video_Synth-ETC_Mother_and-Modes](https://github.com/sylatupa/Video_Synth-ETC_Mother_and-Modes)
        ** written by Critter and Guitari for the ETC. This is installed on a Raspberry Pi that is connected to WiFi and controlled by Node-Red and This_Thing.

This jewel is wifi enabled and so getting it onto the network to send OSC communication to pure data will be one demonstration. Also, controlling it with OSC, perhaps putting them in a 5x5 grid and controlling them by index.

This device only works locally, with a raspberry pi that has an MQTT broker and a Node-Red Server. 

The ESP32 has the ability to send data using many communication protocols, such as TCP, UDP, MQTT, Serial.
But, this device only sends MQTT data, any additional inter-networktivity is handled using Node-Red flows.

* The purpose of the Digital Multi tool is the following:
** To use the ESP32, as it is a small, low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth, and can be powered using a battery. 
** To design an an enclosure for ESP32 that can speed up the design, development, implement, and iterate lifecycle. The lazer cut patterns can be downloaded and slighly adapted for future uses cases. This bridges the gap between prototyping on a breadboard to prototyping for more embedded applications.
** To build a framework that handles the common features of the ESP32 system on a chip; with the reuse of the framework, time can be spend developing the individual programs/apps/python scripts. The framework includes the ability to navigate to different programs, run or disable them. When programs are enabled the data is shared on the board using a publisher / subscriber design patter, and the data is also shared over MQTT to a broker on the network. Other features found in the framework are WIFI connection, OLED menu display, touch sensor menu navigation (only up,down,left,right).

https://en.wikipedia.org/wiki/ESP32
https://www.dx.com/p/mma7361-accelerometer-module-tilt-slant-angle-sensor-2017571?tc=USD&ta=US&gclid=EAIaIQobChMI_ryRraW_3wIVQyCtBh0HgghsEAQYAiABEgKiq_D_BwE#.XCRk_7dlB-E
http://arduinolearning.com/code/arduino-mma7361-accelerometer-example.php
https://www.hackster.io/julianfschroeter/esp32-voice-streamer-52bd7e

### Please see the following projects that were developed inS parallel. You will see the enclosure, server, and sound and video clients that work with this software

* Using Node-Red, MQTT, and the OSC (UDP) protocol, data is routed from the de


Some exploritory projects and summaries of the current state of Tangible Interaction with embeded Internet of Things devices, they can be found here: [Research Summary](https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/RESEARCH_SUMMARY.md). A thought provoking list can be found in *Internet of Tangible Things (IoTT)* and resonates with some of the features that can be found in the Digital_Thing and peripherial projects:
```
T1. Meaningful representations and controls of  [...] connectivity status, interconnections, as well as information capture [...]
T2. Rich Interactions that exploit the natural human skills [...]
T3. Persistent physical representations that could last in case of power or connectivity outage [...]
T4. Spatial interactions [...] with multiple IOT objects
T5. Immediacy and intuitiveness of the interaction [...] (low latency)
T6. [...] designed for daily routines, which free users' cognitive resources and do not disrupt attention.
T7. Facilitated reflections on IoT object meaning and working principles, as well as support for associating and sharing memories.
T8. Long-lasting interactions with IoT objects exploiting emotional durable designs, to cope with electronic waste due to technological obsolescence. 
```

# Why use the ESP32?
## Reasonings and Motivations
Build something that is more constrained with inputs/outputs and cpu power, than tools that I typically use such as Raspberry Pis
Go through the process of packaging a design in way that can be picked up an internet audience
An experimental approach to the media environment
“Instead of fulfilling pre-figured roles or enacing pre-determined schema, media create conditions for social relations to emerge dynamically (or rhizomatically) in the space.” (Garrett Johnson. Catalogue of Logics of Subjectivity.)


# Enclosure Design and Construction
## Reasonings and Motivations

In anticipation that this object will change overtime, additional layers of acrylic can be added or removed to make the necessary room for any expansions made for the ESP2866.

# The Framework 
## Reasonings and Motivations
[State_Machine]

# The Digital_Multi_Tool use cases are listed below:
## Classic Living System Monitor-- to observe Climate and Place Data
* Sensors include: Temp, Humidity, Noise (Sound Amplitude), Motion, Light

# Sound and Video Controller
# Something Fun with Media Creation (Sound and/or Video)
##*Bells and Whistles
MUSIC with Accelerometer:
--Drone that changes pitch up and down
--Arpegiator 

# The Server for Edge Computing.

* Something to consider with IOT development is 'where' will the data be. This implementations networking only extends locally--no internet is needed. Instead, all computing and networking is achieved with a wifi-router and raspberry pi. The benefits that are achieved include lowering the cost of internet computing, decreasing the latency (increasing the speed that the user will experince feedback from the sensed data). And, for this project, removing the work that is required to connect to the internet allows for more time to be spent on what can actually be done with Tangible or Embedded IOT.

* Node-Red and a Mosquitto (MQTT) server is used to move internetwork the data. Protocols are used such as MQTT from the Digital Thing to the Mosquitto Server and then Node-Red and then another application. The MQTT Server and Node-Red live on a Raspberry Pi that is connected by ethernet cable to a dedicated wifi router to achieve Edge Computing.
--
# Physical Description:
* Laser cut acrylic
* Stained wood panels. 
* Sandwiched on top of each other.
* A visible, through the acrylic, void inside for boards and sensor modules.
Human Interface Device (Hid) - something like a computer mouse
Input for musical instrument

With this application I'm demonstrating a device that has an application that works both online and offline, 'stand-alone'.
LEDs around the edge
 
Listening with out using your ears , Haptics skin music , Lauren Hayes. Communicating with other improvisors. Notification tool

# Digital Multi-Tool embedded software
Please see this chart on how the software works, and how the user can navigate through configured programs.
https://www.lucidchart.com/invitations/accept/83a8f492-7b02-4a9a-af31-d71b3470497e
## Navigation

### Software
Using a state machine, implemented with a series of if statements that allow the user to select programs.
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/process_and_state_diagram.png

# Hardware

OLED Screen : Benefits and reasoning
Accelerometer sensor issue : Issues with getting any data

Really moving through solving the problems of the project, while not spending too much time just on navigation
![18650 Battery][18650 | width=10]
![esp32_w_bat Board][esp32_w_bat | width=10]
![esp32_w_sd Board][esp32_w_sd | width=10]
![max9814 amplified microphone][max9814 | width=10]
![mma7361 accelerometer][mma7361 | width=10]
![mma7361_accel accelerometer][mma7361_accel | width=10]

* ESP8266 TTGO  G620
* Accelerometer MMA7361 
** https://www.aliexpress.com/item/MMA7361-Angle-Sensor-Inclination-Accelerometer-Acceleration-Module-For-Arduino/32597885640.html
* Lithium Battery

## Wifi
I have a left over wifi router that I used. I can unplug the Wifi router and take it with me where ever I'm using my Digital Things. This is connected to the INTRA-net--only a local connection is used for intra-networktivity.  This system has completed features that include:

# ESP32
Creates its own wifi hotspot for advanced configuration and re-connecting to wifi.
Limited inputs and outputs:
Touch sensitive 
Haptic Feedback
Lithium Ion battery with on board battery charging, or it can run off usb.
Bluetooth and Wifi

# Raspberry Pi

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

## Getting Started

### Prerequisites

Networking:

Running headless:

### Installing

#### This software can be run in a variety of ways. 

##### On Ubuntu:
Python3.6:

##### Ubuntu-Port of Micro-Python:

##### On The ESP32:

### Running the tests

### Deployment


## Contributing

#(comment) Please read [CONTRIBUTING.md](https://gist.github.com/sylatupa/4d0b51c97d2bd8cf210a60c0e7a7d175) for details on our code of conduct, and the process for submitting pull requests to us.






## License

Product design and presentation like 
* https://nsynthsuper.withgoogle.com/
* https://enchantedobjects.com/#/ambient-orb/
* https://github.com/googlecreativelab/open-nsynth-super 
* https://www.instructables.com/id/MeArm-Build-a-Small-Hackable-Robot-Arm/
* https://perso.aquilenet.fr/~sven337/english/2016/07/14/DIY-wifi-baby-monitor.html



## An Arizona State University Herberger, Institute for the Design and the Arts, Digital Culture Masters Final Project, 2019.

    3. Two examples of data being sampled, displayed, and sent over the network. On board Temp, Hall / Magnetic field
    2. Project scope
        1. Wants
            1. Differences in the rate (freq.) of how often the programs are run (temp vs accelerometer)
            2. being able to turn on and off the MQTT
            3. Other Optimizations
        2. Needs
            1. Getting the accelerometer to work—or, some other way to get human motion, reed sensor
    3. Next Steps
        1. 1 week to work on accelerometer and assembly of objects.
        2. Reading / Research
        3. Documentation

Outcomes of meeting :
1. Writing / Documentation required outcomes
        1. With the on-board temperature—explain its use case for getting ambient temperature
        2. Document future wants, or “What is the future for this project” “Next Steps”
        3. Document the source of code used, document in the code above the function (PEP 8 standard)
    2. Tips on approaching the narrative  
        1. When I hold it, I understand why I want to use it.
        2. Justification of WHY are we doing this? And demonstrate the success 
            1. Start of rational** 
                1. Why use ESP32: Affordable and has enough systems on a chip to adequately run the programs put onto it. Battery, etc.
                2. This mobile device does have some functionality of a cell phone
                    1. —but the cost is dramatically less
                    2. the potential for the battery to last much longer than a cell phone
                    3. These reasons, when combined, then allow for applications to be used outdoors in places where it could be damaged or stolen.
                        1. ** added as a needed DEMO
        3. Importance of why to have it all on the board
            1. Start of rational** The design process can be very clunky when developing hardware devices. The internet shows countless attempts to do hardware prototyping, with jumper wires running in all directions, connected to a breadboard, and attached to the micro-controller. 
            2. Start of rational** How to solve the problem of increasing the speed prtotyping—so that the development of the hardware is not bottle necked by the ‘Enclosure building task’, but the Enclosure building task does not restrict the previous tasks of component acquisition and assembly?
        4. What is the data and why
            1. Start of rational** An accelerometer can be used as a human interface device that allows a person to digitize movement by turning acceleration of a ‘rigid body’ into 3D point data. This is desirable because… I’m interested increasing the use all parts of the human to interact with a digital system?  
            2. Accelerometer data detects movement of objects that we are interested in.
        5. Why collect the data away from the device?
            1. There are additional applications that this device has a part in
                1. This device is a controller
                    1. **DEMO
                    2. **Video Synthesizer
            2. This device is not suitable for high quality audio. I want sound to be a feedback mechanism for the user, so that will be done in the ‘Space’ not directly to the user. Augmenting the space
                1. **DEMO Augmenting the space
            3. 
    3. The project needs to demo 2,3,4 applications in a clear use case.
        1. An improvisational sound synthesis can be good and clear, and will satisfy one demo.
        2. IOT example
        3. Outdoor example
    4. “plug and play”, really? 
            1. Do a survey of how people in the market are currently doing ‘plug and play’
                1. explain why I didnt just by a lilly pad, or would I?
                2. QUESTION:: Turino?? Using music and coding
            2. Explain what modularity / adaptability / ‘plug and play’ this project has accomplished and the decisions that were made for those design decisions.
    5. Data shown on the screen needs to have better contextualization, like max and min
            1. Accelerometer data would be best shown using a Polar Graph

QUESTION:: In what way do I discuss some of the design decisions, if they were made for aesthetic reasons OR the decision was based on the novelty of the feature? Such as:
    • I like the sound of the Piezo Buzzer
    • I like the look of cut acrylic, and laser cut wood.
    • I like the look of hardware. I like how the boards look exposed, visually. 
    • I like organized rainbow wires.
(Read this as: Not only do I like the feature, but I also think other people like these aesthetics OR novelty, too.)

[All the videos](https://www.youtube.com/watch?v=zzlslcG2fdA&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf)
[Place Sense](https://www.youtube.com/watch?v=dvjA3GYnUuc&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=4)
[A Fly By](https://www.youtube.com/watch?v=zzlslcG2fdA&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=1)
[Some Sounds](https://www.youtube.com/watch?v=B9ACMyeBL88&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=3)
[Spirit Level](https://www.youtube.com/watch?v=ZxfC2JU0sd4&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=7)

[state_machine]: ./Images/process_and_state_diagram.png
[wood_enclosure]: ./Images/enclosure/wood_enclosure.jpg

[18650]: ./Images/sensor_modules/18650_bat.png
[esp32_w_bat]: ./Images/sensor_modules/esp32_w_bat.jpg
[esp32_w_sd]: ./Images/sensor_modules/esp32_w_sd.png 
[max9814]: ./Images/sensor_modules/max9814.jpg
[mma7361]: ./Images/sensor_modules/mma7361.jpg 
[mma7361_accel]: ./Images/sensor_modules/mma7361_accel.png

[newnew]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/sensor_modules/18650_bat.png

https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/2019-02-08%2020.50.47.jpg
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/cutting_bolts.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/dupont_wire_crimp.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/hot_glue_sensor_modules.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/iot_network_for_artists.jpg
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/image1.png
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/outside_light_sensor.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/place_sense.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/process_and_state_diagram.png
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/submission.png

https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/the_band.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/the_layers.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/the_layers2.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/wire_sensor_modules.JPG
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/wire_sensor_modules_2.JPG

VIDEO LINK IMAGES
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/all_the_things.png
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/place_sense.png
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/spirit_level.png
https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/sound_wand.png
