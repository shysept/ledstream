import serial #imports serial library
import time
import os
import time
import ledcolors

#arduino serial port
serialData= serial.Serial('com5',9600)
mode=0

def pickSwitch():   #switch to pick between colors
    if (mode==1):
     colorPicker()
    else:
     colorfromTxt()
    

def colorPicker():   #manual color picker
    redRGB, greenRGB, blueRGB=input('Enter RGB values from 255-0:').split()
    print("Red input is",redRGB)
    print("Green input is",greenRGB)
    print("Blue input is",blueRGB)

    redRGB= redRGB+'*' #adds * ;  .  to the end of string for arduino to catch it 
    greenRGB= greenRGB+';'
    blueRGB= blueRGB+'.'
    serialData.write(redRGB.encode())
    serialData.write(greenRGB.encode())
    serialData.write(blueRGB.encode())
 
def colorfromTxt():  #picks color from txt
    with open('mixitup/rgbinputs.txt') as f:
        txtRGB=f.read()
        redRGB, greenRGB, blueRGB=txtRGB.split()
    redRGB= redRGB+'*' #adds * ;  .  to the end of string for arduino to catch it 
    greenRGB= greenRGB+';'
    blueRGB= blueRGB+'.'
    serialData.write(redRGB.encode())
    serialData.write(greenRGB.encode())
    serialData.write(blueRGB.encode())
    print(txtRGB)
    time.sleep(10)
    f.close()()
        
        
  

#infinite loop to continously listen to arduino 
while (1==1):
    if (serialData.inWaiting()>0): #reads if there is output
        myData= serialData.readline().decode('utf-8') #puts the data in myData and decodes utf-8
        #print(myData)
    try:
        pickSwitch()
    except:
        print("Wrong input! Correct syntax: 0 0 0")   
         
serialData.close