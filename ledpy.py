from codecs import getincrementaldecoder
import serial #imports serial library
import time
import os
from tkinter import *
from tkinter import colorchooser
from colorTable import colorTable
from ledcolortuple import *

#arduino serial port
serialData= serial.Serial('com5',9600)
mode=2  #mode 0 manual,  mode 1 color table, mode 2 mixitup

def pickSwitch():   #switch to pick between colors
    if (mode==0):
     colorPicker()
    elif (mode==1):
     colorfromTable()
    else:
     colorfromTxt()
     
     
     
#RGB input ,to check if the
rgbCurrentValue=0
i=0
 
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
    except:
        print("Wrong input! Correct syntax: 0 0 0")
        
 
 
def colorfromTxt():  #picks color from txt
    global rgbCurrentValue
    with open('mixitup/rgbinputs.txt') as f:
        txtRGB=f.read()
        f.close()        
        while rgbCurrentValue!=txtRGB:        
            rgbCurrentValue=txtRGB
            #print("txt rgb is "+ txtRGB)
            txtRGB=txtRGB.lower()        
            mixitupInput=txtRGB      
            try:
                mixitupInput=colorList(mixitupInput)                     #refers to ledcolortuple if they entered name of the RGB value such as red,purple etc , if its not on the list splits the entry  and returns redRGB,greenRGB,blueRGB values
                redRGB, greenRGB, blueRGB=mixitupInput[0:3]             
            except:
                redRGB=255                                               #this is incase of invalid entry , and sets color to these values instead
                greenRGB=0
                blueRGB=255            
            finally:
                redRGB=str(redRGB)
                greenRGB=str(greenRGB)
                blueRGB=str(blueRGB)
                charAdd(redRGB, greenRGB, blueRGB)                         
                time.sleep(15)
            break
        else: #sleeps for 30 seconds if input is the same as old one
                time.sleep(30)
        print(txtRGB," ",i)
        i=i+1
        
    


def colorfromTable():  #picks color from the tkinter then returns the Red Green Blue rgb values
    redRGB,greenRGB,blueRGB=colorTable() 
    redRGB=str(redRGB)   #turns the ints into strings so it can be read by arduino
    greenRGB=str(greenRGB)  
    blueRGB=str(blueRGB)  
    print("The RGB Colors are red: "+str(redRGB)+" green: "+str(greenRGB)+" blue: "+str(blueRGB))
    charAdd(redRGB, greenRGB, blueRGB) 




#infinite loop to continously listen to arduino 
"""while (1==1):
    if (serialData.inWaiting()>0): #reads if there is output
        myData= serialData.readline().decode('utf-8') #puts the data in myData and decodes utf-8
        #print(myData)
        pickSwitch()
        print(serialData.readline().decode('ascii'))
"""
        
while(1==1):
    pickSwitch()
         
         
         
serialData.close