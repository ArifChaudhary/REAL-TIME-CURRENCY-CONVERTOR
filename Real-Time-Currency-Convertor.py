from tkinter import *
import datetime
import time
from tkinter import messagebox
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

# creat new frame
app = Tk()
# change title & size of frame
app.title("Currency Convertor")
app.geometry("500x400")
app.configure(bg="#6f42c1")
# add text title
titlePage = Label(app, text='Real Time Currency Converter',fg="#fff", height=1, font=('Arial', 22), bg="#6f42c1")
# add element to frame
titlePage.pack()




# amount
amountLabel = Label(app, text='Enter Amount', fg="#fff", font=('Arial', 14), bg="#6f42c1")
amountLabel.pack()
amountLabel.place(x=20, y=100)
amountInput = StringVar(app)
amount = Entry(app, width=10, font=('Arial', 15), textvariable=amountInput)
amount.pack()
amount.place(x=270, y=100)


# Currencies list
CurrencyCodes_List = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK',
                      'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']
# From
fromLabel = Label(app, text='Convert From', fg="#fff", font=('Arial', 14), bg="#6f42c1")
fromLabel.pack()
fromLabel.place(x=20, y=150)


in1 = StringVar(app)
in1.set('Select')
fromOption = OptionMenu(app, in1, *CurrencyCodes_List)
fromOption.place(x=275, y=150)

# to
toLabel = Label(app, text='Convert To', fg="#fff", font=('Arial', 14), bg="#6f42c1")
toLabel.pack()
toLabel.place(x=20, y=200)


in2 = StringVar(app)
in2.set('Select')
toOption = OptionMenu(app, in2, *CurrencyCodes_List)
toOption.place(x=275, y=200)



# output
output = Entry(app, width=10, font=('Arial', 15))
output.pack()
output.place(x=270, y=330)



# function convert
def convert():
    c = CurrencyRates()
    value = amountInput.get()
    fromCurrency = in1.get()
    toCurrency = in2.get()
    if value == '':
        messagebox.showerror('Error', 'please enter value you want to convert it')
    elif (fromCurrency == "Select" or toCurrency == "Select"):
        messagebox.showerror('Error', 'please select option')
    else :
        res = c.convert(fromCurrency, toCurrency,  float(value))
        result = float('{:.4f}'.format(res))
        output.delete(0, END)
        output.insert(0, str(result))
        

def clear():
    value = amountInput.get()
    fromCurrency = in1.get()
    toCurrency = in2.get()
    if( value == "" and fromCurrency =="" and toCurrency ==""):
        messagebox.showinfo("Warning","No Amount Entered!")

    in1.delete(0, END)
    in2.delete(0, END)
    amountInput.delete(0, END) 
    output.delete(0, END) 
    convert.delete(0, END)



# button convert
btnConvert = Button(app, text='Convert', width=15, height=1, bg='#198754', fg='#fff', command=convert)
btnConvert.pack()
btnConvert.place(x=170, y=250)


# answer
resultLabel = Label(app, text='Converted Amount Is ', fg="#fff", font=('Arial', 14), bg="#6f42c1")
resultLabel.pack()
resultLabel.place(x=20, y=330)


#------delete
delete_btn = Button(app, text='CLEAR', width=10, height=1, bg='#D70000', fg='#fff', command=clear)
delete_btn.pack()
delete_btn.place(x=400, y=330)


# Run app infinity
app.mainloop()
