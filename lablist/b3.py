
from tkinter import*
from tkinter import messagebox

def clear():
    ptext.delete(0,END)
    rtext.delete(0,END)
    ttext.delete(0,END)
    citext.delete(0,END)
    ptext.focus_set()

def calculate():
    if ptext.get() and rtext.get() and ttext.get():
        try:
            p=float(ptext.get())
            r=float(rtext.get())
            t=float(ttext.get())
            amount=p*((1+r/100)**t)
            ci=amount-p
            citext.insert(0,ci)
        except:
            messagebox.showwarning('Invalid Data','Enter numbers only') 
    else:
        messagebox.showwarning('Missing Data','Enter all values')


root=Tk()
root.configure(background='light grey')
root.geometry('400x275')
root.title("Compound Interest Calculator")
plbl=Label(root,text="Principal Amount in Rs:",bg='light blue',fg='black')
rlbl=Label(root,text="Rate of Interest: ",bg='light blue', fg='black')
tlbl=Label(root,text="Time in years: ",bg='light blue',fg='black')
cilbl=Label(root,text="Compound Interest: ",bg='light blue',fg='black')
plbl.grid(row=1,column=0,padx=10,pady=10)
rlbl.grid(row=2,column=0,padx=10,pady=10)
tlbl.grid(row=3,column=0,padx=10,pady=10)
cilbl.grid(row=5,column=0,padx=10,pady=10)
ptext=Entry(root)
rtext=Entry(root)
ttext=Entry(root)
citext=Entry(root)
ptext.grid(row=1,column=1,padx=10,pady=10)
rtext.grid(row=2,column=1,padx=10,pady=10)
ttext.grid(row=3,column=1,padx=10,pady=10)
citext.grid(row=5,column=1,padx=10,pady=10)
calc_btn=Button(root,text="Calculate",bg="red",fg="black",command=calculate)
clear_btn=Button(root,text="Clear",bg="red",fg="black",command=clear)
calc_btn.grid(row=4,column=1,pady=10)
clear_btn.grid(row=6,column=1,pady=10)
root.mainloop()
