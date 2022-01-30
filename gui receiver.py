import requests
from cryptography.fernet import Fernet
from tkinter import * 
         
root = Tk()
root.title("Spy Message Receiver")
root.geometry("700x150")

def decryptMessage():                      
    key = e1.get()
    msg=requests.get("https://thingspeak.com/channels/1461170/field/1")
    msg=msg.json()['feeds'][-1]['field1']
    encMessage = str(msg)
    encMessage = encMessage.encode()
    key = key.encode()
    fernet = Fernet(key)
    decMessage = fernet.decrypt(encMessage)
    e2 = Entry(root, width=100)
    e2.grid(row = 11, column = 2)
    e2.insert(0, decMessage)

label1 = Label(root, text ='Enter Your Key - ')               
label1.grid(row = 10, column = 1)
label2 = Label(root, text ='Decrypted text - ')
label2.grid(row = 11, column = 1)

e1 = Entry(root, width=100)
e1.grid(row = 10, column = 2)

ent = Button(root, text = "decrypt and read", bg ="red", fg ="white", command = decryptMessage)
ent.grid(row = 13, column = 2)

root.mainloop()