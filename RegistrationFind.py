import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def findRes():
    t=tkinter.Tk()
    t.geometry('1450x1250')
    z=Canvas(t,height=1000,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(800,100,text='   REGISTRATION   ',font="Times 40 bold")
    def cleardata():
        t.destroy()
    def finddata():
        x=b.get()
        db=pymysql.connect(host='localhost',user='root',password='root', database='frontOM')
        cur=db.cursor()
        st="select * from Registration where Resid='%s'"%(x)
        cur.execute(st)
        data=cur.fetchall()
        if len(data)==0:
            messagebox.showerror('ERROR','NO SUCH ENTRY FOUND')
        else:    
            s="select Sname , Address , City , Phone , Email , Courseid , Feeid from Registration where Resid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
            d.insert(0,(data[0]))
            f.insert(0,(data[1]))
            h.insert(0,(data[2]))
            j.insert(0,(data[3]))
            l.insert(0,(data[4]))
            n.insert(0,(data[5]))
            p.insert(0,(data[6])) 
            db.commit()
            db.close() 
    a=Label(t,text=' Registration-id ',font="Times 15 bold",bd=5,bg="lightyellow" ,fg="black")
    a.place(x=500,y=180)
    b=Entry(t,width=30)
    b.place(x=800,y=180)
    c=Label(t,text=' Student-Name ',font="Times 15 bold",bd=5,bg="lightyellow" ,fg="black")
    c.place(x=500,y=240)
    d=Entry(t,width=30)
    d.place(x=800,y=240)
    e=Label(t,text=' Address ',font="Times 15 bold",bd=5,bg="lightyellow" ,fg="black")
    e.place(x=500,y=300)
    f=Entry(t,width=30)
    f.place(x=800,y=300)
    g=Label(t,text=' City  ',font="Times 15 bold",bd=5,bg="lightyellow" ,fg="black")
    g.place(x=500,y=360)
    h=Entry(t,width=30)
    h.place(x=800,y=360)
    i=Label(t,text=' Phone ',font="Times 15 bold",bd=5,bg="lightyellow" ,fg="black")
    i.place(x=500,y=420)
    j=Entry(t,width=30)
    j.place(x=800,y=420)
    k=Label(t,text=' E-mail ',font="Times 15 bold",bd=5,bg="lightyellow" ,fg="black")
    k.place(x=500,y=480)
    l=Entry(t,width=30)
    l.place(x=800,y=480)
    m=Label(t,text=' Course-id  ',font="Times 15  bold",bd=5,bg="lightyellow" ,fg="black")
    m.place(x=500,y=540)
    n=Entry(t,width=30)
    n.place(x=800,y=540)
    o=Label(t,text=' Fee-id ',font="Times 15 bold",bd=5,bg="lightyellow" ,fg="black")
    o.place(x=500,y=610)
    p=Entry(t,width=30)
    p.place(x=800,y=610)
    bt=Button(t,text=' Find ',command=finddata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=800,y=660)
    bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=900,y=660)
    t.mainloop();
#findRes()    