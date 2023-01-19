import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
def UpdateBatch():
  t=tkinter.Tk()
  t.geometry('1450x1250')
  z=Canvas(t,height=800,width=1500,bg='lightgreen')
  z.place(x=1,y=1)
  z.create_text(800,100,text='   BATCH  DATA   UPDATE   ',font="Times 30 bold")
  def cleardata():
      t.destroy()
  def updatedata():
    db=pymysql.connect(host='Localhost',user='root',password='root',db='frontom')
    cur=db.cursor()
    p=b.get()
    q=d.get()
    r=f.get()
    
    st="update  batchdata set Courseid='%s' ,Time='%s' where Batchid='%s' " %(q,r,p)
    cur.execute(st)
    messagebox.showinfo(' UPDATE ',' DATA UPDATED')
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    db.commit()
  def finddata():
      x=b.get()
      db=pymysql.connect(host='localhost',user='root',password='root', db='frontOM')
      cur=db.cursor()
      st="select * from Batchdata   where  Batchid='%s' "%(x)
      cur.execute(st)
      data=cur.fetchall()
      if (not data):
          messagebox.showerror('ERROR','NO SUCH ENTRY FOUND')
          
      else:
          st="select Courseid,Time from batchdata where Batchid='%s'"%(x)
          cur.execute(st)
          data=cur.fetchone()
          d.insert(0,(data[0]))
          f.insert(0,(data[1]))
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
  bt.place(x=1000,y=200)
  bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
  bt.place(x=900,y=400)
  bt=Button(t,text=' update ',command=updatedata,font="Times 10 bold",bg="green" ,fg="white")
  bt.place(x=800,y=400)
  t.mainloop();      
      
      
#UpdateBatch()  