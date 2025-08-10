import sqlite3, datetime, requests
from flask import Flask, request

def sendget(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful!")
        print("Content:")
        print(response)  # Assuming the response is JSON
    else:
        print(f"Request failed with status code: {response.status_code}")
    return response    

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask server!</h1>"

@app.route('/data')
def get_data():
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
    conn = sqlite3.connect('weather.db')

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
    rtfreq REAL
);
'''
    cursor.execute(create_table_sql)
    conn.commit() # Commit changes to the database
    print("Table 'wdata' created successfully.")

    event_time = datetime.datetime.now()
    # Insert a single row
    cursor.execute("INSERT INTO wdata (tempf, humidity,indoortempf,rainin, windspeedmph,event_time,baromin,windgustmph,winddir,id_user,dailyrainin,solarradiation,uv,absbaromin,softwaretype,action,realtime,rtfreq,indoorhumidity) VALUES (?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (tempf, humidity, indoortempf, rainin, windspeedmph,event_time, baromin,windgustmph,winddir,id_user,dailyrainin,solarradiation,uv,absbaromin,softwaretype,action,realtime,rtfreq,indoorhumidity))

    conn.commit()
    print("Data inserted successfully.")
    
    #This is where we can repeat the data we received to wunderground.com or other pws recording sites. for test I send to my test site
    # here we can also do the fix on the daily rain fall value due to bug in my weather station that reboots every 30 minutes  
    host = "192.168.1.22:8080" 
    path = "/data?"
    urlsend="http://"+host+path+"ID="+id_user+"&PASSWORD="+password+"&action=updateraw&dateutc=now&winddir="+winddir+"&windspeedmph="+windspeedmph+"&tempf="+tempf+"&humidity="+humidity+"baromin="+baromin+"&rainin="+rainin    
    
    #status=sendget(urlsend)
    #print (f"sendget status{status}")

    return f"<h1>Temp F.: {tempf}</h1>"

if __name__ == '__main__':
    app.run(debug=True) #defalt port 5000
