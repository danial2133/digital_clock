from tkinter import *
import time

##Graphic Page and Title and Size
CLOCK_DiGI_CRS = Tk()
CLOCK_DiGI_CRS.title('DIGI clock crs')
CLOCK_DiGI_CRS.geometry:('600×400')

##Is a function for timing.
def myTIme():
##It YOU can changes ('H%')
    hour = time.strftime('%I')
##It YOU can't chahnge :)
    minute = time.strftime("%M")
    secend = time.strftime('%S')
    am_pm = time.strftime('%p')
    day = time.strftime('%A')
    zone = time.strftime('%Z')
##To connect to time
    myText = hour + ":" + minute + ":" + secend + " " + am_pm
##To connect the area of time and is the day
    myText2 = day + ",  " + zone
##configure
    myLabel.config(text=myText)
    myLabel2.config(text=myText2)
    myLabel.after(1000, myTIme)

##Label of the clock
myLabel = Label(CLOCK_DiGI_CRS, text="", font=('Arial', 18))
myLabel.pack()

##Label of the day and zone
myLabel2 = Label(CLOCK_DiGI_CRS, text="", font=("Arial", 18))
myLabel2.pack()

myTIme()
CLOCK_DiGI_CRS.mainloop()

## Hello humans I'm DiGi Clock. My creator is Danial
##github : https://github.com/danial2133