 
import urllib.request
from cryptography.fernet import Fernet
from tkinter import * 
         
root = Tk()
root.title("Spy Message Sender")
root.geometry("700x150")

def encryptMessage():                      
    pt = e1.get()
    key = str(e2.get())
    key = key.encode()
    fernet = Fernet(key)
    msg = fernet.encrypt(pt.encode())
    msg = msg.decode()
    b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=M0EFAIMXXCZPY7T8&field1='+msg)
    e3 = Entry(root, width=100)
    e3.grid(row = 12, column = 2)
    e3.insert(0, msg)

label1 = Label(root, text ='plain text - ')               
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='encryption key - ')
label2.grid(row = 11, column = 1)
label3 = Label(root, text ='encrypted text - ')
label3.grid(row = 12, column = 1)
e1 = Entry(root, width=100)
e1.grid(row = 10, column = 2)
e2 = Entry(root, width=100)
e2.grid(row = 11, column = 2)

ent = Button(root, text = "encrypt and send", bg ="red", fg ="white", command = encryptMessage)
ent.grid(row = 13, column = 2)

root.mainloop()