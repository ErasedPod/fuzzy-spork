# program for NB to control his board from India
# I changed things

import RPi.GPIO as GPIO
##import tkinter 
import time
##from tkinter import *

# set gpio 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
##GPIO.setup(7, GPIO.OUT)
##GPIO.output(7, GPIO.HIGH)
##GPIO.setup(11, GPIO.OUT)
##GPIO.output(11, GPIO.HIGH)
##GPIO.setup(12, GPIO.OUT)
##GPIO.output(12, GPIO.HIGH)
##GPIO.setup(13, GPIO.OUT)
##GPIO.output(13, GPIO.HIGH)
##GPIO.setup(15, GPIO.OUT)
##GPIO.output(15, GPIO.HIGH)
##GPIO.setup(16, GPIO.OUT)
##GPIO.output(16, GPIO.HIGH)
##GPIO.setup(18, GPIO.OUT)
##GPIO.output(18, GPIO.HIGH)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)

# set pinstate
##pin7 = 1
##pin11 = 1
##pin12 = 1
##pin13 = 1
##pin15 = 1
##pin16 = 1
##pin18 = 1
##pin22 = 1

##global msg
##
##
### main window
##top = tkinter.Tk()
##top.title("Testing Control")
##top.configure(background = "slate gray")
# main window size
##top.geometry("250x300")

# button functions

# even motors
##def click7():
##    global pin7
##    if pin7 == 0:
##        GPIO.output(7, GPIO.HIGH)
####        msg1 = print( "Pin 7 High, even motors on")
##        pin7 = 1
##        B["background"]="green2"
##        
##    else:
##        GPIO.output(7, GPIO.LOW)
####        msg2 = print( "Pin 7 Low, even motors Off ")
##        pin7 = 0.
##        B["background"]="red"
##
### odd motors        
##def click11():
##    global pin11
##    if pin11 == 0:
##        GPIO.output(11, GPIO.HIGH)
####        msg3 = print( "Pin 11 High, odd motors on ")
##        pin11 = 1
##        B2["background"]="green2"
##        
##    else:
##        GPIO.output(11, GPIO.LOW)
##        msg4 = print( "Pin 11 Low,odd motors off")
##        pin11 = 0
##        B2["background"]="red"
##
### door switch
##def click12():
##    global pin12
##    if pin12 == 0:
##        GPIO.output(12, GPIO.HIGH)
####        msg5 = print( "Pin 12 High, Door closed")
##        pin12 = 1
##        B3["background"]="deep sky blue"
##        
##    else:
##        GPIO.output(12, GPIO.LOW)
####        msg6 = print( "Pin 12 Low, Door open")
##        pin12 = 0
##        B3["background"]="indianred2"
##
### temp 1        
##def click13():
##    global pin13
##    if pin13 == 0:
##        GPIO.output(13, GPIO.HIGH)
####        msg7 = print( "Pin 13 High, Temp 1 High")
##        pin13 = 1
##        B4["background"]="yellow"
##        
##    else:
##        GPIO.output(13, GPIO.LOW)
##        msg8 = print( "Pin 13 Low, Temp 1 Low")
##        pin13 = 0
##        B4["background"]="royalblue1"
##
### relay 5
##def click15():
##    global pin15
##    if pin15 == 0:
##        GPIO.output(15, GPIO.HIGH)
####        msg9 = print( "Pin 15 High, iVend On")
##        pin15 = 1
##        B5["background"]="green"
##    else:
##        GPIO.output(15, GPIO.LOW)
####        msg10 = print( "Pin 15 Low, iVend Off")
##        pin15 = 0
##        B5["background"]="red"


### relay 6        
##def click16():
##    global pin16
##    if pin16 == 0:
##        GPIO.output(16, GPIO.HIGH)
####        msg11 = print( "Pin 16 High, Relay 6 Off")
##        pin16 = 1
##        
##    else:
##        GPIO.output(16, GPIO.LOW)
####        msg12 = print( "Pin 16 Low, Relay 6 On")
##        pin16 = 0

### relay 7
##def click18():
##    global pin18
##    if pin18 == 0:
##        GPIO.output(18, GPIO.HIGH)
####        msg13 = print( "Pin 18 High, Relay 7 Off")
##        pin18 = 1
##        
##    else:
##        GPIO.output(18, GPIO.LOW)
####        msg14 = print( "Pin 18 Low, Relay 7 On")
##        pin18 = 0
time.sleep(2)
GPIO.output(22, GPIO.LOW)
time.sleep(5)
GPIO.output(22, GPIO.HIGH)
print('Done')
time.sleep(2)
# power        
##def click22():
##    global pin22
##    if pin22 == 0:
##        GPIO.output(22, GPIO.HIGH)
####        msg15 = print( "Pin 22 High, Power on")
##        pin22 = 1
##        B8["background"]="orange red"
##        
##    else:
##        GPIO.output(22, GPIO.LOW)
####        msg16 = print( "Pin 22 Low, Power off")
##        pin22 = 0
##        B8["background"]="peach puff" 

#######clock#######
##time1 = ''
##clock = Label(top, font=('times', 10, 'bold'), bg='slate gray')
##clock.pack()
##
##def tick():
##    global time1
##    # get the current local time from the PC
##    time2 = time.strftime('%H:%M:%S')
##    # if time string has changed, update it
##    if time2 != time1:
##        time1 = time2
##        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
##    clock.after(200, tick)
##
##tick()
###################
##
##
##      
###labels
##lbl1 = tkinter.Label(text = "Manual Controls", font = 12, bd=1, relief = SUNKEN) 
##lbl1.pack()
###lbl1.place(x = 5, y = 25)
##lbl1.configure(background = "slate gray")
##
    
# buttons

# even motors
##B = Button(top, text = "Even Motors", command = click7, width = 14)
##B.pack()
###B.place(x = 5,y = 50)
##B["background"]="green2"
##
### odd motors
##B2 = Button(top, text = "Odd Motors", command = click11, width = 14)
##B2.pack()
###B2.place(x = 5,y = 80)
##B2["background"]="green2"

# door switch
##B3 = Button(top, text = "Door", command = click12, width = 14)
##B3.pack()
###B3.place(x = 5,y = 110)
##B3["background"]="deep sky blue"
##
### temp 1
##B4 = Button(top, text = "Temp 1", command = click13, width = 14)
##B4.pack()
###B4.place(x = 5,y = 140)
##B4["background"]="yellow"

### iVend
##B5 = Button(top, text = "iVend", command = click15, width = 14)
##B5.pack()
###B5.place(x = 5,y = 170)
##B5["background"]="green"

### relay 6
##B6 = Button(top, text = "Relay 6", command = click16, width = 14)
##B6.pack()
###B6.place(x = 5,y = 200)
##B6["background"]="green"

### relay 7
##B7 = Button(top, text = "Relay 7", command = click18, width = 14)
##B7.pack()
###B7.place(x = 5,y = 230)
##B7["background"]="green"

# power
##B8 = Button(top, text = "Power", command = click22, width = 14)
##B8.pack()
###B8.place(x = 5,y = 260)
##B8["background"]="Orange red"



##top.mainloop()
