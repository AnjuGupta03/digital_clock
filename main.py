import tkinter as tk
from tkinter import Label
import datetime

def date_time():
    time = datetime.datetime.now()
    hr =time.strftime('%I')
    mi =time.strftime('%M')
    sec =time.strftime('%S')
    am =time.strftime('%P')
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,date_time) #recall the program





clock = tk.Tk()
clock.title(  'Digital Clock')
clock.geometry('1000x300')
clock.config(bg='black')


lab_hr=Label(clock,text ="00",font =('Times',60,"bold italic"),bg='black',fg='lightgreen')
lab_hr.place(x=120,y=50,height=110,width=100)

lab_hr_txt=Label(clock,text ="Hours",font =('Times',30,"bold italic"),bg='black',fg='lightgreen')
lab_hr_txt.place(x=120,y=190,height=40,width=100)

lab_min=Label(clock,text ="00",font =('Times',60,"bold italic"),bg='black',fg='lightgreen')
lab_min.place(x=340,y=50,height=100,width=100)

lab_min_txt=Label(clock,text ="Min.",font =('Times',30,"bold italic"),bg='black',fg='lightgreen')
lab_min_txt.place(x=340,y=190,height=40,width=100)


lab_sec=Label(clock,text ="00",font =('Times',60,"bold italic"),bg='black',fg='lightgreen')
lab_sec.place(x=560,y=50,height=110,width=100)

lab_sec_txt=Label(clock,text ="Sec.",font =('Times',30,"bold italic"),bg='black',fg='lightgreen')
lab_sec_txt.place(x=560,y=190,height=40,width=100)


lab_am=Label(clock,text ="00",font =('Times',60,"bold italic"),bg='black',fg='lightgreen')
lab_am.place(x=780,y=50,height=110,width=100)

lab_am_txt=Label(clock,text ="AM/PM",font =('Times',25,"bold italic"),bg='black',fg='lightgreen')
lab_am_txt.place(x=780,y=190,height=40,width=100)

date_time()
clock.mainloop()