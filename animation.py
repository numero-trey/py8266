import machine
from math import sin, radians
import os


class Throbber:
    def __init__(self, strip):
        self.strip = strip
        self.speed = 2
        self.pos = 0
        self.color = 0
        self.brightness = 255
        self.timer = None

    def do_step(self):
        v = int(sin(radians(self.pos)) * 255)
        self.strip.set_all_leds(self.color, 255, v)
        self.strip.blit()
        self.pos += self.speed
        if self.pos >= 180:
            self.color += int(os.urandom(1)[0] * 86 / 256) + 16
            self.color %= 256
        self.pos %= 180

    def run(self, delay):
        self.timer = machine.Timer(-1)
        self.timer.init(
            period=delay,
            mode=machine.Timer.PERIODIC,
            callback=lambda t: self.do_step())

    def stop(self):
        self.timer.deinit()


class Spinner:
    def __init__(self, strip):
        self.strip = strip
        self.speed = 0
        self.pos = 0
        self.color = 0
        self.brightness = 255
        self.timer = None

    def do_step(self):
        self.strip.set_all_leds(0, 0, 0)
        self.strip.leds[self.pos].set_hsv(self.color, 255, self.brightness)
        self.strip.blit()
        self.pos += 1
        self.pos %= self.strip.num_leds
        self.color += self.speed
        self.color %= 1

    def run(self, delay):
        self.timer = machine.Timer(-1)
        self.timer.init(
            period=delay,
            mode=machine.Timer.PERIODIC,
            callback=lambda t: self.do_step())

    def stop(self):
        self.timer.deinit()
