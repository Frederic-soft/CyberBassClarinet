Cyber bass clarinet
=====================
I had temporary issues in my left pinky during a few months in 2020 and could no longer push the low-D and G sharp/D sharp keys on my bass clarinet.

I transformed the tip of the keys into capacitive touchpads to be sensed by an ESP32 development board, which in turn drives a servo-motor to pull the keys.

Contents
--------
* The ```Micropython``` folder contains the [Micropython](https://micropython.org/) code used to program the ICQUANZC Mini32 v1.3 development board I used.

* The openscad folder contains the [OpenScad](https://www.openscad.org/) source code of the block that holds the servo-motor on the upper clarinet body, as well as the rendered STL file that you can use to print this piece.

* The MP4 file shows how the system works.

How to build yours
------------------
The ESP32 and its 1000mAh 3.7V lithium battery are wrapped in black tape and stuck to the clarinet body using double-sided tape.

The 3D-printed servo-motor support is also stuck using double-sided tape.

I tried different solutions to link the servo-motor and the keys.
The best one seems to be to use soft brass wire, as found on Champagne bottles to secure the cork.
Fishing wire will break early and may get tangled.

To carry your bass clarinet in its case, switch the ESP32 off, remove the servor motor from its support.
The ESP32, the servo-motor and all the wiring stay with the lower body.
The upper body only has the 3D-printed support.

<img width="100%" src="https://raw.githubusercontent.com/Frederic-soft/CyberBassClarinet/main/CyberBassClarinet.jpg"/>

© Frédéric Boulanger frederic.softdev@gmail.com  
2019-08-28  
This software is licensed under the Eclipse Public License 2.0
