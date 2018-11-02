import network
import time
from SI7006A20 import SI7006A20
from pysense import Pysense
import json
import urequest

py = Pysense()
si = SI7006A20(py)

# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('Michiel de Router', auth=(network.WLAN.WPA2, '10180747727837478378'))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())

x = 0
while x < 100:
    print("Temperature: " + str(si.temperature()*0.75)+ "deg C")
    ambTemp=str(si.temperature()*0.75) # ambient temp
    print(ambTemp)
    r=urequest.request("POST","http://192.168.178.20:8000",ambTemp,None)
    print('post succesful!')
    print(r)
    r.close()
    time.sleep(300)
    x += 1
print(x)