from ledcolortuple import *
import time

redRGB=0
greenRGB=0
blueRGB=0
rgbCurrentValue=0


    
    
def colorfromTxt():  #picks color from txt
    with open('mixitup/rgbinputs.txt') as f:
        global redRGB,greenRGB,blueRGB,rgbCurrentValue
        txtRGB=f.read()
        while rgbCurrentValue!=txtRGB:
            #print("txt rgb is "+ txtRGB)
            rgbCurrentValue=txtRGB
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
                print(redRGB)
                print(greenRGB)
                print(blueRGB)
                time.sleep(5)
            break
        else:
                time.sleep(15)
            # charAdd(redRGB, greenRGB, blueRGB)                         
        f.close()
        print("txt rgb is "+ txtRGB)   
x=0


while (1==1):    
    print(redRGB)
    print(greenRGB)
    print(blueRGB)    
    print(rgbCurrentValue)         
    colorfromTxt()
    x=x+1
    print("x is ", x)