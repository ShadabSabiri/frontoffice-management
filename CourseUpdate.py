import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
def UpdateCourse():
  t=tkinter.Tk()
  t.geometry('1450x1250')
  z=Canvas(t,height=700,width=1500,bg='lightgreen')
  z.place(x=1,y=1)
  z.create_text(800,100,text='   COURSE   UPDATE   ',font="Times 40 bold")
  def cleardata():
      t.destroy()
  def updatedata():
    db=pymysql.connect(host='Localhost',user='root',password='root',db='frontOM')
    cur=db.cursor()
    p=b.get()
    q=d.get()
    r=int(f.get())
    s=h.get()
    st="update  Course set Cname='%s' ,Duration=%d,Feeid='%s' where Courseid='%s' " %(q,r,s,p)
    cur.execute(st)
    messagebox.showinfo(' UPDATE ',' DATA UPDATED')
    b.delete(0,100)
    d.delete(0,100)
    f.delete(0,100)
    h.delete(0,100)
    db.commit()
    db.close()    
  def finddata():
      x=b.get()
      db=pymysql.connect(host='localhost',user='root',password='root', database='frontOM')
      cur=db.cursor()
      st="select * from course where Courseid='%s'"%(x)
      cur.execute(st)
      data=cur.fetchall()
      if len(data)==0:
          messagebox.showerror('ERROR','NO SUCH ENTRY FOUND')
      
      
      else:
          
          s="select Cname , Duration , Feeid from Course where Courseid='%s'"%(x)
          cur.execute(s)
          data=cur.fetchone()
          d.insert(0,(data[0]))
          f.insert(0,(data[1]))
          h.insert(0,(data[2]))
          db.commit()
          db.close()
  a=Label(t,text=' Courseid ',font="Times 20 bold",bd=1,bg="white" ,fg="black")
  a.place(x=500,y=200)
  b=Entry(t,width=30)
  b.place(x=800,y=200)
  c=Label(t,text=' Cname ',font="Times 20 bold",bd=1,bg="white" ,fg="black")
  c.place(x=500,y=260)
  d=Entry(t,width=30)
  d.place(x=800,y=260)
  e=Label(t,text=' Duration ',font="Times 20 bold",bd=1,bg="white" ,fg="black")
  e.place(x=500,y=320)
  f=Entry(t,width=30)
  f.place(x=800,y=320)
  g=Label(t,text=' Fee-id ',font="Times 20 bold",bd=1,bg="white" ,fg="black")
  g.place(x=500,y=380)
  h=Entry(t,width=30)
  h.place(x=800,y=380)
  bt1=Button(t,text=' UPDATE ',command=updatedata,font="Times 10 bold",bg="green" ,fg="white")
  bt1.place(x=800,y=440)
  bt2=Button(t,text=' BACK ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
  bt2.place(x=880,y=440)
  bt2=Button(t,text=' FIND ',command=finddata,font="Times 10 bold",bg="green" ,fg="white")
  bt2.place(x=1000,y=200)
  t.mainloop()
#UpdateCourse()  
  