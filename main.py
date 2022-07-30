
from tkinter import *
from tkvideo import tkvideo
from process_module import process
from speak_module import speak
from time_module import get_hours, get_date
from database import put_last_seen, get_last_seen, speak_is_on
import time

# greet
previous_date = get_last_seen()

today_date = get_date()
if previous_date == today_date:
    put_last_seen(today_date)
    greet = "Welcome back"
else:
    put_last_seen(today_date)
    hour = int(get_hours())

    if 5 <= hour < 12:
        greet = "Good morning"
    elif 12 <= hour < 16:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

if speak_is_on():
    speak(greet)

# process module
def myFunction(event):
    output_label["text"] = ""
    out = process(inp.get())
    output_label["text"] = out

    if speak_is_on():
        speak(out)

# text to speech
def anotherFun(event):
    if speak_is_on():
        output_speech['text'] = "ON"
    else:
        output_speech['text'] = "OFF"

# combine 2 functions
def toCall(event):
    myFunction('<return>')
    anotherFun('<return>')


root = Tk()
root.title("Project: Arrow")
root.geometry("1280x720")
root.resizable(width=False, height=False)

# background
my_label = Label(root)
my_label.place(x=0, y=0)
player = tkvideo("ArrowGUI.mp4", my_label, loop=1, size=(1280, 720))
player.play()

# output by Arrow

output_label = Label(root, text=greet, bg="black", fg="cyan", justify=LEFT, font=("Times New Roman", 16), wraplengt=325)
output_label.place(x=830, y=35)

# input command
inp = StringVar()
entry = Entry(root, textvariable=inp, bg="black", fg="cyan", justify=CENTER, width=13, font=("Times New Roman", 26),
              relief=RIDGE)
entry.place(x=971, y=640)
root.bind('<Return>', toCall)

# text to speech
if speak_is_on():
    val = "ON"
else:
    val = "OFF"

output_speech = Label(root, text=val.upper(), bg="black", fg="cyan", justify=LEFT, font=("Times New Roman", 10),
                      wraplengt=325)
output_speech.place(x=1145, y=256)


class Clock:
    def __init__(self):
        self.time1 = ''
        if int(time.strftime('%H')) < 12:
            a= "AM"
        else:
            a="PM"
        self.time2 = time.strftime('%I:%M'+" "+ a)
        self.watch = Label(root, text=self.time2, font=('times', 30, 'bold'), bg="black", fg="cyan")
        self.watch.place(x=120, y=40)

        self.changeLabel()  # calling it manually

    def changeLabel(self):
        if int(time.strftime('%H')) < 12:
            a= "AM"
        else:
            a="PM"
        self.time2 = time.strftime('%I:%M'+" "+ a)
        self.watch.configure(text=self.time2)
        self.watch.after(200, self.changeLabel)  # it'll call itself continuously


obj1 = Clock()
root.mainloop()

if speak_is_on():
    speak("goodbye")
