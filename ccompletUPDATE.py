import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
def UpdateCComplete():
  t=tkinter.Tk()
  t.geometry('1450x1250')
  z=Canvas(t,height=800,width=1500,bg='lightgreen')
  z.place(x=1,y=1)
  z.create_text(800,100,text='   CERTIFICATE UPDATE   ',font="Times 30 bold")
  def finddata():
      x=b.get()
      db=pymysql.connect(host='localhost',user='root',password='root', database='frontOM')
      cur=db.cursor()
      s="select * from CComplete where CertificateNo='%s'"%(x)
      cur.execute(s)
      data=cur.fetchone()
      messagebox.showinfo('FOUND','DATA FOUND')
      d.insert(0,(data[0]))
      f.insert(0,(data[1]))
   
      db.commit()
      db.close()
  def cleardata():
      t.destroy()
  def updatedata():
    db=pymysql.connect(host='Localhost',user='root',password='root',db='frontom')
    cur=db.cursor()
    p=b.get()
    q=d.get()
    r=ff.get()
    st="update  CComplete set DOComplete='%s' ,Resid='%s' where CertificateNo='%s' " %(q,r,p)
    cur.execute(st)
    messagebox.showinfo(' UPDATE ',' DATA UPDATED')
    b.delete(0,100)
    d.delete(0,100)
    ff.delete(0,100)
    db.commit()
  def finddata():
      x=b.get()
      db=pymysql.connect(host='localhost',user='root',password='root', db='frontOM')
      cur=db.cursor()
      
      s="select DOComplete , Resid  from ccomplete where CertificateNo='%s'"%(x)
      cur.execute(s)
      data=cur.fetchone()
      if len(data)==0:
          messagebox.showerror('ERROR','NO SUCH ENTRY FOUND')
         
      else:
          messagebox.showinfo('FOUND','DATA FOUND')
          d.insert(0,data[0])
          ff.insert(0,data[1])
          
          db.commit()
          db.close()
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
  ff=Entry(t,width=30)
  ff.place(x=830,y=320)
  bt=Button(t,text=' Update',command=updatedata,font="Times 10 bold",bg="green" ,fg="white")
  bt.place(x=830,y=380)
  bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
  bt.place(x=900,y=380)
  bt=Button(t,text=' Find ',command=finddata,font="Times 10 bold",bg="green" ,fg="white")
  bt.place(x=1050,y=200)
  t.mainloop() 
#UpdateCComplete()               