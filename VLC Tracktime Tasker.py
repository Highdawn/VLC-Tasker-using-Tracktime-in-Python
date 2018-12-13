import requests
import re
import time
import sys
from tkinter import *
text="Start"
t=1
x=0


timeStamps = [0,39,56,58,122,158,176,178,209]
tasks = ["Start","Build Up","Drop","Main Chorus","Bridge","Build Up","Drop","Main Chorus"]

def getInfo():
    s = requests.Session()
    s.auth = ('', 'pass')# Username is blank, just provide the password
    r = s.get('http://localhost:8080/requests/status.xml', verify=False)
    text= r.text
    return (int(re.search('<time>(.+?)</time>', text).group(1)))
def task():
    global x
    global timeStamps
    curTime= getInfo()
    l1['text']= curTime
    tStart = timeStamps[x]
    tEnd = timeStamps[x+1]
    if curTime>=tStart and curTime<=tEnd :
        l2['text']= tasks[x]
    elif curTime > int(tEnd):
        x=x+1
    elif curTime < int(tStart):
        x=x-1
    elif curTime == 0:
        x=0
    window.after(25, task)  # reschedule event in 2 seconds
        
#GUI
window=Tk()
l1= Label(window, text="Hi", bd=50, font="Arial 50")
l1.pack()

l2= Label(window, text="Hi", bd=50, font="Arial 50")
l2.pack()
window.after(2000, task)
window.mainloop()



