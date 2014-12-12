# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import requests

from neopixel import *

# LED strip configuration:
LED_COUNT   = 59      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

# I'm going to use a var to check if I've seen the color before
color = 'black'
cheerlights = color

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)


# Main program logic follows:
if __name__ == '__main__':

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print 'Press Ctrl-C to quit.'
    while True:
        # Read the thingspeak feed to get the current color
        try:
            r = requests.get('http://api.thingspeak.com/channels/1417/field/1/last.json').json()
            cheerlights = r['field1']
        except:
            pass
        if cheerlights != color:
            #New color, do stuff
            if cheerlights == 'red':
                colorWipe(strip, Color(255, 0, 0))  # Red wipe
            elif cheerlights == 'green':
                colorWipe(strip, Color(0, 255, 0))  # Green wipe
            elif cheerlights == 'blue':
                colorWipe(strip, Color(0, 0, 255))  # Blue wipe
            elif cheerlights == 'purple':
                colorWipe(strip, Color(102, 51, 204)) # Purple wipe
            elif cheerlights == 'cyan':
                colorWipe(strip, Color(0, 255, 255))  # Cyan wipe
            elif cheerlights == 'magenta':
                colorWipe(strip, Color(255, 0, 255))  # Magenta wipe
            elif cheerlights == 'yellow':
                colorWipe(strip, Color(255, 255, 0))  # Yellow wipe
            elif cheerlights == 'orange':
                colorWipe(strip, Color(255, 153, 0))  # Orange wipe
            elif (cheerlights == 'white' or cheerlights == 'warmwhite'):
                colorWipe(strip, Color(255, 255, 255)) # White wipe
            elif (cheerlights == 'black' or cheerlights == 'off'):
                colorWipe(strip, Color(0, 0, 0))  # Black wipe
            else:
                print 'non-match!'
            print cheerlights
            color = cheerlights
            time.sleep(16)

        # Theater chase animations.
        theaterChase(strip, Color(127, 127, 127))  # White theater chase
        theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        theaterChase(strip, Color(  0, 127,   0))  # Green theater chase
        # Rainbow animations.
        rainbow(strip)
        rainbowCycle(strip)
        theaterChaseRainbow(strip)
