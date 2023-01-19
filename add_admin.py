# add admin
from tkinter import *
import tkinter
from tkinter import messagebox
import pymysql
def new_admin():
    t=tkinter.Tk()
    t.geometry('1500x800')
    #t.maxsize(1,1080)   
    
    t.title('NEW ADMIN')
    w=Canvas(t,height=800,width=800,bg="lightgreen")
    w.place(x=1,y=1)
    def cleardata():
        t.destroy()
    def addAdmin():
       db= pymysql.connect(host='localhost',user='root',password='root',db='frontom')
       cur=db.cursor()
       p=a.get()
       q=b.get()
       r=c.get()
       if len(p)==0 or  len(q)==0 or  len(r)==0 :
           messagebox.showerror('ERROR','ENTER ALL FIELDS')
           t.destroy()
       else:    
           if q==r:
               st="select * from admin_info where adminid='%s'"%(p)
               cur.execute(st)
               data=cur.fetchall()
               if len(data)==0:
                   st="insert into admin_info values('%s','%s')"%(p,q)
                   cur.execute(st)
                   messagebox.showinfo('SAVED','NEW ADMIN ADDED')
                   db.commit()
                   db.close()
                   t.destroy()
               else:
                   messagebox.showerror('ERROR','''THIS USERNAME ALREADY EXIST''')
                   a.delete(0,100)
                   b.delete(0,100)
                   c.delete(0,100)
                   
                   
           else:
               messagebox.showerror('ERROR',"PASSWORD DOESN'T MATCH")
               b.delete(0,100)
               c.delete(0,100)
           
          
       
    l=Label(t,text="ADD ADMIN" ,font="Times 25 bold",bg='white')
    l.place(x=560,y=50)
    a1=Label(t,text='USER ID ',font='Times 15 bold')
    a1.place(x=500,y=220)
    a=Entry(t,width=30)
    a.place(x=700,y=220)
    b1=Label(t,text='PASSWORD ',font='Times 15 bold')
    b1.place(x=500,y=280)
    b=Entry(t,width=30)
    b.place(x=700,y=280)
    c1=Label(t,text='RE-ENTER',font='Times 15 bold')
    c1.place(x=500,y=340)
    c=Entry(t,width=30)
    c.place(x=700,y=340)


    btn1=Button(t,text='ADD ADMIN',font='Times 10 bold',bg='green',fg='white',command=addAdmin)
    btn1.place(x=700,y=380)
    btn2=Button(t,text='Back',font='Times 10 bold',bg='green',fg='white',command=cleardata)
    btn2.place(x=800,y=380)
    t.mainloop()
#new_admin()    