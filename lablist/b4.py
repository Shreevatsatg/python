from tkinter import*
def btn_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)
    
def btn_equal():
    global expression
    try:
        result=str(eval(expression))
        input_text.set(result)    
        expression=''
    except ZeroDivisionError:
        input_text.set('Zero Division Error')
    except:
        input_text.set('Invalid Input')
        
def btn_clear():
    global expression
    expression=''
    input_text.set('')

#Creating the root window and adjusting its size
root=Tk()
root.resizable(0,0)
root.geometry("400x500")
root.title("Calculator")
input_text=StringVar()
expression=''

#Entry Widget
input_field=Entry(root,textvariable=input_text,width=45,bd=5,bg="light grey")
input_field.place(x=30,y=50)

#First Row Buttons
btn7=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(7),text="7")
btn7.place(x=30,y=100)

btn8=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(8),text="8")
btn8.place(x=100,y=100)

btn9=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(9),text="9")
btn9.place(x=170,y=100)

btnplus=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click("+"),text="+")
btnplus.place(x=240,y=100)

#Second Row Buttons
btn4=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(4),text="4")
btn4.place(x=30,y=170)

btn5=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(5),text="5")
btn5.place(x=100,y=170)

btn6=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(6),text="6")
btn6.place(x=170,y=170)

btnminus=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click("-"),text="-")
btnminus.place(x=240,y=170)

#Third row buttons
btn1=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(1),text="1")
btn1.place(x=30,y=240)

btn2=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(2),text="2")
btn2.place(x=100,y=240)

btn3=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(3),text="3")
btn3.place(x=170,y=240)

btnstar=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click("*"),text="*")
btnstar.place(x=240,y=240)

#Fourth row buttons

btndot=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click("."),text=".")
btndot.place(x=30,y=310)
        
btnce=Button(root,padx=20,pady=14,bd=4,bg='white',command=btn_clear,text="C")
btnce.place(x=100,y=310)

btn0=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click(0),text="0")
btn0.place(x=170,y=310)

btndiv=Button(root,padx=20,pady=14,bd=4,bg='white',command=lambda:btn_click("/"),text="/")
btndiv.place(x=240,y=310)

#Last one Single button

btneq=Button(root,padx=125,pady=14,bd=4,bg='white',command=btn_equal,text="=")
btneq.place(x=30,y=380)

root.mainloop()
