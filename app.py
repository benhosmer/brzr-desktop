#!/usr/bin/env python

import platform
import sqlite3


platform_type = platform.machine()
lcd_enabled = False
text = ['Platform:', 'LCD?:']
params = [platform_type, lcd_enabled]

# If our platform is arm, see if we have the LCD Library.
if platform_type == 'Arm':
    try:
        from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
        lcd_enabled = True
    except:
        print "You don't appear to have the LCD Lbrary, defaulting to the\
               standrd command-line interface..."
        pass


def checker(text, params ):
    """Goofy function to keep sanity.
    """
    for platform, lcd in zip(text, params):
        print platform, '-->', lcd 


checker(text=text, params=params)


"""
If we have an LCD and are on ARM, we're probably running on a raspberry
pi. If we aren't we need to simply print the UI to the user instead of 
outputting to the LCD.
"""

"""
First order of business, tell the user we are ready to scan, and prompt them
to scan some text. Use the LCD if we can, if not just print
def scanner(input):
    if lcd_enabled = True:
        if platform_type == 'Arm':
"""


#print "Platform:", platform_type
#print "Lcd?:", lcd_enabled

"""Get this: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_CharLCDPlate/LCDtest.py
"""

