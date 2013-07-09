#!/usr/bin/env python

import platform
import sqlite3
database_name = "db/test.db"
idnum = None  # None == NULL in sql. This increments our record id automatically.

lcd_enabled = False  # Default to no LCD.
con = sqlite3.connect(database_name)
cur = con.cursor()


# @TODO: Some the LCD only has 16 characters. We need to add new lines and
# be brief with our messages, otherwise they won't fit on the screen. It would
# also be nice to accpet multiple strings: "mystring", "myotherstring"
class CustomOutput(object):
    """Format the message output for command-line, or the LCD if we are using a Pi.
    """
    def formatter(self, message):
        if lcd_enabled:
            lcd = Adafruit_CharLCDPlate()
            lcd.clear()
            lcd.message(output)
        else:
            print message

message = CustomOutput()


def check_platform():
    """Determines our platform. If it is ARM, most likely it
    is a Raspberry Pi. If it is a Pi, check if the LCD library is present. 
    Format the UI messages accordingly.
    """
    global lcd_enabled
    platform_type = platform.machine()
    message.formatter("Checking platform type...")
    if platform_type == 'armv6l':
        try:
            from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
            lcd_enabled = True
            return lcd_enabled
        except:
            message.formatter("You don't appear to have the LCD Lbrary, defaulting to the"\
                  " standard command-line interface...")
    message.formatter("Platform Type: " + platform_type)
    

def verify_database(database_name, event_name):
    """Connect to the database and see if the table exists. Otherwise the rest is pointless
    """
    try:
        con.cursor()
        message.formatter("Database found!"), database_name
        cur.execute("SELECT * FROM conference WHERE event_name")
        message.formatter("Table found!")
    except:
        message.formatter("Error: Database or table not found!")


def add_records(event_name):
    """Prompt the user to enter a record and then store it with the event event_name.
    """
    message.formatter("Ready..." + "\nScan a barcode:")
    attendee_id = raw_input()
    with con:
        cur.execute("INSERT INTO conference VALUES (?, ?, ?)", (idnum, attendee_id, event_name))
        con.commit()
    with con:
        cur.execute("SELECT attendee_id FROM conference where attendee_id=(?) and event_name=(?)", (attendee_id, event_name))
        result = cur.fetchone()
        success_msg = "Record " + "".join(result) + "\nadded."
        message.formatter(success_msg)
