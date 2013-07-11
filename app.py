#!/usr/bin/env python

import settings
from brzr.brzr import *


# Check our platform to see if we are on a Pi and have the LCD Library
check_platform()

# Confirm the database and table exists.
verify_database(database_name=settings.database_name, event_name=settings.event_name)

# Tell the user we are ready to scan a barcode and then wait for input.
# Loop forever. There is probably a better way to do this.
while True:
    add_records(database_name=settings.database_name, event_name=settings.event_name)
