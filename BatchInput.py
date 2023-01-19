import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def insbatch():
    t=tkinter.Tk()
    t.geometry('1450x1250')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(800,100,text='  BATCH  DATA  ',font="Times 35 bold")
    def cleardata():
        t.destroy()
    def savedata():
        x=b.get()
        y=d.get()
        pp=f.get()
        db=pymysql.connect(host='localhost',user='root',password='root', database="frontOM")
        cur=db.cursor()
        if len(x)==0 or len(y)==0 or len(pp)==0  :
            messagebox.showerror('ERROR','ENTER ALL FIELDS')
        else:
            s="insert into Batchdata values ('%s','%s','%s')"%(x,y,pp)
            cur.execute(s)
            db.commit()
            messagebox.showinfo('Saved..','Data Saved' )
            db.close()
            b.delete(0,100)
            d.delete(0,100)
            f.delete(0,100)
            
            
    a=Label(t,text=' Batch-id ',font="Times 15 bold",bd=1)
    a.place(x=500,y=200)
    b=Entry(t,width=30)
    b.place(x=800,y=200)
    c=Label(t,text=' Course-id ',font="Times 15 bold",bd=1)
    c.place(x=500,y=260)
    d=Entry(t,width=30)
    d.place(x=800,y=260)
    e=Label(t,text=' Batch-Time',font="Times 15 bold",bd=1 )
    e.place(x=500,y=320)
    f=Entry(t,width=30)
    f.place(x=800,y=320)
    bt=Button(t,text=' Save ',command=savedata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=800,y=400)
    bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=900,y=400)
    t.mainloop();
    
#insbatch()
       