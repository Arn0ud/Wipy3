#Imports
import pycom
import time
from machine import ADC
import urequest

pycom.heartbeat(False)#Disable LED heartbeat

#Configure the ADC
adc = ADC(0)
adc_c = adc.channel(pin='P13')

#We will push the information to the initialstate Cloud every 10 seconds
#The sensor used is the ALS PT19 you could find some on Adafruit.
#The ouput of the sensor is analog, for testing purposes we are going to work
#with the raw reading which will be the ADC counts
while True:
    adc_c()
    AmbientLight=adc_c.value()#We get the value of the counts here
    print(AmbientLight)# we print the  value stored on AmbientLight

    #here we will do the GET request to the Initialstate cloud with your credentials.
    #Note* Replace the accessKey and bucketKey with your own credentials
    r=urequest.request("POST","http://192.168.178.20"+str(AmbientLight),None)
    r.close()
    time.sleep(10)
