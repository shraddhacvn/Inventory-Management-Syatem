from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime
 
def pay():
    totall = float(tot.cget("text"))
    if(e11.get()==""):
        messagebox.showinfo("","Please enter amount")
    else:
        pay = float(e11.get())
        if(pay<totall):
            messagebox.showinfo("","Please enter sufficient amount")
        else:
            bal = pay - totall
            balText.set(bal)

def deleteSelected():
    x = listBox.selection()
    listBox.delete(x)

def remove_all():
    for record in listBox.get_children():
        listBox.delete(record)
    totText.set("0.0")
    balText.set("0.0")
    e11.delete(0,'end')
    messagebox.showinfo("","You removed all the items!")
        

def print_bill():
    if(e11.get()==""):
        messagebox.showinfo("","Please Pay Amount")
    else:
        tott = float(totText.get())
        top = Toplevel()
        top.geometry("400x500")
        top.config(bg="white")
       
        d = Label(top, text=f'{d1}')
        d.pack()
        t = Label(top, text=f'{t1}')
        t.pack()
        
        l = Label(top, text='\n\n---------RECIEPT----------')
        l.pack()
        l.config(bg="white")
        heading = Label(top, text='\nItem\t\tPRICE\t\tQTY\t\tTOTAL')
        heading.pack()
        heading.config(bg="white")
        
       
        for child in listBox.get_children():
            item = (listBox.item(child, 'values')[0])
            price = float(listBox.item(child, 'values')[1])
            qty = float(listBox.item(child, 'values')[2])
            tot = float(listBox.item(child, 'values')[3])
            item1 = Label(top, text=f'{item}\t\t{price}\t\t{qty}\t\t{tot}')
            item1.config(bg="white")
            item1.pack()

        tot = Label(top, text=f'\nTotal\t{tott}')
        tot.config(bg="white")
        tot.pack()

        l1 = Label(top, text='\n\nSave Paper, Go Electronic!',font=("Arial Bold", 10),fg="#00FF00")
        l1.pack()
        l1.config(bg="white")
        
 
def show():

    if(var1.get()==0 and var2.get()==0 and var3.get()==0 and var4.get()==0 and var5.get()==0 and var6.get()==0 and var7.get()==0 and var8.get()==0 and var9.get()==0 and var10.get()==0):
         messagebox.showinfo("","Please Select at least one item")
    else:
        tot = 0
        if(var1.get()):
            price = int(e1.get())
            qty = int(q1.get())
            tot = int(price * qty)
            tempList = [['Rice', e1.get(), q1.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList,start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))
     
        if (var2.get()):
            price = int(e2.get())
            qty = int(q2.get())
            tot = int(price * qty)
            tempList = [['Sugar', e2.get(), q2.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))
     
        if (var3.get()):
            price = int(e3.get())
            qty = int(q3.get())
            tot = int(price * qty)
            tempList = [['LEAF', e3.get(), q3.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))
     
        if (var4.get()):
            price = int(e4.get())
            qty = int(q4.get())
            tot = int(price * qty)
            tempList = [['Wheat', e4.get(), q4.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
     
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))
     
        if (var5.get()):
            price = int(e5.get())
            qty = int(q5.get())
            tot = int(price * qty)
            tempList = [['Salt', e5.get(), q5.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))

        if (var6.get()):
            price = int(e6.get())
            qty = int(q6.get())
            tot = int(price * qty)
            tempList = [['Vegetable Oil', e6.get(), q6.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))

        if (var7.get()):
            price = int(e7.get())
            qty = int(q7.get())
            tot = int(price * qty)
            tempList = [['Oats', e7.get(), q7.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))

        if (var8.get()):
            price = int(e8.get())
            qty = int(q8.get())
            tot = int(price * qty)
            tempList = [['Jaggery', e8.get(), q8.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))

        if (var9.get()):
            price = int(e9.get())
            qty = int(q9.get())
            tot = int(price * qty)
            tempList = [['Besan Flour', e9.get(), q9.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))

        if (var10.get()):
            price = int(e10.get())
            qty = int(q10.get())
            tot = int(price * qty)
            tempList = [['Termeric Powder', e10.get(), q10.get(), tot]]
            tempList.sort(key=lambda e: e[1], reverse=True)
            for i, (item, price, qty, tot) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(item, price, qty, tot))
     
        sum1 = 0.0
        for child in listBox.get_children():
            sum1 += float(listBox.item(child, 'values')[3])
        totText.set(sum1)

 
root = Tk()
root.title("Inventory Management System")
root.geometry("900x900")
root['background']='#87CEEB'
global e1
global e2
global e3
global e4

global totText
global balText
global listBox
global dateText
global timeText

dateText = StringVar()
timeText = StringVar()
d1 = StringVar()
totText = IntVar()
balText = IntVar()

dateText = date.today()
d1 = dateText.strftime("%d/%m/%Y")

timeText = datetime.now()
t1 = timeText.strftime("%H:%M:%S")


 
Label(root, text="Items List",font="arial 10 bold", bg="cyan").place(x=5, y=10)
Label(root, text="Price",font="arial 10 bold", bg="cyan").place(x=180, y=10)
Label(root, text="Quantity",font="arial 10 bold", bg="cyan").place(x=330, y=10)
 
var1 = IntVar()
Checkbutton(root, text="Rice", variable=var1, bg = "skyblue").place(x=10, y=50)
 
var2 = IntVar()
Checkbutton(root, text="Sugar", variable=var2, bg = "skyblue").place(x=10, y=80)
 
var3 = IntVar()
Checkbutton(root, text="LEAF", variable=var3, bg = "skyblue").place(x=10, y=110)
 
var4 = IntVar()
Checkbutton(root, text="Wheat", variable=var4, bg = "skyblue").place(x=10, y=140)
 
var5 = IntVar()
Checkbutton(root, text="Salt", variable=var5, bg = "skyblue").place(x=10, y=170)

var6 = IntVar()
Checkbutton(root, text="Vegetable Oil", variable=var6, bg = "skyblue").place(x=10, y=200)

var7 = IntVar()
Checkbutton(root, text="Oats", variable=var7, bg = "skyblue").place(x=10, y=230)

var8 = IntVar()
Checkbutton(root, text="Jaggery", variable=var8, bg = "skyblue").place(x=10, y=260)

var9 = IntVar()
Checkbutton(root, text="Besan Flour", variable=var9, bg = "skyblue").place(x=10, y=290)

var10 = IntVar()
Checkbutton(root, text="Turmeric Powder", variable=var10, bg = "skyblue").place(x=10, y=320)


Label(root, text="Total", bg = "skyblue").place(x=600, y=10) 
Label(root, text="Pay", bg = "skyblue").place(x=600, y=50)
Label(root, text="Balance", bg = "skyblue").place(x=600, y=80)
 
#text entry for price
e1 = Entry(root, justify='center')
e1.insert(END, '60')
e1.configure(state='readonly')
e1.place(x=140, y=50)
 
e2 = Entry(root, justify='center')
e2.insert(END, '40')
e2.configure(state='readonly')
e2.place(x=140, y=80)
 
e3 = Entry(root, justify='center')
e3.insert(END, '30')
e3.configure(state='readonly')
e3.place(x=140, y=110)
 
e4 = Entry(root, justify='center')
e4.insert(END, '36')
e4.configure(state='readonly')
e4.place(x=140, y=140)
 
e5 = Entry(root, justify='center')
e5.insert(END, '20')
e5.configure(state='readonly')
e5.place(x=140, y=170)

e6 = Entry(root, justify='center')
e6.insert(END, '150')
e6.configure(state='readonly')
e6.place(x=140, y=200)

e7 = Entry(root, justify='center')
e7.insert(END, '100')
e7.configure(state='readonly')
e7.place(x=140, y=230)

e8 = Entry(root, justify='center')
e8.insert(END, '70')
e8.configure(state='readonly')
e8.place(x=140, y=260)

e9 = Entry(root, justify='center')
e9.insert(END, '120')
e9.configure(state='readonly')
e9.place(x=140, y=290)

e10 = Entry(root, justify='center')
e10.insert(END, '125')
e10.configure(state='readonly')
e10.place(x=140, y=320)

#text entry for quantity 
q1 = Entry(root, justify='center')
q1.place(x=300, y=50)
 
q2 = Entry(root, justify='center')
q2.place(x=300, y=80)
 
q3 = Entry(root, justify='center')
q3.place(x=300, y=110)
 
q4 = Entry(root, justify='center')
q4.place(x=300, y=140)
 
q5 = Entry(root, justify='center')
q5.place(x=300, y=170)

q6 = Entry(root, justify='center')
q6.place(x=300, y=200)

q7 = Entry(root, justify='center')
q7.place(x=300, y=230)

q8 = Entry(root, justify='center')
q8.place(x=300, y=260)

q9 = Entry(root, justify='center')
q9.place(x=300, y=290)

q10 = Entry(root, justify='center')
q10.place(x=300, y=320)

 
 
tot = Label(root, text="",font="arial 22 bold", textvariable=totText, bg = "skyblue")
tot.place(x=650, y=10)
 
 
e11 = Entry(root)
e11.place(x=650, y=50)
 
e12 = Entry(root)
 
balance = Label(root, text="",font="arial 22 bold", textvariable=balText, bg = "skyblue").place(x=650, y=80)

Button(root, text="Add",command = show,height=3, width= 13).place(x=10, y=360)
Button(root, text="Pay Now",command = pay,height=3, width= 13).place(x=650, y=120)
Button(root, text="Delete Selected",command = deleteSelected,height=3, width= 13).place(x=160, y=360)
Button(root, text="Remove All",command = remove_all,height=3, width= 13).place(x=280, y=360)
Button(root, text="Print", command=print_bill, height=3, width=13).place(x=650, y=190)

cols = ('item', 'price', 'qty','total')
listBox = ttk.Treeview(root, columns=cols, show='headings')
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=450)
 
root.mainloop()
