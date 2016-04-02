import machine
from math import sin, radians, log

class Throbber:
    def __init__(self, strip):
        self.strip = strip
        self.speed = 1
        self.pos = 0
        self.color = 0
        self.brightness = 255
        self.timer = None

    def do_step(self):
        v = int(sin(radians(self.pos)))
        self.strip.set_all_leds(self.color, 1, v)
        self.strip.blit()
        self.pos += self.speed
        self.pos %= 180

    def run(self, delay):
        self.timer = machine.Timer(-1)
        self.timer.init(
            period=delay,
            mode=machine.Timer.PERIODIC,
            callback=lambda t: self.do_step())

class Spinner:
    def __init__(self, strip):
        self.strip = strip
        self.speed = 0
        self.pos = 0
        self.color = 0
        self.brightness = 1
        self.timer = None

    def do_step(self):
        self.strip.set_all_leds(0, 0, 0)
        self.strip.leds[self.pos].set_hsv(self.color, 1, self.brightness)
        self.strip.blit()
        self.pos += 1
        self.pos %= self.strip.num_leds
        self.color += self.speed
        self.color %= 1

    def run(self, delay):
        tim = machine.Timer(-1)
        self.timer = tim.init(
            period=delay,
            mode=machine.Timer.PERIODIC,
            callback=lambda t: self.do_step())
