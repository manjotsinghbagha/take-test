#!/usr/bin/env python
# coding: utf-8


from tkinter import *
from tkinter.ttk import *
import os



login = Tk()                                              #creat window named login

login.title("Log in for Test")                            #giving window title

login.geometry('500x300')                                 #giving window's size

blank = Label(login, )                                  #creating empty line    #using lable creat line

blank.grid(column=0, row=0)                             #giving its possition

lbl_1 = Label(login, text="Plese Enter Name")              #using lable creat line

lbl_1.grid(column=0, row=1)                                #giving lable a possition

name = Entry(login,width=10)                               # creating input box

name.grid(column=1, row=1)                                 #giving position to input box

    
lbl_2 = Label(login, text="Plese Select subject")                #using lable creat line

lbl_2.grid(column=0, row=2)                                      #giving lable a possition
  
subject=Combobox(login)                                          #creating  drop down list(combobox)

subject['values']= ("math","eng")            #give menu items

subject.current()                                                #set the selected item

subject.grid(column=1, row=2)                                    #give it's position

def clicked():                                                   #defining function for buutton's
    
    print(subject.get())                                         # get input fron list
    
    print(name.get())                                            # get entered value from input box
    
    
    filename = subject.get()+'.txt'     #acessing file name
    f = open(filename, 'r')                #read file
    text = f.read()                        #save read data to a varible 
    f.close()                              #closing file
    read_line=text.split("\n")
    read_line

    opt_1=tuple(read_line[1].split("#"))
    opt_2=tuple(read_line[3].split("#"))
    opt_3=tuple(read_line[5].split("#"))
    opt_4=tuple(read_line[7].split("#"))
    opt_5=tuple(read_line[9].split("#"))
    
    
    
    
    window = Tk()                                                #creating new winndow

    window.title("test")                                          #giving title

    
    
    
    q1 = Label(window, text="Question:"+read_line[0])                              #using lable creat line
    q1.grid(column=0, row=3)

    q2 = Label(window, text="Question:"+read_line[2])                           #using lable creat line
    q2.grid(column=0, row=5)
    
    q3 = Label(window, text="Question:"+read_line[4])                             #using lable creat line
    q3.grid(column=0, row=7)
    
    q4 = Label(window, text="Question:"+read_line[6])                              #using lable creat line
    q4.grid(column=0, row=9)

    q5 = Label(window, text="Question:"+read_line[8])                             #using lable creat line
    q5.grid(column=0, row=11)
    
    
    
    
    ans1=Combobox(window)                                          #creating  drop down list(combobox)

    ans1['values']= opt_1          #give menu items

    ans1.current()                                                #set the selected item
    
    ans1.grid(column=0, row=4)    
    
    
    
    
    ans2=Combobox(window)                                          #creating  drop down list(combobox)

    ans2['values']= opt_2            #give menu items

    ans2.current()                                                #set the selected item
    
    ans2.grid(column=0, row=6)    
    
    
    
    ans3=Combobox(window)                                          #creating  drop down list(combobox)

    ans3['values']= opt_3            #give menu items

    ans3.current()                                                #set the selected item
    
    ans3.grid(column=0, row=8)    
    
    
    
    ans4=Combobox(window)                                          #creating  drop down list(combobox)

    ans4['values']= opt_4            #give menu items

    ans4.current()                                                #set the selected item
    
    ans4.grid(column=0, row=10)    
    
    
    
    ans5=Combobox(window)                                          #creating  drop down list(combobox)

    ans5['values']= opt_5            #give menu items

    ans5.current()                                                #set the selected item
    
    ans5.grid(column=0, row=12)    
    
    

    def sub():
        print(1,ans1.get())
        print(2,ans2.get())
        print(3,ans3.get())
        print(4,ans4.get())
        print(5,ans5.get())
        
        
        sub_ans_file = open("ans "+name.get()+" "+subject.get()+".txt", "w")
        # write to this file some text
        sub_ans_file.write(f"the given answer are as follow  \n name ={name.get()} \n subject= {subject.get()}  \n answer 1 {ans1.get()} \n answer 2 {ans2.get()} \n answer 3 {ans3.get()}   \n answer 4 {ans4.get()}  \n answer 5 {ans5.get()}")
        sub_ans_file.close()


    
    bt2 = Button(window, text="submit", command=sub )             #creating submit button
    bt2.grid(column=0, row=14)

    bt3 = Button(window, text="close", command=window.destroy )             #creating submit button
    bt3.grid(column=0, row=15)
    
    window.mainloop()                                # declaring end of new window


    
    
btn = Button(login, text="submit", command=clicked )                         #creating submit button
btn.grid(column=0, row=3)

btnn2 = Button(login, text="close", command=login.destroy )                #creating exit button
btnn2.grid(column=3, row=3)

mainloop()                                    # declaring end of window namedans5
