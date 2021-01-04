from tkinter import *
from datetime import date
from tkinter import ttk
import time
import datetime as dt
import csv

root = Tk()
root.geometry("800x500")
root.title("Milk Calculator")
#root.resizable(0,0)

# loading image
photo = PhotoImage(file = 'milk.png')
# creating a Label widget to show the image we load
myimage = Label(image=photo)
# placing the image Label widget using grid method
myimage.grid(row=0, column=1)
w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 20))
w.grid(row=0,column=2)
#Function to calculate the price
"""def writeincsv():
    filename = "milk.csv"
    with open(filename,"w") as csvfile:"""


def calculateMilk():
    month_dict ={"January":31,"February":29,"March":31,"April":30,
                 "May":31,"June":30,"July":31,"August":31,"September":30,
                 "October":31,"November":30,"December":31}
    #Fetching the current year whether it is leap year or not
    current_date = date.today()
    current_year = current_date.year
    month = monthchoosen.get()
    month_no = month_dict[month]
    if month == 'February':
        if (current_year % 4 == 0 and current_year % 100 != 0) or current_year % 400 == 0:
            month_no = 29
    #Calculating total price
    Total = (month_no - int(dayEntry.get())) * int(priceEntry.get())
    Label(text=f"Milk Total for month {monthchoosen.get()} is {Total}",font = 'bold').grid(row=6, column=1)


Label(text="Select the Month").grid(row=1, column=0, padx=90)
Label(text="Liters").grid(row=2, column=0)
Label(text="Price per Liters").grid(row=3, column=0)
Label(text="No. of Days not available").grid(row=4, column=0)

monthValue = StringVar()
literValue = StringVar()
price = StringVar()
dayValue = StringVar()

#defining text variable
#monthEntry = Entry(root, textvariable=monthValue)
monthchoosen = ttk.Combobox(root, textvariable = monthValue)
monthchoosen['values'] = ('January',
                          'February',
                          'March',
                          'April',
                          'May',
                          'June',
                          'July',
                          'August',
                          'September',
                          'October',
                          'November',
                          'December')
monthchoosen.grid(row=1,column=1,pady=10)
#monthchoosen.current()
literEntry = Entry(root, textvariable=literValue)
priceEntry = Entry(root, textvariable=price)
dayEntry = Entry(root, textvariable=dayValue)

#monthEntry.grid(row=1, column=1, pady=10)

literEntry.grid(row=2, column=1, pady=10)
priceEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

Button(text="Calculate price", command=calculateMilk,bg='green',font='bold').grid(row=5, column=1, pady=10)

root.mainloop()