import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
def findEnq():
    t=tkinter.Tk()
    t.geometry('1400x1200')
    t.title('Fee find')
    z=Canvas(t,height=1000,width=1600,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(800,100,text='   ENQUIRY  DATA  FIND   ',font="Times 30 bold")
    def finddata():
             x=b.get()
             db=pymysql.connect(host='localhost',user='root',password='root', db='frontom')
             cur=db.cursor()
             s="select Ename , Address , City , Phone , Email ,DOEnquiry , Courseid from enquiry where Enqid='%s'"%(x)
             cur.execute(s)
             data=cur.fetchone()
             if len(data)==0:
                 messagebox.showerror('ERROR','ENTER VALID ENQID')
             else:
                 messagebox.showinfo('FOUND','DATA FOUND SUCCESFULLY')
                 d.insert(0,data[0])
                 f.insert(0,data[1])
                 h.insert(0,data[2])
                 j.insert(0,data[3])
                 l.insert(0,data[4])
                 n.insert(0,data[5])
                 p.insert(0,data[6]) 
                 db.commit()
                 db.close() 
    def cleardata():
        t.destroy()
    
    a=Label(t,text=' Enquiry-id ',font="Times 20 bold",bg="white" ,fg="black")
    a.place(x=500,y=180)
    b=Entry(t,width=30)
    b.place(x=800,y=180)
    c=Label(t,text=' Student-Name ',font="Times 20 bold",bg="white" ,fg="black")
    c.place(x=500,y=240)
    d=Entry(t,width=30)
    d.place(x=800,y=240)
    e=Label(t,text=' Address ',font="Times 20 bold",bg="white" ,fg="black")
    e.place(x=500,y=300)
    f=Entry(t,width=30)
    f.place(x=800,y=300)
    g=Label(t,text=' City  ',font="Times 20 bold",bg="white" ,fg="black")
    g.place(x=500,y=360)
    h=Entry(t,width=30)
    h.place(x=800,y=360)
    i=Label(t,text=' Phone ',font="Times 20 bold",bg="white" ,fg="black")
    i.place(x=500,y=420)
    j=Entry(t,width=30)
    j.place(x=800,y=420)
    k=Label(t,text=' E-mail ',font="Times 20 bold",bg="white" ,fg="black")
    k.place(x=500,y=480)
    l=Entry(t,width=30)
    l.place(x=800,y=480)
    m=Label(t,text=' Date Of Enquiry ',font="Times 20 bold",bg="white" ,fg="black")
    m.place(x=500,y=540)
    n=Entry(t,width=30)
    n.place(x=800,y=540)
    o=Label(t,text=' Course-id  ',font="Times 20 bold",bg="white" ,fg="black")
    o.place(x=500,y=600)
    p=Entry(t,width=30)
    p.place(x=800,y=600)
    bt=Button(t,text="Find ",command=finddata,font="Times  15 bold",bg="green" ,fg="white")
    bt.place(x=800,y=640)
    bt=Button(t,text="Back",command=cleardata,font="Times  15 bold",bg="green" ,fg="white")
    bt.place(x=900,y=640)
    t.mainloop()
#findEnq()    