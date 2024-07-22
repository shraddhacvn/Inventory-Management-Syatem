from tkinter import *
from tkinter import messagebox
from subprocess import call
 
 
def Ok():
    uname = e1.get()
    password = e2.get()
 
    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
 
    elif(uname == "Shraddha" and password == "shrcvn" or uname == "Kaveri" and password == "kv123" or uname == "Neha" and password == "neha01"):
 
        messagebox.showinfo("","Login Success")
        root.destroy()
        call(["python","InvetoryMP.py"])
 
    else :
        messagebox.showinfo("","Incorrent Username and Password")

def Reset():
    e1.delete(0,'end')
    e2.delete(0,'end')

def Quit():
    root.destroy()
 
 
root = Tk()
root.title("Login")
root.geometry("600x500")
root['background']='#87CEEB'
global e1
global e2

Label(root, text="Login Here!", font=25, bg="lightgray").place(x=250, y=30) 
Label(root, text="Username", font=15, bg="skyblue").place(x=150, y=100)
Label(root, text="Password",font=15, bg="skyblue").place(x=150, y=150)
 
e1 = Entry(root,width=25)
e1.place(x=270, y=100)
 
e2 = Entry(root,width=25)
e2.place(x=270, y=150)
e2.config(show="*")
 

Button(root, text="Login", command=Ok ,height = 2, width = 16).place(x=280, y=190)
Button(root, text="Reset", command=Reset ,height = 2, width = 8).place(x=270, y=250)
Button(root, text="Quit", command=Quit ,height = 2, width = 8).place(x=350, y=250)
 
root.mainloop()
