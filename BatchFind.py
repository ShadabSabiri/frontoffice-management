import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
def findbatch():
    t=tkinter.Tk()
    t.geometry('1400x1200')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(800,100,text='   BATCH  DATA  FIND   ',font="Times 40 bold")
    def cleardata():
        t.destroy()
    def finddata():
        x=b.get()
        db=pymysql.connect(host='localhost',user='root',password='root', database='frontOM')
        cur=db.cursor()
        st="select * from Batchdata   where  Batchid='%s' "%(x)
        cur.execute(st)
        data=cur.fetchall()
        if len(data)==0:
            messagebox.showerror('ERROR','NO SUCH ENTRY FOUND')
            
        else:
            
            s="select * from Batchdata where Batchid='%s'"%(x)
            cur.execute(s)
            data=cur.fetchone()
            messagebox.showinfo('FOUND','DATA FOUND')
            d.insert(0,(data[1]))
            f.insert(0,(data[2]))
            db.commit()
            db.close()
           
        
        
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
    bt=Button(t,text=' Find ',command=finddata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=800,y=400)
    bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=900,y=400)
    t.mainloop();
    
#findbatch()
           

        
            
    