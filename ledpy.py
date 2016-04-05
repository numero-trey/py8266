from esp import neopixel_write
import machine

GAMMA = 2.8
GAMMA_SHIFT = 40


class Led(object):
    def __init__(self, hsv=(0, 0, 0), rgb=None):
        self.set_hsv(0, 0, 0)

    def set_hsv(self, *hsv):
        self.h = hsv[0]
        self.s = hsv[1]
        self.v = hsv[2]

    def to_rgb(self):
        return hsv_to_rgb_rainbow_opt(self.h, self.s, self.v)


class LedStrip:
    def __init__(self, pin, num_leds):
        self.pin = machine.Pin(pin, machine.Pin.OUT)
        self.num_leds = num_leds
        self.leds = []
        for i in range(num_leds):
            self.leds.append(Led())

    def blackout(self):
        for i in range(self.num_leds):
            self.leds[i].set_hsv(0, 0, 0)
        self.blit()

    def set_all_leds(self, h, s, v):
        for i in range(self.num_leds):
            self.leds[i].set_hsv(h, s, v)

    def _get_buff(self):
        buff = bytearray(self.num_leds * 3)
        for i in range(self.num_leds):
            r, g, b = self.leds[i].to_rgb()
            buff[i * 3] = g
            buff[i * 3 + 1] = r
            buff[i * 3 + 2] = b
        return buff

    def blit(self):
        neopixel_write(self.pin, self._get_buff(), True)


def scale_gamma(val):
    return int((((val + GAMMA_SHIFT)/(255 + GAMMA_SHIFT)) ** GAMMA) * 255)


def hsv_to_rgb_rainbow_opt(hue, sat, val):
    """Convert HSV to RGB with constant brightness in rainbow mode."""
    K255 = 255
    K171 = 171
    K170 = 170
    K85 = 85

    offset = hue & 0x1F
    offset8 = offset << 3
    third = offset8 // 3
    r = g = b = 0

    if (hue & 0x80) == 0:
        if (hue & 0x40) == 0:
            if (hue & 0x20) == 0:
                r = K255 - third
                g = third
                b = 0
            else:
                r = K171
                g = K85 + third
                b = 0
        else:
            if (hue & 0x20) == 0:
                twothirds = offset8 * 2 // 3  # 256 * 2 / 3
                r = K171 - twothirds
                g = K170 + third
                b = 0
            else:
                r = 0
                g = K255 - third
                b = third
    else:
        if (hue & 0x40) == 0:
            if (hue & 0x20) == 0:
                r = 0
                twothirds = offset8 * 2 // 3
                g = K171 - twothirds
                b = K85 + twothirds
            else:
                r = third
                g = 0
                b = K255 - third
        else:
            if (hue & 0x20) == 0:
                r = K85 + third
                g = 0
                b = K171 - third
            else:
                r = K170 + third
                g = 0
                b = K85 - third
    if sat != 255:
        if sat == 0:
            r = b = g = 255
        else:
            if r:
                r = r * sat >> 8
            if g:
                g = g * sat >> 8
            if b:
                b = b * sat >> 8
            desat = 255 - sat
            desat = desat * desat >> 8
            brightness_floor = desat
            r += brightness_floor
            g += brightness_floor
            b += brightness_floor

    if val != 255:
        val = scale_gamma(val)
        if val == 0:
            r = g = b = 0
        else:
            if r:
                r = r * val >> 8
            if g:
                g = g * val >> 8
            if b:
                b = b * val >> 8

    return (r, g, b)
