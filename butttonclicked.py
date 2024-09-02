from tkinter import *

root=Tk()
root.geometry("600x600")
root.config(bg="Blue")

x=True
count=1

def clicked(b):
    global x,count
    if b["text"] == " " and x==True:
        b["text"]="Wop"
        x=False
        count+=1

    elif b["text"]== " " and x==False:
        b["text"]="dap"
        x=True
        count+=1
    
    elif b["text"]=="Wop" and x==False:
        b["text"]="dap"
        x=True
        count+=1

    elif b["text"]=="dap" and x==True:
        b["text"]="Wop"
        x=False
        count+=1




b1=Button(text=" ",font=("arial",18),fg="Red",command=lambda: clicked(b1))
b1.grid(row=0,column=0,padx=10,pady=10)
b2=Button(text=" ",font=("arial",18),fg="Red",command=lambda: clicked(b2))
b2.grid(row=2,column=2)
#b3=Button(text="",font=("arial",18),fg="Red",command=botcot)
#b3.grid(row=3,column=3) 

root.mainloop()