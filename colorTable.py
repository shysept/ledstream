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
  red,green,blue=chosenColor[0]
  print(red,green,blue)
  
  