#!/usr/bin/env python

import platform
import sqlite3

class FeedbackMessage:
        """Output a success or error message depending on the user's platform
        """
        def platform_checker():
            platform_type = platform.machine()
            lcd_enabled = False
            text = ['Platform:', 'LCD?:']
            params = [platform_type, lcd_enabled]


def check_platform():
    """A function that determines our platform. If it is ARM, most likely it
    is a Raspberry Pi. If it is a Pi, check if the LCD library is present. 
    Format the UI messages accordingly.
    """
    platform_type = platform.machine()
    lcd_enabled = False
    text = ['Platform:', 'LCD?:']
    params = [platform_type, lcd_enabled]
    print "Checking platform type..."
    if platform_type == 'Arm':
        try:
            from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
            lcd_enabled = True
        except:
            print "You don't appear to have the LCD Lbrary, defaulting to the"\
                  " standrd command-line interface..."
    print "You don't appear to be using a Raspberry Pi, we'll default to the"\
          " command-line interface."


# Create a table with the following SQL syntax:
# create table (id integer primary key, name text, xloc int, yloc int);
# insert into places values(NULL, 'Stream', 300.3, 100.4);
# select * from places;
# 1|Stream|300.3|100.4

con = sqlite3.connect('db/testing.db')


def read_records():
    """Read the records from the database
    """
    with con:
        cur = con.cursor()
        cur.execute("select * from places")
        rows = cur.fetchall()
        for row in rows:
            print row


def add_records(idnum, name, xloc, yloc):
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO places VALUES (?, ?, ?, ?)", (idnum, name, xloc, yloc))
        con.commit()


def checker(text, params ):
    """Goofy function to keep sanity.
    """
    for platform, lcd in zip(text, params):
        print platform, '-->', lcd 


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

