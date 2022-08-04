import serial #imports serial library
import time
import os
import time
import ledcolors
from tkinter import *
from tkinter import colorchooser
import colorTable

#arduino serial port
serialData= serial.Serial('com5',9600)
mode=1  #mode 0 manual,  mode 1 color table, mode 2 mixitup

def pickSwitch():   #switch to pick between colors
    if (mode==0):
     colorPicker()
    elif (mode==1):
     print('uwu')
    else:
     colorfromTxt()
 
 
def charAdd(redRGB, greenRGB, blueRGB): #adds characters to RGB colors, red(*) green(;)  blue(.)  to the end of string for arduino to catch it  
                #sends the RGB Values to Ardunio
        redRGB= redRGB+'*' #adds * ;  .  to the end of string for arduino to catch it 
        greenRGB= greenRGB+';'
        blueRGB= blueRGB+'.'
        serialData.write(redRGB.encode())
        serialData.write(greenRGB.encode())
        serialData.write(blueRGB.encode())            

def colorPicker():   #manual color picker
    try:
        redRGB, greenRGB, blueRGB=input('Enter RGB values from 255-0:').split()
        print("Red input is",redRGB)
        print("Green input is",greenRGB)
        print("Blue input is",blueRGB)
        charAdd(redRGB, greenRGB, blueRGB)
        """ redRGB= redRGB+'*' #adds * ;  .  to the end of string for arduino to catch it 
        greenRGB= greenRGB+';'
        blueRGB= blueRGB+'.'
        serialData.write(redRGB.encode())
        serialData.write(greenRGB.encode())
        serialData.write(blueRGB.encode()) """
    except:
        print("Wrong input! Correct syntax: 0 0 0")
        
 
 
 
def colorfromTxt():  #picks color from txt
    with open('mixitup/rgbinputs.txt') as f:
        txtRGB=f.read()
        redRGB, greenRGB, blueRGB=txtRGB.split()
        charAdd(redRGB, greenRGB, blueRGB)
    print(txtRGB)
    time.sleep(10)
    f.close()
        
  

#infinite loop to continously listen to arduino 
while (1==1):
    if (serialData.inWaiting()>0): #reads if there is output
        myData= serialData.readline().decode('utf-8') #puts the data in myData and decodes utf-8
        #print(myData)
        pickSwitch()

         
         
serialData.close