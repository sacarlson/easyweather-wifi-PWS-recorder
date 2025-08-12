easyweather wifi PWS recorder/repeater

This very simple python program will setup a local website on Linux using python that will recieve and record data from an easyweather pro wifi weather station.  The data recieved will be recorded and corrected for the daily rain fall error present in the firmware of the device I now own.  The error is due to the problem with the device I have that forces itself to reset every 30 minute that will zero the present days rain fall count of the device when it sends its next data point to ecowitt or wunderground.com after reset.  
  Instead of sending data direct to ecowitt or other, the weather station device will be programed to send the data to this local net server running this program.  Each time data is received this program will correct the daily rain fall data and send the rest of the received data to eather ecowitt or wunderground or both.  later we might find a way to make use of the collected local data but for now this is all we need.

The config.ini file is used to setup wether you want to repeat the collected data or not.  If data is to be repeated it provides the setup of what host you want to send the repeated data to including what port the user ID and password etc.

I have now also added the code that fixes my problem with daily rain fall due to 30 minute resets.  This feature may not be needed for your device so you might want to set send_corrected_rain = no in config to disable corretion.

I found that sqlitebrowser db browser for sqlite works fantastic to view the local caputured data and can even graph the data to some degree.  I highly recomend it for testing the results of the captured data.

This is still in very early development and is not setup with any security in mind.  Not sure it will ever be feasible to set it up on a full world WAN network without doing some much better security checks.

I'm running this on Linux mint on my home PC but should run on most any Linux or even windows with python3 installed

to install the only thing I needed to add to python3 was Flask, request modules and venv.  seems the other imports I use were already built into python3.

to install venv vertual envirnment for python
apt install python3.10-venv

to install Flask and request modules within venv:
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv

Activate the environment
$ . .venv/bin/activate

Install Flask module
pip install Flask

Install requests module
pip install requests

then just cd to myproject and run start.sh or
$ flask --app weather_repeater.py run --host=0.0.0.0 

Other programs included:
The helloworld.py is just used as a test and what I used to learn from. I used it to verify that the repeater sends the request get with correct data and format before I started sending data to wunderground.  you can use it to test or play with as you will.

I also did some preliminary tests with sqlite_example.py to learn how to use sqlite with python before I incorporated it into the weather_repeater.py.  This is my first python project so I had to learn each step one at a time.  I left these program  in the package just as a reference of how some things work.

I must say I had fun playing with this project. I found python to be a very easy language to learn with such fantastic support to be found.  I hope you have as much fun with it as I have.  Good Luck.

