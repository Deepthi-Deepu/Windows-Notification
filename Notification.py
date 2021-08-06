
from plyer import notification
import tkinter as tk
from tkinter import*
from tkinter import filedialog
root = tk.Tk()
root.geometry("400x250")
root.title("Notification app")
root.configure(bg="#728FCE")
title = StringVar()
message = StringVar()
Label(root,text="Windows Notification App",bg="#728FCE",fg='#404042',font="Verdana 20 bold").pack()
Label(root,text="Title",bg="#728FCE",font="Verdana 10 bold").place(x=60,y=40)
Entry(root,text="Title",width=50,textvariable = title).place(x=150,y=40)
Label(root,text="Message",bg="#728FCE",font="Verdana 10 bold").place(x=60,y=80)
Entry(root,width=50,textvariable=message).place(x=150,y=80)
Label(root,text="Icon Path",bg="#728FCE",font="Verdana 10 bold").place(x=60,y=120)
label_file_explorer=Label(root,text="Icon:",width=44,fg="blue")
label_file_explorer.place(x=150,y=120)
def select_icon():
    global filename
    filename=filedialog.askopenfilename(initialdir="/",title="select a file",filetypes=(("ICO file","*.ico*"),("all files","*.*")))
    label_file_explorer.configure(text="Icon:"+filename)
def Send_Notification():
    notification.notify(title=str(title.get()),message =str(message.get()),app_icon=filename,timeout=20,)
def clear():
    title.set('')
    message.set('')
Button(root,text="Select Icon",width=15,command=select_icon,fg='#fff',bg='#404042').place(x=60,y=190)
Button(root,text="Send Notification",width=15,fg='#fff',bg='#404042',command=Send_Notification).place(x=190,y=190)
Button(root,text="clear",width=15,fg='#fff',bg='#404042',command=clear).place(x=320,y=190)
root.mainloop()