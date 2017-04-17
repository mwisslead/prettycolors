'''command line program usage example'''

from __future__ import print_function

import math
import argparse

from unittest import TestCase

import numpy as np

import matplotlib.pyplot as plt

from prettycolors import generate_colors


class TestGenerate(TestCase):
    def test_generate_color(self):
        '''main function to run if ran as main'''

        colors = 24
        factor = next(i for i in range(int(math.sqrt(colors)), 0, -1) if colors % i is 0)
        img = np.reshape(generate_colors(colors), (factor, colors//factor, 3))

        plt.imshow(img, interpolation='none')
        plt.show()
