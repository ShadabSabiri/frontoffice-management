import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def insCour():
  t=tkinter.Tk()
  t.geometry('1450x1250')
  z=Canvas(t,height=800,width=1500,bg='lightgreen')
  z.place(x=1,y=1)
  z.create_text(700,100,text='  COURSE  ',font="Times 40 bold")
  def cleardata():
      t.destroy()
  def savedata():
    x=b.get()
    y=d.get()
    pp=int(f.get())
    rr=h.get()
    db=pymysql.connect(host='localhost',user='root',password='root', database="frontOM")
    cur=db.cursor()
    if len(x)==0 or len(y)==0 or len(str(pp))==0 or len(rr)==0: 
        messagebox.showerror('ERROR','ENTER ALL FIELDS')
        
    else:    
        s="insert into Course values('%s','%s',%d ,'%s')"%(x,y,pp,rr)
        cur.execute(s)
        db.commit()
        messagebox.showinfo('Saved..','Data Saved' )
        db.close()
        
        b.delete(0,100)
        d.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)    
  a=Label(t,text=' Course-id ',font="Times 15 bold",bd=1 ,fg="black")
  a.place(x=500,y=200)
  b=Entry(t,width=30)
  b.place(x=700,y=200)
  c=Label(t,text=' Course-Name ',font="Times 15 bold",bd=1 ,fg="black")
  c.place(x=500,y=260)
  d=Entry(t,width=30)
  d.place(x=700,y=260)
  e=Label(t,text=' Duration',font="Times 15 bold",bd=1,fg="black")
  e.place(x=500,y=320)
  f=Entry(t,width=30)
  f.place(x=700,y=320)
  g=Label(t,text=' Fees-id',font="Times 15 bold",bd=1 ,fg="black")
  g.place(x=500,y=380)
  h=Entry(t,width=30)
  h.place(x=700,y=380)
  bt=Button(t,text=' Save ',command=savedata,font="Times 10 bold",bg="green" ,fg="white")
  bt.place(x=700,y=440)
  bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
  bt.place(x=800,y=440)
  t.mainloop();
#insCour()  