#!/usr/bin/env python

import settings
from brzr import *

#database_name = settings.database_name
#table_name = settings.table_name

# Debug
#checker(text=text, params=params)

# Check our platform to see if we are on a Pi and have the LCD Library
check_platform()

# Confirm the database and table exists.
#check_database(database_name, table_name)
verify_database(database_name=settings.database_name)

# Tell the user we are ready to scan a barcode

# If we are ready to scan, wait for input
## When we get input, store it as a new record.
## Tell the user it worked.
## Repeat
"""Get this: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_CharLCDPlate/LCDtest.py
"""
