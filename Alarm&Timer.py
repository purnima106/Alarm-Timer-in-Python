from tkinter import *
from tkinter.messagebox import *
from datetime import *
from time import strftime
from time import sleep
from tkinter import messagebox
import pygame 
pygame.init()


def f1():
	sw.deiconify()
	mw.withdraw()
def f2():
	mw.deiconify()
	sw.withdraw()

mw = Tk()
mw.title("Alarmtal Clock")
mw.geometry("1200x438+100+100")
mw.configure(bg = "black")
f = ("Arial",70,"bold")
sf = ("French Script MT", 40, "bold")
m = ("Arial",15,"bold")
mw.iconbitmap("Alarm.ico")
bg = PhotoImage(file = "Alarm.png")
lab_bg = Label(mw, image= bg)
lab_bg.place(x=0, y=0)

def time():
	str = strftime("%H:%M:%S:%p")
	lab.config(text = str)
	lab.after(1000, time)
d = datetime.now()
hr = d.hour
msg = ""
if hr < 12:
	msg = "Good Morning 🌄"
elif hr < 16:
	msg = "Good Afternoon ☀️"
else:
	msg = "Good Evening 🌗"

lab_greet = Label(mw, text = msg,font = sf ,bg = "light pink")
lab_greet.pack(pady = 60)

lab = Label(mw, font = f,background = "black",foreground = "lime",width = 30)
btn1 = Button(mw,text = "Features",font = m,bg = "black",fg = "deepskyblue",bd = 10,command = f1)
btn1.pack(side=RIGHT, padx=50, pady=100)
 
lab.pack(anchor = "center")
time()

sw = Toplevel(mw)
sw.title("Timer⏱️")
sw.geometry("500x438+100+100")
sw.iconbitmap("Alarm.ico")
s = ("Arial", 30)
bg2 = PhotoImage(file = "Alarm.png")
lab_bg2= Label(sw, image= bg2)
lab_bg2.place(x=0, y=0)

pygame.mixer.init()
pygame.init()

def play():
	pygame.mixer.music.load("Alarmnew.mp3")
	pygame.mixer.music.play(loops = 0)

lab_timer=Label(sw, text = "Timer", font = sf,bg = "black",fg = "deepskyblue")
sw.configure(bg = "black")
lab_timer.pack(pady = 5)
btn2 = Button(sw, text = "Back",font = s,command = f2,width = 8,bd = 8,bg = "black" , fg = "deepskyblue")
btn2.pack(pady = 150)
sw.withdraw()

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set( "00 " )
minute.set("00")
second.set("00")

ent_hour = Entry(sw,width = 4,font = ("Arial", 18),textvariable = hour)
ent_minute = Entry(sw,width = 4,font = ("Arial", 18),textvariable = minute)
ent_second = Entry(sw,width = 4,font = ("Arial", 18),textvariable = second)
ent_second.place(x = 260, y = 90)
ent_minute.place(x= 210, y = 90)
ent_hour.place(x =160,y = 90)

def submit():
	
	try:
		input_val = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
		if input_val < 0:
			messagebox.showwarning("Issue", "No Negative")
	except ValueError:
		messagebox.showwarning("Issue", "Only Numbers")

	while input_val > -1:
		mins,secs = divmod(input_val,60)
		hours = 0
		if mins > 60:
			hours , mins = divmod(mins ,60)

		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		sw.update()
		sleep(1)

		if (input_val == 0):
			messagebox.showinfo("Timer","TIMES UP!!")
		input_val -= 1


btn3 = Button(sw,text = "SET TIMER",bg = "deepskyblue",bd = "10",command =lambda :[ submit(), play()])
btn3.place(x = 210,y = 150)


def on_closing():
	if askyesno("Quit?" , "Are you sure?"):
		mw.destroy()

sw.protocol("WM_DELETE_WINDOW", on_closing)
mw.protocol("WM_DELETE_WINDOW", on_closing)


mw.mainloop()
