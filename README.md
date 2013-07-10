# BRZR Desktop

### We've each been there at some point in time. Waiting in line at the conference registration check-in table to pick up our shirt and name tag, as the poor volunteer tries to look up our name, find our badge, and check us in. This can take 30 seconds or longer sometimes, and with 300 people waiting to check in, it would be great to speed this process up.

### What is it?

_BRZR_, pronounced breezer, is a suite of open source conference attendee check-in applications that try to ease the bottleneck of accounting for attendees the morning of a conference or camp. Development is initially funded by the Innovision Directorate of the [National Geospatial Intelligence Agency.](http://www.nga.mil)

Using an inexpensive [laser barcode scanner](http://www.amazon.com/gp/product/B003OUQ174/ref=oh_details_o02_s01_i00?ie=UTF8&psc=1), like the one below, you can quickly scan UPC codes on attendee badges as they check-in at the registration table before the conference begins.

![](http://ecx.images-amazon.com/images/I/31jZezFndXL._SX385_.jpg)

For portability and ease of use, this application can be used with a [Raspberry Pi](http://raspberrypi.org).

![](http://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/RaspberryPi.jpg/320px-RaspberryPi.jpg)

If you add the [LCD Display](http://www.adafruit.com/products/1110), you don't even need to lug a monitor around with you. 

![](http://www.adafruit.com/images/medium/1110_MED.jpg)

### How does it work?

The desktop application is written entirely in [Python](http://python.org) which makes it cross-platform and usable on almost all operating systems.

When you print your attendee badges, simply add a [UPC](http://en.wikipedia.org) to the badge with a unique number assigned to a pre-registered attendee. When the attendee checks in the day of the conference, scan the barcode and you're done. BRZR stores this barcode and you can export it later to account for attendance.

### Requirements

1. [Python 2.7](http://python.org)

2. [SQLite3](http://www.sqlite.org/)

3. Optional: To use this with a Raspberry Pi with the [LCD Display](http://www.adafruit.com/products/1110), you'll need to add the [Adafruit_CharLCDPlate](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCDPlate) directory to the `brzr` directory of this application. The `Adafruit_I2c.py` and the `AdafruitMCP230xx.py` is symlinked to their respective folders from the Adafruit repository. Simply copy these two files into the `Adafruit_CharLCDPLATE` directory as well. In the `Adafruit_CharLCDPlate`, now create an empty `__init__.py` file. This is part of [Adafruit's](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code) awesome opensource repository.

4. Your brzr application folder should now look like this:

        >|- brzr-desktop
            |-- brzr
                |--- Adafruit_CharLCDPlate
                   |---- Adafruit_CharLCDPlate.py
                   |---- Adafruit_I2C.py			
                   |---- Adafruit_MCP230xx.py
                   |---- __init.py__
                |--- brzr.py
                |--- __init.py__
            |-- db
                |--- schema.sql
            |-- brzr.cfg
            |-- settings.py
            |-- app.py
            |-- README.md

#### Getting Started

1. Clone this repository.

2. Set up the database:
    
    2.1 Import the schema.sql from the db directory:
    
    2.1.1  `$ sqlite3 db/yourdbname.db < db/schema.db`

3. Copy the `brzr.cfg.example` to `brzr.cfg`

4. Edit the `brzr.cfg` with the path to your database, and add your event name.

5. Start the application: `$ python app.py`

6. Scan an attendee's Barcode.

7. Repeat.

8. Export the database:
    
    8.1 `$ sqlite> mydb.db`  
    
    8.2 `$ sqlite> .mode csv`
    
    8.3 `$ sqlite> .header on`
    
    8.4 `$ sqlite> .out export.csv`
    
    8.5 `$ sqlite> select * from attendees;`
    
    8.6 `$ sqlite> .exit`
    
    8.7 Your export.csv contains a CSV dump of the database.

6. Profit! 

7. **NOTE:** If you're using the LCD, you'll need start the application with root privileges to access the SMBUS: `$ sudo python app.py`

### License

BRZR is entirely open source under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html) license.

***Note: This README is incomplete***

 
