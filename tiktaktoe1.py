from tkinter import *
root=Tk()
root.geometry("600x600")


turn=True
count=0

#disable all button
def DAB():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#function that add X and O while clicking
def  clicked(b):
    global turn,count
    if b["text"] == " " and turn==True:
        b["text"]="X"
        turn=False
        count+=1
        whowon()
    
    elif b["text"] == " " and turn==False:
        b["text"]="O"
        turn=True
        count+=1
        whowon()
    
#who won
winner=False

def whowon():
    global winner
    #X win
    #horizontals
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        winner=True
        b1.config(bg="Red")
        b2.config(bg="Red")
        b3.config(bg="Red")
        DAB()

    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        winner=True
        b4.config(bg="Red")
        b5.config(bg="Red")
        b6.config(bg="Red")
        DAB()

    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        winner=True
        b7.config(bg="Red")
        b8.config(bg="Red")
        b9.config(bg="Red")
        DAB()

    #verticals
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        winner=True
        b1.config(bg="Red")
        b4.config(bg="Red")
        b7.config(bg="Red")
        DAB()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        winner=True
        b2.config(bg="Red")
        b5.config(bg="Red")
        b8.config(bg="Red")
        DAB()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        winner=True
        b3.config(bg="Red")
        b6.config(bg="Red")
        b9.config(bg="Red")
        DAB()
    #Diagonal
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        winner=True
        b1.config(bg="Red")
        b5.config(bg="Red")
        b9.config(bg="Red")
        DAB()
    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        winner=True
        b3.config(bg="Red")
        b5.config(bg="Red")
        b7.config(bg="Red")
        DAB()
    
    #O win
    #horizontals
    elif b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        winner=True
        b1.config(bg="Red")
        b2.config(bg="Red")
        b3.config(bg="Red")
        DAB()

    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        winner=True
        b4.config(bg="Red")
        b5.config(bg="Red")
        b6.config(bg="Red")
        DAB()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        winner=True
        b7.config(bg="Red")
        b8.config(bg="Red")
        b9.config(bg="Red")
        DAB()
    #verticals
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        winner=True
        b1.config(bg="Red")
        b4.config(bg="Red")
        b7.config(bg="Red")
        DAB()
    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        winner=True
        b2.config(bg="Red")
        b5.config(bg="Red")
        b8.config(bg="Red")
        DAB()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        winner=True
        b3.config(bg="Red")
        b6.config(bg="Red")
        b9.config(bg="Red")
        DAB()
    #Diagonal
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        winner=True
        b1.config(bg="Red")
        b5.config(bg="Red")
        b9.config(bg="Red")
        DAB()
    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        winner=True
        b3.config(bg="Red")
        b5.config(bg="Red")
        b7.config(bg="Red")
        DAB()

#command can take callable function with no argument
#so either we have to write there lambda or functools.partial

b1=Button(root,text=" ",font=("arial",10,"bold"),bg="SystemButtonFace",command=lambda: clicked(b1),width=20,height=10)
b1.grid(row=0,column=0)
b2=Button(root,text=" ",font=("arial",10),command=lambda: clicked(b2),width=20,height=10)
b2.grid(row=1,column=0)
b3=Button(root,text=" ",font=("arial",10),command=lambda: clicked(b3),width=20,height=10)
b3.grid(row=2,column=0)

b4=Button(root,text=" ",font=("arial",10),command=lambda: clicked(b4),width=20,height=10)
b4.grid(row=0,column=1)
b5=Button(root,text=" ",font=("arial",10),command=lambda: clicked(b5),width=20,height=10)
b5.grid(row=1,column=1)
b6=Button(root,text=" ",font=("arial",10),command=lambda: clicked(b6),width=20,height=10)
b6.grid(row=2,column=1)

b7=Button(root,text=" ",font=("arial",10),command=lambda: clicked(b7),width=20,height=10)
b7.grid(row=0,column=2)
b8=Button(root,text=" ",font=("arial",10),command=lambda: clicked(b8),width=20,height=10)
b8.grid(row=1,column=2)
b9=Button(root,text=" ",font=("arial",10),command=lambda: clicked(b9),width=20,height=10)
b9.grid(row=2,column=2)


root.mainloop()