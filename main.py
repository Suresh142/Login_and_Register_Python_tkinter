from tkinter import *
import mysql.connector
import tkinter.messagebox as m
from operator import itemgetter

mainWindow = Tk()
mainWindow.title("tkinter")
mainWindow.geometry("400x400")

bigText = Label(text="Login and Registration",font="Verdana 20 bold")
bigText.place(x=30,y=30)

def Register():
    registerWindow = Tk()
    registerWindow.title("Register")
    registerWindow.geometry("400x400")

    con = mysql.connector.connect(host="localhost",user="root",password="",database="loginandregister")
    cursor = con.cursor()

    bigText = Label(text="Registration",font="verdana 20 bold")
    bigText.place(x=100,y=30)

    name = Label(registerWindow,text="Name")
    name.place(x=90,y=100)
    age = Label(registerWindow, text="Age")
    age.place(x=90,y=140)
    email = Label(registerWindow, text="Email")
    email.place(x=90,y=180)
    password = Label(registerWindow, text="Password")
    password.place(x=90,y=220)

    e1 = Entry(registerWindow)
    e1.place(x=180,y=100)
    e2 = Entry(registerWindow)
    e2.place(x=180, y=140)
    e3 = Entry(registerWindow)
    e3.place(x=180, y=180)
    e4 = Entry(registerWindow)
    e4.place(x=180, y=220)

    def clearEntryBox():
        e1.delete(first=0,last=100)
        e2.delete(first=0,last=100)
        e3.delete(first=0,last=100)
        e4.delete(first=0,last=100)
    def error():
        m.showerror(title="error",message="passwords not same")

    def insert():
        insert = ("insert into register (name,age,email,password) values(%s,%s,%s,%s)")
        values = [e1.get(),e2.get(),e3.get(),e4.get()]
        if e3.get() :
            m.showinfo(title="Done",message="Account Created")
        else:
            error()
    register = Button(registerWindow,text="Register",fg="green",command=insert)
    register.place(x=175,y=260)
    btnExit = Button(registerWindow, text="Exit", bg="red", command=registerWindow.destroy)
    btnExit.place(x=350, y=350)

def Login():
    loginWindow = Tk()
    loginWindow.title("Login")
    loginWindow.geometry("400x400")

    con = mysql.connector.connect(host="localhost", user="root", password="", database="loginandregister")
    cursor = con.cursor()
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="loginandregister")
    cursor2 = conn.cursor()

    bigText = Label(text="Login", font="verdana 20 bold")
    bigText.place(x=140, y=30)

    emai = Label(loginWindow, text="Email")
    emai.place(x=100, y=150)
    password = Label(loginWindow, text="Password")
    password.place(x=100,y=180)

    e1 = Entry(loginWindow)
    e1.place(x=160,y=150)
    e2 = Entry(loginWindow)
    e2.place(x=160,y=180)
    def check ():
        sqlCommand1 = "select email from register"
        sqlCommand2 = "select password from register"

        cursor.execute(sqlCommand1)
        cursor2.execute(sqlCommand2)
        email = e1.get()
        password = e2.get()
        e=[]
        p=[]
        for i in cursor:
            e.append(i)
        for j in cursor2:
            p.append(j)
        res=list(map(itemgetter(0),e))
        res2=list(map(itemgetter(0),p))
        k = len(res)
        i=1
        while i<k:
            if res[i]==email and res2[i]==password:
                m.showinfo(title="Deo",message="Login Is Done")
                break
            i+=1
        else:
            m.showinfo(title="error",message="Some went wrong")

    login = Button(loginWindow, text="Login", fg="green", command=check)
    login.place(x=160, y=200)
    btnExit = Button(loginWindow, text="Exit", bg="red", command=loginWindow.destroy)
    btnExit.place(x=350, y=350)

    mainWindow.destroy()
    loginWindow.mainloop()

goToLogin = Button(mainWindow,text="Login",fg="green",font="verdana 10 bold",command=Login)
goToLogin.place(x=120,y=200)

goToRegister = Button(mainWindow,text="Register",fg="green",font="verdana 10 bold",command=Register)
goToRegister.place(x=180,y=200)

btnExit = Button(mainWindow,text="Exit",bg="red",command=mainWindow.destroy)
btnExit.place(x=350,y=350)

mainWindow.mainloop()
