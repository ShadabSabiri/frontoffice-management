from tkinter import *
from tkinter import messagebox

from FeesINPUT import *
from CourseInput import *
from BatchInput import *
from CCompleteInput import *
from EnquiryInput import *
from RegistrationInput import *


from FeesDelete import *
from BAtchDelete import *
from CourseDelete import *
from CCcompleteDelete import * 
from RegistrationDelete import *
from EnquiryDelete import *

from FeesFind import *
from CourseFind import *
from BatchFind import *
from CCompleteFind import *
from RegistrationFind import *
from EnquiryFind import *

from FeesUpdate import *
from CourseUpdate import *
from BatchUpdate import *
from RegistrationUpdate import *
from ccompletUPDATE import *
from EnquiryUpdate import *


def mainmenu():
    tt =tkinter.Tk()
    tt.title(" Project ")
    tt.geometry("1800x1200")
    tt.config(bg="lightgreen")
    tt.option_add("*Font", ('Times', 15))
    
    def cleardata():
        tt.destroy()
    
        


    menubar = Menu(tt, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  

    m1 = Menu(menubar , tearoff=0)  
    m1.add_command(label=" INPUT DATA" , command=insfee)  
    m1.add_command(label=" FIND " , command=findfees)  
    m1.add_command(label=" UPDATE " , command =UpdateFees)  
    m1.add_command(label=" DELETE " , command=delfee)    
    menubar.add_cascade(label="  FEES  ", menu= m1 , font="Times 50 bold")  

    m2 = Menu(menubar, tearoff=0)  
    m2.add_command(label=" INPUT DATA" ,  command=insCour)  
    m2.add_command(label=" FIND " , command=findCourse) 
    m2.add_command(label=" UPDATE " , command=UpdateCourse)  
    m2.add_command(label=" DELETE " , command =delcou) 
    menubar.add_cascade(label=" COURSE ", menu=m2)  

    m3 = Menu(menubar, tearoff=0)  
    m3.add_command(label=" INPUT DATA" , command=insbatch)  
    m3.add_command(label=" FIND " , command=findbatch) 
    m3.add_command(label=" UPDATE " , command=UpdateBatch)  
    m3.add_command(label=" DELETE " , command =delbat)    
    menubar.add_cascade(label="  BATCH DATA  ", menu= m3)  

    m4 = Menu(menubar, tearoff=0)  
    m4.add_command(label=" INPUT DATA" , command =insRes)  
    m4.add_command(label=" FIND " , command =findRes) 
    m4.add_command(label=" UPDATE ",command=UpdateRegistration)  
    m4.add_command(label=" DELETE " , command=delres)  
    menubar.add_cascade(label="  REGISTRATION  ", menu=m4)
      
    m5 = Menu(menubar, tearoff=0)  
    m5.add_command(label=" INPUT DATA" , command =insCComplete)  
    m5.add_command(label=" FIND " , command=findCComplete)  
    m5.add_command(label=" UPDATE " , command=UpdateCComplete)  
    m5.add_command(label=" DELETE " , command=delccom)    
    menubar.add_cascade(label="  COURSE COMPLETE  ", menu= m5)  

    m6 = Menu(menubar, tearoff=0)  
    m6.add_command(label=" INPUT DATA" , command=insEnq)  
    m6.add_command(label=" FIND " , command =findEnq)  
    m6.add_command(label=" UPDATE " ,command=UpdateEnquiry)  
    m6.add_command(label=" DELETE " , command = delenq) 
    menubar.add_cascade(label=" ENQUIRY  ", menu=m6)  

    tt.config(menu=menubar)
    a=Label(tt,text='  FRONT   OFFICE   MANAGEMENT      ',font="Times 65 bold" , bd=10 , bg="Red" ,fg="black")   
    a.place(x=0,y=50)

    a=Label(tt,text=' Front Office Management in the hotel industry involves the work',font="Times 35 bold",bd=1, bg="lightgreen")   
    a.place(x=50,y=250)
    a=Label(tt,text=' of reserving accommodations in the hotel, registering guests, ',font="Times 35 bold",bd=1, bg="lightgreen")   
    a.place(x=50,y=320)
    a=Label(tt,text=' maintaining guest accounts with the hotel, night auditing, and  ',font="Times 35 bold",bd=1, bg="lightgreen")   
    a.place(x=50,y=390)
    a=Label(tt,text=' coordination with various other departments for providing  ',font="Times 35 bold",bd=1 , bg="lightgreen")   
    a.place(x=50,y=460)
    a=Label(tt,text=' best guest services.  ',font="Times 35 bold",bd=1 , bg="lightgreen")   
    a.place(x=50,y=530)
        
    bt=Button(tt,text='Exit',font=("italic",10),fg="white",bg="red",command=cleardata)
    bt.place(x=1480,y=0)
    tt.mainloop()
 
    
   