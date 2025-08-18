import sqlite3, datetime, requests, configparser
from flask import Flask, request

lastday = 0
lastweek = 0
lastmonth = 0
lastyear = 0
mydailyrainin = 0.00
myweeklyrainin = 0.00
mymonthlyrainin = 0.00
myyearlyrainin = 0.00
lastdailyrainin = 0.00

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

def sendget(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful!")
        print("Content:")
        print(response)  # Assuming the response is JSON
    else:
        print(f"Request failed with status code: {response.status_code}")
    return response   

def correctrain(dailyrainin):
    global lastday
    global mydailyrainin
    global lastdailyrainin
    event_time = datetime.datetime.now()
    print(f"even_time: {event_time}")
    day = event_time.day
    print(f"day: {day}")
    if day > lastday:
        print ("true")
        lastday = day
        mydailyrainin = 0.00
        lastdailyrainin = 0.00
    else:
        print (f"dailyrainin: {dailyrainin}")
        if lastdailyrainin < float(dailyrainin):
            mydailyrainin = (float(dailyrainin) - lastdailyrainin) + mydailyrainin
            lastdailyrainin = float(dailyrainin)
        else:
            if lastdailyrainin > float(dailyrainin):
                if float(dailyrainin) > 0:
                    lastdailyrainin = float(dailyrainin)
   
    print (f"mydailyrainin: {mydailyrainin}")
    print (f"lastdailyrainin: {lastdailyrainin}")
    return mydailyrainin
 

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask server!</h1>"

@app.route('/data')
def get_data():
    global config
    # Access query parameters from a GET request
    tempf = request.args.get('tempf')
    humidity = request.args.get('humidity')
    indoortempf = request.args.get('indoortempf')
    indoorhumidity = request.args.get('indoorhumidity')
    id_user = request.args.get('ID')
    password = request.args.get('PASSWORD')
    winddir = request.args.get('winddir')
    windspeedmph = request.args.get('windspeedmph')
    windgustmph = request.args.get('windgustmph')
    rainin = request.args.get('rainin')
    dailyrainin = request.args.get('dailyrainin')
    solarradiation = request.args.get('solarradiation')
    uv = request.args.get('UV')
    absbaromin = request.args.get('absbaromin')
    baromin = request.args.get('baromin')
    softwaretype = request.args.get('softwaretype')
    action = request.args.get('action')
    realtime = request.args.get('realtime')
    rtfreq = request.args.get('rtfreq') 
 
    print("Temp F:",tempf)
    print("")
    print("humidity:",humidity)
    
     # Connect to a database file (creates it if it doesn't exist)
    conn = sqlite3.connect(config['DATABASE']['filename'])

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # SQL command to create a table named 'users'
    create_table_sql = '''
CREATE TABLE IF NOT EXISTS wdata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_time TIMESTAMP,
    tempf REAL,
    humidity REAL,
    indoortempf REAL,
    indoorhumidity REAL,
    id_user TEXT,
    password TEXT,
    winddir REAL,
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
    rtfreq REAL,
    mydailyrainin REAL
);
'''
    cursor.execute(create_table_sql)
    conn.commit() # Commit changes to the database
    print("Table 'wdata' created successfully.")
    mydailyrainin = correctrain(dailyrainin)
    print (f"mydailyrainin in mm: {mydailyrainin*25.4}")
    event_time = datetime.datetime.now()
    # Insert a single row
    cursor.execute("INSERT INTO wdata (tempf, humidity,indoortempf,rainin, windspeedmph,event_time,baromin,windgustmph,winddir,id_user,dailyrainin,solarradiation,uv,absbaromin,softwaretype,action,realtime,rtfreq,indoorhumidity,mydailyrainin) VALUES (?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (tempf, humidity, indoortempf, rainin, windspeedmph,event_time, baromin,windgustmph,winddir,id_user,dailyrainin,solarradiation,uv,absbaromin,softwaretype,action,realtime,rtfreq,indoorhumidity,mydailyrainin))

    conn.commit()
    print("Data inserted successfully.")
    
    
    
    #This is where we can repeat the data we received to wunderground.com or other pws recording sites. for test I send to my test site
    # here we can also do the fix on the daily rain fall value due to bug in my weather station that reboots every 30 minutes
    port = config['SERVER']['port']  
    host = config['SERVER']['host']
    host = host+port
    path = config['SERVER']['path']
    id_user = config['USER']['id_user']
    password = config['USER']['password']
    if config.getboolean('SERVER', 'send_corrected_rain'):
        dailyrainin = str(mydailyrainin)
    print (f"host: {host}")

    urlsend="http://"+host+path+"ID="+id_user+"&PASSWORD="+password+"&action=updateraw&dateutc=now&winddir="+winddir+"&windspeedmph="+windspeedmph+"&tempf="+tempf+"&humidity="+humidity+"&baromin="+baromin+"&absbaromin="+absbaromin+"&rainin="+rainin+"&dailyrainin="+dailyrainin+"&UV="+uv+"&solarradiation="+solarradiation+"&windgustmph="+windgustmph    

    if config.getboolean('SERVER', 'enable_repeater'):    
        status=sendget(urlsend)
        print (f"sendget status{status}")
    print (f"urlsend: {urlsend}")

    return f"<h1>Temp F.: {tempf}</h1>"

if __name__ == '__main__':
    app.run(debug=True) #defalt port 5000
