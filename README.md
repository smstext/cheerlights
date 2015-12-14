CheerlightsPi
=============

Control Adafruit NeoPixels using a RaspberryPi and the [Cheerlights](http://www.cheerlights.com) feed!

Clone or download this project at [Github](https://github.com/davidbradway/CheerlightsPi).

## Desription
Last year, I was inspired by [Dave Koerner's NØHIO LOGBOOK](http://n0hio.wordpress.com/2013/12/06/cheerlights-project).

Then I put together a Cheerlights display using a Ubuntu computer, Adafruit FLORA Arduino, and 8 FLORA NeoPixels:
https://www.youtube.com/watch?v=lJNamwgsGlE
https://plus.google.com/photos?pid=5957627945770423090&oid=116675413971505814200

This year, thanks to Tony DiCola's Python wrapper for the the excellent rpi_ws281x library created by Jeremy Garff, I could redo the project and cut out the Arduino!
[Follow the Adafruit guide here to get your NeoPixels working with Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview)

## Installation, with some of the Requirements listed
    sudo apt-get update
    sudo apt-get install -y python-pip python-serial python-requests
    pip install requests
    git clone git@github.com:davidbradway/CheerlightsPi.git

## Requires the rpi_ws281x library be installed
### Easy install on Raspbian
    wget https://github.com/tdicola/rpi_ws281x/raw/master/python/dist/rpi_ws281x-1.0.0-py2.7-linux-armv6l.egg
    sudo easy_install rpi_ws281x-1.0.0-py2.7-linux-armv6l.egg

### Compile if Easy install doesn't work
    sudo apt-get update
    sudo apt-get install -y build-essential python-dev git scons swig
    git submodule init
    git submodule update
    cd rpi_ws281x
    scons
    cd python
    sudo python setup.py install
    # Test Library
    sudo python rpi_ws281x/python/examples/strandtest.py 

## Test the cheerlights feed
    python test_cheerlights_feed.py

## Usage
    cd CheerlightsPi/
    sudo python cheerlights.py

## (Optional) Set up the Python script as a service/daemon
    # Make script service start at boot
    sudo cp cheerlights.sh /etc/init.d/
    sudo chmod 755 /etc/init.d/cheerlights.sh
    sudo update-rc.d cheerlights.sh defaults
    
    # (Optional) To remove the script from start-up, run the following command:
    sudo update-rc.d -f cheerlights.sh remove

    # (Optional) commands for service
    sudo /etc/init.d/cheerlights.sh start
    sudo /etc/init.d/cheerlights.sh status
    sudo /etc/init.d/cheerlights.sh stop

## (Optional) Set up Cron job to respawn service if killed or dropped repeatedly
    sudo crontab -e
    # Add this to root's CRON, and remove the '#' before the '* * * * *...'
    # m h  dom mon dow   command
    #* * * * * /home/pi/repos/CheerlightsPi/autorestart.sh

    # (Optional) Crontab with logging
    #* * * * * /bin/bash /home/pi/repos/CheerlightsPi/autorestart.sh >> /home/pi/myscript.log 2>&1

    # (Optional) check the cron log
    grep CRON /var/log/syslog

    # (Optional) or continuously monitor it
    tail -f /var/log/syslog | grep CRON
