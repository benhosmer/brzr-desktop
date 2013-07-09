#!/usr/bin/env python

import settings
from brzr.brzr import *


#database_name = settings.database_name
#table_name = settings.table_name

# Debug
#checker(text=text, params=params)

# Check our platform to see if we are on a Pi and have the LCD Library
check_platform()

# Confirm the database and table exists.
verify_database(database_name=settings.database_name, event_name=settings.event_name)

# Tell the user we are ready to scan a barcode and then wait for input.
add_records(event_name=settings.event_name)

# If we are ready to scan, wait for input
## When we get input, store it as a new record.
## Tell the user it worked.
## Repeat
"""Get this: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_CharLCDPlate/LCDtest.py
"""
