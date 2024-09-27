import pyshorteners
from  tkinter import *
root=Tk()

root.geometry("700x500")
root.title("Url Shortner")
root.configure(bg="grey")

url_mapping = {}

def short():
    url = Entry1.get()
    if url:
        try:
            s = pyshorteners.Shortener().tinyurl.short(url)
            Entry2.delete(0, END) 
            Entry2.insert(END, s)
        except Exception as e:
            Entry2.delete(0, END)
            Entry2.insert(END, "Error: " + str(e))
    else:
        Entry2.delete(0, END)
        Entry2.insert(END, "Please enter a URL.")

Label(root,text="Enter your url link" ,font="impack 17 bold",bg="black",fg="white").pack(fill="x")
Entry1=Entry(root,font="10",bd=4,width="60")
Entry1.pack(pady=30)

btn=Button(root,text="Click",font="impack 12 bold",bg="blue",fg="white",width="14",command=short)
btn.pack(pady=40)

Entry2=Entry(root,font="impack 16 bold",bg="black",fg="white",width=24)
Entry2.pack(pady=30)

mainloop()
