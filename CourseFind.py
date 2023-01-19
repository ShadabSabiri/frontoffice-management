import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
def findCourse():
    t=tkinter.Tk()
    t.geometry('1400x1200')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(700,100,text='   COURSE  DATA  FIND   ',font="Times 40 bold")
    def cleardata():
        t.destroy()
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
    b.place(x=700,y=200)
    c=Label(t,text=' Cname ',font="Times 20 bold",bd=1,bg="white" ,fg="black")
    c.place(x=500,y=260)
    d=Entry(t,width=30)
    d.place(x=700,y=260)
    e=Label(t,text=' Duration ',font="Times 20 bold",bd=1,bg="white" ,fg="black")
    e.place(x=500,y=320)
    f=Entry(t,width=30)
    f.place(x=700,y=320)
    g=Label(t,text=' Fee-id ',font="Times 20 bold",bd=1,bg="white" ,fg="black")
    g.place(x=500,y=380)
    h=Entry(t,width=30)
    h.place(x=700,y=380)
    fb=Button(t,text="Find ",command=finddata,font="Times  10 bold",bg="green" ,fg="white")
    fb.place(x=700,y=460)
    fb1=Button(t,text="Back",command=cleardata,font="Times  10 bold",bg="green" ,fg="white")
    fb1.place(x=800,y=460)
    t.mainloop()
    
#findCourse()    