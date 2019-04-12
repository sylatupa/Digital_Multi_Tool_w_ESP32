# The Enclosure for the Digital_Multi_Tool_w_ESP32 -- a lasercut, stacked sandwhich style, enclosure with simple and adaptable shapes and sizes. 

All the SVG paths were draw in Inkscape. Because Inkscape prints by converting to raster, the files were brought into Corel Draw. 
There was a lot of conversion mistakes and much of my work had to be redone--but the general shapes and size were all figured out.
There are around 6 shapes, mix and matched they are used to create various enclosures. 
 
The enclosures held long and thin TTGO brand ESP32's. It made sense to try and match the scale of the boards in length and width.

The aesthetic of the enclosure was first seen with a raspberry pi. 

The reasons for the design decisions are the following:

I didnt have enough time to do multiple iterations but I knew that the first cut wouldn't be perfect. 

* The purpose of the Digital Multi tool is the following:
** To design an an enclosure for ESP32 that can speed up the design, development, implement, and iterate lifecycle. The lazer cut patterns can be downloaded and slighly adapted for future uses cases. This bridges the gap between prototyping on a breadboard to prototyping for more embedded applications.


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

## Authors
* **S P Y-M** - *Wrote and collected supporting code.
## License


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

Hello, thank you for meeting me today. Please read my summary of the meeting below.
I have some sections to draw your attention:
            ▪ rational** – see these for my discussion. Read these as my reasons for the decisions. Please push back on these if you see anything too weak, or pull it if you think its good.
            ▪ QUESTION – I have a couple questions.

Summary of what we discussed:
    1. Walk through of device
        1. OLED Screen : Benefits and reasoning
        2. Accelerometer sensor issue : Issues with getting any data
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

Outcomes of meeting:

    1. Writing / Documentation required outcomes
        1. With the on-board temperature—explain its use case for getting ambient temperature
        2. Document future wants, or “What is the future for this project” “Next Steps”
        3. Document the source of code used, document in the code above the function (PEP 8 standard)
    2. Tips on approaching the narrative:
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

F

