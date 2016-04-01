"""
Micropython NodeMCU Library

Provides pin constants for running Micropython on the NodeMCU board.

:copyright: (c) 2015 by Trey Chandler.
:license: GPL 3, see LICENSE for more details.
"""

__title__ = 'py8266_node_mcu'
__version__ = '0.1'
__build__ = 0x00001
__author__ = 'Trey Chandler'
__license__ = 'GPL 3'
__copyright__ = 'Copyright 2016 Trey Chandler'

from machine import Pin

PIN_D0 = 16
PIN_D1 = 5
PIN_D2 = 4
PIN_D3 = 0
PIN_D4 = 2
PIN_D5 = 14
PIN_D6 = 12
PIN_D7 = 13
PIN_D8 = 15
PIN_D9 = 3
PIN_RX = 3
PIN_D10 = 1
PIN_TX = 1
PIN_SD3 = 10
PIN_SD2 = 9
PIN_LED = 16

def led_on():
    led = Pin(PIN_LED, Pin.OUT)
    led.low()

def led_off():
    led = Pin(PIN_LED, Pin.OUT)
    led.high()
