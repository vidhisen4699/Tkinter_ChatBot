from cgitb import text
from tkinter import *
root = Tk()

root.title("CHATBOT")
# root.geometry("500x500")

# e=Entry(root,width=100)
e= Entry(root,width = 30,fg = "blue")
e.grid(row=0,column=1)

def send():
    send="YOU :"+ e.get()
    text.insert(END,"\n"+send)
    if (e.get()=="hello"):
        text.insert(END,"\n"+"Bestie :hii")
    elif (e.get()=="hii"):
        text.insert(END,"\n"+"Bestie :Hello")
    elif (e.get()=="how are you"):
        text.insert(END,"\n"+"Bestie :fine and you")
    elif (e.get()=="yes,i'm also fine"):
        text.insert(END,"\n"+"Bestie :nice to hear")
    elif (e.get()=="i miss you a lots"):
        text.insert(END,"\n"+"Bsetie :i also")
    else:
        text.insert(END,"\n"+"Bestie :sorry i didn't get it")
    e.delete(0,END)

text=Text(root)
text.grid(row=0,column=0,columnspan=2)
# e=Entry(root,width=100)
send=Button(root,text="send",command=send,bg="light blue").grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()