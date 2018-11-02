# Push data from the Light Sensor to InitialState Cloud

I am testing this program with a WiPy, I have the boot file configured to connect the board to my home WiFi.

I am using this Light Sensor ALS PT19 you could find it on [Adafruit](https://www.adafruit.com/product/2748), we are going to read the Analog value of the sensor. Just connect 3.3V and GND and wire the output to P13 or G5 on the expansion board.

[Initial State](https://www.initialstate.com/) is a very easy to setup cloud, ideal for a maker where we just want something to WORK.
Setup an account , create a new Stream Bucket, get your credentials and just paste them on the program.

Dont forget to add the lib folder and the urequest.py library

![alt text](https://github.com/SeaSlugLabs/Pycom-Examples/blob/master/WiPy/ADC-Light-Sensor-To-Cloud/WipyInitialState.png)
