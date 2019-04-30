# Digital_Thing -- an IOT Digital Client and Multi Tool
## A Micro-Python framework, for embedded and internet of things projects. This code was developed for the ESP32.

![wood_enclosure][wood_enclosure]

## Table of Contents
  1. [Introduction](#introduction)
  2. [Milestones from the project](#milestones)
  3. [Parallel projects that work with the Digital_Thing](#parallel_projects)
  4. [Enclosure Design and Construction](#enclosure)
  5. [The Software](#software)
  6. [The Hardware](#hardware)
7. [Use Cases](#use_cases)
  8. [Place_Sense: Classic Living System Monitor](#place_sense)
9. [Sound and Video Controller](#controller)
  10. [The Edge Server: Raspberry Pi, Node-Red, MQTT, Wifi, and some custom Scripts](#the_server)
  11. [Getting Started](#getting_started)
12. [Deployment](#deployment)


## Introduction
  *Welcome,* this repository has the code and supporting material for you to develop micro-python programs for the ESP32. This_Thing works inside the [Edges](https://en.wikipedia.org/wiki/Edge_computing) of the WiFi network when paired with a Raspberry pi, a [mosquitto MQTT server](https://mosquitto.org/), and [Node-Red](https://nodered.org/). This enlocuse and construction requires little to no soldering as the connection of the Sensor modules mimics the initial stages of prototyping--using a breadboard. [The enclosure and wiring](https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/tree/master/Enclosure) solve 2 issues--1) An enclosure with features that can adapt per project and 2) the connections can be made and changed in a way that is commonly available and used. With these two observations about contemporary prototyping techniques: 1) [DuPont connections](https://www.google.com/search?q=dupont+connections&client=ubuntu&hs=R4r&channel=fs&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjJvfnT4_XhAhXSvJ4KHbh-D8EQ_AUIECgD&biw=1533&bih=748) are used and 2) [Sensor modules](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20190429090218&SearchText=dht) and other peripherials can typically be found with a number of male pins for voltage, ground, and data. 

* The purpose of the Digital Multi tool is the following:
** To use the ESP32, as it is a small, low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth, and can be powered using a battery. 
** To design an an enclosure for ESP32 that can speed up the design, development, implement, and iterate lifecycle. The lazer cut patterns can be downloaded and slighly adapted for future uses cases. This bridges the gap between prototyping on a breadboard to prototyping for more embedded applications.
** To build a framework that handles the common features of the ESP32 system on a chip; with the reuse of the framework, time can be spend developing the individual programs/apps/python scripts. The framework includes the ability to navigate to different programs, run or disable them. When programs are enabled the data is shared on the board using a publisher / subscriber design patter, and the data is also shared over MQTT to a broker on the network. Other features found in the framework are WIFI connection, OLED menu display, touch sensor menu navigation (only up,down,left,right).

  ```
  Its an Internet of Things device, software and enclosure
  designed to adapt to the the many new IOT concepts and technologies
  and speed up the time it take to get prototypes 
  from off of the work bench and into the world. 
  ```
## milestones
  - [x] Using and authenticating to Network protocols: WiFi and MQTT
  - [x] A publisher and subscriber paradigm that allows multiple programs to run on the board, where some programs publish data and others subscribe to the data in a seamless way (such as an accelerometer creates xyz data and neopixels use that data for some light affect), found here [pub_sub_local.py](https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Digital_Thing/Digital_Thing/pub_sub_local.py)
  - [x] A state-machine, written with a series of if-else statements, that allow for navigation to and the activation of programs--and code for an OLED display to show data and the menu during navigation. found here [Menu.py](https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Digital_Thing/Digital_Thing/Menu.py) and diagramed here [State Machine and Process Diagram](https://raw.githubusercontent.com/sylatupa/Digital_Multi_Tool_w_ESP32/master/Images/process_and_state_diagram.png) or the [Lucid Chart version ](https://www.lucidchart.com/invitations/accept/83a8f492-7b02-4a9a-af31-d71b3470497e). And the GUI with OLED found here, in the [gui.py](./Digital_Thing/gui.py)
  - [x] Touch interaction with the Menu, with the touch points of contact being the 4 corner bolts for the enclosure, found here in the [touchpin_getch.py](./Digital_Thing/Digital_Thing/touchpin_getch.py) 
  - [x] A configuration file that helps manage the name of the board, wifi ssid and password, IP address of the MQTT server, and a list of apps to be used found here in the [this_thing.json](./Digital_Thing/this_thing.json).
  - [x] A configuration file that lists what the program will be publishing or subscribing to , found here in the [app_config.json](./Digital_Thing/app_config.json).
  - [ ] Ability to deactivate currently running programs
  - [ ] Multiple wifi configurations
  - [ ] Using the configuration file with pin numbers, which would allow for abstraction of basic analog sensing programs and thus allow for code reuse for each new analog sensing program.
  - [ ] More explicit and interactive mapping of data publisher to data subscribers.
  - [ ] Publish data over UDP directly (rather than using a intermediate MQTT broker and Node-Red for inter-networktivity.
  - [x] Be able to run on a laptop for more rapid development, but then also seamlesly deploy to ESP32, the two initialization file can be found here in the [init_for_esp32.py](./Digital_Thing/Digital_Thing/init_for_esp32.py) and [init_for_desktop.py](./Digital_Thing/Digital_Thing/init_for_desktop.py)
  - [x] Design a laser cut enclosure that will speed up and bridge the gap of breadboard protoptyping to the deployment of a contained object that can be embedded in a place or interacted with-out cumbersome wires. All information found for that is found here in the [Enclosure Folder](./Enclosure).
  - [x] A collection of python programs that demonstrate how they exsist in this embedded micro-python ecosystem, in the [folder /apps](./Digital_Thing/Digital_Thing/apps) You will see example programs that work with digital and analog sensor pins on the ESP32, neopixels, onboard temperature and hall sensor, DHT11 (TempHumid), MAX9814 Amplified Microphone, OLED screen, MQTT, connecting to WiFi, and accelerometer.
  - [x] A select on pre-built programs that collect or interact with a variety of data and data sources/sinks, found here in the [apps folder](./Digital_Thing/apps)

      ```
      Its a Digital Tool for people living in an Analog World.
      ```

## parallel_projects

The Digital_Thing is built in the context of a Digital Culture, Arts Media and Engineering, Master of Arts program and some of the following project examples are with interactive art and media. 
* [Digital_Culture_Server](https://github.com/sylatupa/Digital_Culture_Server)
** A collection of Node-Red Flows and Python Scripts. This runs on a Raspberry Pi and is connected to WiFi.
** The Digital_Thing takes sensor data and sends it over an MQTT Network. Node Red recieves this data and sends it the ETC Video Synthesizer and the Digital_Culture_Sound_Client, over OSC.  
* [Digital_Culture_Sound_Client](https://github.com/sylatupa/Digital-Culture-Sound-Client)
** A sound synthesizer written in Pure Data. This runs on a Raspberry Pi and is connected to Wifi and controlled by Node-Red and This_Thing.
* [Video_Synth-ETC_Mother_and-Modes](https://github.com/sylatupa/Video_Synth-ETC_Mother_and-Modes)
** written by Critter and Guitari for the ETC. This is installed on a Raspberry Pi that is connected to WiFi and controlled by Node-Red and This_Thing.


Some exploritory projects and summaries of the current state of Tangible Interaction with embeded Internet of Things devices, they can be found here: [Research Summary](https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/RESEARCH_SUMMARY.md). A thought provoking list can be found in *Internet of Tangible Things (IoTT)* and resonates with some of the features that can be found in the Digital_Thing and peripherial projects:
```
T1. Meaningful representations and controls of  [...] connectivity status, interconnections, as well as information capture [...].
T2. Rich Interactions that exploit the natural human skills [...].
T3. Persistent physical representations that could last in case of power or connectivity outage [...].
T4. Spatial interactions [...] with multiple IOT objects.
T5. Immediacy and intuitiveness of the interaction [...] (low latency).
T6. [...] designed for daily routines, which free users' cognitive resources and do not disrupt attention.
T7. Facilitated reflections on IoT object meaning and working principles, as well as support for associating and sharing memories.
T8. Long-lasting interactions with IoT objects exploiting emotional durable designs, to cope with electronic waste due to technological obsolescence. 
  ```

## enclosure
### Enclosure Design and Construction

 [![A Fly By]](https://www.youtube.com/watch?v=zzlslcG2fdA&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=1)

https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/tree/master/Enclosure

In anticipation that this object will change overtime, additional layers of acrylic can be added or removed to make the necessary room for any expansions made for the ESP2866. The Digital_Things physical description is a clear laser cut acrylic and wood panels, sandwiched on top of each other. The sensor modules are clearly visible inside the void of the enclosure. A small amount of color wires connect the ESP32 to the sensor modules. 

Sensor modules can be added to the enclosure by first mounting them on slides and stacking them using standoffs. All the sensor modules share one common ground and voltage from a small PCB with 2 rows of 8 female headers.

## software  

### Navigation
  ![state_machine]
  Using a state machine, implemented with a series of if statements that allow the user to select programs.
  

## hardware
### sensor_modules
  ![18650 Battery ][18650]
  ![esp32_w_bat Board][esp32_w_bat]
  ![esp32_w_sd Board][esp32_w_sd]
  ![max9814 amplified microphone][max9814]
  ![mma7361 accelerometer][mma7361]
  ![mma7361_accel accelerometer][mma7361_accel]

### wifi
  I had a left over wifi router that I used. I can unplug the Wifi router and take it with me where ever I'm using my Digital Things. This is connected to the INTRA-net--only a local connection is used for intra-networktivity.  This system has completed features that include:

### ESP32
  Creates its own wifi hotspot for advanced configuration and re-connecting to wifi.
  Limited inputs and outputs:
  Touch sensitive 
  Haptic Feedback
  Lithium Ion battery with on board battery charging, or it can run off usb.
  Bluetooth and Wifi
1. Why use ESP32: Affordable and has enough systems on a chip to adequately run the programs put onto it. Battery, etc.
  2. This mobile device does have some functionality of a cell phone
  1. —but the cost is dramatically less
  2. the potential for the battery to last much longer than a cell phone
  3. These reasons, when combined, then allow for applications to be used outdoors in places where it could be damaged or stolen.


## use_cases
### The Digital_Multi_Tool use cases are listed below:
[![spirit_level]](https://www.youtube.com/watch?v=ZxfC2JU0sd4&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=7) 

## place_sense
### Classic Living System Monitor-- to observe Climate and Place Data
  * Sensors include: Temp, Humidity, Noise (Sound Amplitude), Motion, Light
[![place_sense]](https://www.youtube.com/watch?v=dvjA3GYnUuc&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=4)

## controller
### Sound and Video Controller
[![sound_wand]](https://www.youtube.com/watch?v=ZxfC2JU0sd4&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=7)

[![Some Sounds]](https://www.youtube.com/watch?v=B9ACMyeBL88&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf&index=3)


## the_server
### The Server for Edge Computing.
  This device only works locally, with a raspberry pi that has an MQTT broker and a Node-Red Server. 

  The ESP32 has the ability to send data using many communication protocols, such as TCP, UDP, MQTT, Serial.
  But, this device only sends MQTT data, any additional inter-networktivity is handled using Node-Red flows.

  * Something to consider with IOT development is 'where' will the data be. This implementations networking only extends locally--no internet is needed. Instead, all computing and networking is achieved with a wifi-router and raspberry pi. The benefits that are achieved include lowering the cost of internet computing, decreasing the latency (increasing the speed that the user will experince feedback from the sensed data). And, for this project, removing the work that is required to connect to the internet allows for more time to be spent on what can actually be done with Tangible or Embedded IOT.

  * Node-Red and a Mosquitto (MQTT) server is used to move internetwork the data. Protocols are used such as MQTT from the Digital Thing to the Mosquitto Server and then Node-Red and then another application. The MQTT Server and Node-Red live on a Raspberry Pi that is connected by ethernet cable to a dedicated wifi router to achieve Edge Computing.
  --
  With this application I'm demonstrating a device that has an application that works both online and offline, 'stand-alone'.
  LEDs around the edge

  Listening with out using your ears , Haptics skin music , Lauren Hayes. Communicating with other improvisors. Notification tool

## See all the videos here:
[![all_the_things]](https://www.youtube.com/watch?v=zzlslcG2fdA&list=PLcqKf5XU9uVOfuwFNbiraGHOt9Q5JuXdf)

## An Arizona State University Herberger, Institute for the Design and the Arts, Digital Culture Masters Final Project, 2019.

  [state_machine]: ./Images/process_and_state_diagram.png
  [wood_enclosure]: ./Images/enclosure/wood_enclosure.jpg

  [18650]: ./Images/sensor_modules/18650_bat.png
  [esp32_w_bat]: ./Images/sensor_modules/esp32_w_bat.jpg
  [esp32_w_sd]: ./Images/sensor_modules/esp32_w_sd.png 
  [max9814]: ./Images/sensor_modules/max9814.jpg
  [mma7361]: ./Images/sensor_modules/mma7361.jpg 
  [mma7361_accel]: ./Images/sensor_modules/mma7361_accel.png

  [newnew]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/sensor_modules/18650_bat.png
  
[cutting_bolts]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/cutting_bolts.JPG
[dupont_wire_crimp]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/dupont_wire_crimp.JPG
[hot_glue_sensor_modules]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/hot_glue_sensor_modules.JPG
[iot_network_for_artists]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/iot_network_for_artists.jpg

[outside_light_sensor]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/outside_light_sensor.JPG
[place_sense]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/place_sense.JPG
[process_and_state_diagram]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/process_and_state_diagram.png
[submission]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/submission.png

[the_band]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/the_band.JPG
[the_layers]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/the_layers.JPG
[the_layers2]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/the_layers2.JPG
[wire_sensor_modules]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/wire_sensor_modules.JPG
[wire_sensor_modules_2]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/wire_sensor_modules_2.JPG

VIDEO LINK IMAGES
[all_the_things]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/all_the_things.png
[place_sense]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/place_sense.png
[spirit_level]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/spirit_level.png
[sound_wand]: https://github.com/sylatupa/Digital_Multi_Tool_w_ESP32/blob/master/Images/sound_wand.png


  An experimental approach to the media environment
“Instead of fulfilling pre-figured roles or enacing pre-determined schema, media create conditions for social relations to emerge dynamically (or rhizomatically) in the space.” (Garrett Johnson. Catalogue of Logics of Subjectivity.)
