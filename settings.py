import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('brzr.cfg')

database_name = config.get('main', 'database_name')
event_name = config.get('main', 'event_name')
