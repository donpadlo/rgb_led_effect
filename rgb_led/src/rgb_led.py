#!/usr/bin/python3
#encoding: UTF-8

import time
from rpi_ws281x import *
import argparse
import math
from random import randrange


# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def showStrip():
    strip.show() 
def setAll(R,G,B):
   for i in range(strip.numPixels()):
    strip.setPixelColor(i, Color(R, G, B))      
   showStrip(); 
def setPixel(Pixel,R,G,B):
    strip.setPixelColor(int(Pixel), Color(int(R), int(G), int(B)))      
def delay(dd):    
    time.sleep(dd/10000);
def RGBLoop():
  for j in range(3):    
    # Fade IN  
    for k in range(255):    
        if j==0: setAll(k,0,0);
        if j==1: setAll(0,k,0);
        if j==2: setAll(0,0,k);
        showStrip();
        delay(3);
    # Fade OUT
    for k in range(256):    
        if j==0: setAll(255-k,0,0);
        if j==1: setAll(0,255-k,0);
        if j==2: setAll(0,0,255-k);
        showStrip();
        delay(3);
def Strobe(red,green,blue,StrobeCount,FlashDelay,EndPause):  
  for j in range(StrobeCount):    
    setAll(red,green,blue);
    showStrip();
    delay(FlashDelay);
    setAll(0,0,0);
    showStrip();
    delay(FlashDelay);
  delay(EndPause);  
def CylonBounce(red,green,blue,EyeSize,SpeedDelay,ReturnDelay):
  for i in range(LED_COUNT-EyeSize-2):    
    setAll(0,0,0);
    setPixel(i, red/10, green/10, blue/10);
    for j in range(EyeSize):        
      setPixel(i+j, red, green, blue);    
    setPixel(i+EyeSize+1, red/10, green/10, blue/10);
    showStrip();
    delay(SpeedDelay);
  delay(ReturnDelay);
  for zz in range(LED_COUNT-EyeSize-2):
    i=LED_COUNT-EyeSize-2-zz;  
    setAll(0,0,0);
    setPixel(i, red/10, green/10, blue/10);
    for j in range(EyeSize):    
      setPixel(i+j, red, green, blue);
    setPixel(i+EyeSize+1, red/10, green/10, blue/10);
    showStrip();
    delay(SpeedDelay);   
  delay(ReturnDelay);
def NewKITT(red,green,blue,EyeSize,SpeedDelay,ReturnDelay):
  RightToLeft(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  LeftToRight(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  OutsideToCenter(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  CenterToOutside(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  LeftToRight(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  RightToLeft(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  OutsideToCenter(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  CenterToOutside(red, green, blue, EyeSize, SpeedDelay, ReturnDelay);
  
def CenterToOutside(red,green,blue,EyeSize,SpeedDelay,ReturnDelay):
  for zz in range(int(LED_COUNT-EyeSize/2)):
    i=LED_COUNT-EyeSize/2-zz;  
    setAll(0,0,0);   
    setPixel(i, red/10, green/10, blue/10);
    for j in range(EyeSize):
      setPixel(i+j, red, green, blue);
    setPixel(i+EyeSize+1, red/10, green/10, blue/10);   
    setPixel(LED_COUNT-i, red/10, green/10, blue/10);
    for j in range(EyeSize):
      setPixel(LED_COUNT-i-j, red, green, blue);
    setPixel(LED_COUNT-i-EyeSize-1, red/10, green/10, blue/10);   
    showStrip();
    delay(SpeedDelay);
  delay(ReturnDelay);
def OutsideToCenter(red,green,blue,EyeSize,SpeedDelay,ReturnDelay):
    for zz in range(int(LED_COUNT-EyeSize/2)):
      i=LED_COUNT-EyeSize/2-zz;      
      setAll(0,0,0);   
      setPixel(i, red/10, green/10, blue/10);
      for j in range(EyeSize):
        setPixel(i+j, red, green, blue);      
      setPixel(i+EyeSize+1, red/10, green/10, blue/10);   
      setPixel(LED_COUNT-i, red/10, green/10, blue/10);
      for j in range(EyeSize):
        setPixel(LED_COUNT-i-j, red, green, blue);        
      setPixel(LED_COUNT-i-EyeSize-1, red/10, green/10, blue/10);   
      showStrip();
      delay(SpeedDelay);  
    delay(ReturnDelay);   
def LeftToRight(red,green,blue,EyeSize,SpeedDelay,ReturnDelay):  
  for zz in range(LED_COUNT-EyeSize-2):
    i=LED_COUNT-EyeSize-2-zz
    setAll(0,0,0);
    setPixel(i, red/10, green/10, blue/10);
    for j in range(EyeSize):
      setPixel(i+j, red, green, blue);    
    setPixel(i+EyeSize+1, red/10, green/10, blue/10);
    showStrip();
    delay(SpeedDelay);
  delay(ReturnDelay);

def RightToLeft(red,green,blue,EyeSize,SpeedDelay,ReturnDelay):
  for zz in range(LED_COUNT-EyeSize-2):
    i=LED_COUNT-EyeSize-2-zz;
    setAll(0,0,0);
    setPixel(i, red/10, green/10, blue/10);
    for j in range(EyeSize):
      setPixel(i+j, red, green, blue);    
    setPixel(i+EyeSize+1, red/10, green/10, blue/10);
    showStrip();
    delay(SpeedDelay);  
  delay(ReturnDelay);
def RunningLights(red,green,blue,WaveDelay):
  Position=0; 
  for j in range(LED_COUNT*2):
      Position=Position+1; 
      for i in range(LED_COUNT):
        setPixel(i,((math.sin(i+Position) * 127 + 128)/255)*red,((math.sin(i+Position) * 127 + 128)/255)*green,((math.sin(i+Position) * 127 + 128)/255)*blue);     
      showStrip();
      delay(WaveDelay);
      
def meteorRain(red,green,blue,meteorSize,meteorTrailDecay,meteorRandomDecay,SpeedDelay):
  setAll(0,0,0);
  for i in range(LED_COUNT+LED_COUNT):
    for j in range(LED_COUNT):  
      if ((meteorRandomDecay==False) or (randrange(10)>5) ):
        fadeToBlack(j, meteorTrailDecay );           
    for j in range(meteorSize):  
      if( ( i-j <LED_COUNT) and (i-j>=0) ):
        setPixel(i-j, red, green, blue);   
    showStrip();
    delay(SpeedDelay);

def fadeToBlack(ledNo,fadeValue):
    oldColor=0;
    r=0; g=0; b=0;
    value=0;   
    oldColor = strip.getPixelColor(ledNo);
    r = (oldColor & 0x00ff0000) >> 16;
    g = (oldColor & 0x0000ff00) >> 8;
    b = (oldColor & 0x000000ff);

    if r<=10: 
      r=0 
    else: 
      r=int(r-(r*fadeValue/256));
    if g<=10: 
      g=0 
    else: 
      g=int(g-(g*fadeValue/256));
    if b<=10: 
      b=0 
    else: 
      b=int(b-(b*fadeValue/256));    
     
    setPixel(ledNo,r,g,b);
   # leds[ledNo].fadeToBlackBy( fadeValue );

     
if __name__ == '__main__':
   strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
   strip.begin()  
   RGBLoop();
   Strobe(255, 255, 255, 10, 50, 3000);   
   Strobe(255, 255, 255, 10, 50, 3000);   
   Strobe(255, 255, 255, 10, 50, 3000);   
   Strobe(255, 255, 255, 10, 50, 3000);   
   Strobe(255, 255, 255, 10, 50, 3000);   
   Strobe(255, 255, 255, 10, 50, 3000);   
   Strobe(255, 255, 255, 10, 50, 3000);   
   Strobe(255, 255, 255, 10, 50, 3000);   
   CylonBounce(200, 200, 100, 10, 1, 5);
   CylonBounce(200, 100, 100, 10, 1, 5);
   CylonBounce(100, 200, 200, 10, 1, 5);
   NewKITT(25, 100, 150, 20, 1, 1);
   RunningLights(255,0,0, 50);
   RunningLights(255,255,255, 50);
   RunningLights(0,0,255, 50);
   meteorRain(25,255,255,10, 24, True, 1);
   meteorRain(155,255,255,10, 24, True, 1);
   meteorRain(155,155,255,10, 24, True, 1);
   meteorRain(155,25,55,10, 24, True, 1);