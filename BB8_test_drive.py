#!/usr/bin/python
from bluepy import btle
import struct
import time
import BB8_driver
import sys

bb8 = BB8_driver.Sphero()

bb8.connect()
red=(254,0,0)
green=(0,254,0)
blue=(0,0,254)

def edge(speed, heading):
    print("edge {} {}".format(speed, heading))
    bb8.roll(speed,heading%360,1, False)
    time.sleep(2.5)

def polygon(speedlist):
    """
    Explain what the function does
    """
    assert len(speedlist) > 1
    angle = 360 / len(speedlist)
    offset = 0
    for speed in speedlist:
        edge(speed, offset) # this moves the Sphero!
        offset = offset + angle

def rectangle(speed1,speed2,heading,colour=green):
    bb8.set_rgb_led(colour[0],colour[1],colour[2],0,False)
    polygon([speed1,speed2,speed1,speed2])

def square(speed,heading,colour=red):
    rectangle(speed, speed, heading=heading, colour=colour)

def triangle(speed,heading,colour=blue):
    bb8.set_rgb_led(colour[0],colour[1],colour[2],0,False)
    polygon([speed,speed,speed])
    
def testall():
    rectangle(20,40,0)
    square(35,0)
    triangle(40,0)

testall()
