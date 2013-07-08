#!/usr/bin/env python

# Todo: Abstract the message to be useful for command-line and the LCD for the Pi.

import platform
import sqlite3
database_name = "db/test.db"
idnum = None  # None == NULL in sql. This increments our record id automatically.

lcd_enabled = False  # Default to no LCD.
con = sqlite3.connect(database_name)
cur = con.cursor()


class CustomOutput(object):
    """Format UI output for command-line, or the LCD if we are using a Pi.
    """
    def formatter(self, message):
        if lcd_enabled:
            lcd = Adafruit_CharLCDPlate()
            lcd.clear()
            lcd.message(output)
        else:
            print message

output = CustomOutput()


def check_platform():
    """Determines our platform. If it is ARM, most likely it
    is a Raspberry Pi. If it is a Pi, check if the LCD library is present. 
    Format the UI messages accordingly.
    """
    global lcd_enabled
    platform_type = platform.machine()
    output.formatter("Checking platform type...")
    if platform_type == 'Arm':
        try:
            from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
            lcd_enabled = True
            return lcd_enabled
        except:
            output.formatter("You don't appear to have the LCD Lbrary, defaulting to the"\
                  " standard command-line interface...")
    #output.formatter("Platform Type:", platform_type)
    #print "***Default Prompt.***"


def verify_database(database_name, event_name):
    """Connect to the database and see if the table exists. Otherwise the rest is pointless
    """
    try:
        con.cursor()
        print "Database found!", database_name
        cur.execute("SELECT * FROM conference WHERE event_name")
        print "Table found!"
    except:
        print "Error: Database or table not found!"


def add_records(event_name):
    """Prompt the user to enter a record and then store it with the event event_name.
    """
    attendee_id = raw_input("Scan a barcode:\n")
    with con:
        cur.execute("INSERT INTO conference VALUES (?, ?, ?)", (idnum, attendee_id, event_name))
        con.commit()
    with con:
        cur.execute("SELECT attendee_id FROM conference where attendee_id=(?) and event_name=(?)", (attendee_id, event_name))
        result = cur.fetchone()
        print "Record", "".join(result), "added."
