from tkinter import *
from tkinter import colorchooser

""""" def click():
  color =  colorchooser.askcolor()

window = Tk()
window.geometry("420x420")
button = Button(text='Select Color',command=click)
button.pack()a
window.mainloop()
 """
def colorTable():
  chosenColor=colorchooser.askcolor()
  redRGB,greenRGB,blueRGB=chosenColor[0]
  print(chosenColor)
  return(redRGB,greenRGB,blueRGB)
  
colorTable()
print("test")
colorTable()
colorTable()
  
  
  
  
  
