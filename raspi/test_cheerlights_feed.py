# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import requests

# I'm going to use a var to check if I've seen the color before
color = 'black'
cheerlights = color


# Main program logic follows:
if __name__ == '__main__':

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
                print 'match'
            elif cheerlights == 'green':
                print 'match'
            elif cheerlights == 'blue':
                print 'match'
            elif cheerlights == 'purple':
                print 'match'
            elif cheerlights == 'cyan':
                print 'match'
            elif cheerlights == 'magenta':
                print 'match'
            elif cheerlights == 'yellow':
                print 'match'
            elif cheerlights == 'orange':
                print 'match'
            elif (cheerlights == 'white' or cheerlights == 'warmwhite'):
                print 'match'
            elif (cheerlights == 'black' or cheerlights == 'off'):
                print 'match'
            else:
                print 'non-match!'
            print cheerlights
            color = cheerlights
            time.sleep(16)
