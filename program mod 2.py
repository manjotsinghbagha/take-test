#!/usr/bin/env python
# coding: utf-8

# In[17]:


from tkinter import *
from tkinter.ttk import *
import os


# In[32]:


login = Tk()                                              #creat window named login

login.title("Log in for Test")                            #giving window title

login.geometry('500x300')                                 #giving window's size

blank = Label(login, )                                  #creating empty line    #using lable creat line

blank.grid(column=0, row=0)                             #giving its possition

lbl_1 = Label(login, text="Plese Enter Name")              #using lable creat line

lbl_1.grid(column=0, row=1)                                #giving lable a possition

txt = Entry(login,width=10)                               # creating input box

txt.grid(column=1, row=1)                                 #giving position to input box

    
lbl_2 = Label(login, text="Plese Select subject")                #using lable creat line

lbl_2.grid(column=0, row=2)                                      #giving lable a possition
  
subject=Combobox(login)                                          #creating  drop down list(combobox)

subject['values']= ("math","eng","comp","math","etc")            #give menu items

subject.current()                                                #set the selected item

subject.grid(column=1, row=2)                                    #give it's position

def clicked():                                                   #defining function for buutton's
    
    print(subject.get())                                         # get input fron list
    
    print(txt.get())                                            # get entered value from input box
    
    
    
    window = Tk()                                                #creating new winndow

    window.title("test")                                          #giving title

    window.geometry('350x200')                                    #giving size
    
    
    
    q1 = Label(window, text="Question:")                              #using lable creat line
    q1.grid(column=0, row=3)

    q2 = Label(window, text="Question:")                           #using lable creat line
    q2.grid(column=0, row=5)
    
    q3 = Label(window, text="Question:")                             #using lable creat line
    q3.grid(column=0, row=7)
    
    q4 = Label(window, text="Question:")                              #using lable creat line
    q4.grid(column=0, row=9)

    q5 = Label(window, text="Question:")                             #using lable creat line
    q5.grid(column=0, row=11)
    
    
    

    chk_state_1_1 = BooleanVar()                        #creating some boolian variable
    chk_state_1_2 = BooleanVar() 
    chk_state_1_3 = BooleanVar()
    chk_state_1_4 = BooleanVar()
    

    chk_state_2_1 = BooleanVar()
    chk_state_2_2 = BooleanVar()
    chk_state_2_3 = BooleanVar()
    chk_state_2_4 = BooleanVar()
    
    chk_state_3_1 = BooleanVar()
    chk_state_3_2 = BooleanVar()
    chk_state_3_3 = BooleanVar()
    chk_state_3_4 = BooleanVar()
    
    chk_state_4_1 = BooleanVar()
    chk_state_4_2 = BooleanVar()
    chk_state_4_3 = BooleanVar()
    chk_state_4_4 = BooleanVar()
    
    chk_state_5_1 = BooleanVar()
    chk_state_5_2 = BooleanVar()
    chk_state_5_3 = BooleanVar()
    chk_state_5_4 = BooleanVar()
    
    
    chk_state_1_1.set(False)                           #giving them default value
    chk_state_1_2.set(False)
    chk_state_1_3.set(False)
    chk_state_1_4.set(False)
    

    chk_state_2_1.set(False)
    chk_state_2_2.set(False)
    chk_state_2_3.set(False)
    chk_state_2_4.set(False)
    
    chk_state_3_1.set(False)
    chk_state_3_2.set(False)
    chk_state_3_3.set(False)
    chk_state_3_4.set(False)
    
    chk_state_4_1.set(False)
    chk_state_4_2.set(False)
    chk_state_4_3.set(False)
    chk_state_4_4.set(False)
    
    chk_state_5_1.set(False)
    chk_state_5_2.set(False)
    chk_state_5_3.set(False)
    chk_state_5_4.set(False)




    
    chk_1_1 = Checkbutton(window, text='Choose', var=chk_state_1_1)          #creating cheak boxes
    chk_1_2 = Checkbutton(window, text='Choose', var=chk_state_1_2)
    chk_1_3 = Checkbutton(window, text='Choose', var=chk_state_1_3)
    chk_1_4 = Checkbutton(window, text='Choose', var=chk_state_1_4)
                 
    
    chk_2_1 = Checkbutton(window, text='Choose', var=chk_state_2_1)
    chk_2_2 = Checkbutton(window, text='Choose', var=chk_state_2_2)
    chk_2_3 = Checkbutton(window, text='Choose', var=chk_state_2_3)
    chk_2_4 = Checkbutton(window, text='Choose', var=chk_state_2_4)
  
                 
    chk_3_1 = Checkbutton(window, text='Choose', var=chk_state_3_1)
    chk_3_2 = Checkbutton(window, text='Choose', var=chk_state_3_2)
    chk_3_3 = Checkbutton(window, text='Choose', var=chk_state_3_3)
    chk_3_4 = Checkbutton(window, text='Choose', var=chk_state_3_4)
    
                 
    chk_4_1 = Checkbutton(window, text='Choose', var=chk_state_4_1)
    chk_4_2 = Checkbutton(window, text='Choose', var=chk_state_4_2)
    chk_4_3 = Checkbutton(window, text='Choose', var=chk_state_4_3)
    chk_4_4 = Checkbutton(window, text='Choose', var=chk_state_4_4)

    
    
    chk_5_1 = Checkbutton(window, text='Choose', var=chk_state_5_1)
    chk_5_2 = Checkbutton(window, text='Choose', var=chk_state_5_2)
    chk_5_3 = Checkbutton(window, text='Choose', var=chk_state_5_3)
    chk_5_4 = Checkbutton(window, text='Choose', var=chk_state_5_4)
        
    
    chk_1_1.grid(column=1, row=4)                    #giving cheak box position
    chk_1_2.grid(column=2, row=4)
    chk_1_3.grid(column=3, row=4)
    chk_1_4.grid(column=4, row=4)

    
    chk_2_1.grid(column=1, row=6)
    chk_2_2.grid(column=2, row=6)
    chk_2_3.grid(column=3, row=6)
    chk_2_4.grid(column=4, row=6)

    
    chk_3_1.grid(column=1, row=8)
    chk_3_2.grid(column=2, row=8)
    chk_3_3.grid(column=3, row=8)
    chk_3_4.grid(column=4, row=8)

    
    chk_4_1.grid(column=1, row=10)
    chk_4_2.grid(column=2, row=10)
    chk_4_3.grid(column=3, row=10)
    chk_4_4.grid(column=4, row=10)

    
    chk_5_1.grid(column=1, row=12)
    chk_5_2.grid(column=2, row=12)
    chk_5_3.grid(column=3, row=12)
    chk_5_4.grid(column=4, row=12)

    
    bt2 = Button(window, text="submit", command=window.destroy )             #creating submit button
    bt2.grid(column=4, row=14)
    
    window.mainloop()                                # declaring end of new window
    
    

btn = Button(login, text="submit", command=clicked )                         #creating submit button
btn.grid(column=0, row=3)

btnn2 = Button(login, text="close", command=login.destroy )                #creating exit button
btnn2.grid(column=3, row=3)

login.mainloop()                                    # declaring end of window named login


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




