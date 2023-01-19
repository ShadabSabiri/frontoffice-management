# login form
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from MainPage import *
from add_admin import *
t=tkinter.Tk()
t.geometry('1500x800')
#t.geometry('650x650')

def show_pass():
    q=b.get()
    if  (not p) or (not q):
        messagebox.showerror('ERROR','ENTER USERNAME AND PASSWORD')
        
    else:
        b.insert(0,b)
        
        
    
    
def cleardata():
    a.delete(0,100)
    b.delete(0,100)
def newuser():
    
    new_admin()
def login():
        db=pymysql.connect(host='localhost',
            user='root',password='root',db='frontom')
        cur=db.cursor()
        p=a.get()
        q=b.get()
        print(type(a.get()))
        print(type(b.get()))
        if len(p)==0 or len(q)==0:
            messagebox.showerror('ERROR','ENTER ALL FIELDS')
            
        else:
            
            st="select * from admin_info where adminid='%s' and passwd='%s'"%(p,q)
            cur.execute(st)
            data=cur.fetchall()
            if (data):
                messagebox.showinfo('SUCCESSFULL','LOGIN SUCCESSFULL')
                mainmenu()
            #save
            else:
                messagebox.showerror('ERROR','EITHER USERNAME OR PASSWORD IS INCORRECT')
                
                
                
                
W=Canvas(t,height=800,width=800,bg='lightgreen')
W.place(x=1,y=1)
W.create_text(650,100,text='ADMIN LOGIN',font="Times 25 bold", fill='black')
a1=Label(t,text='USER ID ',font='Times 15 bold')
a1.place(x=500,y=220)
a=Entry(t,width=30)
a.place(x=700,y=220)
b1=Label(t,text='PASSWORD ',font='Times 15 bold')
b1.place(x=500,y=300)
b=Entry(t,width=30,show='*')
b.place(x=700,y=300)

btn1=Button(t,text='Login',font='Times 10 bold',bg='green',fg='white',command=login)
btn1.place(x=700,y=350)
btn2=Button(t,text='Clear',font='Times 10 bold',bg='green',fg='white',command=cleardata)
btn2.place(x=770,y=350)
#btn2=Button(t,text='Show',font='Times 10 bold',bg='green',fg='white',command=show_pass)
#btn2.place(x=900,y=300)
btn3=Button(t,text='New User?',font='Times 10 bold',bg='green',fg='white',command=newuser)
btn3.place(x=950,y=220)
t.mainloop()



