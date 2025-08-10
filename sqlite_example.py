import sqlite3

# Connect to a database file (creates it if it doesn't exist)
conn = sqlite3.connect('weather.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL command to create a table named 'users'
create_table_sql = '''
CREATE TABLE IF NOT EXISTS wdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tempf REAL,
    humidity REAL,
    indoortempf REAL,
    indoorhumidity REAL,
    id_user TEXT,
    password TEXT,
    windir REAL,
    windspeedmph REAL,
    windgustmph REAL,
    rainin REAL,
    dailyrainin REAL,
    solarradiation REAL,
    uv REAL,
    absbaromin REAL,
    baromin REAL,
    softwaretype TEXT,
    action TEXT,
    realtime TEXT,
    rtfreq REAL
);
'''
cursor.execute(create_table_sql)
conn.commit() # Commit changes to the database
print("Table 'wdata' created successfully.")

# Insert a single row

cursor.execute("INSERT INTO wdata (tempf, humidity,indoortempf) VALUES (?, ?, ?)", (25.8, 73, 27.7))

conn.commit()
print("Data inserted successfully.")
