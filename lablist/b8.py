def clear(): 
    btext.delete(0,END) 
    y1text.delete(0,END) 
    y2text.delete(0,END) 
    y3text.delete(0,END) 
    y4text.delete(0,END) 
    btext.focus_set()
    
from tkinter import *
from tkinter import messagebox
import csv
import pandas as pd
import matplotlib.pyplot as plt

header=['Batsman','2017','2018','2019','2020']
with open('cricket.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(header)   
 
def submit():     
    if y1text.get() and y2text.get() and y3text.get()and y3text.get() and y4text.get():         
        try: 
            row=[btext.get(), int(y1text.get()), int(y2text.get()), int(y3text.get()), int(y4text.get())]             
            with open('cricket.csv', 'a', newline='') as f: 
                writer = csv.writer(f) 
                writer.writerow(row) 
            messagebox.showinfo(message='Submission Succesful')             
            clear()         
        except ValueError: 
            messagebox.showwarning('Invalid Data','Enter numeric values')     
    else: 
        messagebox.showwarning('Missing Data','Enter all values') 
     
def draw(): 
    try: 
        df=pd.read_csv('cricket.csv') 
        df.plot(x='Batsman',kind='bar',title='Cricket Statistics', xlabel='Batsman', ylabel= 'Runs Scored')         
        plt.xticks(rotation=10) 
        plt.show()     
    except TypeError: 
        messagebox.showwarning('No Data Found','Insert Batsman Info') 
 
 
win=Tk() 
win.configure(background='light grey') 
win.geometry('300x350') 
win.title(" Input Cricket Statitics") 
blbl=Label(win,text="Batsman :",bg='light blue',fg='black') 
y1lbl=Label(win,text="Runs in year 2017 :",bg='light blue',fg='black') 
y2lbl=Label(win,text="Runs in year 2018",bg='light blue',fg='black') 
y3lbl=Label(win,text="Runs in year 2019:",bg='light blue', fg='black') 
y4lbl=Label(win,text="Runs in year 2020:",bg='light blue', fg='black') 
 
 
blbl.grid(row=1,column=0,padx=10,pady=10) 
y1lbl.grid(row=2,column=0,padx=10,pady=10) 
y2lbl.grid(row=3,column=0,padx=10,pady=10) 
y3lbl.grid(row=4,column=0,padx=10,pady=10) 
y4lbl.grid(row=5,column=0,padx=10,pady=10) 
 
btext=Entry(win) 
y1text=Entry(win) 
y2text=Entry(win) 
y3text=Entry(win) 
y4text=Entry(win) 
 
btext.grid(row=1,column=1,padx=10,pady=10) 
y1text.grid(row=2,column=1,padx=10,pady=10) 
y2text.grid(row=3,column=1,padx=10,pady=10) 
y3text.grid(row=4,column=1,padx=10,pady=10) 
y4text.grid(row=5,column=1,padx=10,pady=10) 
 
submit_btn=Button(win,text="submit",width=15,bg="red",fg="black",command=submit) 
clear_btn=Button(win,text="Clear",width=15,bg="red",fg="black",command=clear) 
draw_btn=Button(win,text="Draw Chart", width=30, bg="red", fg="black", command=draw) 
 
submit_btn.grid(row=6,column=0,pady=10) 
clear_btn.grid(row=6,column=1,pady=10) 
draw_btn.grid(row=7,column=0,columnspan=2) 
btext.focus_set() 
win.mainloop() 
 
