import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Access values from sections
print(f"id_user: {config['USER']['id_user']}")
print(f"password: {config['USER']['password']}")
print(f"Database filename: {config['DATABASE']['filename']}")
print(f"Server Port: {config['SERVER']['port']}")
print(f"Server path: {config['SERVER']['path']}")
print(f"Server host: {config['SERVER']['host']}")


# Access values with type conversion
print(f"Server Port (int): {config.getint('SERVER', 'port')}")
print(f"Server enable_repeater: {config.getboolean('SERVER', 'enable_repeater')}")
print(f"Server send_corrected_rain: {config.getboolean('SERVER', 'send_corrected_rain')}")

if config.getboolean('SERVER', 'enable_repeater'):
    print("enable _repeater true")

# List all sections
print(f"Sections: {config.sections()}")

# Iterate through options in a section
print("\n[SERVER] options:")
for key in config['SERVER']:
    print(f"  {key}: {config['SERVER'][key]}")
