import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def delbat():
    t=tkinter.Tk() 
    t.geometry('1450x1250')
    z=Canvas(t,height=800,width=1500,bg='lightgreen')
    z.place(x=1,y=1)
    z.create_text(700,100,text='  BATCH DATA  DELETE  ',font="Times 25 bold")
    def cleardata():
        t.destroy()
    def deletedata():
        db=pymysql.connect(host='Localhost',user='root',password='root',db='frontOM')
        cur=db.cursor()
        p=b.get()
        st="delete from Batchdata where Batchid='%s' " %(p)
        cur.execute(st)
        db.commit()
        messagebox.showinfo('DELETE',' DELETED' )
        db.close()
        b.delete(0,100)
        
        
    a=Label(t,text=' Batch-id ',font="Times 15 bold",bd=1)
    a.place(x=500,y=200)
    b=Entry(t,width=30)
    b.place(x=700,y=200)
    bt=Button(t,text=' Delete ',command=deletedata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=700,y=250)
    bt=Button(t,text=' Back ',command=cleardata,font="Times 10 bold",bg="green" ,fg="white")
    bt.place(x=800,y=250)
    t.mainloop();        
#delbat()    