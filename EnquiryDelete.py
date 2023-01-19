import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def delenq():
    t=tkinter.Tk() 
    t.geometry('1450x1250')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(600,100,text='  ENQUIRY  DELETE  ',font="Times 25 bold")
    def clear():
         t.destroy()   
    def deletedata():
        db=pymysql.connect(host='Localhost',user='root',password='root',db='frontOM')
        cur=db.cursor()
        p=b.get()
        st="select * from enquiry where Enqid='%s'"%(p)
        cur.execute(st)
        data=cur.fetchall()
        if len(data)==0:
            messagebox.showerror('ERROR','ENTER VALID ID')
            
        else:
            st="delete from Enquiry where Enqid='%s' " %(p)
            cur.execute(st)
            db.commit()
            messagebox.showinfo('DELETE',' DELETED' )
            db.close()
            b.delete(0,100)
    a=Label(t,text='  Enquiry-id  ',font="Times 20 bold",bg="lightblue")
    a.place(x=400,y=200)
    b=Entry(t,width=30)
    b.place(x=600,y=210)
    bt=Button(t,text=' DELETE ',command=deletedata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=600,y=260)
    bt1=Button(t,text=' Back ',command=clear,font="Times 10 bold",bg="green" ,fg="white")
    bt1.place(x=700,y=260)
    t.mainloop();
#delenq()  