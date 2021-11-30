from tkinter import *
from tkinter.ttk import Combobox
from google_currency import convert
import json
from tkinter import messagebox

root = Tk()
root.geometry("500x400")
root.title("Currency Convertor")
root.config(bg="light sky blue")

with open("data.txt") as f:
    lines = f.readlines()

dictop = {}    
for line in lines:
    opaq = line.split("\t");
    dictop[opaq[1]] =  opaq[2]

def function_calculate():
    try:
        lightbox = SelectFrom_Com1.get()
        heavybox = SelectTo_Com2.get()
        lapto = dictop[lightbox]
        lapti = dictop[heavybox]
        serial = var1.get() 
        opol = convert(lapto, lapti, serial)
        lope = json.loads(opol)
        jsonfix = lope["amount"]
        var2.set(jsonfix)
    except:
        rr = messagebox.askretrycancel("A Problem Has Been Occured", "Please Check your Internet Connection or Check the Amount You Have Entered.")

def function_clear():
    var1.set("0")
    var2.set("0")


Heading = Label(root, text="Currency Convertor", fg="black",bg="dark turquoise", font=("ubuntu", 15, "bold"))
Heading.place(x=170, y=10)


Enter_Lab1 = Label(root, text="Enter The Amount/Value:", bg="dark slate gray", fg="white", font=("ubuntu", 15, "italic"))
Enter_Lab1.place(x=10, y=60)


var1 = IntVar()
Enter_Ent1 = Entry(root, width=20 ,text=var1, bg="white", fg="black", font=("ubuntu", 15, "bold"))
Enter_Ent1.place(x=270, y=60)


SelectFrom_Lab2 = Label(root, text="Select The Currency ( Convert From ): ", bg="teal", fg="white", font=("ubuntu", 10, "bold"))
SelectFrom_Lab2.place(x=10, y=120)


slider = StringVar()
SelectFrom_Com1 = Combobox(root, width=25, textvariable=slider, state="readonly", font=("ubuntu", 10, "bold"))
SelectFrom_Com1['values'] = [item for item in dictop.keys()]
SelectFrom_Com1.current(4)
SelectFrom_Com1.place(x=270, y=120)


SelectTo_Lab3 = Label(root, text="Selecth The Currency ( Convert To ):  ",bg="teal",  fg="white", font=("ubuntu", 10, "bold"))
SelectTo_Lab3.place(x=10, y=160)


foreground = StringVar
SelectTo_Com2 = Combobox(root, width=25, textvariable=foreground,state="readonly", font=("ubuntu", 10, "bold"))
SelectTo_Com2['values'] = [item for item in dictop.keys()]
SelectTo_Com2.current(0)
SelectTo_Com2.place(x=270, y=160)



Calculate_But1 = Button(root, bg="steel blue", text="Calculate", command=function_calculate , fg="white", font=("ubuntu", 15, "bold"), relief=RAISED,\
                            cursor="hand2")
Calculate_But1.place(x=160, y=220)


Clear_But2 = Button(root, bg="steel blue", text="Clear", command=function_clear, fg="white", font=("ubuntu", 15, "bold"), relief=RAISED,\
                            cursor="hand2")
Clear_But2.place(x=270, y=220)


Converted_Lab4 = Label(root, text="Converted Amount/Value : ", bg="dark slate gray", fg="white", font=("ubuntu", 15, "italic"))
Converted_Lab4.place(x=10, y=300)


var2 = IntVar()
Converted_Ent2 = Entry(root, textvariable=var2, fg="blue",state="readonly",width=20, font=("ubuntu", 15, "bold"))
Converted_Ent2.place(x=270, y=300)


Develop_Lab5 = Label(root, text="Developed and Designed By Rohit and Pragati",bg="dark turquoise", fg="black", font=("ubuntu",7, "bold"))
Develop_Lab5.place(x=5, y=380)


Exit_But3=Button(root,bg="steel blue",text="Exit", command=root.destroy, fg="white",font=("arial", 10))
Exit_But3.place(x=460,y=340)


root.mainloop()
