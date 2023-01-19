import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def insCComplete():
    t=tkinter.Tk()
    t.geometry('1450x1250')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(800,100,text='  COURSE COMPLETE ',font="Times 35 bold")
    def cleardata():
        t.destroy()
    def savedata():
        x=b.get()
        y=d.get()
        pp=f.get()
        if (not x) or ( not y) or ( not pp):
              messagebox.showerror('ERROR','ENTER ALL FIELDS')
              t.destroy()
        else:
            
            db=pymysql.connect(host='localhost',user='root',password='root', database="frontOM")
            cur=db.cursor()
            s="insert into CComplete values ('%s','%s','%s')"%(x,y,pp)
            cur.execute(s)
            db.commit()
            messagebox.showinfo('Saved..','Data Saved')
            db.close()
            b.delete(0,100)
            d.delete(0,100)
            f.delete(0,100)
        
    a=Label(t,text=' Certification No. ',font="Times 15 bold",bd=1)
    a.place(x=500,y=200)
    b=Entry(t,width=30)                                                
    b.place(x=830,y=200)
    c=Label(t,text=' Date Of Complete ',font="Times 15 bold",bd=1)
    c.place(x=500,y=260)
    d=Entry(t,width=30)
    d.place(x=830,y=260)
    e=Label(t,text='  Registration-id ',font="Times 15 bold",bd=1 )
    e.place(x=500,y=320)
    f=Entry(t,width=30)
    f.place(x=830,y=320)
    bt=Button(t,text=' Save ',command=savedata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=830,y=380)
    bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=900,y=380)
    t.mainloop();
#insCComplete()    