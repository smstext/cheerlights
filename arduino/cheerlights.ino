#include <Adafruit_NeoPixel.h>

#define PIN 6

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(1, PIN, NEO_GRB + NEO_KHZ800);

void setup()
{
  strip.begin();
  strip.show();  //initialize all pixels to off
  
  // Setup Serial
  Serial.begin(9600);
  delay(100);
  
  Serial.flush();
  delay(100);
}

void loop()
{ 
     // Listen to serial commands from RaspPi
  if(Serial.available() > 0)
  {  
    delay(100); 

    char charIn = 0; 
    byte i = 0; 
    char stringIn[32] = "";
   
    while(Serial.available())
    {
      charIn = Serial.read();
      stringIn[i] = charIn; 
      i += 1;
    }
    
    // Echo Received Commands on the Serial Monitor
    Serial.println("CheerLight Command Received: "+String(stringIn));
    delay(200); 
    
    // Send matching commands LED
    //   Currently it echos the color back to serial for debugging
    if (String(stringIn) == "red")
    {  
            Serial.println("red");
            colorWipe(strip.Color(255, 0, 0), 50); //MAKE IT RED
    }
    else if (String(stringIn) == "green")
    {  
            Serial.println("green");
            colorWipe(strip.Color(0, 255, 0), 50); // MAKE IT GREEN
    }
    else if (String(stringIn) == "blue")
    {  
            Serial.println("blue");
            colorWipe(strip.Color(0, 0, 255), 50); //MAKE IT BLUE
    }
    else if (String(stringIn) == "purple")
    {
            Serial.println("puple");
            colorWipe(strip.Color(102, 51, 204), 50); //MAKE IT PURPLE
     }
     else if (String(stringIn) == "cyan")
     {
             Serial.println("cyan");
             colorWipe(strip.Color(0, 255, 255), 50); //MAKE IT CYAN       
     }
     else if (String(stringIn) == "magenta")
     {
             Serial.println("magenta");
             colorWipe(strip.Color(255, 0, 255), 50); //MAKE IT MAGENTA
     }
     else if (String(stringIn) == "yellow")
     {
             Serial.println("yellow");
             colorWipe(strip.Color(255, 255, 0), 50); //MAKE IT YELLOW
     }
     else if (String(stringIn) == "orange")
     {
             Serial.println("orange");
             colorWipe(strip.Color(255, 153, 0), 50); //MAKE IT ORANGE
     }
     else if (String(stringIn) == "white" || String(stringIn) == "warmwhite")
     {
             Serial.println("white");
             colorWipe(strip.Color(255, 255, 255), 50); //MAKE IT WHITE
     }
     else if (String(stringIn) == "black" || String(stringIn) == "off")
     {
              Serial.println("black");  
              colorWipe(strip.Color(0, 0, 0), 50); //MAKE IT BLACK
      }

  }
 
} // End loop     

void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}
