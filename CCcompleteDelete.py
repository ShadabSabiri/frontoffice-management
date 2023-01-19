import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def delccom():
    t=tkinter.Tk() 
    t.geometry('1450x1250')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    def cleardata():
        t.destroy()
    z.place(x=1,y=1)
    z.create_text(700,100,text=' DELETE CERTIFICATE ',font="Times 30 bold")
    def deletedata():
        db=pymysql.connect(host='Localhost',user='root',password='root',db='frontOM')
        cur=db.cursor()
        p=b.get()
        st="select * from CComplete where CertificateNo='%s' "%(p)
        cur.execute(st)
        data=cur.fetchall()
        if (not data):
            messagebox.showerror('ERROR','ENTER VALID ID')
            b.delete(0,100)
        else:
            
            st="delete from CComplete where CertificateNo='%s' " %(p)
            cur.execute(st)
            db.commit()
            messagebox.showinfo('DELETE',' DELETED' )
            db.close()
            b.delete(0,100)
    a=Label(t,text=' Certification No. ',font="Times 15 bold",bd=1)
    a.place(x=400,y=200)
    b=Entry(t,width=30)                                                
    b.place(x=730,y=200)
    bt=Button(t,text=' Delete ',command=deletedata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=730,y=260)
    bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=800,y=260)
    t.mainloop();
#delccom()    