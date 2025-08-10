easyweather wifi PWS recorder/repeater

This very simple python program will setup a local website on Linux using python that will recieve and record data from an easyweather pro wifi weather station.  The data recieved will be recorded and corrected for the daily rain fall error present in the firmware of the device I now own.  The error is due to the problem with the device I have that forces itself to reset every 30 minute that will zero the present days rain fall count of the device when it sends its next data point to ecowitt or wunderground.com after reset.  
  Instead of sending data direct to ecowitt or other, the weather station device will be programed to send the data to this local net server running this program.  Each time data is received this program will correct the daily rain fall data and send the rest of the received data to eather ecowitt or wunderground or both.  later we might find a way to make use of the collected local data but for now this is all we need.

I plan to use python3 using the import Flask and sqlite support libs.  Flask features makes it easy to setup the website server input.  Sqlite will be used to time stamp and save the data collected.

I found that db browser for sqlite works fantastic to view the local caputured data and even can graph the data to some degree.  I highly recomend it for testing the results of the captured data.

This is still in very early development and is not setup with any security in mind.  Not sure it will ever be feasible to set it up on a full world WAN network without doing some much better security checks.

I'm running this on Linux mint on my home PC but should run on most any Linux or even windows with python3 installed

to install the only thing I needed to add to python3 was Flask.  seems the other imports I use were already built into python3.
to install Flask:
$ mkdir myproject
$ cd myproject
$ python3 -m venv .venv

Activate the environment
$ . .venv/bin/activate

Install Flask
pip install Flask

then just cd to myproject and run start.sh or
$ flask --app weather_repeater.py run --host=0.0.0.0 

I have plans to setup config files to use to costomize the host ports and path and to activate or disable the repeater mode but at time of this writing I hadn't goten that far but have some examples that I had started to play with within this project if you want to add that feature before me.  At this point you must modify the code to put in the custom values you want for your systems.

The helloworld.py is just used as a test. I used it to verify that the repeater sends the request get with correct data and format before I started sending data to wunderground.  you can use it to test or play with as you will.

I also did some preliminary tests with sqlite_example.py to learn how to use sqlite with python before I incorporated it into the weather_repeater.py.  This is my first python project so I had to learn each step one at a time.

I must say I had fun playing with this project. I found python to be a very easy language to learn with such fantastic support to be found.  I hope you have as much fun with it as I have.  Good Luck.

