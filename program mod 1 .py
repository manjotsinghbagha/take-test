#!/usr/bin/env python
# coding: utf-8



from tkinter import *
from tkinter.ttk import *



login = Tk()

login.title("Log in for Test")

login.geometry('500x300')

blank = Label(login, )

blank.grid(column=0, row=0)

lbl_1 = Label(login, text="Plese Enter Name")

lbl_1.grid(column=0, row=1)

txt = Entry(login,width=10)

txt.grid(column=1, row=1)

    
lbl_2 = Label(login, text="Plese Select subject")

lbl_2.grid(column=0, row=2)
  
subject=Combobox(login)

subject['values']= ("math","eng","comp","math","etc")

subject.current(1)

subject.grid(column=1, row=2)

def clicked():
    
    print(subject.get())
    
    print(txt.get())
    
    
    
    test = Tk()

    test.title("Test")

    test.geometry('700x500')




    q1 = Label(test, text="Question:")

    q1.grid(column=0, row=1)

    rad_1_1 = Radiobutton(test,text='First', value="q1 a")

    rad_1_2 = Radiobutton(test,text='Second', value="q1 b")

    rad_1_3 = Radiobutton(test,text='Third', value="q1 c")

    rad_1_4 = Radiobutton(test,text='Fourth', value="q1 d")

    rad_1_1.grid(column=0, row=3)

    rad_1_2.grid(column=1, row=3)

    rad_1_3.grid(column=2, row=3)

    rad_1_4.grid(column=3, row=3)




    q2 = Label(test, text="Question:")

    q2.grid(column=0, row=4)

    rad_2_1 = Radiobutton(test,text='First', value="q2 a")

    rad_2_2 = Radiobutton(test,text='Second', value="q2 b")

    rad_2_3 = Radiobutton(test,text='Third', value="q2 c")
             
    rad_2_4 = Radiobutton(test,text='Fourth', value="q2 d")

    rad_2_1.grid(column=0, row=5)

    rad_2_2.grid(column=1, row=5)

    rad_2_3.grid(column=2, row=5)

    rad_2_4.grid(column=3, row=5)




    q3 = Label(test, text="Question:")

    q3.grid(column=0, row=6)

    rad_3_1 = Radiobutton(test,text='First', value="q3 a")

    rad_3_2 = Radiobutton(test,text='Second', value="q3 b")

    rad_3_3 = Radiobutton(test,text='Third', value="q3 c")
             
    rad_3_4 = Radiobutton(test,text='Fourth', value="q3 d")

    rad_3_1.grid(column=0, row=7)

    rad_3_2.grid(column=1, row=7)

    rad_3_3.grid(column=2, row=7)

    rad_3_4.grid(column=3, row=7)





    q4 = Label(test, text="Question:")

    q4.grid(column=0, row=8)

    rad_4_1 = Radiobutton(test,text='First', value="q4 a")

    rad_4_2 = Radiobutton(test,text='Second', value="q4 b")

    rad_4_3 = Radiobutton(test,text='Third', value="q4 c")

    rad_4_4 = Radiobutton(test,text='Fourth', value="q4 d")

    rad_4_1.grid(column=0, row=9)

    rad_4_2.grid(column=1, row=9)

    rad_4_3.grid(column=2, row=9)

    rad_4_4.grid(column=3, row=9)


    bt2 = Button(test, text="submit", command=test.destroy )

    bt2.grid(column=4, row=10)

    
    
    test.mainloop()
    
    

    

btn = Button(login, text="submit", command=clicked )

btn.grid(column=0, row=3)
btnn = Button(login, text="close", command=login.destroy )

btnn.grid(column=3, row=3)

login.mainloop()

