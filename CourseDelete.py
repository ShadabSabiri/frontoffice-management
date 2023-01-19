import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def delcou():
    t=tkinter.Tk() 
    t.geometry('1450x1250')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(700,100,text='  COURSE DELETE  ',font="Times 40 bold")
    def cleardata():
        t.destroy()
    def deletedata():
        db=pymysql.connect(host='Localhost',user='root',password='root',db='frontOM')
        cur=db.cursor()
        p=b.get()
        st="select * from course where Courseid='%s'"%(p)
        cur.execute(st)
        data=cur.fetchall()
        if len(data)==0:
            messagebox.showerror('ERROR','NO SUCH ENTRY FOUND')
            
        else:    
            st="delete from Course where Courseid='%s' " %(p)
            cur.execute(st)
            db.commit()
            messagebox.showinfo('DELETE',' DELETED' )
            db.close()
            b.delete(0,100)
    a=Label(t,text=' Course-id ',font="Times 15 bold",bd=5, bg="white",fg="black")
    a.place(x=500,y=250)
    b=Entry(t,width=30)
    b.place(x=700,y=250)
    bt=Button(t,text=' DELETE ',command=deletedata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=700,y=300)
    bt=Button(t,text=' BACK ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=800,y=300)
    t.mainloop();
#delcou()    