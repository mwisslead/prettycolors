'''
generate pretty colors by stretching hsv to have each color inhabit an equal amount of the hsv
angle and then returning a srgb color with h = n times the golden angle and s and v equal to 0.95
'''

from .prettycolors import generate_color, generate_colors
