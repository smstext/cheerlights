CheerlightsPi
=============

Control Adafruit NeoPixels using a RaspberryPi and the [Cheerlights](http://www.cheerlights.com) feed.  
Based on original files noisufnoc/CheerlightsPi.  I modified the code to work without the Arduino.
Also based on github.com/tdicola/rpi_ws281x

## Installation
    git clone git@github.com:davidbradway/CheerlightsPi.git
    sudo apt-get install python-pip
    pip install requests

### Easy install on Raspbian
    wget https://github.com/tdicola/rpi_ws281x/raw/master/python/dist/rpi_ws281x-1.0.0-py2.7-linux-armv6l.egg
    sudo easy_install rpi_ws281x-1.0.0-py2.7-linux-armv6l.egg

### Compile if Easy install doesn't work
    sudo apt-get update
    sudo apt-get install build-essential python-dev git scons swig
    git clone https://github.com/tdicola/rpi_ws281x.git
    cd rpi_ws281x
    scons
    cd python
    sudo python setup.py install

## Usage
    sudo python strandtest.py
    sudo python cheerlights.py