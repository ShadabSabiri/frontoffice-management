import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox

def findfees():
    t=tkinter.Tk()
    t.geometry('1400x1200')
    t.title('Fee find')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(750,100,text='   FEES  DATA  FIND   ',font="Times 40 bold")
    def cleardata():
        t.destroy()
    def finddata():
            x=b.get()
            db=pymysql.connect(host='localhost',user='root',password='root', database='frontOM')
            cur=db.cursor()
            st="select * from fees where Feeid='%s' "%(x)
            cur.execute(st)
            data=cur.fetchall()
            if len(data)==0:
                messagebox.showerror('ERROR','NO SUCH ENTRY FOUND')
                
            else:
                
            
                s="select Amount , InsOne , InsTwo from Fees where Feeid='%s'"%(x)
                cur.execute(s)
                data=cur.fetchone()
                d.insert(0,(data[0]))
                f.insert(0,(data[1]))
                h.insert(0,(data[2]))
                db.commit()
                db.close() 
    
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
    bt=Button(t,text=' Find',command=finddata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=700,y=500)
    bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=800,y=500)
    t.mainloop()
#findfees()    