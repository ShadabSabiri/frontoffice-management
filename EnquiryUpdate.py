import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
def UpdateEnquiry():
  t=tkinter.Tk()
  t.geometry('1450x1250')
  z=Canvas(t,height=1000,width=1600,bg='lightgreen')
  z.place(x=1,y=1)
  z.create_text(800,100,text='  ENQUIRY   UPDATE   ',font="Times 40 bold")
  def cleardata():
      t.destroy()
  def updatedata():
    db=pymysql.connect(host='Localhost',user='root',password='root',db='frontom')
    cur=db.cursor()
    a=b.get()
    c=d.get()
    e=f.get()
    g=h.get()
    i=j.get()
    k=l.get()
    m=n.get()
    o=p.get()
    
    st="update enquiry set Ename='%s' ,Address='%s' , City ='%s' ,Phone='%s' ,Email='%s' ,DOEnquiry='%s',Courseid='%s'   where Enqid='%s' " %(c,e,g,i,k,m,o,a)
    cur.execute(st)
    messagebox.showinfo(' UPDATE ',' DATA UPDATED')
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    h.delete(0,100)
    j.delete(0,100)
    l.delete(0,100)
    n.delete(0,100)
    p.delete(0,100)
    db.commit()
  def finddata():
           x=b.get()
           db=pymysql.connect(host='localhost',user='root',password='root', db='frontom')
           cur=db.cursor()
           s="select Ename , Address , City , Phone , Email ,DOEnquiry , Courseid from Enquiry where Enqid='%s'"%(x)
           cur.execute(s)
           data=cur.fetchone()
           if len(data)==0:
               messagebox.showerror('ERROR','ENTER VALID ENQID')
           else:
              #  messagebox.showinfo('FOUND','DATA FOUND SUCCESFULLY')
               d.insert(0,data[0])
               f.insert(0,data[1])
               h.insert(0,data[2])
               j.insert(0,data[3])
               l.insert(0,data[4])
               n.insert(0,data[5])
               p.insert(0,data[6]) 
               db.commit()
               db.close() 
  a=Label(t,text=' Enquiry-id ',font="Times 25 bold",bd=1,bg="white" ,fg="black")
  a.place(x=500,y=200)
  b=Entry(t,width=30)
  b.place(x=800,y=200)
  c=Label(t,text=' Student-Name ',font="Times 25 bold",bd=1,bg="white" ,fg="black")
  c.place(x=500,y=250)
  d=Entry(t,width=30)
  d.place(x=800,y=250)
  e=Label(t,text=' Address ',font="Times 25 bold",bd=1,bg="white" ,fg="black")
  e.place(x=500,y=300)
  f=Entry(t,width=30)
  f.place(x=800,y=300)
  g=Label(t,text=' City  ',font="Times 25 bold",bd=1,bg="white" ,fg="black")
  g.place(x=500,y=350)
  h=Entry(t,width=30)
  h.place(x=800,y=350)
  i=Label(t,text=' Phone ',font="Times 25 bold",bd=1,bg="white" ,fg="black")
  i.place(x=500,y=400)
  j=Entry(t,width=30)
  j.place(x=800,y=400)
  k=Label(t,text=' E-mail ',font="Times 25 bold",bd=1,bg="white" ,fg="black")
  k.place(x=500,y=450)
  l=Entry(t,width=30)
  l.place(x=800,y=450)
  m=Label(t,text=' Date Of Enquiry ',font="Times 25 bold",bd=1,bg="white" ,fg="black")
  m.place(x=500,y=500)
  n=Entry(t,width=30)
  n.place(x=800,y=500)
  o=Label(t,text=' Course-id  ',font="Times 25 bold",bd=1,bg="white" ,fg="black")
  o.place(x=500,y=550)
  p=Entry(t,width=30)
  p.place(x=800,y=550)
  bt=Button(t,text=' Update ',command=updatedata,font=" MONOtype 10 bold",bg="green" ,fg="white")
  bt.place(x=800,y=600)
  bt1=Button(t,text=' Back ',command=cleardata,font=" MONOtype 10 bold",bg="green" ,fg="white")
  bt1.place(x=900,y=600)
  bt1=Button(t,text=' find ',command=finddata,font=" MONOtype 10 bold",bg="green" ,fg="white")
  bt1.place(x=1000,y=200)
  t.mainloop();
#UpdateEnquiry()  
  