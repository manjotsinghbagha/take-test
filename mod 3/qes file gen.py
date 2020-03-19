#!/usr/bin/env python
# coding: utf-8

# In[10]:


from tkinter import * 
import tkinter as tk
import os

def sub():
    creat_file = open(subject.get()+".txt", "w")
    
    creat_file.write(qes1.get() + '\n' + opt_1_a.get()+ ' # ' + opt_1_b.get() + ' # '+ opt_1_c.get() + ' # '+ opt_1_d.get() +'\n'+ qes2.get() +'\n'+ opt_2_a.get() + ' # ' + opt_2_b.get() + ' # ' + opt_2_c.get() + ' # ' + opt_2_d.get() + '\n' + qes3.get() + '\n'+ opt_3_a.get() + ' # '+ opt_3_b.get() + ' # '+ opt_3_c.get() + ' # '+ opt_3_d.get() + '\n' + qes4.get()+'\n' + opt_4_a.get() + ' # '+ opt_4_b.get() + ' # '+ opt_4_c.get() + ' # '+ opt_4_d.get() + '\n'  +  qes5.get() + '\n' + opt_5_a.get() + ' # '+ opt_5_b.get() + ' # '+ opt_5_c.get() + ' # '+ opt_5_d.get() )
    creat_file.close()
    

top = Tk()                                        


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font10 = "-family {Nimbus Sans} -size 9 -weight bold -slant "     "roman -underline 1 -overstrike 0"
font9 = "-family {Nimbus Sans} -size 9 -weight bold -slant "     "roman -underline 0 -overstrike 0"

top.geometry("890x450+250+140")
top.title("creat question file")

creat = tk.Button(top)
creat.place(relx=0.225, rely=0.8, height=27, width=58)
creat.configure(font=font9)
creat.configure(text='''creat''',command=sub )

close = tk.Button(top)
close.place(relx=0.618, rely=0.8, height=27, width=59)
close.configure(font=font9)
close.configure(text='''close''',command=top.destroy)


subject = tk.Entry(top)
subject.place(relx=0.528, rely=0.156,height=19, relwidth=0.164)
subject.configure(background="white")
subject.configure(font="TkFixedFont")

Label = tk.Label(top)
Label.place(relx=0.303, rely=0.156, height=17, width=153)
Label.configure(font=font10)
Label.configure(text='''Plese Enter Subject Name''')

Labe2 = tk.Label(top)
Labe2.place(relx=0.056, rely=0.244, height=17, width=63)
Labe2.configure(font=font9)
Labe2.configure(text='''question 1''')

Labe3 = tk.Label(top)
Labe3.place(relx=0.056, rely=0.356, height=17, width=63)
Labe3.configure(font=font9)
Labe3.configure(text='''question 2''')

Labe4 = tk.Label(top)
Labe4.place(relx=0.056, rely=0.467, height=17, width=63)
Labe4.configure(font=font9)
Labe4.configure(text='''question 3''')

Labe5 = tk.Label(top)
Labe5.place(relx=0.056, rely=0.578, height=17, width=61)
Labe5.configure(font=font9)
Labe5.configure(text='''question 4''')

Labe6 = tk.Label(top)
Labe6.place(relx=0.056, rely=0.689, height=17, width=63)
Labe6.configure(font=font9)
Labe6.configure(text='''question 5''')

qes1 = tk.Entry(top)
qes1.place(relx=0.146, rely=0.244,height=19, relwidth=0.771)
qes1.configure(background="white")
qes1.configure(font="TkFixedFont")

qes2 = tk.Entry(top)
qes2.place(relx=0.146, rely=0.356,height=19, relwidth=0.771)
qes2.configure(background="white")
qes2.configure(font="TkFixedFont")

qes3 = tk.Entry(top)
qes3.place(relx=0.146, rely=0.467,height=19, relwidth=0.771)
qes3.configure(background="white")
qes3.configure(font="TkFixedFont")

qes4 = tk.Entry(top)
qes4.place(relx=0.146, rely=0.578,height=19, relwidth=0.771)
qes4.configure(background="white")
qes4.configure(font="TkFixedFont")

qes5 = tk.Entry(top)
qes5.place(relx=0.146, rely=0.689,height=19, relwidth=0.76)
qes5.configure(background="white")
qes5.configure(font="TkFixedFont")

Labe7 = tk.Label(top)
Labe7.place(relx=0.067, rely=0.289, height=17, width=45)
Labe7.configure(text='''option ''')
 
Labe8 = tk.Label(top)
Labe8.place(relx=0.067, rely=0.4, height=17, width=48)
Labe8.configure(text='''option 2''')
Labe9 = tk.Label(top)
Labe9.place(relx=0.067, rely=0.511, height=17, width=48)
Labe9.configure(text='''option 3''')

Labe10 = tk.Label(top)
Labe10.place(relx=0.067, rely=0.622, height=17, width=48)
Labe10.configure(text='''option 4''')

Labe11 = tk.Label(top)
Labe11.place(relx=0.067, rely=0.733, height=17, width=48)
Labe11.configure(text='''option 5''')

opt_1_a = tk.Entry(top)
opt_1_a.place(relx=0.157, rely=0.289,height=19, relwidth=0.164)
opt_1_a.configure(background="white")
opt_1_a.configure(font="TkFixedFont")

opt_1_b = tk.Entry(top)
opt_1_b.place(relx=0.348, rely=0.289,height=19, relwidth=0.164)
opt_1_b.configure(background="white")
opt_1_b.configure(font="TkFixedFont")

opt_1_c = tk.Entry(top)
opt_1_c.place(relx=0.528, rely=0.289,height=19, relwidth=0.164)
opt_1_c.configure(background="white")
opt_1_c.configure(font="TkFixedFont")

opt_1_d = tk.Entry(top)
opt_1_d.place(relx=0.73, rely=0.289,height=19, relwidth=0.164)
opt_1_d.configure(background="white")
opt_1_d.configure(font="TkFixedFont")

opt_2_a = tk.Entry(top)
opt_2_a.place(relx=0.157, rely=0.4,height=19, relwidth=0.164)
opt_2_a.configure(background="white")
opt_2_a.configure(font="TkFixedFont")
 
opt_2_b = tk.Entry(top)
opt_2_b.place(relx=0.337, rely=0.4,height=19, relwidth=0.164)
opt_2_b.configure(background="white")
opt_2_b.configure(font="TkFixedFont")

opt_2_c = tk.Entry(top)
opt_2_c.place(relx=0.528, rely=0.4,height=19, relwidth=0.164)
opt_2_c.configure(background="white")
opt_2_c.configure(font="TkFixedFont")

opt_2_d = tk.Entry(top)
opt_2_d.place(relx=0.73, rely=0.4,height=19, relwidth=0.164)
opt_2_d.configure(background="white")
opt_2_d.configure(font="TkFixedFont")
opt_3_a = tk.Entry(top)
opt_3_a.place(relx=0.157, rely=0.511,height=19, relwidth=0.164)
opt_3_a.configure(background="white")
opt_3_a.configure(font="TkFixedFont")

opt_3_b = tk.Entry(top)
opt_3_b.place(relx=0.337, rely=0.511,height=19, relwidth=0.164)
opt_3_b.configure(background="white")
opt_3_b.configure(font="TkFixedFont")

opt_3_c = tk.Entry(top)
opt_3_c.place(relx=0.528, rely=0.511,height=19, relwidth=0.164)
opt_3_c.configure(background="white")
opt_3_c.configure(font="TkFixedFont")

opt_3_d = tk.Entry(top)
opt_3_d.place(relx=0.73, rely=0.511,height=19, relwidth=0.164)
opt_3_d.configure(background="white")
opt_3_d.configure(font="TkFixedFont")

opt_4_a = tk.Entry(top)
opt_4_a.place(relx=0.157, rely=0.622,height=19, relwidth=0.164)
opt_4_a.configure(background="white")
opt_4_a.configure(font="TkFixedFont")

opt_4_b = tk.Entry(top)
opt_4_b.place(relx=0.337, rely=0.622,height=19, relwidth=0.164)
opt_4_b.configure(background="white")
opt_4_b.configure(font="TkFixedFont")

opt_4_c = tk.Entry(top)
opt_4_c.place(relx=0.528, rely=0.622,height=19, relwidth=0.164)
opt_4_c.configure(background="white")
opt_4_c.configure(font="TkFixedFont")

opt_4_d = tk.Entry(top)
opt_4_d.place(relx=0.73, rely=0.622,height=19, relwidth=0.164)
opt_4_d.configure(background="white")
opt_4_d.configure(font="TkFixedFont")

opt_5_a = tk.Entry(top)
opt_5_a.place(relx=0.157, rely=0.733,height=19, relwidth=0.164)
opt_5_a.configure(background="white")
opt_5_a.configure(font="TkFixedFont")

opt_5_b = tk.Entry(top)
opt_5_b.place(relx=0.337, rely=0.733,height=19, relwidth=0.164)
opt_5_b.configure(background="white")
opt_5_b.configure(font="TkFixedFont")

opt_5_c = tk.Entry(top)
opt_5_c.place(relx=0.528, rely=0.733,height=19, relwidth=0.164)
opt_5_c.configure(background="white")
opt_5_c.configure(font="TkFixedFont")

opt_5_d = tk.Entry(top)
opt_5_d.place(relx=0.73, rely=0.733,height=19, relwidth=0.164)
opt_5_d.configure(background="white")
opt_5_d.configure(font="TkFixedFont")







top.mainloop()


# In[ ]:




