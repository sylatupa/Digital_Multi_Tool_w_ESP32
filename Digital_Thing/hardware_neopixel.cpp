#include <Adafruit_NeoPixel.h>

#define PixelCount 7
#define PixelPin 34

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(PixelCount, PixelPin, NEO_GRB + NEO_KHZ800);

void setup(){
  pixels.begin();
}

void loop(){
  for(byte x = 0; x < 20; x++){
    rotatePixels(true);
    delay(500);
  }
  for(byte x = 0; x < 20; x++){
    rotatePixels(false);
    delay(500);
  }
}

void rotatePixels(bool pixColour){
  static char currentPos = PixelCount;
 
  uint32_t colour = 0xFF0000; // Default to Red
 
  currentPos++;
 
  if(pixColour == true){
    colour = 0xFF00; // Green
  }
 
  pixels.setPixelColor((currentPos - 1) % PixelCount, 0);
  pixels.setPixelColor((currentPos + 0) % PixelCount, colour);
  pixels.setPixelColor((currentPos + 1) % PixelCount, colour);
  pixels.setPixelColor((currentPos + 2) % PixelCount, colour);
  pixels.setPixelColor((currentPos + 3) % PixelCount, colour);
 
  pixels.show();
 
}  
