import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Access values from sections
print(f"id_user: {config['USER']['id_user']}")
print(f"Database filename: {config['DATABASE']['filename']}")
print(f"Server Port: {config['SERVER']['port']}")

# Access values with type conversion
print(f"Server Port (int): {config.getint('SERVER', 'port')}")

# List all sections
print(f"Sections: {config.sections()}")

# Iterate through options in a section
print("\n[SERVER] options:")
for key in config['SERVER']:
    print(f"  {key}: {config['SERVER'][key]}")
