import os
from machine import UART
from network import WLAN
uart = UART(0, 115200)
os.dupterm(uart)

wlan = WLAN(mode=WLAN.STA)
wlan.scan()

wlan.connect(ssid='test', auth=(WLAN.WPA2, 'password'))

while not wlan.isconnected():
    pass

print(wlan.ifconfig()) # prints out local IP to allow for easy connection via Pymakr Plugin or FTP Client
