import time
import machine
import node_mcu

#############################################
# NeoPixel (ws2812) init on pin D2
import ledpy
import animation
strip = ledpy.LedStrip(node_mcu.PIN_D2, 12)
throbber = animation.Throbber(strip)
throbber.run(30)
# spinner = animation.Spinner(strip)

##############################################
# Network Init
import network
wlan = network.WLAN(network.STA_IF)


def wlan_connect(essid, pw):
    wlan.active(True)
    wlan.scan()
    wlan.connect(essid, pw)
#
# def home_connect():
#     wlan_connect("devnet", "secret")
#
# def rev_connect():
#     wlan_connect("worknet", "secret")

##############################################
# PWM init on pin D1
pwm0 = machine.PWM(machine.Pin(node_mcu.PIN_D1))

print("Updating clockspeed")
machine.freq(160000000)
print("Clock set to 160Mhz")

print("Booding complet.")
