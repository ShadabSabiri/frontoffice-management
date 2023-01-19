import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
def findCComplete():
    t=tkinter.Tk()
    t.geometry('1400x1200')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(800,100,text='   COURSE  COMPLETI0N  FIND   ',font="Times 30 bold")
    def cleardata():
        t.destroy()
    def finddata():
        x=b.get()
        db=pymysql.connect(host='localhost',user='root',password='root', db='frontom')
        cur=db.cursor()
        
        s="select DOComplete , Resid  from ccomplete where CertificateNo='%s'"%(x)
        cur.execute(s)
        data=cur.fetchone()
        if (not data ):
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
    bt=Button(t,text=' Find ',command=finddata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=830,y=380)
    bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=900,y=380)
    t.mainloop()
#findCComplete()