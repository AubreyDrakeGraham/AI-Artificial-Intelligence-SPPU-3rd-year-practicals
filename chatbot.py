from tkinter import *

chat =Tk()
chat.title("chatbot")

def send():
    message="you : " + e.get()
    txt.insert(END,message)
    user=e.get().lower()
    if user=="hello":
        txt.insert(END,"\nBot:hi\n")
    elif user=="hi" or user=="hii" or user=="hiiii":
        txt.insert(END,"\nBot:Hello\n")
    elif user=="how are you":
        txt.insert(END,"\nBot: fine! and you\n")
    elif user=="fine" or user=="i am good" or user=="i am doing good":
        txt.insert(END,"\nBot: Great! how can I help you.\n")
    else:
        txt.insert(END,"\nBot: Sorry I didn't get you.\n")
        e.delete(0,END)

txt = Text()
txt.grid(row=0, column=0)

e = Entry(width=100)
e.grid(row=1, column=0)

send = Button(text="Send", command=send)
send.grid(row=1, column=1)

chat.mainloop()