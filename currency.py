import tkinter as tk
from tkinter import *
import tkinter.messagebox

class currency:
    def __init__(self,root):
        self.root=root
        self.root.title("currency convertor")
        self.root.geometry("700x500")
        variable1=tk.StringVar(root)
        variable2=tk.StringVar(root)
        variable1.set("currency")
        variable2.set("currency")
        frame1=Frame(self.root,bg='#4d5d78')
        frame1.place(x=0,y=0,width=700,height=500)
        title=Label(frame1,text="Currency Convertor",font=("times new roman",26,"bold"),bg="#4d5d78",fg="black").place(x=200,y=40)
        #for creating a label for amount
        amount=Label(frame1,text="Amount :",font=("times new roman",19,"bold"),bg="#4d5d78",fg="black").place(x=20,y=130)
        # for taking input from the user 
        # self.amount=Entry(frame1,font=("times new roman",19),bg="#9fcfd1",fg="black").place(x=200,y=130,width=400)
        #for creating a label for from currency
        amount=Label(frame1,text="From Currency:",font=("times new roman",19,"bold"),bg="#4d5d78",fg="black").place(x=20,y=180)
        # for taking input from the user 
        # self.amount=Entry(frame1,font=("times new roman",19),bg="#9fcfd1",fg="black").place(x=200,y=180,width=400)
        #for creating a label for to cuurent
        amount=Label(frame1,text="To Currency:",font=("times new roman",19,"bold"),bg="#4d5d78",fg="black").place(x=20,y=230)
        # for taking input from the user 
        # self.amount=Entry(frame1,font=("times new roman",19),bg="#9fcfd1",fg="black").place(x=200,y=230,width=400)
        amount=Label(frame1,text="Coverted Amount:",font=("times new roman",19,"bold"),bg="#4d5d78",fg="black").place(x=20,y=280)
        Amount1_field = Entry(root)
        Amount1_field.place(x=220,y=130,width=400,height=30)
 
        Amount2_field = Entry(root)
        Amount2_field.place(x=220,y=280,width=400,height=30)
        CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]
        FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list).place(x=220,y=180)
        ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list).place(x=220,y=230)
        def RealTimeCurrencyConversion():
          from forex_python.converter import CurrencyRates
          c = CurrencyRates()
          from_currency = variable1.get()
          to_currency = variable2.get()
          if (Amount1_field.get() == ""):
           tk.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
 
          elif (from_currency == "currency" or to_currency == "currency"):
           tk.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency from menu.")
 
          else:
           new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
           new_amount = float("{:.4f}".format(new_amt))
           Amount2_field.insert(0, str(new_amount))
        def clear_all():
           Amount1_field.delete(0, tk.END)
           Amount2_field.delete(0, tk.END)
        Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=RealTimeCurrencyConversion).place(x=250,y=350)
        # Label_9.grid(row=6, column=0)  
        Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all).place(x=250,y=420)
        # Label_9.grid(row=10, column=0)
 

root=Tk()
object=currency(root)

root.mainloop()



