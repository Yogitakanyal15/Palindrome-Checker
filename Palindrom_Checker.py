#Palindrome Checker
from tkinter import *

root=Tk()
root.title("Palindrome Cheker")
enter=Entry(root,width=50,borderwidth=5)
enter.grid(row=0,column=0,columnspan=4,padx=20, pady=20)

def Palindrome():
    string=enter.get()
    length=len(string)
    for i in range(length//2):
        if(string[i]!=string[length-1-i]):
            myLabel=Label(root,text=string+" is not palindrome!")
            myLabel.grid(row=3,column=0,columnspan=4,padx=20, pady=20)
            return
    myLabel=Label(root,text=string+" is palindrome!")
    myLabel.grid(row=3,column=0,columnspan=4,padx=20, pady=20)

myButton=Button(root,text="Submit",command=Palindrome)
myButton.grid(row=1,column=1, columnspan=2,padx=20, pady=20)

root.mainloop()
        
        
