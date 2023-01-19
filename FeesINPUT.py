import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def insfee():
 t=tkinter.Tk()
 t.geometry('1450x1250')
 z=Canvas(t,height=800,width=1500,bg='lightgreen')
 z.place(x=1,y=1)
 z.create_text(700,100,text='   FEES   ',font="Times 40 bold")
 def cleardata():
     t.destroy()
 def savedata():
     x=b.get()
     y=int(d.get())
     pp=int(f.get())
     rr=int(h.get())
     db=pymysql.connect(host='localhost',user='root',password='root', database="frontOM")
     cur=db.cursor()
     if len(x)==0 :
         messagebox.showerror('ERROR','ENTER ALL FIELDS')
     else:
         s="insert into fees values('%s',%d,%d,%d)"%(x,y,pp,rr)
         cur.execute(s)
         db.commit()
         messagebox.showinfo('    Information    ','   Data Saved   ')
         db.close()
         b.delete(0,100)
         d.delete(0,100)
         f.delete(0,100)
         h.delete(0,100)
        
 a=Label(t,text=' Feesid ',font="Times 15 bold",bg="white" ,fg="black")
 a.place(x=500,y=260)
 b=Entry(t,width=30)
 b.place(x=700,y=260)
 c=Label(t,text=' Amount ',font="Times 15 bold",bg="white" ,fg="black")
 c.place(x=500,y=320)
 d=Entry(t,width=30)
 d.place(x=700,y=320)
 e=Label(t,text=' Installment01',font="Times 15 bold",bg="white" ,fg="black")
 e.place(x=500,y=380)
 f=Entry(t,width=30)
 f.place(x=700,y=380)
 g=Label(t,text=' Installment02',font="Times 15 bold",bg="white" ,fg="black")
 g.place(x=500,y=440)
 h=Entry(t,width=30)
 h.place(x=700,y=440)
 bt=Button(t,text=' Save ',command=savedata,font="Times 10 bold",bg="green" ,fg="white")
 bt.place(x=700,y=500)
 bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
 bt.place(x=800,y=500)
 t.mainloop();
#insfee() 
 
 