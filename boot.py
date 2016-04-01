"""
Init code to play around in REPL on the NodeMCU hardware. Imports libs, defines
some pins, and such.
"""

import time
import machine
import node_mcu

#############################################
# NeoPixel (ws2812) init on pin D2
from ws2812 import NeoPixel
neo_pin = machine.Pin(node_mcu.PIN_D2, machine.Pin.OUT)
pixels = NeoPixel(neo_pin, 12)

##############################################
# Network Init
import network
wlan = network.WLAN(network.STA_IF)

def wlan_connect(essid, pw):
    wlan.active(True)
    wlan.scan()
    wlan.connect(essid, pw)

def home_connect():
    wlan_connect("devnet", "secret")

def rev_connect():
    wlan_connect("worknet", "secret")

##############################################
# PWM init on pin D1
pwm0 = machine.PWM(machine.Pin(node_mcu.PIN_D1))
