'''primary module functions'''

import math
import colorsys

import numpy as np

GOLDEN_ANGLE = 720/(3+math.sqrt(5))


def lrgb2srgb(lrgb):
    '''convert linear rgb to srgb'''
    func = lambda lval: (12.92*lval) if lval < 0.0031308 else (1+0.055)*(lval**(1/2.4)) - 0.055
    return np.vectorize(func)(lrgb)


def hue_stretch(hue):
    '''stretch different regions of the hue so that each "color" is equally likely'''
    hues = np.linspace(-22.5, 382.5, 10)
    mapped = np.array([-13, 8, 27, 81, 134, 230, 243, 255, 347, 368])
    return np.interp(hue, hues, mapped)


def generate_color(color_num, saturation=0.9, value=0.9):
    '''
    create a nice looking color
    color_num: color in sequence to generate
    '''
    hue = (color_num * GOLDEN_ANGLE) % 360
    hue = hue_stretch(hue)
    return lrgb2srgb([[np.array(colorsys.hsv_to_rgb(hue, saturation, value))]])


def generate_colors(num_colors, saturation=0.9, value=0.9):
    '''create a sorted list of colors containing "num_colors" elements'''
    def get_hue(rgb_color):
        '''get hsv hue from an srgb color'''
        return colorsys.rgb_to_hsv(*(rgb_color[0][0]))[0]

    return sorted([generate_color(i, saturation, value) for i in range(num_colors)], key=get_hue)
