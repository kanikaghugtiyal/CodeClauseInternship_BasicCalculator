from tkinter import *
def click(event):
    global value
    text=event.widget.cget("text")
    print(text)

    if(text=="="):
        if value.get().isdigit():
            Value=int(value.get())
        else:
            Value=eval(screen.get())
            value.set(Value)
            screen.update()
            
    elif(text=="C"):
        value.set("")
        screen.update()

    else:
        value.set(value.get()+text)
        screen.update()

root=Tk()
root.geometry("500x500")
root.title(" Calculator")

value=StringVar()
value.set(" ")
screen=Entry(root,textvar=value ,font="lucida 40 bold")
screen.pack(fill=X, ipadx=10, padx=8,pady=8)


fr=Frame(root,bg="grey")
fr.pack()


btn=Button(fr,text="+",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=17,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="9",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right" ,padx=17,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="8",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=17,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="7",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=16,pady=5)
btn.bind("<Button-1>",click)

fr=Frame(root,bg="grey")
fr.pack()

btn=Button(fr,text="-",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=17,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="6",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right" ,padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="5",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="4",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=18,pady=5)
btn.bind("<Button-1>",click)

fr=Frame(root,bg="grey")
fr.pack()

btn=Button(fr,text="*",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right" ,padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="3",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right" ,padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="2",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="1",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=16,pady=5)
btn.bind("<Button-1>",click)

fr=Frame(root,bg="grey")
fr.pack()

btn=Button(fr,text="/",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="C",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right",padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="0",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right" ,padx=18,pady=5)
btn.bind("<Button-1>",click)

btn=Button(fr,text="=",padx=20,pady=18,font="lucida 20 bold")
btn.pack(side="right" ,padx=15,pady=5)
btn.bind("<Button-1>",click)

root.mainloop()
