#https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image

from colorthief import ColorThief
color_thief = ColorThief('/path/to/imagefile')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)